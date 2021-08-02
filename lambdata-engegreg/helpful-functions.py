import pandas as pd
from random import randrange

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


    