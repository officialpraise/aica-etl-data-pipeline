import json


def store_as_json(data, filename):
    """
    Stores data (e.g., a list of dictionaries) into a JSON file.

    Args:
        data (list): The data to be stored in the JSON file.
        filename (str): The name and path of the output JSON file.

    Returns:
        None
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def store_as_csv(dataframe, filename):
    """
    Stores a pandas DataFrame as a CSV file.

    Args:
        dataframe (pd.DataFrame): The DataFrame to be saved.
        filename (str): The name and path for the output CSV file.

    Returns:
        None
    """
    # Save the DataFrame to a CSV file without the pandas index
    dataframe.to_csv(filename, index=False)