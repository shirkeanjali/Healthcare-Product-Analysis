# Healthcare Product Price Intelligence Analysis

## Objectives

 - Analyze pricing trends across healthcare product categories
 - Segment products into Budget, Mid-range, and Premium price bands
 - Evaluate the impact of discounts on customer ratings
 - Identify category-level pricing and discount strategies

## Tools & Technologies

1. **Python** – Core programming
2. **BeautifulSoup & Requests** – Web scraping
3. **Pandas & NumPy** – Data cleaning, preprocessing, and analysis
4. **Matplotlib & Seaborn** – Data visualization
5. **Streamlit** – Interactive dashboard

## Project Workflow

### 1.Data Collection
- Product details such as category, price, discounts, and customer ratings were collected through web scraping.

### 2.Data Cleaning & Preprocessing
- Removed currency symbols and text noise
- Handled missing and inconsistent values
- Converted numerical fields to proper data types
- Created derived features like price_segment and discount_segment

### 3.Exploratory Data Analysis (EDA)
- Category-wise average price analysis
- Discount segmentation vs customer ratings
- Price segmentation to understand market positioning

### 4.Visualization & Dashboard
- Bar charts, box plots, and heatmaps
- Interactive Streamlit dashboard with category, price, and discount filters

## Key Insights
- Certain categories follow premium pricing strategies, indicating quality-driven demand
- Products with discounts show higher customer engagement
- Mid-range products dominate, balancing affordability and trust
