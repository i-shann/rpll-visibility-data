# RPLL Visibility Data Logger (2025-2026)

## Project Overview
This project automates the collection of visibility data (in meters) for **Ninoy Aquino International Airport (RPLL)**. The data is pulled directly from the NOAA Aviation Weather API and processed to maintain historical archive.

## Data Structure
The data is stored in `RPLL-visibility-data-2026.csv` with the following columns:
* **station**: The ICAO code for the airport (RPLL).
* **valid**: The timestamp of the observation (YYYY-MM-DD HH:MM).
* **visibility_meters**: The visibility recorded in meters (e.g., 9999 for 10km+).

## Automation (GitHub Actions)
This repository uses **GitHub Actions** to fetch data automatically.
- **Frequency**: Every hour (at the top of the hour).
- **Self-Healing**: The script fetches the last 24 hours of data per run. If the GitHub server misses a cycle, it will automatically backfill the missing hours during the next successful run.
- **Deduplication**: The script checks timestamps before appending; it will never save the same observation twice.

## Instructions 
### 1. How to download the data
Simply download the `RPLL-visibility-data-2026.csv` file from this repository. It is updated hourly.

### 2. Monitoring
If you suspect data is missing, check the **Actions** tab at the top of the GitHub page.
- **Green Check**: The script ran successfully.
- **Red X**: There is an error (likely an API change or permission issue).

### 3. Modifying the Script
The logic lives in `logger.py`. If you need to collect other data points (like Temperature or Pressure), modify the `sync_and_heal()` function to include those JSON keys from the NOAA API.

---
**Maintained by:** Visibility Monitoring Team
**Last Setup Update:** January 2026
