# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:02:24 2022

@author: rossgra
"""

import numpy as np
from numpy.core.fromnumeric import std
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy
from scipy.stats import mannwhitneyu
import statistics as stat
# I am goign to bring in the NO- hood section first
#for Megajouels
#No_hood_MJ_path = "C:/Users/gvros/Box/OSU, CSC, CQC Project files/MJ per SAE - No_Hood.csv" #rossgra or gvros
#Hood_MJ_Path = "C:/Users/gvros/Box/OSU, CSC, CQC Project files/MJ per SAE - Hood.csv"
#### for FUEL_REMOVED _perd
No_hood_MJ_path = "C:/Users/gvros/Box/OSU, CSC, CQC Project files/24 Hour Remove - No_Hood.csv" #rossgra or gvros
Hood_MJ_Path = "C:/Users/gvros/Box/OSU, CSC, CQC Project files/24 Hour Remove - Hood.csv"
######For Fuel removed per 24 hours per SAE
#No_hood_MJ_path = "C:/Users/gvros/Box/OSU, CSC, CQC Project files/24 Hour Remove SAE - No_Hood.csv" #rossgra or gvros
#Hood_MJ_Path = "C:/Users/gvros/Box/OSU, CSC, CQC Project files/24 Hour Remove SAE - Hood.csv"

Level_of_confidence = 0.05
No_hood_MJ = pd.read_csv(No_hood_MJ_path)
Hood_MJ = pd.read_csv(Hood_MJ_Path)
#C:\Users\rossgra\Box\Classes\Software Dev C:\Users\rossgra\Box\OSU, CSC, CQC Project files
HH_1N = [x for x in No_hood_MJ.iloc[:, 0] if x != -1]
HH_2N = [x for x in  No_hood_MJ.iloc[:, 11] if x != -1]
HH_3N = [x for x in  No_hood_MJ.iloc[:, 22] if x != -1]
HH_4N = [x for x in  No_hood_MJ.iloc[:, 33] if x != -1]

HH_1H = [x for x in Hood_MJ.iloc[:, 0] if x != -1]
HH_2H = [x for x in Hood_MJ.iloc[:, 11] if x != -1]
HH_3H = [x for x in Hood_MJ.iloc[:, 22] if x != -1]

Mj_1N_Phase = [x for x in No_hood_MJ.iloc[:, 5] if x != -1]
Mj_2N_Phase = [x for x in No_hood_MJ.iloc[:, 16] if x != -1]
Mj_3N_Phase = [x for x in No_hood_MJ.iloc[:, 27] if x != -1]
Mj_4N_Phase = [x for x in No_hood_MJ.iloc[:, 38] if x != -1]

Mj_1H_Phase = [x for x in Hood_MJ.iloc[:, 5] if x != -1]
Mj_2H_Phase = [x for x in Hood_MJ.iloc[:, 16] if x != -1]
Mj_3H_Phase = [x for x in Hood_MJ.iloc[:, 27] if x != -1]

Mj_filter_1N_Phase = [x for x in No_hood_MJ.iloc[:, 6] if x != -1]
Mj_filter_2N_Phase = [x for x in No_hood_MJ.iloc[:, 17] if x != -1]
Mj_filter_3N_Phase = [x for x in No_hood_MJ.iloc[:, 28] if x != -1]
Mj_filter_4N_Phase = [x for x in No_hood_MJ.iloc[:, 39] if x != -1]

Mj_filter_1H_Phase = [x for x in Hood_MJ.iloc[:, 6] if x != -1]
Mj_filter_2H_Phase = [x for x in Hood_MJ.iloc[:, 17] if x != -1]
Mj_filter_3H_Phase = [x for x in Hood_MJ.iloc[:, 28] if x != -1]

Fuel_1N_Phase = [x for x in No_hood_MJ.iloc[:, 3] if x != -1]
Fuel_2N_Phase = [x for x in No_hood_MJ.iloc[:, 14] if x != -1]
Fuel_3N_Phase = [x for x in No_hood_MJ.iloc[:, 25] if x != -1]
Fuel_4N_Phase = [x for x in No_hood_MJ.iloc[:, 36] if x != -1]

Fuel_1H_Phase = [x for x in Hood_MJ.iloc[:, 3] if x != -1]
Fuel_2H_Phase = [x for x in Hood_MJ.iloc[:, 14] if x != -1]
Fuel_3H_Phase = [x for x in Hood_MJ.iloc[:, 25] if x != -1]

Avg_Fuel_1N = [x for x in No_hood_MJ.iloc[:, 2] if x != -1]
Avg_Fuel_2N = [x for x in No_hood_MJ.iloc[:, 13] if x != -1]
Avg_Fuel_3N = [x for x in No_hood_MJ.iloc[:, 24] if x != -1]
Avg_Fuel_4N = [x for x in No_hood_MJ.iloc[:, 35] if x != -1]

Avg_Fuel_1H = [x for x in Hood_MJ.iloc[:, 2] if x != -1]
Avg_Fuel_2H = [x for x in Hood_MJ.iloc[:, 13] if x != -1]
Avg_Fuel_3H = [x for x in Hood_MJ.iloc[:, 24] if x != -1]

Phase_1N_day_count = [x for x in No_hood_MJ.iloc[:, 1] if x != -1]
Phase_2N_day_count = [x for x in No_hood_MJ.iloc[:, 12] if x != -1]
Phase_3N_day_count = [x for x in No_hood_MJ.iloc[:, 23] if x != -1]
Phase_4N_day_count = [x for x in No_hood_MJ.iloc[:, 34] if x != -1]

Phase_1H_day_count = [x for x in Hood_MJ.iloc[:, 1] if x != -1]
Phase_2H_day_count = [x for x in Hood_MJ.iloc[:, 12] if x != -1]
Phase_3H_day_count = [x for x in Hood_MJ.iloc[:, 23] if x != -1]

Filter_1N_day_count = [x for x in No_hood_MJ.iloc[:, 7] if x != -1]
Filter_2N_day_count = [x for x in No_hood_MJ.iloc[:, 18] if x != -1]
Filter_3N_day_count = [x for x in No_hood_MJ.iloc[:, 29] if x != -1]
Filter_4N_day_count = [x for x in No_hood_MJ.iloc[:, 40] if x != -1]

Filter_1H_day_count = [x for x in Hood_MJ.iloc[:, 7] if x != -1]
Filter_2H_day_count = [x for x in Hood_MJ.iloc[:, 18] if x != -1]
Filter_3H_day_count = [x for x in Hood_MJ.iloc[:, 29] if x != -1]

cooking_times_1N = [x for x in No_hood_MJ.iloc[:, 8] if x != -1]
cooking_times_2N = [x for x in No_hood_MJ.iloc[:, 19] if x != -1]
cooking_times_3N = [x for x in No_hood_MJ.iloc[:, 30] if x != -1]
cooking_times_4N = [x for x in No_hood_MJ.iloc[:, 41] if x != -1]

cooking_times_1H = [x for x in Hood_MJ.iloc[:, 8] if x != -1]
cooking_times_2H = [x for x in Hood_MJ.iloc[:, 19] if x != -1]
cooking_times_3H = [x for x in Hood_MJ.iloc[:, 30] if x != -1]
#1N to 2N
# for Phase
MJ_Phase_1N_to_2_comon = []
MJ_Phase_2N_to_1_comon = []

Day_count_MJ_Phase_1N_2N = []
count_n = 0
for row_1N, hh_1N in enumerate(HH_1N):
    if hh_1N == str(-1):
        break
    for row_2N, hh_2N in enumerate(HH_2N):
        if hh_1N == hh_2N:
            MJ_Phase_1N_to_2_comon.append(Mj_1N_Phase[row_1N])
            MJ_Phase_2N_to_1_comon.append(Mj_2N_Phase[row_2N])
            Day_count_MJ_Phase_1N_2N.append(Phase_1N_day_count[row_1N] +Phase_2N_day_count[row_2N] )
            count_n = count_n + 1
            
N_MJ_Phase_1N_2N =  count_n -1

#for filter 
MJ_filter_1N_to_2_comon = []
MJ_filter_2N_to_1_comon = []

Day_count_MJ_filter_1N_2N = []
count_n = 0
for row_1N, hh_1N in enumerate(HH_1N):
    if hh_1N == str(-1):
        break
    for row_2N, hh_2N in enumerate(HH_2N):
        if hh_1N == hh_2N:
            MJ_filter_1N_to_2_comon.append(Mj_filter_1N_Phase[row_1N])
            MJ_filter_2N_to_1_comon.append(Mj_filter_2N_Phase[row_2N])
            
            Day_count_MJ_filter_1N_2N.append(Filter_1N_day_count[row_1N] +Filter_2N_day_count[row_2N] )
            count_n = count_n + 1
            
N_MJ_filter_1N_2N = count_n -1



#1N to 2N

###################____________________HOOOD
# for Phase
MJ_Phase_1H_to_2_comon = []
MJ_Phase_2H_to_1_comon = []

Day_count_MJ_Phase_1H_2H = []
count_n = 0
for row_1H, hh_1H in enumerate(HH_1H):
    if hh_1H == str(-1):
        break
    for row_2H, hh_2H in enumerate(HH_2H):
        if hh_1H == hh_2H:
            MJ_Phase_1H_to_2_comon.append(Mj_1H_Phase[row_1H])
            MJ_Phase_2H_to_1_comon.append(Mj_2H_Phase[row_2H])
            Day_count_MJ_Phase_1H_2H.append(Phase_1H_day_count[row_1H] +Phase_2H_day_count[row_2H] )
            count_n = count_n + 1
            
N_MJ_Phase_1H_2H =  count_n -1

#for filter 
MJ_filter_1H_to_2_comon = []
MJ_filter_2H_to_1_comon = []

Day_count_MJ_filter_1H_2H = []
count_n = 0
for row_1H, hh_1H in enumerate(HH_1H):
    if hh_1H == str(-1):
        break
    for row_2H, hh_2H in enumerate(HH_2H):
        if hh_1H == hh_2H:
            MJ_filter_1H_to_2_comon.append(Mj_filter_1H_Phase[row_1H])
            MJ_filter_2H_to_1_comon.append(Mj_filter_2H_Phase[row_2H])
            
            Day_count_MJ_filter_1H_2H.append(Filter_1H_day_count[row_1H] +Filter_2H_day_count[row_2H] )
            count_n = count_n + 1
            
N_MJ_filter_1H_2H = count_n -1


#1N to 3N

MJ_Phase_1N_to_3_comon = []
MJ_Phase_3N_to_1_comon = []

Day_count_MJ_Phase_1N_3N = []
count_n = 0
breakme = 0
for row_1N, hh_1N in enumerate(HH_1N):
    if hh_1N == (-1) :
        break
    for row_3N, hh_3N in enumerate(HH_3N):
        if hh_1N == hh_3N:
            
            MJ_Phase_1N_to_3_comon.append(Mj_1N_Phase[row_1N])
            MJ_Phase_3N_to_1_comon.append(Mj_3N_Phase[row_3N])
            Day_count_MJ_Phase_1N_3N.append(Phase_1N_day_count[row_1N] + Phase_3N_day_count[row_3N])
            count_n = count_n + 1

            
N_MJ_Phase_1N_3N = count_n -1
#for filter 
MJ_filter_1N_to_3_comon = []
MJ_filter_3N_to_1_comon = []

Day_count_MJ_filter_1N_3N = []
count_n = 0
for row_1N, hh_1N in enumerate(HH_1N):
    if hh_1N == str(-1):
        break
    for row_3N, hh_3N in enumerate(HH_3N):
        if hh_1N == hh_3N:
            
            MJ_filter_1N_to_3_comon.append(Mj_filter_1N_Phase[row_1N])
            MJ_filter_3N_to_1_comon.append(Mj_filter_3N_Phase[row_3N])
            
            Day_count_MJ_filter_1N_3N.append(Filter_1N_day_count[row_1N] +Filter_3N_day_count[row_3N] )
            count_n = count_n + 1
            
N_MJ_filter_1N_3N = count_n -1
#1N to 3N

###################____________________HOOOD
# for Phase

MJ_Phase_1H_to_3_comon = []
MJ_Phase_3H_to_1_comon = []

Day_count_MJ_Phase_1H_3H = []
count_n = 0
breakme = 0
for row_1H, hh_1H in enumerate(HH_1H):
    if hh_1H == (-1) :
        break
    for row_3H, hh_3H in enumerate(HH_3H):
        if hh_1H == hh_3H:
            
            MJ_Phase_1H_to_3_comon.append(Mj_1H_Phase[row_1H])
            MJ_Phase_3H_to_1_comon.append(Mj_3H_Phase[row_3H])
            Day_count_MJ_Phase_1H_3H.append(Phase_1H_day_count[row_1H] + Phase_3H_day_count[row_3H])
            count_n = count_n + 1

            
N_MJ_Phase_1H_3H = count_n -1
#for filter 
MJ_filter_1H_to_3_comon = []
MJ_filter_3H_to_1_comon = []

Day_count_MJ_filter_1H_3H = []
count_n = 0
for row_1H, hh_1H in enumerate(HH_1H):
    if hh_1H == str(-1):
        break
    for row_3H, hh_3H in enumerate(HH_3H):
        if hh_1H == hh_3H:
            
            MJ_filter_1H_to_3_comon.append(Mj_filter_1H_Phase[row_1H])
            MJ_filter_3H_to_1_comon.append(Mj_filter_3H_Phase[row_3H])
            
            Day_count_MJ_filter_1H_3H.append(Filter_1H_day_count[row_1H] +Filter_3H_day_count[row_3H] )
            count_n = count_n + 1
            
N_MJ_filter_1H_3H = count_n -1



#1N to 4N

MJ_Phase_1N_to_4_comon = []
MJ_Phase_4N_to_1_comon = []
Day_count_MJ_Phase_1N_4N = []
count_n = 0
for row_1N, hh_1N in enumerate(HH_1N):
    if hh_1N == str(-1):
        break
    for row_4N, hh_4N in enumerate(HH_4N):
        if hh_1N == hh_4N:
            MJ_Phase_1N_to_4_comon.append(Mj_1N_Phase[row_1N])
            MJ_Phase_4N_to_1_comon.append(Mj_4N_Phase[row_4N])
            Day_count_MJ_Phase_1N_4N.append(Phase_1N_day_count[row_1N] +Phase_4N_day_count[row_4N] )
            count_n = count_n + 1
print('length of 1n and 4 n:', len(MJ_Phase_1N_to_4_comon), len(MJ_Phase_4N_to_1_comon) )
N_MJ_Phase_1N_4N = count_n -1
#for filter 
MJ_filter_1N_to_4_comon = []
MJ_filter_4N_to_1_comon = []
Day_count_MJ_filter_1N_4N = []
count_n = 0
for row_1N, hh_1N in enumerate(HH_1N):
    if hh_1N == str(-1):
        break
    for row_4N, hh_4N in enumerate(HH_4N):
        if hh_1N == hh_4N:
            MJ_filter_1N_to_4_comon.append(Mj_filter_1N_Phase[row_1N])
            MJ_filter_4N_to_1_comon.append(Mj_filter_4N_Phase[row_4N])
            Day_count_MJ_filter_1N_4N.append(Filter_1N_day_count[row_1N] +Filter_4N_day_count[row_4N] )
            count_n = count_n + 1
            
N_MJ_filter_1N_4N = count_n -1



#2N to 3N

MJ_Phase_2N_to_3_comon = []
MJ_Phase_3N_to_2_comon = []
Day_count_MJ_Phase_2N_3N = []
count_n = 0
for row_2N, hh_2N in enumerate(HH_2N):
    if hh_2N == str(-1):
        break
    for row_3N, hh_3N in enumerate(HH_3N):
        if hh_2N == hh_3N:
            MJ_Phase_2N_to_3_comon.append(Mj_2N_Phase[row_2N])
            MJ_Phase_3N_to_2_comon.append(Mj_3N_Phase[row_3N])
            Day_count_MJ_Phase_2N_3N.append(Phase_2N_day_count[row_2N] +Phase_3N_day_count[row_3N] )
            count_n = count_n + 1
            
N_MJ_Phase_2N_3N = count_n -1
#for filter 
MJ_filter_2N_to_3_comon = []
MJ_filter_3N_to_2_comon = []
Day_count_MJ_filter_2N_3N = []
count_n = 0
for row_2N, hh_2N in enumerate(HH_2N):
    if hh_2N == str(-1):
        break
    for row_3N, hh_3N in enumerate(HH_3N):
        if hh_2N == hh_3N:
            MJ_filter_2N_to_3_comon.append(Mj_filter_2N_Phase[row_2N])
            MJ_filter_3N_to_2_comon.append(Mj_filter_3N_Phase[row_3N])
            Day_count_MJ_filter_2N_3N.append(Filter_2N_day_count[row_2N] +Filter_3N_day_count[row_3N] )
            count_n = count_n + 1
            
N_MJ_filter_2N_3N = count_n - 1
#2N to 3N

###################____________________HOOOD
# for Phase
MJ_Phase_2H_to_3_comon = []
MJ_Phase_3H_to_2_comon = []
Day_count_MJ_Phase_2H_3H = []
count_n = 0
for row_2H, hh_2H in enumerate(HH_2H):
    if hh_2H == str(-1):
        break
    for row_3H, hh_3H in enumerate(HH_3H):
        if hh_2H == hh_3H:
            MJ_Phase_2H_to_3_comon.append(Mj_2H_Phase[row_2H])
            MJ_Phase_3H_to_2_comon.append(Mj_3H_Phase[row_3H])
            Day_count_MJ_Phase_2H_3H.append(Phase_2H_day_count[row_2H] +Phase_3H_day_count[row_3H] )
            count_n = count_n + 1
            
N_MJ_Phase_2H_3H = count_n -1
#for filter 
MJ_filter_2H_to_3_comon = []
MJ_filter_3H_to_2_comon = []
Day_count_MJ_filter_2H_3H = []
count_n = 0
for row_2H, hh_2H in enumerate(HH_2H):
    if hh_2H == str(-1):
        break
    for row_3H, hh_3H in enumerate(HH_3H):
        if hh_2H == hh_3H:
            MJ_filter_2H_to_3_comon.append(Mj_filter_2H_Phase[row_2H])
            MJ_filter_3H_to_2_comon.append(Mj_filter_3H_Phase[row_3H])
            Day_count_MJ_filter_2H_3H.append(Filter_2H_day_count[row_2H] +Filter_3H_day_count[row_3H] )
            count_n = count_n + 1
            
N_MJ_filter_2H_3H = count_n - 1



#3N to 4N

MJ_Phase_3N_to_4_comon = []
MJ_Phase_4N_to_3_comon = []
Day_count_MJ_Phase_3N_4N = []
count_n = 0
for row_3N, hh_3N in enumerate(HH_3N):
    if hh_3N == str(-1):
        break
    for row_4N, hh_4N in enumerate(HH_4N):
        if hh_3N == hh_4N:
            MJ_Phase_3N_to_4_comon.append(Mj_3N_Phase[row_3N])
            MJ_Phase_4N_to_3_comon.append(Mj_4N_Phase[row_4N])
            Day_count_MJ_Phase_3N_4N.append(Phase_3N_day_count[row_3N] +Phase_4N_day_count[row_4N] )
            count_n = count_n + 1

N_MJ_Phase_3N_4N = count_n -1
#for filter 
MJ_filter_3N_to_4_comon = []
MJ_filter_4N_to_3_comon = []
Day_count_MJ_filter_3N_4N = []
count_n = 0
for row_3N, hh_3N in enumerate(HH_3N):
    if hh_3N == str(-1):
        break
    for row_4N, hh_4N in enumerate(HH_4N):
        if hh_3N == hh_4N:
            MJ_filter_3N_to_4_comon.append(Mj_filter_3N_Phase[row_3N])
            MJ_filter_4N_to_3_comon.append(Mj_filter_4N_Phase[row_4N])
            Day_count_MJ_filter_3N_4N.append(Filter_3N_day_count[row_3N] +Filter_4N_day_count[row_4N] )
            count_n = count_n + 1
            
N_MJ_filter_3N_4N = count_n - 1



T_stat_1N_2N, P_val_1N_2N = scipy.stats.ttest_ind(MJ_Phase_1N_to_2_comon,MJ_Phase_2N_to_1_comon, axis=0, equal_var=True)
degree_1N_2N = (N_MJ_Phase_1N_2N -1) *Level_of_confidence
if degree_1N_2N < abs(T_stat_1N_2N):
    print('1N and 2N Phase rejects the null', T_stat_1N_2N,'P-value', P_val_1N_2N,'Sample size N', N_MJ_Phase_1N_2N)
else:
    print('1N and 2N Phase accepts the null', T_stat_1N_2N,'P-value', P_val_1N_2N,'Sample size N', N_MJ_Phase_1N_2N)
T_sign_1N_2N, P_sign_1N_2N = scipy.stats.wilcoxon(MJ_Phase_1N_to_2_comon, MJ_Phase_2N_to_1_comon)

T_stat_1N_2N_filter, P_val_1N_2N_filter = scipy.stats.ttest_ind(MJ_filter_1N_to_2_comon,MJ_filter_2N_to_1_comon, axis=0, equal_var=True)
degree_1N_2N_filter = (N_MJ_filter_1N_2N -1) *Level_of_confidence
if degree_1N_2N_filter < abs(T_stat_1N_2N_filter):
    print('1N and 2N Filter rejects the null', T_stat_1N_2N_filter,'P-value', P_val_1N_2N_filter,'Sample size N', N_MJ_filter_1N_2N)
else:
    print('1N and 2N Filter accepts the null', T_stat_1N_2N_filter,'P-value', P_val_1N_2N_filter,'Sample size N', N_MJ_filter_1N_2N)
T_sign_1N_2N_filter, P_sign_1N_2N_filter = scipy.stats.wilcoxon(MJ_filter_1N_to_2_comon, MJ_filter_2N_to_1_comon)

# 1n to 2n HOOOOOOD

T_stat_1H_2H, P_val_1H_2H = scipy.stats.ttest_ind(MJ_Phase_1H_to_2_comon,MJ_Phase_2H_to_1_comon, axis=0, equal_var=True)
degree_1H_2H = (N_MJ_Phase_1H_2H -1) *Level_of_confidence
if degree_1H_2H < abs(T_stat_1H_2H):
    print('1H and 2H Phase rejects the null', T_stat_1H_2H,'P-value', P_val_1H_2H,'Sample size N', N_MJ_Phase_1H_2H)
else:
    print('1H and 2H Phase accepts the null', T_stat_1H_2H,'P-value', P_val_1H_2H,'Sample size N', N_MJ_Phase_1H_2H)
T_sign_1H_2H, P_sign_1H_2H = scipy.stats.wilcoxon(MJ_Phase_1H_to_2_comon, MJ_Phase_2H_to_1_comon)

T_stat_1H_2H_filter, P_val_1H_2H_filter = scipy.stats.ttest_ind(MJ_filter_1H_to_2_comon,MJ_filter_2H_to_1_comon, axis=0, equal_var=True)
degree_1H_2H_filter = (N_MJ_filter_1H_2H -1) *Level_of_confidence
if degree_1H_2H_filter < abs(T_stat_1H_2H_filter):
    print('1H and 2H Filter rejects the null', T_stat_1H_2H_filter,'P-value', P_val_1H_2H_filter,'Sample size N', N_MJ_filter_1H_2H)
else:
    print('1H and 2H Filter accepts the null', T_stat_1H_2H_filter,'P-value', P_val_1H_2H_filter,'Sample size N', N_MJ_filter_1H_2H)
T_sign_1H_2H_filter, P_sign_1H_2H_filter = scipy.stats.wilcoxon(MJ_filter_1H_to_2_comon, MJ_filter_2H_to_1_comon)




T_stat_1N_3N, P_val_1N_3N = scipy.stats.ttest_ind(MJ_Phase_1N_to_3_comon,MJ_Phase_3N_to_1_comon, axis=0, equal_var=True)
degree_1N_3N = (N_MJ_Phase_1N_3N -1) *Level_of_confidence
if degree_1N_3N < abs(T_stat_1N_3N):
    print('1N and 3N Phase rejects the null', T_stat_1N_3N,'P-value', P_val_1N_3N,'Sample size N', N_MJ_Phase_1N_3N)
else:
    print('1N and 3N Phase accepts the null', T_stat_1N_3N,'P-value', P_val_1N_3N,'Sample size N', N_MJ_Phase_1N_3N)
T_sign_1N_3N, P_sign_1N_3N = scipy.stats.wilcoxon(MJ_Phase_1N_to_3_comon, MJ_Phase_3N_to_1_comon)

T_stat_1N_3N_filter, P_val_1N_3N_filter = scipy.stats.ttest_ind(MJ_filter_1N_to_3_comon,MJ_filter_3N_to_1_comon, axis=0, equal_var=True)
degree_1N_3N_filter = (N_MJ_filter_1N_3N -1) *Level_of_confidence
if degree_1N_3N_filter < abs(T_stat_1N_3N_filter):
    print('1N and 3N Filter rejects the null', T_stat_1N_3N_filter,'P-value', P_val_1N_3N_filter,'Sample size N', N_MJ_filter_1N_3N)
else:
    print('1N and 3N Filter accepts the null', T_stat_1N_3N_filter,'P-value', P_val_1N_3N_filter,'Sample size N', N_MJ_filter_1N_3N)
T_sign_1N_3N_filter, P_sign_1N_3N_filter = scipy.stats.wilcoxon(MJ_filter_1N_to_3_comon, MJ_filter_3N_to_1_comon)

# 1n to 3n HOOOOOOD

T_stat_1H_3H, P_val_1H_3H = scipy.stats.ttest_ind(MJ_Phase_1H_to_3_comon,MJ_Phase_3H_to_1_comon, axis=0, equal_var=True)
degree_1H_3H = (N_MJ_Phase_1H_3H -1) *Level_of_confidence
if degree_1H_3H < abs(T_stat_1H_3H):
    print('1H and 3H Phase rejects the null', T_stat_1H_3H,'P-value', P_val_1H_3H,'Sample size N', N_MJ_Phase_1H_3H)
else:
    print('1H and 3H Phase accepts the null', T_stat_1H_3H,'P-value', P_val_1H_3H,'Sample size N', N_MJ_Phase_1H_3H)
T_sign_1H_3H, P_sign_1H_3H = scipy.stats.wilcoxon(MJ_Phase_1H_to_3_comon, MJ_Phase_3H_to_1_comon)

T_stat_1H_3H_filter, P_val_1H_3H_filter = scipy.stats.ttest_ind(MJ_filter_1H_to_3_comon,MJ_filter_3H_to_1_comon, axis=0, equal_var=True)
degree_1H_3H_filter = (N_MJ_filter_1H_3H -1) *Level_of_confidence
if degree_1H_3H_filter < abs(T_stat_1H_3H_filter):
    print('1H and 3H Filter rejects the null', T_stat_1H_3H_filter,'P-value', P_val_1H_3H_filter,'Sample size N', N_MJ_filter_1H_3H)
else:
    print('1H and 3H Filter accepts the null', T_stat_1H_3H_filter,'P-value', P_val_1H_3H_filter,'Sample size N', N_MJ_filter_1H_3H)
T_sign_1H_3H_filter, P_sign_1H_3H_filter = scipy.stats.wilcoxon(MJ_filter_1H_to_3_comon, MJ_filter_3H_to_1_comon)




T_stat_1N_4N, P_val_1N_4N = scipy.stats.ttest_ind(MJ_Phase_1N_to_4_comon,MJ_Phase_4N_to_1_comon, axis=0, equal_var=True)
degree_1N_4N = (N_MJ_Phase_1N_4N -1) *Level_of_confidence
if degree_1N_4N < abs(T_stat_1N_4N):
    print('1N and 4N Phase rejects the null', T_stat_1N_4N,'P-value', P_val_1N_4N,'Sample size N', N_MJ_Phase_1N_4N)
else:
    print('1N and 4N Phase accepts the null', T_stat_1N_4N,'P-value', P_val_1N_4N,'Sample size N', N_MJ_Phase_1N_4N)

T_sign_1N_4N, P_sign_1N_4N = scipy.stats.wilcoxon(MJ_Phase_1N_to_4_comon, MJ_Phase_4N_to_1_comon)
    
T_stat_1N_4N_filter, P_val_1N_4N_filter = scipy.stats.ttest_ind(MJ_filter_1N_to_4_comon,MJ_filter_4N_to_1_comon, axis=0, equal_var=True)
degree_1N_4N_filter = (N_MJ_filter_1N_4N -1) *Level_of_confidence
if degree_1N_4N_filter < abs(T_stat_1N_4N_filter):
    print('1N and 4N Filter rejects the null', T_stat_1N_4N_filter,'P-value', P_val_1N_4N_filter,'Sample size N', N_MJ_filter_1N_4N)
else:
    print('1N and 4N Filter accepts the null', T_stat_1N_4N_filter,'P-value', P_val_1N_4N_filter,'Sample size N', N_MJ_filter_1N_4N)
T_sign_1N_4N_filter, P_sign_1N_4N_filter = scipy.stats.wilcoxon(MJ_filter_1N_to_4_comon, MJ_filter_4N_to_1_comon)      

T_stat_2N_3N, P_val_2N_3N = scipy.stats.ttest_ind(MJ_Phase_2N_to_3_comon,MJ_Phase_3N_to_2_comon, axis=0, equal_var=True)
degree_2N_3N = (N_MJ_Phase_2N_3N -1) *Level_of_confidence
if degree_2N_3N < abs(T_stat_2N_3N):
    print('2N and 3N Phase rejects the null', T_stat_2N_3N,'P-value', P_val_2N_3N,'Sample size N', N_MJ_Phase_2N_3N)
else:
    print('2N and 3N Phase accepts the null', T_stat_2N_3N,'P-value', P_val_2N_3N,'Sample size N', N_MJ_Phase_2N_3N)
T_sign_2N_3N, P_sign_2N_3N = scipy.stats.wilcoxon(MJ_Phase_2N_to_3_comon, MJ_Phase_3N_to_2_comon)

T_stat_2N_3N_filter, P_val_2N_3N_filter = scipy.stats.ttest_ind(MJ_filter_2N_to_3_comon,MJ_filter_3N_to_2_comon, axis=0, equal_var=True)
degree_2N_3N_filter = (N_MJ_filter_2N_3N -1) *Level_of_confidence
if degree_2N_3N_filter < abs(T_stat_2N_3N_filter):
    print('2N and 3N Filter rejects the null', T_stat_2N_3N_filter,'P-value', P_val_2N_3N_filter,'Sample size N', N_MJ_filter_2N_3N)
else:
    print('2N and 3N Filter accepts the null', T_stat_2N_3N_filter,'P-value', P_val_2N_3N_filter,'Sample size N', N_MJ_filter_2N_3N)
T_sign_2N_3N_filter, P_sign_2N_3N_filter = scipy.stats.wilcoxon(MJ_filter_2N_to_3_comon, MJ_filter_3N_to_2_comon)    


# 2n to 3n HOOOOOOD

T_stat_2H_3H, P_val_2H_3H = scipy.stats.ttest_ind(MJ_Phase_2H_to_3_comon,MJ_Phase_3H_to_2_comon, axis=0, equal_var=True)
degree_2H_3H = (N_MJ_Phase_2H_3H -1) *Level_of_confidence
if degree_2H_3H < abs(T_stat_2H_3H):
    print('2H and 3H Phase rejects the null', T_stat_2H_3H,'P-value', P_val_2H_3H,'Sample size N', N_MJ_Phase_2H_3H)
else:
    print('2H and 3H Phase accepts the null', T_stat_2H_3H,'P-value', P_val_2H_3H,'Sample size N', N_MJ_Phase_2H_3H)
T_sign_2H_3H, P_sign_2H_3H = scipy.stats.wilcoxon(MJ_Phase_2H_to_3_comon, MJ_Phase_3H_to_2_comon)

T_stat_2H_3H_filter, P_val_2H_3H_filter = scipy.stats.ttest_ind(MJ_filter_2H_to_3_comon,MJ_filter_3H_to_2_comon, axis=0, equal_var=True)
degree_2H_3H_filter = (N_MJ_filter_2H_3H -1) *Level_of_confidence
if degree_2H_3H_filter < abs(T_stat_2H_3H_filter):
    print('2H and 3H Filter rejects the null', T_stat_2H_3H_filter,'P-value', P_val_2H_3H_filter,'Sample size N', N_MJ_filter_2H_3H)
else:
    print('2H and 3H Filter accepts the null', T_stat_2H_3H_filter,'P-value', P_val_2H_3H_filter,'Sample size N', N_MJ_filter_2H_3H)
T_sign_2H_3H_filter, P_sign_2H_3H_filter = scipy.stats.wilcoxon(MJ_filter_2H_to_3_comon, MJ_filter_3H_to_2_comon)



T_stat_3N_4N, P_val_3N_4N = scipy.stats.ttest_ind(MJ_Phase_3N_to_4_comon,MJ_Phase_4N_to_3_comon, axis=0, equal_var=True)
degree_3N_4N = (N_MJ_Phase_3N_4N -1) *Level_of_confidence
if degree_3N_4N < abs(T_stat_3N_4N):
    print('3N and 4N Phase rejects the null', T_stat_3N_4N,'P-value', P_val_3N_4N,'Sample size N', N_MJ_Phase_3N_4N)
else:
    print('3N and 4N Phase accepts the null', T_stat_3N_4N,'P-value', P_val_3N_4N,'Sample size N', N_MJ_Phase_3N_4N)
T_sign_3N_4N, P_sign_3N_4N = scipy.stats.wilcoxon(MJ_Phase_3N_to_4_comon, MJ_Phase_4N_to_3_comon)  
    
T_stat_3N_4N_filter, P_val_3N_4N_filter = scipy.stats.ttest_ind(MJ_filter_3N_to_4_comon,MJ_filter_4N_to_3_comon, axis=0, equal_var=True)
degree_3N_4N_filter = (N_MJ_filter_3N_4N -1) *Level_of_confidence
if degree_3N_4N_filter < abs(T_stat_3N_4N_filter):
    print('3N and 4N Filter rejects the null', T_stat_3N_4N_filter,'P-value', P_val_3N_4N_filter,'Sample size N', N_MJ_filter_3N_4N)
else:
    print('3N and 4N Filter accepts the null', T_stat_3N_4N_filter,'P-value', P_val_3N_4N_filter,'Sample size N', N_MJ_filter_3N_4N)
T_sign_3N_4N_filter, P_sign_3N_4N_filter = scipy.stats.wilcoxon(MJ_filter_3N_to_4_comon, MJ_filter_4N_to_3_comon)    

whole_t_stat = [T_stat_1N_2N, T_stat_1N_3N, T_stat_1N_4N, T_stat_2N_3N, T_stat_3N_4N] 
whole_p_test = [P_val_1N_2N,P_val_1N_3N,P_val_1N_4N,P_val_2N_3N,P_val_3N_4N]
Whole_sample = [N_MJ_Phase_1N_2N, N_MJ_Phase_1N_3N, N_MJ_Phase_1N_4N, N_MJ_Phase_2N_3N, N_MJ_Phase_3N_4N]
Whole_degree = [degree_1N_2N, degree_1N_3N, degree_1N_4N, degree_2N_3N, degree_3N_4N]
Whole_sighn_t_stat = [T_sign_1N_2N,T_sign_1N_3N,T_sign_1N_4N,T_sign_2N_3N,T_sign_3N_4N]
Whole_sighn_p_test = [P_sign_1N_2N,P_sign_1N_3N,P_sign_1N_4N,P_sign_2N_3N,P_sign_3N_4N]

STD_1 = [np.std(MJ_Phase_1N_to_2_comon), np.std(MJ_Phase_1N_to_3_comon),np.std(MJ_Phase_1N_to_4_comon),np.std(MJ_Phase_2N_to_3_comon),np.std(MJ_Phase_3N_to_4_comon)]
Median_1 = [stat.median(MJ_Phase_1N_to_2_comon), stat.median(MJ_Phase_1N_to_3_comon),stat.median(MJ_Phase_1N_to_4_comon),stat.median(MJ_Phase_2N_to_3_comon),stat.median(MJ_Phase_3N_to_4_comon)]
Mean_1 = [np.average(MJ_Phase_1N_to_2_comon),np.average(MJ_Phase_1N_to_3_comon),np.average(MJ_Phase_1N_to_4_comon),np.average(MJ_Phase_2N_to_3_comon),np.average(MJ_Phase_3N_to_4_comon)]
STD_2 = [np.std(MJ_Phase_2N_to_1_comon), np.std(MJ_Phase_3N_to_1_comon),np.std(MJ_Phase_4N_to_1_comon),np.std(MJ_Phase_3N_to_2_comon),np.std(MJ_Phase_4N_to_3_comon)]
Median_2 = [stat.median(MJ_Phase_2N_to_1_comon), stat.median(MJ_Phase_3N_to_1_comon),stat.median(MJ_Phase_4N_to_1_comon),stat.median(MJ_Phase_3N_to_2_comon),stat.median(MJ_Phase_4N_to_3_comon)]
Mean_2 = [np.average(MJ_Phase_2N_to_1_comon),np.average(MJ_Phase_3N_to_1_comon),np.average(MJ_Phase_4N_to_1_comon),np.average(MJ_Phase_3N_to_2_comon),np.average(MJ_Phase_4N_to_3_comon)]

No_hood_percent_days_Filtered = [sum(Filter_1N_day_count)/sum(Phase_1N_day_count),sum(Filter_2N_day_count)/sum(Phase_2N_day_count),sum(Filter_3N_day_count)/sum(Phase_3N_day_count),sum(Filter_4N_day_count)/sum(Phase_4N_day_count) ]
hood_percent_days_Filtered = [sum(Filter_1H_day_count)/sum(Phase_1H_day_count),sum(Filter_2H_day_count)/sum(Phase_2H_day_count),sum(Filter_3H_day_count)/sum(Phase_3H_day_count)]

Hood_percentage = {'Phase':['1H','2H','3H'], 'Percentatges of hood filter':hood_percent_days_Filtered}
No_Hood_percentage = {'Phase':['1N','2N','3N','4N'],'Percentatges of No hood filter':No_hood_percent_days_Filtered}
df_percent_hood = pd.DataFrame(Hood_percentage)
df_percent_No_hood = pd.DataFrame(No_Hood_percentage)

whole_t_stat_H = [T_stat_1H_2H, T_stat_1H_3H, T_stat_2H_3H] 
whole_p_test_H = [P_val_1H_2H,P_val_1H_3H,P_val_2H_3H]
Whole_sample_H = [N_MJ_Phase_1H_2H, N_MJ_Phase_1H_3H,N_MJ_Phase_2H_3H]
Whole_degree_H = [degree_1H_2H, degree_1H_3H, degree_2H_3H]
Whole_sighn_t_stat_H = [T_sign_1H_2H,T_sign_1H_3H,T_sign_2H_3H]
Whole_sighn_p_test_H = [P_sign_1H_2H,P_sign_1H_3H,P_sign_2H_3H]

STD_1_H = [np.std(MJ_Phase_1H_to_2_comon), np.std(MJ_Phase_1H_to_3_comon),np.std(MJ_Phase_2H_to_3_comon)]
Median_1_H = [stat.median(MJ_Phase_1H_to_2_comon), stat.median(MJ_Phase_1H_to_3_comon),stat.median(MJ_Phase_2H_to_3_comon)]
Mean_1_H = [np.average(MJ_Phase_1H_to_2_comon),np.average(MJ_Phase_1H_to_3_comon),np.average(MJ_Phase_2H_to_3_comon)]
STD_2_H = [np.std(MJ_Phase_2H_to_1_comon), np.std(MJ_Phase_3H_to_1_comon),np.std(MJ_Phase_3H_to_2_comon)]
Median_2_H = [stat.median(MJ_Phase_2H_to_1_comon), stat.median(MJ_Phase_3H_to_1_comon),stat.median(MJ_Phase_3H_to_2_comon)]
Mean_2_H = [np.average(MJ_Phase_2H_to_1_comon),np.average(MJ_Phase_3H_to_1_comon),np.average(MJ_Phase_3H_to_2_comon)]



Non_filtered_no_hood = {'Phase':['1n-2N','1n-3n','1n-4n','2n-3n', '3n-4n'],'T-statistic':whole_t_stat, 'P Value':whole_p_test,
                'T-statistic-Sign-Test':Whole_sighn_t_stat, 'P Vaue-Sign Test':Whole_sighn_p_test,
                'Deggree of Confidence':Whole_degree, 'Sample Size':Whole_sample,'Std _1':STD_1,'median _1':Median_1,'mean _1':Mean_1,'Std _2':STD_2,'median _2':Median_2,'mean _2':Mean_2   }

df_Non_filtered_no_hood = pd.DataFrame(Non_filtered_no_hood, columns=['Phase','T-statistic','P Value','T-statistic-Sign-Test',
                                                              'P Vaue-Sign Test','Deggree of Confidence','Sample Size', 'Std _1','median _1','mean _1','Std _2','median _2','mean _2'])


Non_filtered_hood = {'Phase _Hood':['1H-2H','1H-3H','2H-3H'],'T-statistic':whole_t_stat_H, 'P Value':whole_p_test_H,
                'T-statistic-Sign-Test':Whole_sighn_t_stat_H, 'P Vaue-Sign Test':Whole_sighn_p_test_H,
                'Deggree of Confidence':Whole_degree_H, 'Sample Size':Whole_sample_H,'Std _1':STD_1_H,'median _1':Median_1_H,'mean _1':Mean_1_H,'Std _2':STD_2_H,'median _2':Median_2_H,'mean _2':Mean_2_H   }

df_Non_filtered_hood = pd.DataFrame(Non_filtered_hood, columns=['Phase _Hood','T-statistic','P Value','T-statistic-Sign-Test',
                                                              'P Vaue-Sign Test','Deggree of Confidence','Sample Size', 'Std _1','median _1','mean _1','Std _2','median _2','mean _2'])


whole_t_stat_filter = [T_stat_1N_2N_filter, T_stat_1N_3N_filter, T_stat_1N_4N_filter, T_stat_2N_3N_filter, T_stat_3N_4N_filter] 
whole_p_test_filter = [P_val_1N_2N_filter,P_val_1N_3N_filter,P_val_1N_4N_filter,P_val_2N_3N_filter,P_val_3N_4N_filter]
Whole_sample_filter = [N_MJ_Phase_1N_2N, N_MJ_Phase_1N_3N, N_MJ_Phase_1N_4N, N_MJ_Phase_2N_3N, N_MJ_Phase_3N_4N]
Whole_degree_filter = [degree_1N_2N, degree_1N_3N, degree_1N_4N, degree_2N_3N, degree_3N_4N]
Whole_sighn_t_stat_filter = [T_sign_1N_2N_filter,T_sign_1N_3N_filter,T_sign_1N_4N_filter,T_sign_2N_3N_filter,T_sign_3N_4N_filter]
Whole_sighn_p_test_filter = [P_sign_1N_2N_filter ,P_sign_1N_3N_filter,P_sign_1N_4N_filter,P_sign_2N_3N_filter,P_sign_3N_4N_filter]

whole_t_stat_filter_H = [T_stat_1H_2H_filter, T_stat_1H_3H_filter, T_stat_2H_3H_filter] 
whole_p_test_filter_H = [P_val_1H_2H_filter,P_val_1H_3H_filter,P_val_2H_3H_filter]
Whole_sample_filter_H = [N_MJ_Phase_1H_2H, N_MJ_Phase_1H_3H, N_MJ_Phase_2H_3H]
Whole_degree_filter_H = [degree_1H_2H, degree_1H_3H, degree_2H_3H]
Whole_sighn_t_stat_filter_H = [T_sign_1H_2H_filter,T_sign_1H_3H_filter,T_sign_2H_3H_filter]
Whole_sighn_p_test_filter_H = [P_sign_1H_2H_filter ,P_sign_1H_3H_filter,P_sign_2H_3H_filter]

filtered_No_hood = {'Phase Filtered ':['1n-2N - Filter','1n-3n - Filter','1n-4n - Filter','2n-3n - Filter', '3n-4n - Filter'],'T-statistic':whole_t_stat_filter, 'P Value':whole_p_test_filter,
                'T-statistic-Sign-Test':Whole_sighn_t_stat_filter, 'P Vaue-Sign Test':Whole_sighn_p_test_filter,
                'Deggree of Confidence':Whole_degree_filter, 'Sample Size':Whole_sample_filter }

df_filtered_No_hood = pd.DataFrame(filtered_No_hood, columns=['Phase Filtered ' ,'T-statistic','P Value','T-statistic-Sign-Test',
                                                              'P Vaue-Sign Test','Deggree of Confidence','Sample Size'])

filtered_hood = {'Phase Filtered HOOD':['1H-2H - Filter','1H-3H - Filter','2H-3H - Filter'],'T-statistic':whole_t_stat_filter_H, 'P Value':whole_p_test_filter_H,
                'T-statistic-Sign-Test':Whole_sighn_t_stat_filter_H, 'P Vaue-Sign Test':Whole_sighn_p_test_filter_H,
                'Deggree of Confidence':Whole_degree_filter_H, 'Sample Size':Whole_sample_filter_H }

df_filtered_hood = pd.DataFrame(filtered_hood, columns=['Phase Filtered HOOD' ,'T-statistic','P Value','T-statistic-Sign-Test',
                                                              'P Vaue-Sign Test','Deggree of Confidence','Sample Size'])


Kj_per_sae_no_hood = {'median':[np.median(Mj_1N_Phase),np.median(Mj_2N_Phase),np.median(Mj_3N_Phase),np.median(Mj_4N_Phase)],
                        'Phase':['1n','2n','3n','4n']}

df_Kj_per_sae_no_hood = pd.DataFrame(Kj_per_sae_no_hood)

Kj_per_sae_filter_no_hood = {'median filter':[np.median(Mj_filter_1N_Phase),np.median(Mj_filter_2N_Phase),np.median(Mj_filter_3N_Phase),np.median(Mj_filter_4N_Phase)],
                        'Phase':['1n','2n','3n','4n']}

df_Kj_per_sae_filter_no_hood = pd.DataFrame(Kj_per_sae_filter_no_hood)

Kj_per_sae_mean_no_hood = {'mean':[np.mean(Mj_1N_Phase),np.mean(Mj_2N_Phase),np.mean(Mj_3N_Phase),np.mean(Mj_4N_Phase)],
                        'Phase':['1n','2n','3n','4n']}

df_Kj_per_sae_mean_no_hood = pd.DataFrame(Kj_per_sae_mean_no_hood)

###hood
print('Hood section')
Kj_per_sae_Hood = {'median':[np.median(Mj_1H_Phase),np.median(Mj_2H_Phase),np.median(Mj_3H_Phase)],
                        'Phase':['1H','2H','3H']}

df_Kj_per_sae_Hood = pd.DataFrame(Kj_per_sae_Hood)

Kj_per_sae_filter_Hood = {'median filter':[np.median(Mj_filter_1H_Phase),np.median(Mj_filter_2H_Phase),np.median(Mj_filter_3H_Phase)],
                        'Phase':['1H','2H','3H']}

df_Kj_per_sae_filter_Hood = pd.DataFrame(Kj_per_sae_filter_Hood)

Kj_per_sae_mean_Hood = {'mean':[np.mean(Mj_1H_Phase),np.mean(Mj_2H_Phase),np.mean(Mj_3H_Phase)],
                        'Phase':['1H','2H','3H']}
df_Kj_per_sae_mean_Hood = pd.DataFrame(Kj_per_sae_mean_Hood)

pATH = "C:/Users/gvros/Box/OSU, CSC, CQC Project files/P_TEST_NO_HOOD_24hour.csv"
df_Non_filtered_no_hood.to_csv(pATH, index=False,mode='a')
df_filtered_No_hood.to_csv(pATH, index=False,mode='a')

df_Non_filtered_hood.to_csv(pATH, index=False,mode='a')
df_filtered_hood.to_csv(pATH, index=False,mode='a')
df_percent_hood.to_csv(pATH, index=False,mode='a')
df_percent_No_hood.to_csv(pATH, index=False,mode='a')

df_Kj_per_sae_no_hood.to_csv(pATH, index=False,mode='a')
df_Kj_per_sae_filter_no_hood.to_csv(pATH, index=False,mode='a')
df_Kj_per_sae_mean_no_hood.to_csv(pATH, index=False,mode='a')
df_Kj_per_sae_Hood.to_csv(pATH, index=False,mode='a')
df_Kj_per_sae_filter_Hood.to_csv(pATH, index=False,mode='a')
df_Kj_per_sae_mean_Hood


MJ_Phase_1N_to_3_comon
Mj_filter_3N_Phase