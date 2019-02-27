import pandas as pd
import numpy as np

def init_risk():
    data = pd.read_csv('./data/3dieases_People.csv',engine='python')
    r = data.iloc[:,-5:]
    return r