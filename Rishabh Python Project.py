# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 09:13:19 2022

@author: HP
"""

import pandas as pd
import numpy as np

# Task 1: Create a dataframe “Camera_data” using Camera.csv
Camera_data=pd.read_csv(r"M:\Python\Python Project\Python Project Questions\Camera.csv")
Camera_data
Camera_data.shape           #(1038, 13)
Camera_data.columns
# ['Model','Release date','Max resolution','Low resolution',
# 'Effective pixels','Zoom wide(W)','Zoom tele(T)',
# 'Normal focus range','Macro focus range','Storage included',
# 'Weight(inc. batteries)','Dimensions','Price']


# Task 2: Find out the percentage of blank values in each column.
Camera_data.isnull().sum()/len(Camera_data)
# Model                      0.000000
# Release date               0.000000
# Max resolution             0.000963
# Low resolution             0.052023
# Effective pixels           0.000000
# Zoom wide(W)               0.081888
# Zoom tele(T)               0.000000
# Normal focus range         0.000000
# Macro focus range          0.000963
# Storage included           0.120424
# Weight(inc.batteries)      0.022158
# Dimensions                 0.015414
# Price                      0.000000


# Task 3: View the statistical summary of the data.
Camera_data.describe()


# Task 4: Replace all the blank values with NaN.
Camera_data.replace(" ",np.nan,inplace=True)          


# Task 5: Now replace all the Blank values with the column median.
Camera_data.fillna(Camera_data.median(),inplace=True)


# Task 6: Add a new column “Discounted_Price” in which give a discount of 
# 5% in the Price column.
Camera_data['Discounted_Price']=Camera_data['Price']*0.95
Camera_data['Discounted_Price']


# Task 7: Drop the columns Zoom Tele & Macro Focus range
Camera_data.drop(['Zoom tele (T)','Macro focus range'],axis=1,inplace=True)


# Task 8: Replace the Model Name “Agfa ePhoto CL50” with “Agfa ePhoto 
# CL250”
Camera_data['Model'].replace({'Agfa ePhoto CL50':'Agfa ePhoto CL250'},inplace=True)


# Task 9: Rename the column name from Release Date to Release Year.
Camera_data.rename(columns={'Release date':'Release Year'},inplace=True)
Camera_data


# Task 10: Which is the most expensive Camera?
Camera_data['Price'].max()
print(Camera_data[Camera_data['Price']==Camera_data['Price'].max()]['Model'])
# Canon EOS-1Ds
# Canon EOS-1Ds Mark II
# Canon EOS-1Ds Mark III


# Task 11: Which camera have the least weight?
Camera_data['Weight (inc. batteries)'].min()      #100
print(Camera_data[Camera_data['Weight (inc. batteries)']==Camera_data['Weight (inc. batteries)'].min()]['Model'])
# Casio Exilim EX-S20


# Task 12: Group the data on the basis of their release year.
Camera_data.groupby('Release Year').count()    
Camera_data.groupby(by=['Release Year'])['Model'].unique()


# Task 13: Extract the Name, Storage Included, Price, Discounted_Price & 
# Dimensions columns.
Camera_data[['Model','Storage included','Price','Discounted_Price','Dimensions']]


# Task 14: Extract the records for the cameras released in the year 2005 & 
# 2006
Year=[2005,2006]
Camera_data2=Camera_data[Camera_data['Release Year'].isin(Year)]



# Task 15: Find out 2007’s expensive & Cheapest Camera.
Camera_data3=Camera_data[(Camera_data['Release Year']==2007)&(Camera_data['Price'])]
np.max(Camera_data3)          #Sony DSLR-A700
np.min(Camera_data3)          #Canon EOS 40D


# Task 16: Which Year maximum number of models is released?
Camera_data.groupby(by=['Release Year'])['Model'].count()
# 2007    163


























