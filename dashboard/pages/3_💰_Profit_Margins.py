import streamlit as st
import pandas as pd

st.title("💰 Profit Margins (Mocked)")

data = {
    "Product": ["Soap", "Oil", "Toothpaste", "Cold Drink"],
    "Margin (%)": [12, 18, 15, 10]
}
df = pd.DataFrame(data)
st.dataframe(df)

st.info("Later we'll connect this to the actual Supabase view or API.")
