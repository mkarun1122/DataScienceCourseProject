# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 00:54:40 2024

@author: Arun M

Topic:
 Identifying missing values
 Approaches to fill the missing values
"""


 # import libs 

import os 
import numpy as np
import pandas as pd 



# working dir 
os.chdir("D:/2024/NPTEL/DS/spyderPandasDemo")


# reading csv file 
cars_data = pd.read_csv("Toyota.csv", index_col=0,na_values=["??","?????"])

# Creating copies of original data
cars_data2=cars_data.copy()
cars_data3=cars_data.copy()
cars_data4=cars_data.copy()


# In Pandas dataframes, missing data is represented by NaN 
# (an acronym for Not a Number)

# 1. To check the count of missing values present in each column
cars_data2.isna().sum()
cars_data3.isnull().sum()
cars_data4.isnull().sum()
# 2. Subsetting the rows that have one or more missing values
missing = cars_data2[cars_data2.isnull().any(axis=1)]


"""
Approached to fill the missing values
Two ways of approach  
1)Fill the missing values by mean / median, in case of
numerical variable 
2) Fill the missing values with the class which has
maximum count, in case of categorical variable

Look at the description to know whether numerical
variables should be imputed with mean or median

"""

cars_data2.describe()


# 3. Imputing missing values of ‘Age’,
#  Calculating the mean value of the Age variable
cars_data2['Age'].mean()

#  To fill NA/NaN values using the specified value
cars_data4['Age'].fillna(cars_data4['Age'].mean(), inplace=True)

# 4. Imputing missing values of ‘KM’ , 
# To fill NA/NaN values using the specified value
cars_data4['KM'].fillna(cars_data4['KM'].median(), inplace=True)
 
"""
 5.Imputing missing values of ‘FuelType’

• Returns a Series containing counts of unique values
• The values will be in descending order so that the
first element is the most frequently-occurring
element
• Excludes NA values by default 
"""
cars_data4['FuelType'].value_counts()
# To get the mode value of FuelTyp
cars_data4['FuelType'].value_counts().index[0]
cars_data4['FuelType'].fillna(cars_data4['FuelType'].value_counts().index[0], 
                              inplace=True)

# 5. Imputing missing values of ‘MetColor’
# To get the mode value of MetColor
cars_data4['MetColor'].mode()

cars_data4['MetColor'].fillna(cars_data4['FuelType'].mode()[0], inplace=True)

# 6. Imputing missing values using lambda functions
# To fill the NA/ NaN values in both numerical and categorial variables at one stretch
cars_data5=cars_data.copy()
cars_data5.isnull().sum()
cars_data5 = cars_data5.apply(
   lambda x:x.fillna(x.mean())
   if x.dtype == 'float'
   else 
   x.fillna(x.value_counts().index[0]))

np.unique(cars_data5['FuelType'])

