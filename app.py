
import streamlit as st
import pandas as pd

# Sample data for the dashboard
data = [
    {
        "Name of the Course": "Data Analysis 101",
        "Progress": 75,
        "Status": "Started",
        "Started On": "2023-08-01",
        "Completed On": "",
        "Expired After": 5
    },
    {
        "Name of the Course": "Python Programming",
        "Progress": 100,
        "Status": "Completed",
        "Started On": "2023-06-15",
        "Completed On": "2023-07-15",
        "Expired After": 0
    },
    {
        "Name of the Course": "Project Management",
        "Progress": 40,
        "Status": "",
        "Started On": "2023-07-01",
        "Completed On": "",
        "Expired After": 0
    }
]

# Create a DataFrame
df = pd.DataFrame(data)

# Update status based on Expired After and Completed On
df["Status"] = df.apply(lambda row: "Not Completed" if row["Expired After"] == 0 and row["Status"] != "Completed" else row["Status"], axis=1)

# Add Extension and Retake links based on conditions
df["Extension"] = df["Status"].apply(lambda x: "Request Extension" if x == "Not Completed" else "")
df["Retake"] = df["Status"].apply(lambda x: "Retake Course" if x == "Started" else "")

# Streamlit dashboard layout
st.title("Learner Dashboard")

for _, row in df.iterrows():
    st.subheader(row["Name of the Course"])
    st.progress(row["Progress"])
    st.write(f"**Status:** {row['Status']}")
    st.write(f"**Started On:** {row['Started On']}")
    st.write(f"**Completed On:** {row['Completed On']}")
    st.write(f"**Expired After:** {row['Expired After']} days")
    if row["Extension"]:
        st.button(row["Extension"])
    if row["Retake"]:
        st.button(row["Retake"])
    st.markdown("---")
