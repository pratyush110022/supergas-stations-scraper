# SUPERGAS AutoGas Dealer Scraper

Python data collection for SUPERGAS dealer locations. The script queries the dealer-search API across a configured latitude/longitude grid, combines results, removes duplicate dealer IDs, and exports an Excel workbook.

## How it works

1. Defines a grid of latitude and longitude search points.
2. Sends POST requests to the SUPERGAS dealer-search endpoint for the Autogas dealer type.
3. Builds a bounding box around each grid point and collects the returned dealer records.
4. Stores records by dealer ID so repeated results from overlapping search areas do not create duplicate rows.
5. Sorts the results by station/dealer name and writes an Excel workbook.

## Data fields

The workbook includes fields returned by the source such as:

- Dealer ID and station/dealer name
- Latitude and longitude
- Phone, email, and website
- Store type
- Preferred-partner and delivery flags
- Bio flag and icon metadata

## Files

- Super_Scraper.py — scraper entry point
- `SUPERGAS_All_Stations.xlsx` — existing scraper output workbook
- requirements.txt — Python dependencies

## Requirements and setup

- Python 3.10 or a compatible version
- Packages listed in requirements.txt

    python -m venv .venv
    .venv/Scripts/Activate.ps1
    pip install -r requirements.txt

## Configuration and run

Review Super_Scraper.py before running. The API URL, request headers, grid coordinate lists, and output filename are defined near the top of the script. Edit the latitudes and longitudes lists to change search coverage.

Run:

    python Super_Scraper.py

The script creates SUPERGAS_All_Stations.xlsx in the current working directory. If Excel writing fails because the workbook engine is missing, install openpyxl.

## Notes

- Search completeness depends on the API's response for each grid box; the configured grid is an approximation of coverage, not a guarantee that every dealer is returned.
- Source API behavior and response fields can change.
- Follow the source website's terms and applicable policies when collecting or redistributing data.

## Synthetic sample data

[`sample_synthetic_12_records.csv`](sample_synthetic_12_records.csv) contains **12 synthetic test records** using the scraper's output schema. These records were generated for schema inspection and portfolio/demo purposes; they were not collected from the source website or API. Names and addresses are fictional, contact details and example.com links are placeholders, coordinates are illustrative, and ratings/prices are not real or current. Do not use them for real-world navigation or pricing decisions.
