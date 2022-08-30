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

Path_Stove_1 = "D:/CCT-Stove-1-Matrix.csv"
Path_Stove_2 = "D:/CCT-Stove-2-Matrix.csv"
Path_Stove_3 = "D:/CCT-Stove-3-Matrix.csv"

TSF = pd.read_csv(Path_Stove_1)
CQC = pd.read_csv(Path_Stove_2)
CQC_JFK = pd.read_csv(Path_Stove_3)

print(TSF.iloc[1,2])

Name_TSF = TSF.iloc[:,0]
Wood_TSF = TSF.iloc[:,1]
Cooked_TSF = TSF.iloc[:,4]
Charcoal_TSF = TSF.iloc[:,5]
Flour_In_TSF = TSF.iloc[:,6]
Stir_TSF = TSF.iloc[:,7]
Boil_TSF = TSF.iloc[:,8]
CE_Time_TSF = TSF.iloc[:,9]

# Filtering out 



Name_CQC =  CQC.iloc[:,0]
Wood_CQC = CQC.iloc[:,1]
Cooked_CQC = CQC.iloc[:,4]
Charcoal_CQC = CQC.iloc[:,5]
Flour_In_CQC = CQC.iloc[:,6]
Stir_CQC = CQC.iloc[:,7]
Boil_CQC = CQC.iloc[:,8]
CE_Time_CQC = CQC.iloc[:,9]

Name_CQC_JFK = CQC_JFK.iloc[:,0]
Wood_CQC_JFK = CQC_JFK.iloc[:,1]
Cooked_CQC_JFK = CQC_JFK.iloc[:,4]
Charcoal_CQC_JFK = CQC_JFK.iloc[:,5]
Flour_In_CQC_JFK = CQC_JFK.iloc[:,6]
Stir_CQC_JFK = CQC_JFK.iloc[:,7]
Boil_CQC_JFK = CQC_JFK.iloc[:,8]
CE_Time_CQC_JFK = CQC_JFK.iloc[:,9]