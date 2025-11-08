import os
from scripts.analyze import print_basic_analysis, top_10_largest_countries_by_area, plot_countries_per_region, plot_top_populated_countries
from scripts.cleaning import clean_data
from scripts.extraction import extract_from_api, extract_from_csv
from scripts.merge import merge_data
from scripts.storage import store_as_csv, store_as_json
from scripts.transform import transform_api_data, transform_csv_data

 # Define constants for file paths and API URL
CSV_FILE_PATH = os.path.join('data', 'all_countries.csv')
WORLD_BANK_API_URL = 'http://api.worldbank.org/v2/country?format=json&per_page=300'
RAW_JSON_OUTPUT_PATH = 'data/api_extracted_data.json'
TRANSFORMED_CSV_OUTPUT_PATH = 'output/final_country_data.csv'

print("Starting the ETL pipeline...")

# --- EXTRACT ---
print("\nStep 1: Extracting data...")
csv_dataframe = extract_from_csv(CSV_FILE_PATH)
api_data = extract_from_api(WORLD_BANK_API_URL)

# Proceed only if both extractions were successful
if csv_dataframe is not None and api_data is not None:
    print("Data extraction successful.")

    # --- LOAD (Raw Data) ---
    print("\nStep 2: Storing raw extracted API data as JSON...")
    store_as_json(api_data, RAW_JSON_OUTPUT_PATH)
    print(f"Raw API data stored at '{RAW_JSON_OUTPUT_PATH}'")

    # --- TRANSFORM ---
    print("\nStep 3: Transforming data...")
    transformed_csv = transform_csv_data(csv_dataframe)
    transformed_api = transform_api_data(api_data)
    print("Data transformation successful.")

    # --- MERGE ---
    print("\nStep 4: Merging datasets...")
    merged_data = merge_data(transformed_csv, transformed_api)
    print("Merging successful.")

    # --- CLEAN ---
    print("\nStep 5: Cleaning data...")
    cleaned_data = clean_data(merged_data)
    print("Data cleaning successful.")

    # --- LOAD (Transformed Data) ---
    print("\nStep 6: Storing transformed data as CSV...")
    store_as_csv(cleaned_data, TRANSFORMED_CSV_OUTPUT_PATH)
    print(f"Transformed data stored at '{TRANSFORMED_CSV_OUTPUT_PATH}'")

    # --- BONUS: ANALYSIS ---
    print("\nStep 7: Performing bonus analysis...")
    print_basic_analysis(cleaned_data)
    top_10_largest_countries_by_area(cleaned_data)
    plot_countries_per_region(cleaned_data)
    plot_top_populated_countries(cleaned_data)
    print("Analysis plots saved in 'output' directory.")

    print("\nETL Pipeline finished successfully!")
else:
    print("\nETL Pipeline failed due to errors in data extraction.")