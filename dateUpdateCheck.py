from datetime import datetime, timedelta
import pandas as pd
import requests
import json

def check_update(all_data_date_list: list, mission_data: list):
    msg_str = f"New info in PSP\n"

    for df_m in mission_data:
        range_window = df_m[(df_m["TIME"].dt.date > (datetime.now() - timedelta(weeks=1)).date()) & (df_m["TIME"].dt.date <= (datetime.now()).date())]
        if(max(range_window["ProtonSpeed"]) > 0):
            for info_mission in all_data_date_list.keys():
                msg_str += (info_mission + f" : {all_data_date_list[info_mission]}\n")
            requests.post('https://ntfy.sh/PSP_SWP_SPI_SF0A_L3_MOM_dolphin', f'NEW INFO\n{msg_str}')
            with open('lastUpdate.json', 'w', encoding='utf-8') as f:
                json.dump(all_data_date_list, f, ensure_ascii=False, indent=4)
        else:
            print("Still the same...")