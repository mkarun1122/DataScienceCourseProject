# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 23:40:02 2024

@author: Arun M

We will learn how to create basic plots using seaborn library:
• Scatter plot
• Histogram
• Bar plot
• Box and whiskers plot
• Pairwise plots

Seaborn is a Python data visualization library
based on matplotlib

• It provides a high-level interface for drawing
attractive and informative statistical graphics

"""

# import libs 

import os 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


# working dir 
os.chdir("D:/2024/DS/spyderPandasDemo")


# reading csv file 
cars_data = pd.read_csv("Toyota.csv", index_col=0,na_values=["??","?????"])


# removing missing values 
cars_data.dropna(axis=0,inplace=True)

#   1. Scatter plot of Price vs Age with default arguments
sns.set(style="darkgrid")
sns.regplot(x=cars_data['Age'],y=cars_data['Price'])
#   By default, fit_reg = True It estimates and plots a regression 
#   model relating the x and y variables

# 2.    Scatter plot of Price vs Age without the regression fit line
sns.regplot(x=cars_data['Age'],y=cars_data['Price'],fit_reg=False)


"""
 Scatter plot of Price vs Age by FuelType
 Using hue parameter, including another variable to show the fuel
types categories with different colors

"""

sns.lmplot(x='Age',y='Price',data=cars_data,
           fit_reg=False, hue='FuelType',
           legend=True, palette="Set1")


# 3. Histogram with default kernel density estimate
sns.displot(cars_data['Age'],kde=True)

# 4. Histogram without kernel density estimate
sns.displot(cars_data['Age'],kde=False)

# 5.  Histogram with fixed no. of bins
sns.displot(cars_data['Age'],kde=False,bins=5)

# 6.  Frequency distribution of fuel type of the cars
sns.countplot(x=cars_data['FuelType'],data=cars_data)

# 7. Grouped bar plot of FuelType and Automatic
#crosstab data using pds
pd.crosstab(index=cars_data['Automatic'], columns=cars_data['FuelType']
            ,dropna=True)
#   here te graph
sns.countplot(x='FuelType',data=cars_data,hue='Automatic')

"""
 8. Box and whiskers plot – numerical variable
 Box and whiskers plot of Price to visually interpret the
five-number summary
"""
sns.boxplot(y=cars_data['Price'])

# 9.    Box and whiskers plot for numerical vs categorical variable
#       Price of the cars for various fuel types 
sns.boxplot(x=cars_data['FuelType'],y=cars_data['Price'])


# 10.   Grouped box and whiskers plot of Price vs FuelType and Automatic
sns.boxplot(x='FuelType',y='Price',hue='Automatic',data=cars_data)

"""
 11.   Box-whiskers plot and Histogram
 Let’s plot box-whiskers plot and histogram on the same window
 Split the plotting window into 2 parts 
"""
f,(ax_box,ax_hist)=plt.subplots(2,gridspec_kw={"height_ratios":(.15,.85)})

#  Now, add create two plots
sns.boxplot(cars_data['Price'],ax=ax_box)
# sns.distplot(cars_data['Price'],ax=ax_hist,kde=False) --> Depricated
sns.histplot(cars_data['Price'], kde=True)


# 12.   Pairwise plots
"""
It is used to plot pairwise relationships in a dataset
Creates scatterplots for joint relationships and histograms for univariate distributions
"""
sns.pairplot(cars_data,kind="scatter",hue="FuelType")
plt.show()

