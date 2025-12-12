from datetime import datetime
import pandas as pd
import requests
import json

def check_update(last_date, data_info):
    requests.post('https://ntfy.sh/PSP_SWP_SPI_SF0A_L3_MOM_dolphin', f'NEW INFO: {last_date.year}-{last_date.month}-{last_date.day}')
    with open('lastUpdate.json', 'w', encoding='utf-8') as f:
        json.dump(data_info, f, ensure_ascii=False, indent=4)