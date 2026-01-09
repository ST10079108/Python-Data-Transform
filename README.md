# Python-Data-Transform

# Python Data Transformation Project

## Overview
This project demonstrates a simple data pipeline step where raw CSV data is ingested,
validated, transformed, and exported in a cleaned format.

## Features
- Loads raw CSV data using pandas
- Performs basic data validation (row count, column inspection)
- Adjust column names
- Deletes null records
- Outputs a cleaned CSV file ready for loading into a database

## Instructions to run
1. Ensure Python and pandas are installed
2. Place `raw_data.csv` in the same directory as the script
3. Run:
   ```bash
   python transform_data.py
