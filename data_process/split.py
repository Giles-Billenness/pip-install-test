import pandas as pd
import numpy as np
import os
from argparse import ArgumentParser

def split_Data():
    parser = ArgumentParser(description="Process a collection or individual zip file")
    parser.add_argument("pathToData", help="The path to the data to be processed")
    arguments = parser.parse_args()

    df = pd.read_csv(arguments.pathToData, sep='\t')
    n = round(df.shape[0]/2)
    list_df = np.array_split(df, n)
    for df in list_df:
        df.to_csv(os.path.dirname(pathToData) + str(df.index[0]) + '.csv', sep='\t', index=False)
