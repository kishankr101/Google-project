import streamlit as st
import pymongo
import pandas as pd
import plotly.express as px

# Securely fetch secrets from Streamlit Cloud
@st.cache_resource
def init_connection():
    return pymongo.MongoClient(st.secrets["mongo"]["uri"])

client = init_connection()
db = client.oyo_clone

st.title("OYO Business Insights 📊")

# Load Bookings
data = list(db.bookings.find())
if data:
    df = pd.DataFrame(data)
    st.metric("Total Revenue", f"${df['totalPrice'].sum():,.2f}")
    
    # Revenue Trend Line
    fig = px.line(df, x='createdAt', y='totalPrice', title="Revenue Growth")
    st.plotly_chart(fig)
else:
    st.write("No booking data available yet.")
  
