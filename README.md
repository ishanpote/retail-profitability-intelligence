# Retail Profitability Intelligence

A comprehensive data analysis project designed to uncover profit-draining categories, optimize inventory turnover, and identify seasonal product behavior in retail operations.

## 📊 Project Overview

This project analyzes transactional retail data to provide actionable insights for improving business profitability. By combining SQL for data processing, Python for statistical analysis, and Tableau for visualization, we identify optimization opportunities across product categories, inventory management, and seasonal trends.

### Key Objectives

- **Profit Analysis**: Identify profit-draining categories and sub-categories
- **Inventory Optimization**: Analyze inventory turnover rates and their correlation with profitability
- **Seasonal Behavior**: Discover seasonal product trends and demand patterns
- **Strategic Planning**: Provide data-driven recommendations for inventory and pricing strategies

## 🛠️ Tools & Technologies

| Component | Tools |
|-----------|-------|
| **Data Processing** | SQL, Python (Pandas) |
| **Data Analysis** | Python (Pandas, NumPy) |
| **Visualization** | Seaborn, Tableau |
| **Reporting** | PDF, Tableau Dashboards |

## 📁 Project Structure

```
retail-profitability-intelligence/
├── README.md
├── data/                          # Raw and processed datasets
├── sql/                          # SQL queries for data extraction and analysis
│   └── *.sql                     # Category profitability, inventory analysis queries
├── python/                       # Python scripts for analysis
│   ├── data_cleaning.py         # Data import and cleaning
│   ├── profit_analysis.py       # Profit margin calculations
│   └── correlation_analysis.py  # Inventory vs profitability correlation
├── notebooks/                    # Jupyter notebooks for exploratory analysis
├── dashboards/                   # Tableau dashboard files
│   └── retail_profitability_dashboard.twb
└── reports/                      # Final insights and recommendations
    └── insights_report.pdf
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- SQL Database (MySQL, PostgreSQL, or SQL Server)
- Tableau Desktop (for dashboard development)
- Required Python libraries:
  ```bash
  pip install pandas numpy seaborn matplotlib sqlalchemy
  ```

### Workflow

1. **Data Import & Cleaning**
   ```bash
   python python/data_cleaning.py
   ```
   - Load transactional data into SQL database
   - Identify and handle missing/null records

2. **SQL Analysis**
   - Execute queries to calculate profit margins by category and sub-category
   - Generate inventory turnover reports
   - Query seasonal data patterns

3. **Python Statistical Analysis**
   ```bash
   python python/correlation_analysis.py
   ```
   - Analyze correlation between inventory days and profitability
   - Calculate key performance metrics
   - Generate visualization charts

4. **Build Tableau Dashboard**
   - Create interactive dashboard with filters:
     - Region
     - Product Type
     - Season
   - Visualize profit trends and inventory metrics

5. **Generate Strategic Recommendations**
   - Identify slow-moving items
   - Highlight overstocked categories
   - Provide actionable insights for optimization

## 📋 Key Analyses

### 1. Profit Margin Analysis
- Profit margins calculated by category and sub-category
- Identification of high and low-profit products
- Trend analysis across time periods

### 2. Inventory Turnover Correlation
- Statistical correlation between inventory days and profitability
- Identification of optimal inventory levels
- Detection of obsolete inventory

### 3. Seasonal Product Behavior
- Seasonal demand patterns by product type
- Peak and off-season performance metrics
- Forecasting recommendations

### 4. Regional Performance
- Performance metrics by geographic region
- Regional inventory optimization strategies
- Cross-region benchmarking

## 📊 Deliverables

### 1. **Tableau Dashboard**
   - Interactive visualizations with drill-down capabilities
   - Real-time filters for region, product type, and season
   - KPI tracking and performance indicators

### 2. **SQL Queries** (`sql/queries.sql`)
   - Profit margin calculations
   - Inventory analysis queries
   - Seasonal trend queries
   - Category performance queries

### 3. **PDF Report** (`reports/insights_report.pdf`)
   - Executive summary
   - Detailed findings from analysis
   - Key performance indicators
   - Strategic recommendations for:
     - Slow-moving items
     - Overstocked categories
     - Inventory optimization
     - Pricing strategies

## 💡 Key Insights

The analysis reveals:
- Products/categories with below-average profit margins
- Inventory management inefficiencies
- Seasonal demand patterns
- Opportunities for strategic reallocation
- Recommendations for inventory reduction and profitability improvement

## 📈 How to Use Results

1. **For Category Managers**: Use profit analysis to optimize product mix
2. **For Supply Chain**: Use inventory correlation data to improve stock levels
3. **For Pricing Teams**: Use seasonal insights for dynamic pricing strategies
4. **For Planning Teams**: Use forecasts for budget allocation

## 🔍 Data Requirements

- **Transactional Data**: Sales transactions with dates, products, quantities, and prices
- **Product Data**: Category, sub-category, and product hierarchy
- **Inventory Data**: Stock levels, holding costs
- **Seasonal Data**: Calendar information for seasonal classification

## 📝 Notes

- All personally identifiable information has been anonymized
- Analysis assumes data quality standards are met
- Recommendations should be validated with domain experts
- Regular updates recommended for ongoing insights

## 👤 Author

**Ishan Pote**

## 📄 License

This project is provided as-is for analytical purposes.

---

**Last Updated**: June 2026

For questions or collaboration, please reach out!
