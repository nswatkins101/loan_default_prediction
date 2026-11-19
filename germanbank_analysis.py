import pandas as pd
import numpy as np
import matplotlib as plt

import statsmodels
import sklearn

def main():

    # load data
    df = pd.read_excel('germanbank_encoded.xlsx')
    print(df.head())
    print(df.columns)



    return 0

if __name__ == '__main__':
    main()
