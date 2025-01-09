import numpy as np
import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:

    # try to open and read Excel file
    try:
        if filepath.endswith('.csv'):
            return pd.read_csv(filepath)
        elif filepath.endswith('.xlsx'):
            return pd.read_excel(filepath)
        else:
            raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")
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
    # Perform group by and aggregation
    return df.groupby(group_by_column).agg(agg_func)


def remove_sparse_columns(df: pd.DataFrame, threshold: int) -> pd.DataFrame:
    """
    remove sparse columns from dataframe
    :param df: dataframe
    :param threshold: integer
    :return: dataframe
    """
    # calculate the sum of each column
    column_totals = df.sum()

    # keep only the columns that meet the condition
    return df[list(column_totals[column_totals > threshold].index)]


def dimensionality_reduction(df: pd.DataFrame, num_components: int, meta_columns: list[str]) -> pd.DataFrame:
    #Saving meta data
    meta_data = df[meta_columns]

    #removing meta columns
    non_meta_data = df.drop(columns = meta_columns)

    #Calculate the mean of each column
    mean = non_meta_data.mean()

    #Normalize the data
    normalized_non_meta_data = non_meta_data - mean

    # Convert to NumPy array for covariance calculation
    normalized_array = normalized_non_meta_data.to_numpy()

    #Find covariance matrix
    cov_matrix = np.cov(normalized_array, rowvar=False)

    #Calculate the eigenvalues and eigenvectors
    eigen_vals, eigen_vecs = np.linalg.eigh(cov_matrix)

    #Sort eigen values and save list of orginal indexes
    sorted_indices = np.argsort(eigen_vals)[::-1]

    #Sort vects by sorted_indices
    sorted_eigen_vecs = eigen_vecs[:, sorted_indices]

    #Take only num_components columns
    principal_components = sorted_eigen_vecs[:, :num_components]

    #Project the data onto the principal components
    #matrix multiplication between a pandas.DataFrame (normalized_non_meta_data) and a NumPy ndarray (principal_components) NxM dot Mxnum_components
    reduced_data = np.dot(normalized_array, principal_components)

    # Convert reduced data to a DataFrame
    reduced_df = pd.DataFrame(
        reduced_data,
        columns=[f'PC{i + 1}' for i in range(num_components)],
        index=df.index
    )

    #Combine reduced data and meta data
    result_df = pd.concat([meta_data, reduced_df], axis=1)

    return result_df

