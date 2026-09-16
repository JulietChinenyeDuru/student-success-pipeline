import streamlit as st
import pandas as pd

st.title("Student Success Analytics Dashboard")

summary = pd.read_csv("output/summary.csv")
results = pd.read_csv("output/results.csv")

st.subheader("Outcome Summary")
st.dataframe(summary)

st.subheader("Mean grade by outcome")
st.bar_chart(summary.set_index("target")["mean_grade"])

st.subheader("Mean risk score by outcome")
st.bar_chart(summary.set_index("target")["mean_risk_score"])

st.subheader("Sample records")
st.dataframe(results.head(20))
