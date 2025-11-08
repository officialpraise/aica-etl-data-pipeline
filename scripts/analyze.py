import matplotlib.pyplot as plt
import os

def print_basic_analysis(dataframe):
    """
    Performs a simple analysis on the final DataFrame and prints the results.

    Args:
        dataframe (pd.DataFrame): The final merged and transformed DataFrame.

    Returns:
        None
    """
    print("\n--- Basic Data Analysis ---")
    print("\nNumber of countries per region:")
    print(dataframe['region'].value_counts())
    print("\nTop 10 most populated countries in the dataset:")
    # Display the 10 largest countries by population
    print(dataframe.nlargest(10, 'population')[['country_name', 'population', 'region']])

def top_10_largest_countries_by_area(dataframe):
    """
    Analyzes and prints the top 10 largest countries by area.

    Args:
        dataframe (pd.DataFrame): The final merged and transformed DataFrame.

    Returns:
        None
    """
    print("\nTop 10 largest countries by area:")
    print(dataframe.nlargest(10, 'area')[['country_name', 'area', 'region']])

def plot_countries_per_region(dataframe, output_path='output'):
    """
    Generates and saves a pie chart of the number of countries per region.

    Args:
        dataframe (pd.DataFrame): The DataFrame containing country data.
        output_path (str): The directory to save the plot in.
    """
    region_counts = dataframe['region'].value_counts()
    plt.figure(figsize=(10, 8))
    plt.pie(region_counts, labels=region_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Number of Countries per Region')
    plt.ylabel('')
    plt.savefig(os.path.join(output_path, 'countries_per_region.png'))
    plt.close()

def plot_top_populated_countries(dataframe, output_path='output'):
    """
    Generates and saves a bar chart of the top 10 most populated countries.

    Args:
        dataframe (pd.DataFrame): The DataFrame containing country data.
        output_path (str): The directory to save the plot in.
    """
    top_10_population = dataframe.nlargest(10, 'population')
    plt.figure(figsize=(12, 6))
    plt.bar(top_10_population['country_name'], top_10_population['population'])
    plt.xlabel('Country')
    plt.ylabel('Population')
    plt.title('Top 10 Most Populated Countries')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'top_10_populated_countries.png'))
    plt.close()