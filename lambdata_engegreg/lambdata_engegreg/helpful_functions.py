import pandas as pd
from random import randrange
import pytest

def count_null(df):
    
    return df.isna().sum().sum()


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