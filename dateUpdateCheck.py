from datetime import datetime
import pandas as pd
import requests
import json

def check_update(last_date, all_data_date_list):
    msg_str =''
    for info_mission in all_data_date_list.keys():
        msg_str += (info_mission + f" : {all_data_date_list[info_mission]}\n")
    requests.post('https://ntfy.sh/PSP_SWP_SPI_SF0A_L3_MOM_dolphin', f'NEW INFO\n{msg_str}')
    with open('lastUpdate.json', 'w', encoding='utf-8') as f:
        json.dump(all_data_date_list, f, ensure_ascii=False, indent=4)