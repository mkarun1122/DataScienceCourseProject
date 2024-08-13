# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 22:33:26 2024

@author: Arun
1. Introduction to pandas:
high-performance, easy-to-use data structures and analysis tools
Name pandas is derived from the word Panel Data
Pandas deals with dataframes
two-dimensional size-mutable
potentially heterogeneous tabular
data structure with labeled axes

2. Importing data into Spyder

 Creating copy of original data
 Attributes of data
 Indexing and selecting dataIntroduction to pandas
 Importing data into Spyder
 Creating copy of original data
 Attributes of data
 Indexing and selecting data

"""

import os 
import pandas as pd 
import numpy as np


os.chdir("D://2024//NPTEL//DS//spyderPandasDemo")
cars_data = pd.read_csv("Toyota.csv")

cars_data.dtypes     # return data type of eac columns 
# cars_data.get_dtype_counts() # depricated     # returns counts of unique data types in the dataframe

cars_data.dtypes.value_counts()  # new function return name count and dtype 
cars_data.select_dtypes( exclude=[object])  # returns subset of columns based on dtype 
cars_data.info()  # display summary of data frame  col, non-null count dtype 

print(np.unique(cars_data['KM']))   # unique elements of KM col 

print(np.unique(cars_data['HP']))    # unique elements of HP col 
print(np.unique(cars_data['MetColor']))    # unique elements of MetColor col 
print(np.unique(cars_data['Automatic']))    # unique elements of Automatic col 
print(np.unique(cars_data['Doors']))    # unique elements of Doors col
