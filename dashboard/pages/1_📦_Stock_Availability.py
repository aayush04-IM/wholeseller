import streamlit as st
import pandas as pd
import requests

st.title("📦 Stock Availability")

# Simulated API call (replace with real endpoint later)
url = "https://your-django-api-url/api/products/"
response = requests.get(url)

if response.status_code == 200:
    products = response.json()
    df = pd.DataFrame(products)
    st.dataframe(df)
else:
    st.error("API not reachable.")
