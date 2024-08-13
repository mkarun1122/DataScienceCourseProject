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
import Numpy as np

os.chdir("D:/2024/NPTEL/DS/spyderPandasDemo")
cars_data = pd.read_csv("D:/2024/NPTEL/DS/spyderPandasDemo/Toyota.csv")



