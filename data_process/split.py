import pandas as pd
import numpy as np
import os

def split_Data(pathToData):
    df = pd.read_csv(pathToData, sep='\t')
    n = df.len()/2
    list_df = np.array_split(df, n)
    for df in list_df:
        df.to_csv(os.path.dirname(pathToData) + str(df.index[0]) + '.csv', sep='\t', index=False)
