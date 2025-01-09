# Dimensionality Reduction Application

This project provides a web application for performing dimensionality reduction on datasets using Principal Component Analysis (PCA). It includes data grouping and aggregation features and supports visualizing reduced dimensions. Built using Streamlit, it offers an intuitive interface for handling CSV and Excel files.

---

## Features

1. **File Upload**:
   - Upload CSV or Excel files containing the data to be analyzed.

2. **Grouping and Aggregation**:
   - Group data by a selected column and apply aggregate functions such as `sum`, `mean`, `min`, `max`, etc.

3. **Dimensionality Reduction**:
   - Reduce data dimensions using PCA.
   - Supports visualization for 1D, 2D, and 3D PCA.

4. **Interactive Visualizations**:
   - Use Plotly to display reduced data as scatter plots.

---

## How to Use

1. **Install Requirements**:
   - Install the necessary libraries using `pip install -r requirements.txt`. The main dependencies are:
     - `streamlit`
     - `pandas`
     - `numpy`
     - `plotly`

2. **Run the Application**:
   - Use `streamlit run app.py` to start the app.

3. **Upload Data**:
   - Choose a CSV or Excel file to upload.

4. **Configure Settings**:
   - Select the column to group by and an aggregate function.
   - Specify the number of PCA components (1, 2, or 3).
   - Specify the display type of the data (Row-wise or Party-wise).

5. **View Results**:
   - Click the "Calculate & Display" button to view grouped, aggregated, and reduced data alongside visualizations.

---

## Files and Functions

### `app.py`

This is the main file for running the Streamlit application.

- **Functions**:
  - `display_data`: Visualizes PCA results using scatter plots.
  - Handles file upload, grouping, and dimensionality reduction through user inputs.

### `functions_utils.py`

Contains utility functions for data processing.

- **Functions**:
  - `load_data(filepath)`: Loads data from a file (CSV or Excel).
  - `group_and_aggregate_data(df, group_by_column, agg_func)`: Groups and aggregates a DataFrame.
  - `remove_sparse_columns(df, threshold)`: Removes columns with totals below a threshold.
  - `dimensionality_reduction(df, num_components, meta_columns)`: Performs PCA to reduce dimensionality.

---

## Example Workflow

1. **Upload a Dataset**:
   - The app accepts datasets in CSV or Excel format.

2. **Select Grouping and Aggregation**:
   - Choose a column and an aggregation function (e.g., group by "City" and calculate "sum").

3. **Set PCA Components**:
   - Input the desired number of PCA components (e.g., 2 for 2D visualization).

4. **View Results**:
   - Visualize the reduced data in an interactive chart or download it for further analysis.

---
