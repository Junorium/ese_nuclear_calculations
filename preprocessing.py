import pandas as pd
import numpy as np

def zstandardization(df):
    return (df - np.mean(df))/np.std(df)

def minmaxstandarization(df):
    return (df - np.min(df))/(np.max(df)-np.min(df))

