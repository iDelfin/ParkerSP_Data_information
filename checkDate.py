from convertDataframe import convert_to_df
from dateUpdateCheck import check_update
from datetime import datetime, timedelta
from cdasws import CdasWs
import pandas as pd
import numpy as np
import requests
import json

def dateProcess():
    cdas = CdasWs()

    curr_date = datetime.now()
    curr_date = curr_date - timedelta(days=1)
    with open('lastUpdate.json', 'r', encoding='utf-8') as f:
        last_update = json.load(f)

    print(f"Time interval 2025-01-01 - {curr_date.date()}")
    status, data = cdas.get_data("PSP_SWP_SPI_SF0A_L3_MOM", ["SUN_DIST", "MAGF_INST", "SC_VEL_RTN_SUN"], "2025-01-01T04:04:15.000Z", f"{curr_date.year}-{curr_date.month}-{curr_date.day}T00:00:00.000Z")

    df = convert_to_df(data)

    last_date = df["TIME"][len(df["TIME"])-1].date()
    data_info = {"last_update": f"{last_date.year}-{last_date.month}-{last_date.day}"}

    check_update(last_update, last_date, data_info)