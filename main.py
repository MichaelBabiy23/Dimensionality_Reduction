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
    # identify numeric columns
    numeric_columns = df.select_dtypes(include=[np.integer]).columns

    # calculate the sum of each column
    column_totals = df[numeric_columns].sum()

    # return updated dataframe that suitable for the threshold
    # column_totals[column_totals >= threshold] returns a series (label, index)
    # the index information contains the labels of the rows
    return df[column_totals[column_totals >= threshold].index]
