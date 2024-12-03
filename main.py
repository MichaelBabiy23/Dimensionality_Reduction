import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    '''
    loading data from excel files
    :param filepath:
    :return: dataFrame
    '''
    return pd.read_excel(filepath)


data = load_data(filepath='data/knesset_25.xlsx')
print(data)
