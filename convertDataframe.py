from datetime import datetime
import pandas as pd

def convert_to_df(data):

    df = pd.DataFrame(columns=["TIME","SUN_DIST", "SC_VEL_RTN_SUN", "MAGF_INST"])
    df["TIME"]=pd.to_datetime(data['Epoch'])
    df['SUN_DIST']=data["SUN_DIST"]
    df["MAGF_INST"]=data["MAGF_INST"]
    df["SC_VEL_RTN_SUN"]=data["SC_VEL_RTN_SUN"]
    df["hour"]=df["TIME"].apply(lambda x: x.hour)
    df["minutes"]=df["TIME"].apply(lambda x: x.minute)
    df["seconds"]=df["TIME"].apply(lambda x: x.second)

    return df