import pandas as pd
import numpy as np 

df=pd.read_csv('data.csv',index_col='Country name',decimal=',')

df.columns=['Annee', 'Bonheur', 'Log_PIB', 'Support_social','Esperance_de_vie', 'Liberte','Generosite', 'Corruption', 'Positive_affect','Negative_affect']


df1=df.sort_values('annee')
    
L=[i for i in range(2005,2023)]
df2005=df['annee']==2005





