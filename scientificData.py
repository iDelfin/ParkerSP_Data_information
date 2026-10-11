import pandas as pd
from cdasws import CdasWs
from datetime import datetime, timedelta

class MissionCall:

    def __init__(self, name: str, m_id: str, data_l: list):
        self.mission_name = name
        self.mission_id = m_id
        self.data_list = data_l

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
        df_return = pd.DataFrame.from_dict(self.mission_data)
        df_return["TIME"]=pd.to_datetime(df_return['Epoch'])
        return df_return