import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Sunburst Chart: Soft Skills → Networking → Job Offers")

# Upload Excel file
uploaded_file = st.file_uploader("Upload the Excel file", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, sheet_name='education_career_success')

    # Group Soft Skills Score
    def group_soft_skills(score):
        if score <= 4:
            return "Low"
        elif score <= 7:
            return "Medium"
        else:
            return "High"

    # Group Networking Score
    def group_networking(score):
        if score <= 4:
            return "Low"
        elif score <= 7:
            return "Medium"
        else:
            return "High"

    df['Soft_Skills_Level'] = df['Soft_Skills_Score'].apply(group_soft_skills)
    df['Networking_Level'] = df['Networking_Score'].apply(group_networking)

    # Group data for sunburst
    sunburst_data = df.groupby(['Soft_Skills_Level', 'Networking_Level', 'Job_Offers']).size().reset_index(name='Count')

    # Create sunburst chart
    fig = px.sunburst(
        sunburst_data,
        path=['Soft_Skills_Level', 'Networking_Level', 'Job_Offers'],
        values='Count',
        title='Soft Skills → Networking → Job Offers'
    )

    st.plotly_chart(fig)
