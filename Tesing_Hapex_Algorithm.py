import os
import pandas as pd
import numpy as np
import csv
import glob
import statistics as stat
from datetime import datetime
from csv import reader
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path, PureWindowsPath
import Functions_malawi

Phase  = "1N"
Houshold = 1007
start_spread = 10
cooldown_Length = 30


path = "C:/Users/gvros/Desktop/Practice_HAPEX_detection_Array.csv"
csv_read = pd.read_csv(path)

Path_CE_MErge = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_1_exact/Raw_D_metrics/"+Phase+"_HH_raw_Day_metrics_"+str(Houshold)+"_1_exact_3.55555.csv"
Event_dataframe= pd.read_csv(Path_CE_MErge,skiprows = 2 )

ff_usage = Event_dataframe.iloc[:,3]
ff_temp = Event_dataframe.iloc[:,4]
Kitchen_Hapex = Event_dataframe.iloc[:,8]

Gradient_Hapex = (np.gradient(Kitchen_Hapex))

ABS_Gradient_Hapex = abs(Gradient_Hapex)
Median_Gradient_Hapex = np.median(ABS_Gradient_Hapex)
print('=-=-=-=-=-=-=-=-=-=-==-=-=-',Median_Gradient_Hapex)

csv = csv_read.iloc[:,0]
start = 10
K_H_MIN_tv, K_H_MAX_tv ,K_H_MIN_Count, K_H_MAX_Count  = Functions_malawi.Local_Max_min(csv, start)

K_Hapex_Startup_max, K_Hapex_Next_Startup_min = Functions_malawi.StartUp_max_Next_min(csv, start)
print(K_H_MAX_Count,K_H_MIN_Count,K_Hapex_Startup_max  )
Steady_start_Time_value = Functions_malawi.SteadyState_Finder(csv, 35, K_H_MIN_Count,K_Hapex_Startup_max, K_H_MAX_Count,start)
print('Here is the Steady State: ',Steady_start_Time_value)