#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 15:15:48 2017

@author: JoeRippke

This program parses data contained in .txt files produced by NOAA buoys
deployed on Lake Superior. All of the .txt files in the git repository are
necessary to run this program.

The desired outcome is that this program should output a .csv file that
contains one value for each year of available buoy data. This value represents
the temperature of the surface waters averaged over the three buoys and
averaged over the summer defined as July, August and September.

The buoy data is available at: http://www.ndbc.noaa.gov/
buoys: 45006, 45001 and 45004

This is written in python 3
"""
import BuoyFunctions as bf
import numpy as np

region = ['w','c','e'] # each region corresponds to a buoy
year = [1981+x for x in range(35)]
SummerMeans = [] #empty list where averaged temps are temporarily stored

for yr in range(len(year)): # loop over all of the years in the range
    means =[] # temporary list that hold the mean temperatures of the
    #individual buoys
    for reg in range(len(region)): # loop over each of the buoys
        data = bf.OpenFile(region[reg],year[yr]) # open a datafile and isolate
        # the water temperature column, also define NaN values as 999.0
        mean = bf.SummerMean(data,year[yr]) # calculate the mean temperature
        #for the summer period
        if np.isnan(mean[0]) == False: # throw out NaN values. Data is missing
        # in two data files. this produces NaNs. I want to throw out the NaNs
        # and calculate averages with the remaining values
            means.append(mean) # hold on to the mean value for now
    print(year[yr]) # print the year, just so I can tell it's doing something
    # as it runs
    SummerMeans.append(float(np.mean(means))) # average the values from the
    # three buoys for a single year and append them to a list

bf.SaveFile(year,SummerMeans) # save a .csv file of the temperature data
# indexed by year
bf.SummerPlot(year,SummerMeans) # *bonus function plots the temperature data
