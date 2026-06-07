import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------
# PAGE CONFIG
# --------------------------------
st.set_page_config(
    page_title="ShopSphere E-Commerce Analytics Dashboard",
    page_icon="🛒",
    layout="wide"
)

# --------------------------------
# LOAD DATA
# --------------------------------
df = pd.read_csv("../data/ecommerce_clean.csv")

# --------------------------------
# ROSE COLOR PALETTE
# --------------------------------
DARK_ROSE = "#a8323e"
MEDIUM_ROSE = "#d86a76"
LIGHT_ROSE = "#efb4bc"
EXTRA_LIGHT_ROSE = "#f9dfe3"

# --------------------------------
# SIDEBAR FILTER
# --------------------------------
st.sidebar.header("Region Filter")

selected_region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + sorted(df["Region"].unique().tolist())
)

if selected_region != "All":
    df = df[df["Region"] == selected_region]

# --------------------------------
# KPI CALCULATIONS
# --------------------------------
total_revenue = df["Sales"].sum()

total_profit = df["Profit"].sum()

total_orders = len(df)

return_rate = (
    len(df[df["Returned"] == "Yes"])
    / len(df)
) * 100

# --------------------------------
# TITLE
# --------------------------------
st.title(
    "🛒 ShopSphere E-Commerce Analytics Dashboard"
)

# --------------------------------
# KPI ROW
# --------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Revenue",
        f"₹{total_revenue:,.0f}"
    )

with col2:
    st.metric(
        "Total Profit",
        f"₹{total_profit:,.0f}"
    )

with col3:
    st.metric(
        "Total Orders",
        total_orders
    )

with col4:
    st.metric(
        "Return Rate",
        f"{return_rate:.1f}%"
    )

st.markdown("---")

# --------------------------------
# ROW 2
# --------------------------------
col5, col6 = st.columns(2)

with col5:

    st.subheader("Revenue by Region")

    revenue_region = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales")
    )

    fig1 = px.bar(
    revenue_region,
    x="Sales",
    y="Region",
    orientation="h",
    text="Sales",
    color="Sales",
    color_continuous_scale=[
        EXTRA_LIGHT_ROSE,
        LIGHT_ROSE,
        MEDIUM_ROSE,
        DARK_ROSE
    ],
    range_color=(
        revenue_region["Sales"].min(),
        revenue_region["Sales"].max()
    )
)

    fig1.update_traces(
        texttemplate="₹%{text:,.0f}",
        textposition="outside"
    )

    fig1.update_layout(
    xaxis_title="Revenue (₹)",
    yaxis_title="Region",
    coloraxis_colorbar=dict(
        title="Revenue",
        tickformat=",.0f",
        len=0.75
    )
)

    fig1.update_coloraxes(
    colorbar_tickprefix="₹"
)

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with col6:

    st.subheader("Profit by Category")

    profit_category = (
        df.groupby("Category")["Profit"]
        .sum()
        .reset_index()
        .sort_values("Profit", ascending=False)
    )

    fig2 = px.bar(
    profit_category,
    x="Category",
    y="Profit",
    text="Profit",
    color="Profit",
    color_continuous_scale=[
        EXTRA_LIGHT_ROSE,
        LIGHT_ROSE,
        MEDIUM_ROSE,
        DARK_ROSE
    ],
    range_color=(
        profit_category["Profit"].min(),
        profit_category["Profit"].max()
    )
)

    fig2.update_traces(
    texttemplate="₹%{text:,.0f}",
    textposition="outside"
)

    fig2.update_layout(
    xaxis_title="Product Category",
    yaxis_title="Profit (₹)",
    coloraxis_colorbar=dict(
        title="Profit",
        tickformat=",.0f",
        len=0.75
    )
)

    fig2.update_coloraxes(
    colorbar_tickprefix="₹"
)
    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.markdown("---")

# --------------------------------
# ROW 3
# --------------------------------
col7, col8 = st.columns(2)

with col7:

    st.subheader(
        "Customer Segment Analysis"
    )

    segment_sales = (
        df.groupby("CustomerSegment")["Sales"]
        .sum()
        .reset_index()
    )

    fig3 = px.pie(
        segment_sales,
        names="CustomerSegment",
        values="Sales",
        hole=0.55,
        color="CustomerSegment",
        color_discrete_map={
            "Consumer": DARK_ROSE,
            "Corporate": MEDIUM_ROSE,
            "Home Office": LIGHT_ROSE
        }
    )

    fig3.update_traces(
        textinfo="percent+label"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

with col8:

    st.subheader(
        "Returns Distribution"
    )

    returns_df = (
        df["Returned"]
        .value_counts()
        .reset_index()
    )

    returns_df.columns = [
        "Returned",
        "Count"
    ]

    fig4 = px.pie(
        returns_df,
        names="Returned",
        values="Count",
        color="Returned",
        color_discrete_map={
            "Yes": DARK_ROSE,
            "No": LIGHT_ROSE
        }
    )

    fig4.update_traces(
        textinfo="percent+label"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

st.markdown("---")

# --------------------------------
# DATASET TABLE
# --------------------------------
st.subheader(
    "E-Commerce Dataset"
)

st.dataframe(
    df,
    use_container_width=True
)