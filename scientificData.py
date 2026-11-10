import pandas as pd
import numpy as np
from cdasws import CdasWs
from datetime import datetime, timedelta

class MissionCall:

    def __init__(self, name: str, m_id: str, data_l:list=None):
        self.mission_name = name
        self.mission_id = m_id
        if(data_l != None):
            self.data_list = data_l
        else:
            self.data_list = ['RAD_AU', "HG_LAT", "HG_LON", "SE_LAT", "SE_LON"]

        cdas = CdasWs()
        curr_date = datetime.now() - timedelta(days=1)

        self.mission_status, self.mission_data = cdas.get_data(
            self.mission_id, 
            self.data_list, 
            "2025-01-01T04:04:15.000Z", 
            f"{curr_date.year}-{curr_date.month}-{curr_date.day}T00:00:00.000Z"
        )

    def mission_brief(self):
        print(f"Mission Name: {self.mission_name}\nMission id: {self.mission_id}\nData to retreve: {self.data_list}")

    def observe_data_df(self):
        print(self.mission_status)
        df_return = pd.DataFrame.from_dict(self.mission_data)
        df_return["TIME"]=pd.to_datetime(df_return['Epoch'])
        
        return df_return

    def convert_coord(self, df_md: pd.DataFrame):
        
        df_md["Object_Name"] = self.mission_name
        theta_lat_se = np.radians(df_md["SE_LAT"])
        phi_lon_se = np.radians(df_md["SE_LON"])
        theta_lat_hg = np.radians(df_md["HG_LAT"])
        phi_lon_hg = np.radians(df_md["HG_LON"])

        df_md["x_se_plane"] = (df_md["RAD_AU"] * np.cos(theta_lat_se) * np.cos(phi_lon_se))
        df_md["y_se_plane"] = (df_md["RAD_AU"] * np.cos(theta_lat_se) * np.sin(phi_lon_se))
        df_md["z_se_plane"] = (df_md["RAD_AU"] * np.sin(theta_lat_se))

        df_md["x_hg_plane"] = (df_md["RAD_AU"] * np.cos(theta_lat_hg) * np.cos(phi_lon_hg))
        df_md["y_hg_plane"] = (df_md["RAD_AU"] * np.cos(theta_lat_hg) * np.sin(phi_lon_hg))
        df_md["z_hg_plane"] = (df_md["RAD_AU"] * np.sin(theta_lat_hg))

        return df_md

