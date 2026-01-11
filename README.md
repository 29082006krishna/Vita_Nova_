# 📊 Monthly Sales & Demand Forecasting System

---

## 🌟 Overview

This project implements a **production-grade monthly sales and demand forecasting system** using **deep learning with attention mechanisms and residual connections**. The model is designed for **business-ready forecasting**, supports **user-defined horizons (3 / 6 / 12 months)**, and produces **clean, month-wise numerical and graphical outputs**.

🚫 Daily recursion is intentionally avoided. Instead, the system performs **direct monthly prediction**, ensuring **stable and realistic long-horizon forecasts**.

---

## 🚀 Key Capabilities

✅ Monthly-direct forecasting (no daily roll-forward noise)
✅ Multi-variable prediction:

* 📦 Quantity Sold (Sales)
* 🔁 Reorder Quantity (Demand)

✅ User-controlled forecast horizon (3 / 6 / 12 months)
✅ Calendar-correct month handling (year crossover supported)
✅ Clean, presentation-ready visualizations

---

## 🧱 Data Pipeline

### 🔹 Input Features

* 📈 Quantity Sold (liters/kg)
* 🛒 Reorder Quantity (liters/kg)

### 🔹 Preprocessing

* 🗓️ Date normalization and validation
* 📆 Monthly aggregation using **Month-End alignment (ME)**
* 🔢 Numeric-only aggregation to prevent datatype conflicts
* ⚖️ Min-Max scaling for stable neural network training

### 🔹 Sequence Construction

* ⏳ Lookback window: **12 months**
* 📐 Input shape: `(batch, 12, 2)`
* 🎯 Output shape: `(batch, 2)`

---

## 🧠 Model Architecture

### 🔷 High-Level Design

```
Input → Embedding → Positional Encoding
      → Transformer Encoder (× N layers)
      → Residual Context Fusion
      → Deep Fully Connected Head
      → Monthly Sales & Demand Output
```

---

### 🔹 Core Components

#### 1️⃣ Embedding Layer

* Projects raw inputs into a high-dimensional latent space
* Enables richer temporal representations

#### 2️⃣ Positional Encoding

* Injects month-order information into the model
* Preserves temporal awareness without recurrence

#### 3️⃣ Transformer Encoder

* 🧩 Multi-Head Self-Attention
* 🔗 Captures long-range temporal dependencies
* 🎯 Learns which past months influence future demand

#### 4️⃣ Residual Connections

* 🔁 Combines:

  * Last time-step representation
  * Global sequence context
* 🛡️ Prevents trend flattening
* ⚙️ Stabilizes deep learning dynamics

#### 5️⃣ Deep Feed-Forward Head

* 🧠 Multi-layer nonlinear mapping
* 🔍 Models complex sales–demand relationships

---

## 🎯 Attention Mechanism

✨ Automatically assigns importance weights to historical months
📌 Learns seasonality, trend shifts, and demand spikes
🚀 Eliminates uniform time-step bias present in plain LSTM models

---

## 🧬 Residual Learning

Residual connections ensure:

* 🔄 Stable gradient flow
* 🧠 Preservation of temporal signals
* 📈 Improved long-horizon forecast realism

This design prevents the common **straight-line prediction problem**.

---

## 🔮 Forecasting Strategy

### 📆 Monthly-Direct Prediction

* Predicts each future month explicitly
* ❌ No compounding daily errors
* ✅ Suitable for business planning and inventory decisions

### 🗓️ Calendar-Correct Horizon

| User Input | Forecast Period         |
| ---------- | ----------------------- |
| 3          | Next 3 calendar months  |
| 6          | Next 6 calendar months  |
| 12         | Next 12 calendar months |

---

## 📊 Visualization

### 📉 Historical Graph

* Displays **12 months starting from the current month**
* Handles year transitions correctly
* Month-wise labels only (no day clutter)

### 📈 Forecast Graph

* Uses predicted monthly values
* Clean Month-Year X-axis labels
* Clearly distinguishes future predictions

---

## ⚙️ Training Configuration

* 📉 Loss Function: Mean Squared Error (MSE)
* ⚡ Optimizer: Adam
* 🎚️ Learning Rate: 0.0005
* 🔁 Epochs: 80
* 📦 Batch Size: 16

---

## 💡 Why This Model Works

✔ Transformer attention captures seasonality and trends
✔ Residual blocks prevent forecast collapse
✔ Monthly-direct strategy ensures stability
✔ Deep nonlinear head improves demand sensitivity

---

## 🎓 Academic / Viva Summary

> “A Transformer-based monthly forecasting model with attention and residual learning was implemented to directly predict future sales and demand, ensuring stable, realistic, and calendar-aligned forecasts suitable for real-world decision-making.”

---

## 🏢 Suitable Use Cases

* 📦 Inventory planning
* 🚚 Supply chain optimization
* 🛍️ Retail demand forecasting
* 📊 Business analytics dashboards
* 🎓 Academic projects and hackathons

---

## 📝 Notes

* Architecture is conceptually aligned with lightweight time-series Transformers (LiteFormer-style behavior)
* Implemented using **PyTorch** for flexibility and extensibility

---

## ✅ End of Documentation

---

## 🚀 Features

* 📅 **Monthly-direct sales & demand forecasting** (3 / 6 / 12 months)
* 🧠 **Transformer-based deep learning model**
* 🔍 **Multi-head self-attention** for trend and seasonality capture
* 🔁 **Residual blocks** for stable deep training
* 📈 **Dual-output prediction**: Sales & Demand together
* 🗂️ **Product- and location-specific forecasting**
* 📊 **Clear monthly visualizations** with business-friendly labels
* ⚙️ **Scalable pipeline** (easy to add new products or regions)
* 🧪 **Evaluation-ready** (train/test split, loss tracking)
* 🏆 **Hackathon & academic submission ready**

---

## 🧰 Technology Stack

### 🌐 Frontend

* **HTML** – Structure and layout
* **CSS** – Styling and responsive design
* **JavaScript** – User interaction and dynamic inputs

### 🧠 Backend & ML

* **Python** – Core programming language
* **PyTorch** – Deep learning framework (primary)
* **TensorFlow** – Alternative deep learning framework (experimentation & comparison)
* **NumPy / Pandas** – Data processing and analysis
* **Scikit-learn** – Scaling and preprocessing

### 🔗 API & Server

* **Flask** – Model serving and backend API

### 🗄️ Database

* **PostgreSQL** – Storage of sales, demand, and product data

### 📊 Visualization

* **Matplotlib** – Monthly forecast and historical trend graphs

---

## 🔮 Future Enhancements

* 📌 Holiday & festival awareness
* 🌦️ Weather-based demand features
* 🧾 Promotion and discount signals
* 📱 Full web dashboard with charts
* ☁️ Cloud deployment (AWS / GCP)
* 🤖 Automated retraining pipeline
