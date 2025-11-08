import pandas as pd

def clean_data(dataframe):
    """
    Cleans the merged DataFrame by handling missing values and removing duplicates.

    Args:
        dataframe (pd.DataFrame): The merged DataFrame to be cleaned.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    # Remove rows with any missing values
    dataframe.dropna(inplace=True)
    
    # Remove duplicate rows
    dataframe.drop_duplicates(inplace=True)
    
    return dataframe
