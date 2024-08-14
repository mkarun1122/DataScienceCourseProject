# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 22:57:23 2024

@author: Arun M

What is a histogram?
• It is a graphical representation of data using
bars of different heights
• Histogram groups numbers into ranges and
the height of each bar depicts the frequency
of each range or bin

When to use histograms?
• To represent the frequency distribution of
numerical variables

"""

import os
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 


# setup working directory 
os.chdir("D:/2024/NPTEL/DS/spyderPandasDemo")

# reading csv file using pandas 
cars_data = pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])

# emoving missing values 
cars_data.dropna(axis=0, inplace=True)

# 1. Hist plot 
plt.hist(cars_data['KM'])  # Histogram with default arguments
plt.title("Histogram plot \w default settings ")
plt.show()



"""
# 2. Hist plot - Frequency distribution of kilometre of the cars shows that
most of the cars have travelled between 50000 – 100000 km
and there are only few cars with more distance travelled
"""
plt.hist(cars_data['KM'], 
         color='Green',
         edgecolor='White',
         bins=5)

plt.title('Histogram of kilometer')
plt.xlabel('Kilometer')
plt.ylabel('Frequency')
plt.show()
