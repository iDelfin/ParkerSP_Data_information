import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


class System:
    def __init__(self, name: str, s_type: str, orbitation: list):
        self.name = name
        self.star_type = s_type
        self.orbit = orbitation

    def printSystem(self):
        final_df_mis = pd.DataFrame(columns=["x_se_plane", "y_se_plane"])
        for object_df in self.orbit:
            dict_plot_sys = {}
            dict_plot_sys["x_se_plane"] = object_df.se_lon_list_tail
            dict_plot_sys["y_se_plane"] = object_df.se_lat_list_tail
            temp_df = pd.DataFrame.from_dict(dict_plot_sys)
            temp_df["Object_Name"] = object_df.name
            final_df_mis = pd.concat([final_df_mis, temp_df], axis=0, ignore_index=True)

        plt.figure(figsize=(20,20))
        #sns.dark_palette("#b285bc", as_cmap=True)
        sns.set_style("darkgrid")
        orbit = sns.scatterplot(final_df_mis, x="x_se_plane", y="y_se_plane", hue="Object_Name")
        orbit.set_xlim(-30,30)
        orbit.set_ylim(-30,30)
        plt.scatter(x=0,y=0,s=100,color='r')
        plt.savefig("./Result/SolarSystem/solar_sistem_plt.png")
        plt.show()