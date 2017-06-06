import pandas as pd


def equal_operator(ds1, ds2):
    """
    Enter your code here
    """
    ds1 = pd.Series(ds1)
    ds2 = pd.Series(ds2)
    newList = ds1 == ds2
    return newList

def greater_than_operator(ds1, ds2):
    """
    Enter your code here
    """
    ds1 = pd.Series(ds1)
    ds2 = pd.Series(ds2)
    newList = ds1 > ds2
    return newList


def less_than_operator(ds1, ds2):
    """
    Enter your code here
    """
    ds1 = pd.Series(ds1)
    ds2 = pd.Series(ds2)
    newList = ds1 < ds2
    return newList

equal_operator([2, 4, 6, 8, 10], [1, 3, 5, 7, 10])
