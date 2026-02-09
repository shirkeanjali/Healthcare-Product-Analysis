import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Product Price Intelligence Dashboard",
    layout="wide"
)

# --------------------------------------------------
# Load Data
# --------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("pharmeasy1.csv")

df = load_data()

# --------------------------------------------------
# Validate Required Columns
# --------------------------------------------------
required_columns = [
    "category",
    "price",
    "price_segment",
    "discount_segment",
    "no_of_ratings_given"
]

missing_cols = [col for col in required_columns if col not in df.columns]
if missing_cols:
    st.error(f"Missing columns in CSV: {missing_cols}")
    st.stop()

# --------------------------------------------------
# Sidebar Filters
# --------------------------------------------------
st.sidebar.header("Filters")

category_filter = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["category"].unique()),
    default=sorted(df["category"].unique())
)

price_filter = st.sidebar.multiselect(
    "Select Price Segment",
    options=sorted(df["price_segment"].unique()),
    default=sorted(df["price_segment"].unique())
)

discount_filter = st.sidebar.multiselect(
    "Select Discount Segment",
    options=sorted(df["discount_segment"].unique()),
    default=sorted(df["discount_segment"].unique())
)

filtered_df = df[
    (df["category"].isin(category_filter)) &
    (df["price_segment"].isin(price_filter)) &
    (df["discount_segment"].isin(discount_filter))
]

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("PharmEasy Product Price Intelligence Dashboard")
st.caption("Analysis of pricing strategy, discount impact, and customer engagement")

st.divider()

# --------------------------------------------------
# KPI Metrics
# --------------------------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Products", len(filtered_df))

if len(filtered_df) > 0:
    col2.metric("Average Price", f"₹{round(filtered_df['price'].mean(), 2)}")
    col3.metric(
        "Average Ratings",
        round(filtered_df["no_of_ratings_given"].mean(), 2)
    )
else:
    col2.metric("Average Price", "N/A")
    col3.metric("Average Ratings", "N/A")

st.divider()

# --------------------------------------------------
# Category-wise Average Price (Bar Chart)
# --------------------------------------------------
st.subheader("Category-wise Average Price")

avg_price = (
    filtered_df
    .groupby("category")["price"]
    .mean()
    .sort_values()
)

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(avg_price.index, avg_price.values, color="pink")
ax.set_xlabel("Category")
ax.set_ylabel("Average Price")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

st.pyplot(fig)

st.divider()

# --------------------------------------------------
# Discount Segment vs Ratings (Box Plot)
# --------------------------------------------------
st.subheader("Discount Segment vs Ratings")

fig, ax = plt.subplots(figsize=(6, 4))
sns.boxplot(
    x="discount_segment",
    y="no_of_ratings_given",
    data=filtered_df,
    ax=ax
)
ax.set_xlabel("Discount Segment")
ax.set_ylabel("Number of Ratings")
plt.tight_layout()

st.pyplot(fig)

st.divider()

# --------------------------------------------------
# Category × Price Segment Heatmap
# --------------------------------------------------
st.subheader("Category × Price Segment Heatmap")

heatmap_data = pd.crosstab(
    filtered_df["category"],
    filtered_df["price_segment"]
)

fig, ax = plt.subplots(figsize=(7, 5))
sns.heatmap(
    heatmap_data,
    annot=True,
    fmt="d",
    cmap="YlOrRd",
    ax=ax
)
ax.set_xlabel("Price Segment")
ax.set_ylabel("Category")
plt.tight_layout()

st.pyplot(fig)

st.divider()

# --------------------------------------------------
# Insights Section
# --------------------------------------------------
st.subheader("Key Insights")

st.markdown("""
- **Premium products dominate certain categories**, indicating strong quality perception.
- **Discounted products receive higher engagement**, confirming the impact of promotions.
- **Mid-range products form the core market**, balancing affordability and trust.
- Pricing strategies vary significantly across categories, enabling targeted marketing decisions.
""")

st.divider()

# --------------------------------------------------
# Raw Data View
# --------------------------------------------------
with st.expander("View Filtered Raw Data"):
    st.dataframe(filtered_df)
