# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 15:35:00 2022

@author: rossgra
"""

import itertools
import os
import pandas as pd
import numpy as np
import csv
import glob
from decimal import *
from itertools import chain
import datetime
from io import StringIO
import matplotlib.pyplot as plt
import scipy as scipy
import math


Phase_number = '2N'

datafile_path = 'D:/SAE_Moisture_Split/2N_Moisture_SAE.csv'
SAE_Moist = pd.read_csv(datafile_path)
Household_array = SAE_Moist.iloc[:,0]
First_sense_period = SAE_Moist.iloc[:,16]

# There are going to be two sections
# 1st section - working through interpoilation of Moisture and Adult Eqv
# Moisture- is going to split evenly between the phase
# Standard Adult equivalent - split up evenly through visit days

Moist_1 = SAE_Moist.iloc[:,7:16]
Moist_2 = SAE_Moist.iloc[:,36:45]

Moist_1_Content = []
Moist_2_Content = []

for row, hh in enumerate(Household_array):
    Moist_1_Content.append(np.average(SAE_Moist.iloc[row,7:16]))
    Moist_2_Content.append(np.average(SAE_Moist.iloc[row,36:45]))

# 2nd section - Fuel Removal combination with the SAE and Moisture
Day_count_1 = SAE_Moist.iloc[:,16]
Day_count_3 = SAE_Moist.iloc[:,29]
Days_Observed = 1 + Day_count_1 + Day_count_3

Day_gap_1_1 = []
Day_gap_1_2 = []

for a in Day_count_1:
    if (a % 2) == 0:
        split_1 = a/2
        Day_gap_1_1.append(split_1)
        Day_gap_1_2.append(split_1)
    else:
        split_1 = round(a/2)
        split_1_L = a - split_1
        Day_gap_1_1.append(split_1)
        Day_gap_1_2.append(split_1_L)



Day_gap_3_1 = []
Day_gap_3_2 = []

for a in Day_count_3:
    if (a % 2) == 0:
        split_3 = a/2
        if split_3 == 0:
            Day_gap_3_1.append(1)
            Day_gap_3_2.append(split_3)
        else:
            Day_gap_3_1.append(split_3 + 1)
            Day_gap_3_2.append(split_3)
    else:
        split_3 = round(a/2)
        split_3_L = a - split_3
        split_3_1 = split_3 + 1
        Day_gap_3_1.append(split_3_1)
        Day_gap_3_2.append(split_3_L)
        
SAE_1 = []
SAE_2 = []
SAE_3 = []
SAE_4 = []

print('adult equ, child', SAE_Moist.iloc[0,2],SAE_Moist.iloc[0,18], SAE_Moist.iloc[0,24], SAE_Moist.iloc[0,31])

for row, hh in enumerate(Household_array):
    SAE_1.append(((SAE_Moist.iloc[row,2])*0.5)+
                 ((SAE_Moist.iloc[row,3])*0.8)+
                 ((SAE_Moist.iloc[row,4])*1)+
                 ((SAE_Moist.iloc[row,5])*0.8))
    
    SAE_2.append(((SAE_Moist.iloc[row,18])*0.5)+
                 ((SAE_Moist.iloc[row,19])*0.8)+
                 ((SAE_Moist.iloc[row,20])*1)+
                 ((SAE_Moist.iloc[row,21])*0.8))
    
    SAE_3.append(((SAE_Moist.iloc[row,24])*0.5)+
                 ((SAE_Moist.iloc[row,25])*0.8)+
                 ((SAE_Moist.iloc[row,26])*1)+
                 ((SAE_Moist.iloc[row,27])*0.8))
    
    SAE_4.append(((SAE_Moist.iloc[row,31])*0.5)+
                 ((SAE_Moist.iloc[row,32])*0.8)+
                 ((SAE_Moist.iloc[row,33])*1)+
                 ((SAE_Moist.iloc[row,34])*0.8))


DataFrame_split = {'Household': Household_array, 'Days Observed': Days_Observed,
             'Moisture 1':Moist_1_Content, 'Moisture 2': Moist_2_Content ,
             'Day 1': SAE_Moist.iloc[:,1], 'Split 1 # days': Day_gap_1_1, 
             'SAE Spit 1': SAE_1,
             'Day 2': SAE_Moist.iloc[:,17], 'Split 1.2 # days': Day_gap_1_2, 
             'SAE Spit 1.2': SAE_2, 
             'Day 3': SAE_Moist.iloc[:,23], 'Split 3.1 # days': Day_gap_3_1, 
             'SAE Spit 3.1': SAE_3,
             'Day 4': SAE_Moist.iloc[:,30], 'Split 3.2 # days': Day_gap_3_2, 
             'SAE Spit 3.2': SAE_4}  


DF_SAE_Split = pd.DataFrame(DataFrame_split, columns=['Household','Days Observed','Moisture 1',
                                                      'Moisture 2','Day 1', 'Split 1 # days', 'SAE Spit 1',
                                                      'Split 1.2 # days', 'SAE Spit 1.2','Day 2', 
                                                      'Day 3', 'Split 3.1 # days', 'SAE Spit 3.1',
                                                      'Split 3.2 # days', 'SAE Spit 3.2','Day 4'])
path = "D:/SAE_Moisture_Split/Moisture_SAE_split_"+Phase_number+"_.csv"
DF_SAE_Split.to_csv(path, index=False, mode= 'a')





