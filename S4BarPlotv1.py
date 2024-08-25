# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 23:14:08 2024

@author: Arun M 


What is a bar plot?
• A bar plot is a plot that presents categorical
data with rectangular bars with lengths
proportional to the counts that they
represent


When to use bar plot?
• To represent the frequency distribution of
categorical variables
• A bar diagram makes it easy to compare sets
of data between different groups


"""

# import modules 
import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


#working dir 
os.chdir("D:/2024/DS/spyderPandasDemo")

#reading csv file 
cars_data = pd.read_csv('Toyota.csv',index_col=0,na_values=["??","????"])


#   removing missing values 
cars_data.dropna(axis=0, inplace=True)

#   Bar plot
counts=[979,120,12]
fueltypes=('Petrol','Diesel','CNG')
index = np.arange(len(fueltypes))

plt.bar(index,counts,color=['red','blue','cyan'])
plt.title('Bar plot of Fuel Types ')
plt.xlabel('Fuel Type')
plt.ylabel('Frequency ')
plt.xticks(index,fueltypes,rotation=45)
plt.show()
