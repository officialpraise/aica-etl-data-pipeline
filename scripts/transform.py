import pandas as pd


def transform_csv_data(csv_dataframe):
    """
    Transforms the DataFrame from the CSV file by selecting and renaming columns.

    Args:
        csv_dataframe (pd.DataFrame): The raw DataFrame created from the CSV file.

    Returns:
        pd.DataFrame: The transformed DataFrame with a standardized schema.
    """
    # Select the columns that are relevant for the project
    transformed_df = csv_dataframe[['country', 'capital', 'region', 'population', 'area', 'iso3']]
    # Rename columns for clarity and consistency before merging
    transformed_df = transformed_df.rename(columns={
        'country': 'country_name',
        'iso3': 'country_code_iso3'
    })
    return transformed_df

def transform_api_data(api_data):
    """
    Transforms the raw data extracted from the API into a clean DataFrame.

    Args:
        api_data (list): A list of dictionaries representing the data from the API.

    Returns:
        pd.DataFrame: The transformed DataFrame with selected and renamed columns.
    """
    # Convert the list of dictionaries into a pandas DataFrame
    api_dataframe = pd.DataFrame(api_data)
    # Select and rename columns to prepare for merging
    transformed_df = api_dataframe[['name', 'iso2Code', 'capitalCity', 'longitude', 'latitude']]
    transformed_df = transformed_df.rename(columns={
        'name': 'country_name',
        'iso2Code': 'country_code_iso2'
    })
    return transformed_df