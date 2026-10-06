import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Campus Cafe Dashboard",
    page_icon="☕",
    layout="wide"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f7faf8;
}

.title {
    font-size: 38px;
    font-weight: bold;
    color: #174c3c;
}

.subtitle {
    font-size: 18px;
    color: #555555;
}

.kpi-card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #d8e5df;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
    text-align: center;
}

.kpi-title {
    font-size: 16px;
    color: #555555;
}

.kpi-value {
    font-size: 27px;
    font-weight: bold;
    color: #174c3c;
}

.insight {
    background-color: white;
    padding: 15px;
    border-left: 5px solid #2e8b57;
    border-radius: 8px;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.markdown(
    '<div class="title">☕ Campus Cafe Sales Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Sales • Profit • Products • Categories • Outlet Performance</div>',
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------------------------------------------------
# DATA
# ---------------------------------------------------------

# Category data
category_data = pd.DataFrame({
    "Category": [
        "Food",
        "Beverages",
        "Snacks",
        "Desserts",
        "Others"
    ],
    "Sales": [
        16722.75,
        12864.50,
        11452.30,
        9845.20,
        6660.50
    ]
})

# Outlet data
outlet_data = pd.DataFrame({
    "Outlet": [
        "Library Café",
        "Main Campus",
        "North Campus",
        "West Campus"
    ],
    "Profit": [
        13685.25,
        5842.75,
        4768.50,
        3248.10
    ]
})

# Product data
product_data = pd.DataFrame({
    "Product": [
        "Paneer Wrap",
        "Cold Coffee",
        "Veg Sandwich",
        "French Fries",
        "Chocolate Shake"
    ],
    "Sales": [
        8546.25,
        6782.40,
        6124.80,
        4982.60,
        4623.00
    ]
})

# Monthly sales
monthly_data = pd.DataFrame({
    "Month": [
        "Jan 2024",
        "Feb 2024",
        "Mar 2024"
    ],
    "Sales": [
        22156.75,
        24892.40,
        26495.10
    ]
})

# Region data
region_data = pd.DataFrame({
    "Region": [
        "South Mumbai",
        "North Mumbai",
        "West Mumbai",
        "Central Mumbai"
    ],
    "Sales": [
        26497.00,
        18500.00,
        14500.00,
        14048.25
    ]
})

# ---------------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------------

st.sidebar.header("🔎 Filters")

selected_category = st.sidebar.multiselect(
    "Category",
    category_data["Category"].unique(),
    default=category_data["Category"].tolist()
)

selected_outlet = st.sidebar.multiselect(
    "Outlet",
    outlet_data["Outlet"].unique(),
    default=outlet_data["Outlet"].tolist()
)

selected_region = st.sidebar.multiselect(
    "Region",
    region_data["Region"].unique(),
    default=region_data["Region"].tolist()
)

selected_product = st.sidebar.multiselect(
    "Product",
    product_data["Product"].unique(),
    default=product_data["Product"].tolist()
)

selected_month = st.sidebar.multiselect(
    "Date / Month",
    monthly_data["Month"].unique(),
    default=monthly_data["Month"].tolist()
)

# ---------------------------------------------------------
# KPI VALUES
# ---------------------------------------------------------

total_sales = 73545.25
total_profit = 22545.60
total_quantity = 1344
total_orders = 500

# ---------------------------------------------------------
# KPI CARDS
# ---------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-title">💰 Total Sales</div>
        <div class="kpi-value">₹73,545.25</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-title">📈 Total Profit</div>
        <div class="kpi-value">₹22,545.60</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-title">📦 Total Quantity</div>
        <div class="kpi-value">1,344</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-title">🧾 Number of Orders</div>
        <div class="kpi-value">500</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("")

# ---------------------------------------------------------
# FILTER DATA
# ---------------------------------------------------------

filtered_category = category_data[
    category_data["Category"].isin(selected_category)
]

filtered_outlet = outlet_data[
    outlet_data["Outlet"].isin(selected_outlet)
]

filtered_region = region_data[
    region_data["Region"].isin(selected_region)
]

filtered_product = product_data[
    product_data["Product"].isin(selected_product)
]

filtered_month = monthly_data[
    monthly_data["Month"].isin(selected_month)
]

# ---------------------------------------------------------
# ROW 1 - CATEGORY / OUTLET / PIE
# ---------------------------------------------------------

col1, col2, col3 = st.columns(3)

# Sales by Category
with col1:

    fig_category = px.bar(
        filtered_category,
        x="Category",
        y="Sales",
        title="Sales by Category",
        text="Sales"
    )

    fig_category.update_traces(
        texttemplate="₹%{text:,.2f}",
        textposition="outside"
    )

    fig_category.update_layout(
        xaxis_title="Category",
        yaxis_title="Sales (₹)",
        height=430
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )

# Profit by Outlet
with col2:

    fig_outlet = px.bar(
        filtered_outlet,
        x="Outlet",
        y="Profit",
        title="Profit by Outlet",
        text="Profit"
    )

    fig_outlet.update_traces(
        texttemplate="₹%{text:,.2f}",
        textposition="outside"
    )

    fig_outlet.update_layout(
        xaxis_title="Outlet",
        yaxis_title="Profit (₹)",
        height=430
    )

    st.plotly_chart(
        fig_outlet,
        use_container_width=True
    )

# Sales Share Pie
with col3:

    fig_pie = px.pie(
        filtered_category,
        names="Category",
        values="Sales",
        title="Sales Share by Category",
        hole=0.3
    )

    fig_pie.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig_pie.update_layout(
        height=430
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

# ---------------------------------------------------------
# ROW 2 - MONTHLY SALES / PRODUCTS
# ---------------------------------------------------------

col1, col2 = st.columns(2)

# Monthly Sales Trend
with col1:

    fig_month = px.line(
        filtered_month,
        x="Month",
        y="Sales",
        title="Monthly Sales Trend",
        markers=True,
        text="Sales"
    )

    fig_month.update_traces(
        texttemplate="₹%{text:,.2f}",
        textposition="top center"
    )

    fig_month.update_layout(
        xaxis_title="Month",
        yaxis_title="Sales (₹)",
        height=450
    )

    st.plotly_chart(
        fig_month,
        use_container_width=True
    )

# Top Products
with col2:

    fig_product = px.bar(
        filtered_product.sort_values(
            "Sales",
            ascending=True
        ),
        x="Sales",
        y="Product",
        orientation="h",
        title="Top Selling Products by Sales",
        text="Sales"
    )

    fig_product.update_traces(
        texttemplate="₹%{text:,.2f}",
        textposition="outside"
    )

    fig_product.update_layout(
        xaxis_title="Sales (₹)",
        yaxis_title="Product",
        height=450
    )

    st.plotly_chart(
        fig_product,
        use_container_width=True
    )

# ---------------------------------------------------------
# ROW 3 - REGION
# ---------------------------------------------------------

st.markdown("### 🌍 Regional Sales")

fig_region = px.bar(
    filtered_region.sort_values(
        "Sales",
        ascending=False
    ),
    x="Region",
    y="Sales",
    title="Sales by Region",
    text="Sales"
)

fig_region.update_traces(
    texttemplate="₹%{text:,.2f}",
    textposition="outside"
)

fig_region.update_layout(
    xaxis_title="Region",
    yaxis_title="Sales (₹)",
    height=400
)

st.plotly_chart(
    fig_region,
    use_container_width=True
)

# ---------------------------------------------------------
# KEY INSIGHTS
# ---------------------------------------------------------

st.markdown("---")

st.markdown("## 💡 Key Business Insights")

insights = [
    "Food is the highest-sales category with ₹16,722.75 in sales.",
    "Library Café has the highest outlet sales at ₹13,685.25.",
    "South Mumbai has the highest regional sales at ₹26,497.00.",
    "Paneer Wrap is the highest-selling product by sales at ₹8,546.25.",
    "Total Campus Cafe sales are ₹73,545.25 and total profit is ₹22,545.60."
]

for i, insight in enumerate(insights, start=1):

    st.markdown(
        f"""
        <div class="insight">
            <b>{i}.</b> {insight}
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------------------------------------------------
# DATA TABLE
# ---------------------------------------------------------

st.markdown("---")

st.markdown("### 📊 Category Sales Data")

st.dataframe(
    filtered_category,
    use_container_width=True
)

st.markdown("")

st.caption(
    "Campus Cafe Business Intelligence Dashboard | "
    "Developed using Python, Streamlit, Pandas and Plotly"
)