# scripts/create_dashboard.py

import streamlit as st
import pandas as pd

def load_data():
    df = pd.read_csv('data/cleaned_data.csv')
    return df

def main():
    st.title("Retail Transaction Dashboard")

    df = load_data()

    st.subheader("Top Selling Products")
    st.dataframe(df[['title', 'quantity_sold']].sort_values('quantity_sold', ascending=False))

    st.subheader("Revenue by Product")
    st.bar_chart(df.set_index('title')['order_value'])

if __name__ == "__main__":
    main()
