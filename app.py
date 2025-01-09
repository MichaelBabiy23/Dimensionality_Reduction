import streamlit as st
from functions_utils import load_data, group_and_aggregate_data, dimensionality_reduction
import pandas as pd
import numpy as np
import plotly.express as px

def display_data(df, num_components):
    if  num_components == 0:
        st.write('This is what your data looks like when reduced to 0 dimensions:')
        gif_url = "https://media1.tenor.com/m/RmbNSOau1FkAAAAd/wait-a-minute-wait-a-second.gif"
        st.image(gif_url, caption="This guy will find the data for you", use_column_width=True)
        return
    if num_components == 1:
        fig = px.scatter(df, x='PC1', y=[0] * len(df), title="1D PCA")
    elif num_components == 2:
        fig = px.scatter(df, x='PC1', y='PC2', title="2D PCA")
    elif num_components == 3:
        fig = px.scatter_3d(df, x='PC1', y='PC2', z='PC3', title="2D PCA")
    else:
        st.dataframe(df)
        return
    st.plotly_chart(fig)
    st.dataframe(df)

# Title of the app
st.title("Dimensionality Reduction")

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

print(type(uploaded_file))
if uploaded_file is not None:
    if uploaded_file.name.endswith("csv"):
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith("xlsx"):
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(uploaded_file)

    isReady = False

    # Selectbox for choosing a column from the dataframe
    column = st.selectbox("Select a column to groupby", [""] + list(df.columns))

    agg_func = st.selectbox("Select an aggregate function", [""] + [
    'sum',
    'mean',
    'median',
    'min',
    'max',
    'count', 'std'])

    # Text input for the number of components (only shows if a column is selected)
    num_components = st.text_input("Set a number of components")

    # Radio button to choose between city-wise or party-wise
    selection = st.radio("Select data to display:", ['City-wise', 'Party-wise'], index=0)

    if num_components:
        try:
            num_components = int(num_components)  # Convert the input to an integer

            if num_components < 0:
                st.error("Please enter a positive integer greater than 0.")

            if column != "" and agg_func != "":
                isReady = True

        except ValueError:
            st.error("Invalid input. Please enter a valid integer.")

    if st.button("Calculate & Display", disabled=not isReady):
        aggregated_df = group_and_aggregate_data(df, column, agg_func)
        if selection == "Party-wise":
            aggregated_df = aggregated_df.T
        reduced_df = dimensionality_reduction(aggregated_df, num_components, [])
        display_data(reduced_df, num_components)


