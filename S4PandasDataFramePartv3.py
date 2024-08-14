# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:19:48 2024

@author: Arun M

We will learn how to create basic plots using matplotlib library
• Scatter plot
• Histogram
• Bar plot

Python offers multiple graphing libraries that offers diverse
features

matplotlib • to create 2D graphs and plots
• pandas visualization • easy to use interface, built on
Matplotlib
• seaborn • provides a high-level interface
for drawing attractive and
informative statistical graphics
• ggplot • based on R’s ggplot2, uses
Grammar of Graphics
• plotly • can create interactive plots

"""


"""
1. What is a scatter plot?
• A scatter plot is a set of points that represents
the values obtained for two different variables
plotted on a horizontal and vertical axes

When to use scatter plots?
• Scatter plots are used to convey the relationship
between two numerical variables
• Scatter plots are sometimes called correlation
plots because they show how two variables are
correlated

"""

import os 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# set working directory 
os.chdir("D:/2024/NPTEL/DS/spyderPandasDemo")
# import csv file 
cars_data = pd.read_csv("Toyota.csv", index_col=0,na_values=["?","????"])
#remove missing values 
cars_data.dropna(axis=0,inplace=True)

#   1.  creating scaller plot using matplotlib 
plt.scatter(cars_data['Age'], cars_data['Price'], c='red')
plt.title("Scaller plot of Price Vs Age of cards")
plt.xlabel('Age (Months)')
plt.ylabel('Price (Euros)')
plt.show()





