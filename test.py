#partie python Olivier 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import IPython

def courbe_depuis_DF(df):
    df.plt()
    plt.xlabel(df.loc[0,0])
    plt.show()

def nuage_pt(df):
    L=df.columns.to_list()
    X=df[L[0]].to_list()
    Y=df[L[1]].to_list()
    plt.plot(X,Y)
    plt.xlabel(L[0])
    plt.ylabel(L[1])
    plt.show()