#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 10:05:56 2017

@author: JoeRippke
This file contains functions for use with BuoySummer.py
"""
import pandas as pd
import matplotlib.pyplot as plt
import csv

# This funciton opens .txt files and returns a pandas dataframe of dates and
#temperatures
def OpenFile(region,year):
    
    file = open((region+str(year)+'.txt'),'r')
    # the formatting of the .txt files has changed twice over the years
    # this if statement handles each of the formats
    if year <= 1998:
        columns = ['YY','MM','DD','WTMP'] # defines which columns to use
        dates = ['YY','MM','DD'] # defines the date information columns
        data = pd.read_table(file,sep = '\s+',header = 0,
               usecols = columns, parse_dates = {'date': dates},
               index_col = ['date'], na_values = '999.0') # creates the 
                             # pandas dataframe
        
    elif year >= 1999 and year <= 2006:
        columns = ['YYYY','MM','DD','WTMP']
        dates = ['YYYY','MM','DD']
        data = pd.read_table(file,sep = '\s+',header = 0,
               usecols = columns, parse_dates = {'date': dates},
               index_col = ['date'], na_values = '999.0')
        
    else:
        columns = ['#YY','MM','DD','WTMP']
        dates = ['#YY','MM','DD']
        data = pd.read_table(file,sep = '\s+',skiprows=range(1, 2),header = 0,
               usecols = columns, parse_dates = {'date': dates},
               index_col = ['date'], na_values = '999.0')
        
    pd.to_numeric(data['WTMP'],errors='coerce') # converts the temperature
# values to floating point objects       
    return(data)

# this function identifies the summer period and returns the mean temperature
# over that period
def SummerMean(data,year):
    start = str(year)+'0701' # format the start and end dates for use with pandas
    end = str(year)+'0930'
    summer = data.loc[start:end] # pandas command to isolate the summer
    mean = summer.mean() # calculate the mean
    return(mean)

# this function creates a scatter plot of the averaged temperatures over the 
# years for which data is available
def SummerPlot(year,data):
    plt.close('all')
    plt.scatter(year,data)
    plt.hold(True)
    plt.xlabel('Year')
    plt.ylabel('Temperature [°C]')
    plt.title('Lake Superior Summertime (Jul-Sep)\nAverage Surface Water Temperature')

# This function saves a .csv file of the averaged temperatures
def SaveFile(year,data):
    with open('SummerMeans.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(year,data))