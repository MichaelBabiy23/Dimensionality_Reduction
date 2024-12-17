import numpy as np
import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """
    loading data from excel files
    :param filepath: String
    :return: dataFrame
    """
    # try to open and read Excel file
    try:
        return pd.read_excel(filepath)
    except Exception as e:
        print(f"Error loading file: {e}")
        return pd.DataFrame()


def group_and_aggregate_data(df: pd.DataFrame, group_by_column: str, agg_func) -> pd.DataFrame:
    """
    grouping by and aggregate the data frame
    :param df: DataFrame
    :param group_by_column: String
    :param agg_func: String array
    :return:
    """
    # dropping ballot_code column from the df data frame, grouping by the group_by_column variable and applying agg_func aggregation
    return df.drop(columns='ballot_code').groupby(group_by_column).agg(agg_func)


def remove_sparse_columns(df: pd.DataFrame, threshold: int) -> pd.DataFrame:
    """
    remove sparse columns from dataframe
    :param df: dataframe
    :param threshold: integer
    :return: dataframe
    """
    # index the table by city name and ballot code
    indexed_data = df.set_index(['city_name', 'ballot_code'])

    # calculate the sum of each column
    column_totals = indexed_data.sum()

    return indexed_data[list(column_totals[column_totals > threshold].index)]


def dimensionality_reduction(df: pd.DataFrame, num_components: int, meta_columns: list[str]) -> pd.DataFrame:
    # Saving meta data
    meta_data = df[meta_columns]

    # removing meta collums
    non_meta_data = df.drop(columns=meta_columns)

    # Calculate the mean of each column
    mean = non_meta_data.mean()

    # Normalize the data
    normalized_non_meta_data = non_meta_data - mean

    # Find covariance matrix
    cov_matrix = np.cov(normalized_non_meta_data, rowvar=False)

    # Calculate the eigenvalues and eigenvectors
    eigen_vals, eigen_vecs = np.linalg.eig(cov_matrix)

    # Sort eigen values and save list of orginal indexes
    sorted_indices = np.argsort(eigen_vals)[::-1]

    # Sort vects by sorted_indices
    sorted_eigen_vecs = eigen_vecs[:, sorted_indices]

    # Take only num_components columns
    principal_components = sorted_eigen_vecs[:, :num_components]

    # Project the data onto the principal components
    # matrix multiplication between a pandas.DataFrame (normalized_non_meta_data) and a NumPy ndarray (principal_components) NxM dot Mxnum_components
    reduced_data = normalized_non_meta_data @ principal_components

    labled_columns = {i: f'PC{i + 1}' for i in range(num_components)}
    reduced_data.rename(columns=labled_columns, inplace=True)

    # Combine reduced data and meta data
    result_df = pd.concat([meta_data, reduced_data], axis=1)

    return result_df