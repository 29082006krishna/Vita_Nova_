import streamlit as st
import pandas as pd
import numpy as np
import torch
from sklearn.preprocessing import MinMaxScaler
from src.liteformer_model import LiteFormerDF

# =====================
# CONFIG
# =====================
SEQ_LEN = 30
MODEL_PATH = "models/liteformer_df.pth"  # <-- you can change this
TARGET_COL = "Quantity Sold (liters/kg)"

st.set_page_config(page_title="AI Demand Forecasting", layout="wide")
st.title("📊 AI Demand, Sales & Trend Forecasting")

# =====================
# LOAD DATA
# =====================
uploaded_file = st.file_uploader("Upload Dataset (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")

    features = [
        "Quantity Sold (liters/kg)",
        "Quantity in Stock (liters/kg)",
        "Minimum Stock Threshold (liters/kg)",
        "Reorder Quantity (liters/kg)",
        "Price per Unit (sold)",
        "Approx. Total Revenue(INR)"
    ]

    df = df[["Date"] + features].dropna()
    df.set_index("Date", inplace=True)

    # =====================
    # SCALE DATA
    # =====================
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df)

    # =====================
    # CREATE SEQUENCE
    # =====================
    X = []
    for i in range(len(scaled) - SEQ_LEN):
        X.append(scaled[i:i+SEQ_LEN])
    X = torch.tensor(X[-1:], dtype=torch.float32)

    # =====================
    # LOAD MODEL
    # =====================
    model = LiteFormerDF(input_dim=X.shape[2])
    model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
    model.eval()

    # =====================
    # PREDICT DEMAND
    # =====================
    with torch.no_grad():
        demand_pred = model(X).item()

    # =====================
    # BUSINESS LOGIC
    # =====================
    avg_price = df["Price per Unit (sold)"].mean()
    predicted_sales = demand_pred * avg_price

    recent = df[TARGET_COL].tail(10).mean()
    trend_status = "📈 Trending Up" if demand_pred > recent else "📉 Stable / Declining"

    # =====================
    # OUTPUT
    # =====================
    col1, col2, col3 = st.columns(3)

    col1.metric("Predicted Demand", f"{demand_pred:.2f}")
    col2.metric("Predicted Sales (₹)", f"{predicted_sales:.2f}")
    col3.metric("Trend Status", trend_status)

    st.subheader("📌 Historical Demand")
    st.line_chart(df[TARGET_COL])

    # =====================
    # TOP 5 PRODUCTS
    # =====================
    if "Product Name" in df.columns:
        st.subheader("🏆 Top 5 Products (Historical)")
        top5 = df.groupby("Product Name")[TARGET_COL].sum().sort_values(ascending=False).head(5)
        st.table(top5)
