import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


class System:
    def __init__(self, name: str, type: str, orbitation: list):
        self.name = name
        self.type = type
        self.orbit = orbitation

    def printSystem(self):
        final_df_mis = pd.DataFrame(columns=["RAD_AU", "HG_LAT", "HG_LON", "SE_LAT", "SE_LON", "TIME", "x_se_plane", "y_se_plane", "z_se_plane", "x_hg_plane", "y_hg_plane", "z_hg_plane"])
        for object_df in self.orbit:
            final_df_mis = pd.concat([final_df_mis, object_df], axis=0, ignore_index=True)
    
        plt.figure(figsize=(20,20))
        #sns.dark_palette("#b285bc", as_cmap=True)
        sns.set_style("darkgrid")
        orbit = sns.scatterplot(final_df_mis, x="x_se_plane", y="y_se_plane", hue="Object_Name", markers='_')
        orbit.set_xlim(-30,30)
        orbit.set_ylim(-30,30)
        plt.scatter(x=0,y=0,s=100,color='r')
        plt.savefig("./Result/SolarSystem/solar_sistem_plt.png")
        plt.show()