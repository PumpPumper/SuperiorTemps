#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 10:05:56 2017

@author: JoeRippke
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy import stats

def OpenFile(region,year):
    
    file = open((region+str(year)+'.txt'),'r')
    
    if year <= 1998:
        columns = ['YY','MM','DD','WTMP']
        dates = ['YY','MM','DD']
        data = pd.read_table(file,sep = '\s+',header = 0,
               usecols = columns, parse_dates = {'date': dates},
               index_col = ['date'], na_values = '999.0')
        
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
        
    pd.to_numeric(data['WTMP'],errors='coerce')       
    return(data)

def SummerMean(data,year):
    start = str(year)+'0701'
    end = str(year)+'0930'
    summer = data.loc[start:end]
    mean = summer.mean()
    return(mean)

def SummerPlot(year,data):
    plt.close('all')
    plt.scatter(year,data)
    plt.hold(True)
    plt.xlabel('Year')
    plt.ylabel('Temperature [°C]')
    plt.title('Lake Superior Summertime (Jul-Sep)\nAverage Surface Water Temperature')
    
def SaveFile(year,data):
    with open('SummerMeans.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(year,data))