import os
import pandas as pd
import sqlite3

# Define relative file coordinates
csv_path = os.path.join('data', 'Global_Superstore2.csv')
db_path = os.path.join('data', 'superstore_warehouse.db')

def run_etl_pipeline():
    print("=" * 60)
    print("   STARTING GLOBAL SUPERSTORE ENTERPRISE ETL PIPELINE   ")
    print("=" * 60)
    
    # 1. Extraction Phase
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Missing source file: '{csv_path}'. Please ensure your file is named 'Global_Superstore2.csv' and placed inside the data/ folder.")
    
    print("🔄 Loading raw transactional data (51,290 rows)...")
    df = pd.read_csv(csv_path, encoding='latin-1')
    
    # 2. Transformation Phase
    print("Core Cleaning: Standardizing database schema headers...")
    
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('-', '_').str.lower()
    
    print("Core Cleaning: Addressing data integrity gaps...")
    # Resolve empty postal code blocks with zero default values
    if 'postal_code' in df.columns:
        df['postal_code'] = df['postal_code'].fillna(0).astype(str)
        
    # Standardize order dates to ISO format string (YYYY-MM-DD) for SQLite compatibility
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce').dt.strftime('%Y-%m-%d')
    df['ship_date'] = pd.to_datetime(df['ship_date'], dayfirst=True, errors='coerce').dt.strftime('%Y-%m-%d')
    
    # 3. Loading Phase
    print("💾 Connecting to target database staging layer...")
    conn = sqlite3.connect(db_path)
    
    # Load rows into an optimized analytics fact table
    df.to_sql('orders_fact', conn, if_exists='replace', index=False)
    
    print("\n--- [ETL PIPELINE SUCCESS LOG] ---")
    print(f"✓ Target Database: '{db_path}'")
    print(f"✓ Dimensions Loaded: {df.shape[0]} rows across {df.shape[1]} clean columns.")
    print("=" * 60)
    conn.close()

if __name__ == "__main__":
    run_etl_pipeline()