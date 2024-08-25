

import os 


import pandas as pd

os.chdir("D://2024//DS//spyderPandasDemo")

cars_data1woind = pd.read_csv("Toyota.csv")  # loads data wit unnamed: 0 col 

cars_data = pd.read_csv("Toyota.csv",index_col=0) # first col becomes index col

samp = cars_data.copy(deep=False)   # creates shallow copy , original obj reflects change 
cars_data1 = cars_data.copy(deep=True)   # creates deep copy , original obj not reflects change 

cars_data1.index    # get index or row labels of data frame


cars_data1.columns  # display columns 

cars_data1.size     # Total Number of elements 

cars_data1.shape    # dimentionality of dataframe

cars_data1.memory_usage()   # dataframe memory usage details 
cars_data1.ndim     # array number of axis / dimentions

cars_data1.head(5)      # display first 5 rows from dataframe
cars_data1.tail(10)    # display last 10 rows of data frame 

cars_data1.at[4,'FuelType']     # at provides label-based scalar lookups
cars_data1.iat[5,6]         # iat provides integer-based lookups 

cars_data1.loc[:,'FuelType']


 


