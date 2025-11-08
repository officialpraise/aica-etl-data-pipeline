import pandas as pd
import requests
import json

def extract_from_csv(file_path):
    """
    Extracts data from a specified CSV file into a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file that needs to be read.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the data from the CSV file.
    """
    dataframe = pd.read_csv(file_path)
    return dataframe

def extract_from_api(api_url):
    """
    Extracts JSON data from a public API.

    Args:
        api_url (str): The URL of the API endpoint to fetch data from.

    Returns:
        list: A list of dictionaries containing the core data from the API response.
    """
    response = requests.get(api_url)
    data = response.json()
    # The actual country data is typically in the second element of the response list
    return data[1]