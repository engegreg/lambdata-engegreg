import pandas as pd
from random import randrange
import pytest
"""Simple function that returns the sum of all null values in your dataset"""
def count_null(df):
    
    return df.isna().sum().sum()

"""This function creates a training split out of a provided dataset. 
You can set the percentage by replacing frac with a 
percentage value (eg: train_test_split(df, 0.2))"""
def train_test_split(df, frac):
    train = list()
    train_size = frac * len(df)
    #turn dataframe into list to easily randomize data during tts.
    df_copy = list(df)
    while len(train) < train_size:
        index = randrange(len(df_copy))
        train.append(df_copy.pop(index))

    return train, df_copy

df = pd.read_csv('/home/greg/Documents/OS/lambdata-engegreg/loan_data.csv')

def test_tts():
    assert train == len(df) * 0.2
