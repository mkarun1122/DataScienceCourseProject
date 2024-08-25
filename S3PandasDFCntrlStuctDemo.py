# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 23:02:04 2024

@author: Arun M
"""

"""
 Control structures ◦ If elif family ◦ For ◦ While  Functions

"""

import os 
import numpy as np
import pandas as pd 


os.chdir("D:/2024/DS/spyderPandasDemo")

cars_data1=pd.read_csv('Toyota.csv',index_col=0)
cars_data1.info()
print(np.unique(cars_data1['Price']))
cars_data1.insert(10,"Price Class","")



for i in range(0,len(cars_data1['Price']),1):
    if (cars_data1['Price'][i]<=8450):
        cars_data1['Price Class'][i]="Low"
    elif ((cars_data1['Price'][i]>11950) ):
        cars_data1['Price Class'][i]="High"
    else: cars_data1['Price Class'][i]="Medium"
    
print(np.unique(cars_data1['Price Class']))
cars_data1.head(20)

cars_data1['Price Class'].value_counts()
