import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.title("📈 Brand Demand Trends")

url = "https://your-django-api-url/api/sales/"
response = requests.get(url)

if response.status_code == 200:
    sales = response.json()
    df = pd.json_normalize(sales)
    fig = px.bar(df, x="product.brand", y="quantity", color="city.name", barmode="group")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("API not reachable.")
