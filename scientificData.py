class MissionCall:

    def __init__(self, name: str, m_id: str, data_l: list):
        self.mission_name = name
        self.mission_id = m_id
        self.data_list = data_l

    def mission_brief(self):
        print(f"Mission Name: {self.mission_name}\nMission id: {self.mission_id}\nData to retreve: {self.data_list}")