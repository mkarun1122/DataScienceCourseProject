# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 02:42:50 2024

@author: Arun M
"""

"""
 Importing data
 Concise summary of dataframe
 Converting variable’s data types
 Category vs Object data type
 Cleaning column ‘Doors
 Getting count of missing values 
"""

import os 
import pandas as pd 
import numpy as np


os.chdir("D://2024//DS//spyderPandasDemo")

cars_data = pd.read_csv("Toyota.csv")
cars_data.info()

cars_data1 = pd.read_csv("Toyota.csv", index_col=0, na_values=["??","???"])
cars_data1.info()   #Concise summary of dataframe

#  astype() method is used to explicitly convert data types from one to another

cars_data1['MetColor'] = cars_data1['MetColor'].astype('object')
cars_data1.info()   #Concise summary of dataframe
cars_data1['Automatic'] = cars_data1['Automatic'].astype('object')

# revert back to same data type 
cars_data1['MetColor']=cars_data1['MetColor'].astype('float64')
cars_data1['Automatic']=cars_data1['Automatic'].astype('int64')

cars_data1.head(5)
# nbytes() is used to get the total bytes consumed by the elements of the columns
cars_data1['FuelType'].nbytes 
# cars_data1['FuelType'].astype['int64'].nbytes

#       Checking unique values of variable ‘Doors’ :
print(np.unique(cars_data1['MetColor']))

#   replace() is used to replace a value with the desired value
# cars_data1['Doors'].replace('three',3, inplace=True)
#cars_data1['Doors']=cars_data1['Doors'].replace('three',3, inplace=True)
#cars_data1.replace({'Doors','three',3}, inplace=True) Error: pandas 3.0 depricated and not working

#cars_data1['Doors'].replace({'three', 3}).astype['int64'] 
cars_data1['Doors']= cars_data1['Doors'].astype('int64')
cars_data1.info()
cars_data1.head(10)

# To check the count of missing values present in each column Dataframe.isnull.sum() is used

cars_data1.isnull().sum()

print(np.unique(cars_data1['MetColor']))
print(np.unique(cars_data1['Age']))



#####           Exploratory data analysis     #######
"""
In this lecture
 Frequency tables
 Two-way tables
 Two-way table - joint probability
 Two-way table - marginal probability
 Two-way table - conditional probability
 Correlation

"""

cars_data3 = cars_data1.copy()  ## copying into another DF 

# Frequency tables - To compute a simple cross-tabulation of one, two (or more) factors 
#  By default computes a frequency table of the factors 

pd.crosstab(index=cars_data3['FuelType'], columns='count',dropna=True)

# -----------------------------------------------------

# look at the frequency distribution of gearbox types with respect to different fuel types of the cars
# Two-way table 
pd.crosstab(index=cars_data3['Automatic'], columns=cars_data3['FuelType'],dropna=True)

# -----------------------------------------------------

# Two-way table - joint probability - • Joint probability is the likelihood 
# of two independent events happening at the same time
pd.crosstab(index=cars_data3['Automatic'], columns=cars_data3['FuelType'],
            normalize=True,dropna=True)

# -----------------------------------------------------

#   Two-way table - marginal probability - Marginal probability is the 
# probability of the occurrence of the single event

pd.crosstab(index=cars_data3['Automatic'], columns=cars_data3['FuelType'],
            margins=True,
            dropna=True,
            normalize=True)

# -----------------------------------------------------

#   Two-way table - conditional probability - 

# Conditional probability is the probability of an event ( A ), 
# given that another event ( B ) has already occurred
# Given the type of gear box, probability of different fuel type


pd.crosstab(index=cars_data3['Automatic'], columns=cars_data3['FuelType'],
            margins=True,
            dropna=True,
            normalize='index')

# (in the output sum(0.011876  0.114014  0.874109)=1)

# -----------------------------------------------------


#   Two-way table - conditional probability
#   Conditional probability is the probability of an event ( A ),
#    given that another event ( B ) has already occurred

pd.crosstab(index=cars_data3['Automatic'], 
            columns = cars_data3['FuelType'],
            margins=True,
            dropna=True,
            normalize='columns')
# Result: in the output obsrve Column sum = 1 


""" 
Correlation
DataFrame.corr(self, method='pearson’)

  Correlation: the strength of association between two variables
   Visual representation of correlation: Scatter plots

To compute pairwise correlation of columns excluding NA/null
values
• Excluding the categorical variables to find the Pearson’s
correlation

"""
numerical_data = cars_data3.select_dtypes(exclude=[object])


# Let’ s check the no. of variables available under numerical_data
print(numerical_data.shape)

#   Correlation between numerical variables
corr_matrix = numerical_data.corr()
print(corr_matrix)
