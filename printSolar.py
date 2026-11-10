from matplotlib import pyplot as plt
import seaborn as sns
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

    for object_df in planet_df_list:
        final_df_mis = pd.DataFrame(columns=["RAD_AU", "HG_LAT", "HG_LON", "SE_LAT", "SE_LON", "TIME", "x_se_plane", "y_se_plane", "z_se_plane", "x_hg_plane", "y_hg_plane", "z_hg_plane"])
        final_df_mis = pd.concat([final_df_mis, object_df], axis=0, ignore_index=True)
    sns.scatterplot(final_df_mis, x="x_se_plane", y="y_se_plane", hue="Object_Name", markers='_')
    plt.scatter(x=0,y=0,s=100,color='r')
    plt.show()
    plt.savefig("./Result/SolarSystem/solar_sistem_plt.jpg")
    