import streamlit as st
import pandas as pd

st.title("Student Performance Analysis")

df = pd.read_csv("StudentsPerformance.csv")

st.write("### Dataset")
st.dataframe(df)

st.write("### Average Scores")

math_avg = df["math score"].mean()
reading_avg = df["reading score"].mean()
writing_avg = df["writing score"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Average Math Score", round(math_avg, 2))
col2.metric("Average Reading Score", round(reading_avg, 2))
col3.metric("Average Writing Score", round(writing_avg, 2))

st.write("### Average Score by Test Preparation")

result = df.groupby("test preparation course")[
    ["math score", "reading score", "writing score"]
].mean()
st.bar_chart(result)