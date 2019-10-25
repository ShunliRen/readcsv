import pandas as pd
import numpy as np
import pickle

def csv_to_pl(dir1,dir2,):
    csv = pd.read_csv(dir1)
    miou = list(csv[list(csv.columns)[-1]])
    p = np.asarray(miou)
    with open(dir2, 'wb') as f:
        pickle.dump(p, f)

def csv_to_np(dir1):
    csv = pd.read_csv(dir1)
    miou = list(csv[list(csv.columns)[-1]])
    p = np.asarray(miou)
    return p


# pandas to csv
#csv.to_csv('./another')
