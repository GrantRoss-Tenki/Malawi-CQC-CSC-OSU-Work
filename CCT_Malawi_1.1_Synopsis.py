# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 13:18:47 2022

@author: rossgra
"""

import os
import pandas as pd
import numpy as np
import csv
import glob
from datetime import datetime
from csv import reader
import matplotlib.pyplot as plt
import seaborn as sns
import csv

Path_Stove_1 = "D:/CCT-Stove-1-Matrix.csv"
Path_Stove_2 = "D:/CCT-Stove-2-Matrix.csv"
Path_Stove_3 = "D:/CCT-Stove-3-Matrix.csv"

COl_namnes = ['Household and Test','Wood Used','Flour Used','Water used','Cooked Food',
              'Hot Charcoal','Start to Flour in','Start to Stir','Start to Boil','Cooking Time']

TSF = pd.DataFrame(pd.read_csv(Path_Stove_1, names=COl_namnes, header =0))
CQC = pd.DataFrame(pd.read_csv(Path_Stove_2, names=COl_namnes, header =0))
CQC_JFK = pd.DataFrame(pd.read_csv(Path_Stove_3, names=COl_namnes, header =0))

print('here is the data frame for tsf', TSF['Water used'] )


# Filtering out the non Standardized Water and Flour
TSF_Filter = []
TSF_Non_Filter = []
for TSF_Row, TSF in enumerate(TSF['Flour Used']):
    if TSF == 1300:
        TSF_Filter.append(TSF.iloc[TSF_Row,:])
    else:
        TSF_Non_Filter.append(TSF_Row)
        
CQC_Filter = []
CQC_Non_Filter = []
for CQC_Row, CQC in enumerate(CQC['Flour Used']):
    if CQC == 1300:
        CQC_Filter.append(CQC_Row)
    else:
        CQC_Non_Filter.append(CQC_Row)
        
CQC_JFK_Filter = []
CQC_JFK_Non_Filter = []
for CQC_JFK_Row, CQC_JFK in enumerate(CQC_JFK['Flour Used']):
    if CQC_JFK == 1300:
        CQC_JFK_Filter.append(CQC_JFK_Row)
    else:
        CQC_JFK_Non_Filter.append(CQC_JFK_Row)


print('new tsf matrix ', TSF_Filter)
# Three stone Fire Baseline Matrix Partition


Name_TSF = [];Wood_TSF = [];Cooked_TSF = [];Charcoal_TSF = [];Flour_In_TSF = []
Stir_TSF = [];Boil_TSF = [];CE_Time_TSF = []

for TSF_val in TSF_Filter:
    print('is the first loop for tstf working?  ', TSF_val, TSF_Filter)
    
    Name_TSF.append(TSF.at[TSF_val,'Household and Test'])
    Wood_TSF.append(TSF.iloc[TSF_val,1])
    Cooked_TSF.append(TSF.iloc[TSF_val,4])
    Charcoal_TSF.append(TSF.iloc[TSF_val,5])
    Flour_In_TSF.append(TSF.iloc[TSF_val,6])
    Stir_TSF.append(TSF.iloc[TSF_val,7])
    Boil_TSF.append(TSF.iloc[TSF_val,8])
    CE_Time_TSF.append(TSF.iloc[TSF_val,9])

# CQC Stove Matrix Partition
Name_CQC = [];Wood_CQC = [];Cooked_CQC = [];Charcoal_CQC = [];Flour_In_CQC = []
Stir_CQC = [];Boil_CQC = [];CE_Time_CQC = []

for CQC_val in CQC_Filter:
    Name_CQC.append(CQC.iloc[CQC_val,0])
    Wood_CQC.append(CQC.iloc[CQC_val,1])
    Cooked_CQC.append(CQC.iloc[CQC_val,4])
    Charcoal_CQC.append(CQC.iloc[CQC_val,5])
    Flour_In_CQC.append(CQC.iloc[CQC_val,6])
    Stir_CQC.append(CQC.iloc[CQC_val,7])
    Boil_CQC.append(CQC.iloc[CQC_val,8])
    CE_Time_CQC.append(CQC.iloc[CQC_val,9])
    
# CQC with Jet Flame Matrix Partition
Name_CQC_JFK = [];Wood_CQC_JFK = [];Cooked_CQC_JFK = [];Charcoal_CQC_JFK = []
Flour_In_CQC_JFK = [];Stir_CQC_JFK = [];Boil_CQC_JFK = [];CE_Time_CQC_JFK = []

for JFK_val in CQC_JFK_Filter:
    Name_CQC_JFK = CQC_JFK.iloc[:,0]
    Wood_CQC_JFK = CQC_JFK.iloc[:,1]
    Cooked_CQC_JFK = CQC_JFK.iloc[:,4]
    Charcoal_CQC_JFK = CQC_JFK.iloc[:,5]
    Flour_In_CQC_JFK = CQC_JFK.iloc[:,6]
    Stir_CQC_JFK = CQC_JFK.iloc[:,7]
    Boil_CQC_JFK = CQC_JFK.iloc[:,8]
    CE_Time_CQC_JFK = CQC_JFK.iloc[:,9]