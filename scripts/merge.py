import pandas as pd


def merge_data(csv_df, api_df):
    """
    Merges two DataFrames into a single DataFrame based on a common column.

    Args:
        csv_df (pd.DataFrame): The transformed DataFrame from the CSV data.
        api_df (pd.DataFrame): The transformed DataFrame from the API data.

    Returns:
        pd.DataFrame: A new DataFrame containing the merged data.
    """
    # Perform an inner merge to combine rows that have matching 'country_name' in both DataFrames
    merged_dataframe = pd.merge(csv_df, api_df, on='country_name', how='inner')
    return merged_dataframe