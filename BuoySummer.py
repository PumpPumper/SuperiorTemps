#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 15:15:48 2017

@author: JoeRippke
"""
import BuoyFunctions as bf
import numpy as np

region = ['w','c','e']
year = [1981+x for x in range(35)]
SummerMeans = []

for yr in range(len(year)):
    means =[]
    for reg in range(len(region)):
        data = bf.OpenFile(region[reg],year[yr])
        mean = bf.SummerMean(data,year[yr])
        means.append(mean)
    print(year[yr])
    SummerMeans.append(float(np.mean(means)))

bf.SaveFile(year,SummerMeans)
bf.SummerPlot(year,SummerMeans)

