import requests
import pandas as pd
import re
import time
from datetime import datetime

MASTER_FILE = 'RPLL-visibility-data-2026.csv'
URL = "https://aviationweather.gov/api/data/metar?ids=RPLL&hours=24&format=json"

def sync_and_heal():
    try:
        response = requests.get(URL)
        data = response.json()
        
        new_rows = []
        for report in data:
            raw_time = report.get('reportTime').replace('T', ' ').replace('Z', '')[:16]
            raw_metar = report.get('rawOb', '')
            
            # Extract meters
            match = re.search(r'KT\s+(\d{4})\b', raw_metar)
            vis = int(match.group(1)) if match else (9999 if 'CAVOK' in raw_metar else 9999)
            
            new_rows.append({'station': 'RPLL', 'valid': raw_time, 'visibility_meters': vis})

        # Load, Merge, Deduplicate, and Sort
        df_new = pd.DataFrame(new_rows)
        if os.path.exists(MASTER_FILE):
            df_old = pd.read_csv(MASTER_FILE)
            df_final = pd.concat([df_old, df_new]).drop_duplicates(subset=['valid']).sort_values('valid')
        else:
            df_final = df_new

        df_final.to_csv(MASTER_FILE, index=False)
        print(f"Sync complete at {datetime.now()}. Master file row count: {len(df_final)}")

    except Exception as e:
        print(f"Error: {e}")

import os
while True:
    sync_and_heal()
    time.sleep(3600) 