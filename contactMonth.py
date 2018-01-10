#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 11:40:30 2018

@author: mulugetasemework
"""
import os
import pandas as pd
import numpy as np
import calendar

path = "/..../Phyton"

os.chdir(path)
df= pd.read_csv('HireArt - Data Analyst Exercise 10.12.17 - Sheet1.csv')
Header = list(df.columns.values)
dates = df['Date of Contact']

monthCount = [0]*12

for i in range(0,len(dates)):
    year,month,date = dates[i].split('-')
    monthCount[int(month)-1] += 1

contactMonthIndex = np.argmax(monthCount) + 1

contactMonth = calendar.month_abbr[contactMonthIndex]
