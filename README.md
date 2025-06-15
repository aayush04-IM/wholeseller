# wholeseller
# Mega Wholesale Dashboard 🚀

A cloud-based business intelligence dashboard for monitoring and analyzing the operations of a wholesale distribution company. This project includes a full-stack implementation with a PostgreSQL (Supabase) backend, and Streamlit/Django frontend to visualize insights like stock availability, product demand, profit margins, pricing trends, and customer feedback.

---

## 🔍 Project Overview

**Mega Wholesale Dashboard** is built to help large-scale wholesalers make data-driven decisions across 20+ cities. It offers real-time insights on:

- Stock status and city-wise availability
- Demand trends by brand/product
- Dynamic pricing and profitability analysis
- Customer ratings and feedback analysis
- AI/ML-powered insights and recommendations (coming soon)

---

## ⚙️ Tech Stack

### ✅ Backend:
- **Supabase** (PostgreSQL with REST API support)
- SQL Views for:
  - `view_stock_availability`
  - `view_brand_demand`
  - `view_product_margins`
  - `view_pricing_trends`
  - `view_product_ratings`

### ✅ Frontend:
- **Streamlit** *(MVP version)*  
- **Django** *(Under development for unified software version)*

### ✅ Cloud Hosting:
- **Render** for full-stack deployment
- **Streamlit Cloud** (initial prototype)

### ✅ Others:
- **Pandas, Plotly, Matplotlib** for data viz
- **OpenAI / LangChain (planned)** for GenAI use cases
- **GitHub** for version control
- **Power BI** (optional enterprise reports)

---

## 📊 Features

| Module | Description |
|--------|-------------|
| 🧮 Inventory | Real-time stock monitoring, alerts for low inventory |
| 📈 Demand Analytics | Analyze product/brand demand across cities |
| 💰 Profit Margins | Track pricing vs margins dynamically |
| ⭐ Product Ratings | Analyze customer feedback and average product scores |
| 🧠 AI Assistant *(planned)* | GenAI-based report summaries and insights via LangChain & OpenAI |

---

## 🚧 Current Status

- ✅ Supabase DB schema and views completed
- ✅ Streamlit dashboard MVP working with cloud deployment
- 🔄 Django version in progress for enterprise-grade app
- 🧠 GenAI features (LangChain + CrewAI) coming soon

---

## 🗂️ File Structure

