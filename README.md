# Education Data Pipeline – Peru (INEI ENAHO)

## Overview

This project builds an end-to-end ETL pipeline that processes education data from Peru's INEI 2022 National Census and loads it to PostgreSQL for analysis.

## Pipeline Architecture

Raw Data → Extract → Transform → Load → PostgreSQL → SQL Analysis

## Tech Stack

- Python (Pandas)
- PostgreSQL
- SQL
- JSON (for categorical mappings)

## Pipeline Steps

1. **Extract**: Ingest raw INEI dataset (handles encoding issues)
2. **Transform**:
   - Clean columns
   - Map categorical variables using JSON
   - Standardize data
3. **Load**: Store processed data into PostgreSQL

## Data validation

The pipeline includes validation step that secures the file exists and its not empty for further analysis.

## Example Insights

- Most common education level
- Education level by region
- Education distribution by age groups
- Percentage of population with completed high school

## How to Run

1. Create a PostgreSQL database
2. Run 'sql/schema.sql' to create the table
3. Run 'pipeline.py' to execute the pipeline
4. Run examples queries in 'sql/queries.sql'

## Data

A sample dataset of 100 random entries is included for demonstration.
Full dataset can be obtained from INEI.

## Key Features

- Handles non-UTF8 encoded data (latin-1)
- Config-driven transformations (JSON mappings)
- Modular ETL pipeline
- SQL-based analysis

## Limitations

- The pipeline runs in batch mode only
- Data must be manually updated
- Mappings are hardcoded in JSON file
- Basic data validation
