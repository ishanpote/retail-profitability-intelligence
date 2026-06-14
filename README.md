# Retail Profitability Intelligence

A comprehensive data analysis project analyzing Global Superstore transactional data to uncover profit-draining categories, optimize inventory turnover, and identify seasonal product behavior in retail operations.

## 📊 Project Overview

This project analyzes transactional retail data to provide actionable insights for improving business profitability. By combining SQL for data processing, Python for data staging and warehouse management, and Tableau for interactive visualization, this analysis delivers strategic recommendations for inventory optimization and profitability improvement.

### Key Objectives

- **Profit Analysis**: Identify profit-draining categories and sub-categories across regions
- **Inventory Optimization**: Analyze inventory turnover rates and their correlation with profitability
- **Seasonal Behavior**: Discover seasonal product trends and demand patterns
- **Strategic Planning**: Provide data-driven recommendations for inventory and pricing strategies

## 🛠️ Tools & Technologies

| Component | Tools |
|-----------|-------|
| **Data Source** | Global Superstore CSV Dataset |
| **Data Warehouse** | SQLite (superstore_warehouse.db) |
| **Data Processing** | SQL, Python (Pandas, SQLAlchemy) |
| **Data Analysis** | SQL Analytics Queries |
| **Visualization** | Tableau Desktop (TWBX format) |
| **Reporting** | PDF Reports, PNG Outputs |

## 📁 Project Structure

```
retail-profitability-intelligence/
├── README.md                                              # Project documentation
├── data/                                                  # Raw and processed datasets
│   ├── Global_Superstore2.csv                            # Source data (12MB)
│   └── superstore_warehouse.db                           # SQLite data warehouse
├── src/                                                   # Source code
│   ├── stage_warehouse.py                                # Data import and warehouse staging
│   └── profit_analytics.sql                              # Profitability analysis queries
├── documents/                                            # Analysis reports
│   └── Global_Superstore_Profitability_Analysis.pdf     # Executive analysis report
├── outputs/                                              # Query results and visualizations
│   ├── sql_query_1_results.png                          # Profitability analysis results
│   ├── sql_query_2_results.png                          # Category performance results
│   ├── sql_query_3_results.png                          # Regional analysis results
│   └── tableau_executive_dash.png                       # Dashboard preview
└── Global Superstore Profitability Control Room.twbx    # Interactive Tableau dashboard
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- SQLite (included with Python)
- Tableau Desktop (for dashboard development) or Tableau Reader (for viewing)
- Required Python libraries:
  ```bash
  pip install pandas sqlalchemy
  ```

### Workflow

1. **Setup Data Warehouse**
   ```bash
   python src/stage_warehouse.py
   ```
   - Loads Global Superstore CSV data into SQLite database
   - Creates normalized data warehouse schema
   - Prepares data for analysis

2. **Run SQL Analytics**
   - Execute queries from `src/profit_analytics.sql` to calculate:
     - Profit margins by category and sub-category
     - Regional performance metrics
     - Seasonal demand patterns
     - Inventory efficiency indicators

3. **Review Analysis**
   - Check `documents/Global_Superstore_Profitability_Analysis.pdf` for detailed findings
   - View `outputs/` directory for visualization previews

4. **Interactive Dashboard Exploration**
   - Open `Global Superstore Profitability Control Room.twbx` in Tableau Desktop
   - Filter by Region, Product Category, and Season
   - Drill down into detailed profitability metrics

## 📋 Key Analyses

### 1. Profit Margin Analysis
- Profit margins calculated by category and sub-category
- Identification of high and low-profit products
- Geographic performance comparison
- Trend analysis across time periods

### 2. Inventory Efficiency
- Inventory turnover analysis by product
- Correlation between stock levels and profitability
- Detection of slow-moving and obsolete inventory
- Identification of optimal inventory levels

### 3. Seasonal Product Behavior
- Seasonal demand patterns by product type
- Peak and off-season performance metrics
- Regional seasonal variations
- Forecasting recommendations

### 4. Regional Performance
- Performance metrics by geographic region
- Regional profit distribution
- Regional inventory optimization opportunities
- Cross-region benchmarking

## 📊 Deliverables

### 1. **Interactive Tableau Dashboard**
   - `Global Superstore Profitability Control Room.twbx`
   - Interactive visualizations with drill-down capabilities
   - Real-time filters for region, product category, and season
   - KPI tracking and performance indicators
   - Executive summary and detailed analysis views

### 2. **SQL Analytics** (`src/profit_analytics.sql`)
   - Profit margin calculations by category/sub-category
   - Regional performance queries
   - Seasonal trend analysis
   - Category profitability ranking
   - Inventory efficiency metrics

### 3. **Executive Analysis Report** (`documents/Global_Superstore_Profitability_Analysis.pdf`)
   - Executive summary
   - Detailed findings from SQL and visualization analysis
   - Key performance indicators
   - Strategic recommendations for:
     - Slow-moving items optimization
     - Overstocked category management
     - Inventory reduction strategies
     - Pricing optimization
     - Regional performance improvement

### 4. **Visualization Outputs** (`outputs/`)
   - SQL query result previews (PNG)
   - Tableau dashboard screenshots
   - Profitability charts and trend analysis

## 💡 Key Insights

The analysis reveals:
- Specific product categories with below-average profit margins
- Geographic regions with profit optimization opportunities
- Seasonal patterns affecting product performance
- Inventory management inefficiencies and overstocking issues
- Recommendations for strategic reallocation and pricing adjustments

## 📈 How to Use Results

1. **For Category Managers**: Use profit analysis to optimize product mix and identify underperforming SKUs
2. **For Supply Chain**: Use inventory correlation data and warehouse database to improve stock levels and reduce holding costs
3. **For Pricing Teams**: Use seasonal insights and regional data for dynamic pricing strategies
4. **For Executive Leadership**: Use dashboard for real-time monitoring of profitability metrics and regional performance

## 🔍 Data Source

- **Dataset**: Global Superstore 2
- **Records**: Multi-year transactional data
- **Scope**: Global sales across multiple regions, categories, and product segments
- **Data Fields**: Order dates, products, quantities, prices, profit, region, category, segment

## 📝 Notes

- All analysis based on Global Superstore dataset
- Recommendations should be validated with domain experts before implementation
- Regular updates recommended for ongoing insights as new transactional data arrives
- SQLite warehouse enables reproducible analysis and query validation

## 👤 Author

**Ishan Pote**

## 📄 License

This project is provided as-is for analytical purposes.

---

**Last Updated**: June 2026

For questions or collaboration, please reach out!
