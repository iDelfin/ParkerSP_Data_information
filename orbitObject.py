from cdasws import CdasWs
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

class OrbitObject:
    def __init__(self, name: str, dataset_id: str, o_type: str):

        # Assigne context variables
        self.name = name
        self.ds_id = dataset_id
        self.o_type = o_type

        # Start of coord calculation
        # Defin object of CdasWS
        col_pos = ['RAD_AU', "HG_LAT", "HG_LON", "SE_LAT", "SE_LON"]
        cdas = CdasWs()
        curr_date = datetime.now() - timedelta(days=1)

        # Call the servicce and obtain the data
        # TODO: 
        # -[ ] error managment
        mission_status, mission_data = cdas.get_data(
                    self.ds_id, 
                    col_pos, 
                    "2025-01-01T04:04:15.000Z", 
                    f"{curr_date.year}-{curr_date.month}-{curr_date.day}T00:00:00.000Z"
                )

        # Convert to to DF and transform date to datetime
        df_data = pd.DataFrame.from_dict(mission_data)
        df_data["Epoch"]=pd.to_datetime(df_data['Epoch']) # Could comment tbh

        # Convert lat and lon to radians and assign to theta and phi
        theta_lat_se = np.radians(df_data["SE_LAT"])
        phi_lon_se = np.radians(df_data["SE_LON"])

        # Calculation for ploting
        df_data["x_se_plane"] = (df_data["RAD_AU"] * np.cos(theta_lat_se) * np.cos(phi_lon_se))
        df_data["y_se_plane"] = (df_data["RAD_AU"] * np.cos(theta_lat_se) * np.sin(phi_lon_se))
        df_data["z_se_plane"] = (df_data["RAD_AU"] * np.sin(theta_lat_se))

        # Assigne the current position to plot
        self.curr_se_lon = df_data["x_se_plane"].iloc[-1]
        self.curr_se_lat = df_data["y_se_plane"].iloc[-1]
        self.distance_au = df_data["RAD_AU"].iloc[-1]

    def printGeneralInfo(self):
        print(f"{self.name}\nDistance:\t{self.distance_au:5f}")
        if(self.o_type == "M"):
            print(f"Mission in System")

    def showInMap(self):
        print(f"Still in dev... chowy :c")