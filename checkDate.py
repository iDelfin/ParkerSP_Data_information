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
    with open('lastUpdate.json', 'r', encoding='utf-8') as f:
        last_update = json.load(f)

    print(f"Time interval 2025-01-01 - {curr_date.date()}")
    
    planets_datasets = ["MERCURY_HELIO1DAY_POSITION", "VENUS_HELIO1HR_POSITION", "MARS_HELIO1DAY_POSITION", "JUPITER_HELIO1DAY_POSITION", "SATURN_HELIO1DAY_POSITION"]
    planets = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn"]
    planet_data = []
    planet_df = []
    # Dictionary of data last update
    all_data_date_list = {}
    amount_data = len(planets_datasets)
    
    PSP_status, PSP_data = cdas.get_data("PSP_SWP_SPI_SF0A_L3_MOM", ["SUN_DIST", "MAGF_INST", "SC_VEL_RTN_SUN"], "2025-01-01T04:04:15.000Z", f"{curr_date.year}-{curr_date.month}-{curr_date.day}T00:00:00.000Z")
    print(progressBar(progress, amount_data))
    progress+=1

    for p_ds in planets_datasets:
        p_status, p_data = cdas.get_data(p_ds, ['RAD_AU'], "2025-01-01T04:04:15.000Z", f"{curr_date.year}-{curr_date.month}-{curr_date.day}T00:00:00.000Z")
        planet_data.append(p_data)
        print(progressBar(progress, amount_data))
        progress+=1

    for planet_d in planet_data:
        # Planet Venus (Distance from sun to Venus)
        os.system("cls")
        planet_df.append(convert_to_df(planet_d, ['RAD_AU']))

    # Parker Space Probe data (Distance to the Sun, Magnification & Velocit of Space Probe relative to the Sun)
    os.system("cls")
    PSP_df = convert_to_df(PSP_data, ["SUN_DIST", "MAGF_INST", "SC_VEL_RTN_SUN"])


    for p_df, plane in zip(planet_df, planets):
        # Checking Last data date of Mercury
        last_date = p_df["TIME"][len(p_df["TIME"])-1].date()
        all_data_date_list[f"last_update_{plane}"] = f"{last_date.year}-{last_date.month}-{last_date.day}"

    # Checking Last data date of Parker Space Probe
    PSP_last_date = PSP_df["TIME"][len(PSP_df["TIME"])-1].date()
    all_data_date_list["last_update_PSP"] = f"{PSP_last_date.year}-{PSP_last_date.month}-{PSP_last_date.day}"

    check_update(all_data_date_list)