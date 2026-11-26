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
        #final_df_mis = pd.DataFrame(columns=["RAD_AU", "HG_LAT", "HG_LON", "SE_LAT", "SE_LON", "TIME", "x_se_plane", "y_se_plane", "z_se_plane"])
        dict_plot_sys = {"x_se_plane":[],"y_se_plane":[],"Object_Name":[]}
        for object_df in self.orbit:
            dict_plot_sys["x_se_plane"].append(object_df.curr_se_lon)
            dict_plot_sys["y_se_plane"].append(object_df.curr_se_lat)
            dict_plot_sys["Object_Name"].append(object_df.name)
            #final_df_mis = pd.concat([final_df_mis, object_df], axis=0, ignore_index=True)
        final_df_mis = pd.DataFrame.from_dict(dict_plot_sys)

        plt.figure(figsize=(20,20))
        #sns.dark_palette("#b285bc", as_cmap=True)
        sns.set_style("darkgrid")
        orbit = sns.scatterplot(final_df_mis, x="x_se_plane", y="y_se_plane", hue="Object_Name", markers='_')
        orbit.set_xlim(-30,30)
        orbit.set_ylim(-30,30)
        plt.scatter(x=0,y=0,s=100,color='r')
        plt.savefig("./Result/SolarSystem/solar_sistem_plt.png")
        plt.show()