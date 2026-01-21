import pandas as pd
import numpy as np
import os

def printSolarSystem(planet_df_list, mission_df_list, planets):
    distance_df = pd.DataFrame(columns=["Object", "Distance_AU"])
    for planet, df in zip(planets, planet_df_list):
        single_p_df = pd.DataFrame({"Object":[planet], "Distance_AU":[df.iloc[-1]["RAD_AU"]]})
        distance_df = pd.concat([distance_df, single_p_df], axis=0, ignore_index=True)
    
    print(f'''
\t********
\t********
\t********
\t********
          ''')
    
    for planet_print, distance in zip(distance_df["Object"], distance_df["Distance_AU"]):
        if(not(planet_print in ["Jupiter", "Saturn", "Uranus", "Neptune"])):
            print(f'''
\t    *
\t{planet_print}
   {distance}     
                ''')
        else:
            print(f'''
\t   **
\t   **
\t{planet_print}
   {distance}     
                ''')