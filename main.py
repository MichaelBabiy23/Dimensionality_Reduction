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