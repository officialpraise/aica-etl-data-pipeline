# ETL Pipeline for Country Data

This project implements an ETL (Extract, Transform, Load) pipeline to process country data from two different sources: a CSV file and a World Bank API. The pipeline extracts the data, cleans it, transforms it into a consistent format, merges it, and then stores the final dataset as a CSV file. Additionally, it performs a basic analysis of the transformed data and generates plots.

## Project Structure

```
.
├── data
│   └── all_countries.csv
├── output
│   ├── final_country_data.csv
│   ├── countries_per_region.png
│   └── top_10_populated_countries.png
├── scripts
│   ├── analyze.py
│   ├── cleaning.py
│   ├── extraction.py
│   ├── merge.py
│   ├── storage.py
│   └── transform.py
├── main.py
├── README.md
└── requirements.txt
```

-   `main.py`: The main script that orchestrates the ETL pipeline.
-   `scripts/`: Contains the Python modules for each step of the ETL process.
-   `data/`: Contains the raw data files.
-   `output/`: Contains the final transformed dataset and generated plots.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```
2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the ETL pipeline:**
    ```bash
    python main.py
    ```

## ETL Process

### 1. Extraction

-   Data is extracted from `data/all_countries.csv`.
-   Data is extracted from the World Bank API.

### 2. Transformation

-   The data from both sources is transformed to have a consistent schema.
-   Relevant columns are selected and renamed.

### 3. Merging

-   The two datasets are merged into a single dataset based on the country name.

### 4. Cleaning

-   The merged data is cleaned to handle missing values and duplicates.

### 5. Storage

-   The final, merged and cleaned dataset is saved as `output/final_country_data.csv`.

### 6. Analysis

-   A simple analysis is performed on the final dataset to show:
    -   Number of countries per region.
    -   Top 10 most populated countries.
    -   Top 10 largest countries by area.
-   The following plots are generated and saved in the `output` directory:
    -   A pie chart showing the number of countries per region.
    -   A bar chart showing the top 10 most populated countries.
