from datetime import datetime
import pandas as pd

# More generic function

def convert_to_df(data, data_needed):

    df = pd.DataFrame(columns=data_needed)
    df["TIME"]=pd.to_datetime(data['Epoch'])
    for data_txt in data_needed:
        df[data_txt]=data[data_txt]
    #df['SUN_DIST']=data["SUN_DIST"]
    #df["MAGF_INST"]=data["MAGF_INST"]
    #df["SC_VEL_RTN_SUN"]=data["SC_VEL_RTN_SUN"]
    df["hour"]=df["TIME"].apply(lambda x: x.hour)
    df["minutes"]=df["TIME"].apply(lambda x: x.minute)
    df["seconds"]=df["TIME"].apply(lambda x: x.second)

    return df