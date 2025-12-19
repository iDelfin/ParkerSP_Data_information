from convertDataframe import convert_to_df
from dateUpdateCheck import check_update
from datetime import datetime, timedelta
from progressBar import progressBar
from cdasws import CdasWs
import pandas as pd
import numpy as np
import requests
import json
import os

def dateProcess():
    progress = 1
    cdas = CdasWs()

    curr_date = datetime.now()
    curr_date = curr_date - timedelta(days=1)
    amount_data = 4
    with open('lastUpdate.json', 'r', encoding='utf-8') as f:
        last_update = json.load(f)

    print(f"Time interval 2025-01-01 - {curr_date.date()}")
    
    PSP_status, PSP_data = cdas.get_data("PSP_SWP_SPI_SF0A_L3_MOM", ["SUN_DIST", "MAGF_INST", "SC_VEL_RTN_SUN"], "2025-01-01T04:04:15.000Z", f"{curr_date.year}-{curr_date.month}-{curr_date.day}T00:00:00.000Z")
    print(progressBar(progress, amount_data))
    progress+=1

    mercury_status, mercury_data = cdas.get_data("MERCURY_HELIO1DAY_POSITION", ['RAD_AU'], "2025-01-01T04:04:15.000Z", f"{curr_date.year}-{curr_date.month}-{curr_date.day}T00:00:00.000Z")
    print(progressBar(progress, amount_data))
    progress+=1

    venus_status, venus_data = cdas.get_data("VENUS_HELIO1HR_POSITION", ['RAD_AU'], "2025-01-01T04:04:15.000Z", f"{curr_date.year}-{curr_date.month}-{curr_date.day}T00:00:00.000Z")
    print(progressBar(progress, amount_data))
    progress+=1

    mars_status, mars_data = cdas.get_data("MARS_HELIO1DAY_POSITION", ['RAD_AU'], "2025-01-01T04:04:15.000Z", f"{curr_date.year}-{curr_date.month}-{curr_date.day}T00:00:00.000Z")
    print(progressBar(progress, amount_data))
    progress+=1	

    # Dictionary of data last update
    all_data_date_list = {}

    # Planet Venus (Distance from sun to Venus)
    os.system("cls")
    mercury_df = convert_to_df(mercury_status, ['RAD_AU'])

    # Planet Venus (Distance from sun to Venus)
    os.system("cls")
    venus_df = convert_to_df(venus_data, ['RAD_AU'])
    
    # Planet Mars (Distance from sun to Venus)
    os.system("cls")
    mars_df = convert_to_df(mars_data, ['RAD_AU'])

    # Parker Space Probe data (Distance to the Sun, Magnification & Velocit of Space Probe relative to the Sun)
    os.system("cls")
    PSP_df = convert_to_df(PSP_data, ["SUN_DIST", "MAGF_INST", "SC_VEL_RTN_SUN"])


    # Checking Last data date of Mercury
    mercury_last_date = mercury_df["TIME"][len(mercury_df["TIME"])-1].date()
    all_data_date_list["last_update_mercury"] = f"{mercury_last_date.year}-{mercury_last_date.month}-{mercury_last_date.day}"

    # Checking Last data date of Venus
    venus_last_date = venus_df["TIME"][len(venus_df["TIME"])-1].date()
    all_data_date_list["last_update_venus"] = f"{venus_last_date.year}-{venus_last_date.month}-{venus_last_date.day}"

    mars_last_date = mars_df["TIME"][len(mars_df["TIME"])-1].date()
    all_data_date_list["last_update_mars"] = f"{mars_last_date.year}-{mars_last_date.month}-{mars_last_date.day}"

    # Checking Last data date of Parker Space Probe
    PSP_last_date = PSP_df["TIME"][len(PSP_df["TIME"])-1].date()
    all_data_date_list["last_update_PSP"] = f"{PSP_last_date.year}-{PSP_last_date.month}-{PSP_last_date.day}"

    check_update(all_data_date_list)