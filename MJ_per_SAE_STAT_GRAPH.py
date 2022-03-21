# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:02:24 2022

@author: rossgra
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy
from scipy.stats import mannwhitneyu
# I am goign to bring in the NO- hood section first

No_hood_MJ_path = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/MJ per SAE - No_Hood.csv" #rossgra or gvros
Hood_MJ_Path = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/MJ per SAE - Hood.csv"

Level_of_confidence = 0.05
No_hood_MJ = pd.read_csv(No_hood_MJ_path)
Hood_MJ = pd.read_csv(Hood_MJ_Path)
#C:\Users\rossgra\Box\Classes\Software Dev C:\Users\rossgra\Box\OSU, CSC, CQC Project files
HH_1N = No_hood_MJ.iloc[:, 0]
HH_2N = No_hood_MJ.iloc[:, 11]
HH_3N = No_hood_MJ.iloc[:, 22]
HH_4N = No_hood_MJ.iloc[:, 33]

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
Phase_3N_day_count = [x for x in No_hood_MJ.iloc[:, 13] if x != -1]
Phase_4N_day_count = [x for x in No_hood_MJ.iloc[:, 14] if x != -1]

Phase_1H_day_count = [x for x in Hood_MJ.iloc[:, 1] if x != -1]
Phase_2H_day_count = [x for x in Hood_MJ.iloc[:, 12] if x != -1]
Phase_3H_day_count = [x for x in Hood_MJ.iloc[:, 13] if x != -1]

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



#1N to 3N

MJ_Phase_1N_to_3_comon = []
MJ_Phase_3N_to_1_comon = []

Day_count_MJ_Phase_1N_3N = []
count_n = 0
for row_1N, hh_1N in enumerate(HH_1N):
    if hh_1N == str(-1):
        break
    for row_3N, hh_3N in enumerate(HH_3N):
        if hh_1N == hh_3N:
            print(row_3N,row_1N, hh_1N,hh_3N)
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
    
T_stat_1N_2N_filter, P_val_1N_2N_filter = scipy.stats.ttest_ind(MJ_filter_1N_to_2_comon,MJ_filter_2N_to_1_comon, axis=0, equal_var=True)
degree_1N_2N_filter = (N_MJ_filter_1N_2N -1) *Level_of_confidence
if degree_1N_2N_filter < abs(T_stat_1N_2N_filter):
    print('1N and 2N Filter rejects the null', T_stat_1N_2N_filter,'P-value', P_val_1N_2N_filter,'Sample size N', N_MJ_filter_1N_2N)
else:
    print('1N and 2N Filter accepts the null', T_stat_1N_2N_filter,'P-value', P_val_1N_2N_filter,'Sample size N', N_MJ_filter_1N_2N)
    
T_stat_1N_3N, P_val_1N_3N = scipy.stats.ttest_ind(MJ_Phase_1N_to_3_comon,MJ_Phase_3N_to_1_comon, axis=0, equal_var=True)
degree_1N_3N = (N_MJ_Phase_1N_3N -1) *Level_of_confidence
if degree_1N_3N < abs(T_stat_1N_3N):
    print('1N and 3N Phase rejects the null', T_stat_1N_3N,'P-value', P_val_1N_3N,'Sample size N', N_MJ_Phase_1N_3N)
else:
    print('1N and 3N Phase accepts the null', T_stat_1N_3N,'P-value', P_val_1N_3N,'Sample size N', N_MJ_Phase_1N_3N)
    
T_stat_1N_3N_filter, P_val_1N_3N_filter = scipy.stats.ttest_ind(MJ_filter_1N_to_3_comon,MJ_filter_3N_to_1_comon, axis=0, equal_var=True)
degree_1N_3N_filter = (N_MJ_filter_1N_3N -1) *Level_of_confidence
if degree_1N_3N_filter < abs(T_stat_1N_3N_filter):
    print('1N and 3N Filter rejects the null', T_stat_1N_3N_filter,'P-value', P_val_1N_3N_filter,'Sample size N', N_MJ_filter_1N_3N)
else:
    print('1N and 3N Filter accepts the null', T_stat_1N_3N_filter,'P-value', P_val_1N_3N_filter,'Sample size N', N_MJ_filter_1N_3N)
    
    
T_stat_1N_4N, P_val_1N_4N = scipy.stats.ttest_ind(MJ_Phase_1N_to_4_comon,MJ_Phase_4N_to_1_comon, axis=0, equal_var=True)
degree_1N_4N = (N_MJ_Phase_1N_4N -1) *Level_of_confidence


print('length of 1n and 4 n:', len(MJ_Phase_1N_to_4_comon), len(MJ_Phase_4N_to_1_comon) )
print('Degree of frededom',degree_1N_4N, T_stat_1N_4N )
if degree_1N_4N < abs(T_stat_1N_4N):
    print('1N and 4N Phase rejects the null', T_stat_1N_4N,'P-value', P_val_1N_4N,'Sample size N', N_MJ_Phase_1N_4N)
    T_sign_1N_4N, P_sign_1N_4N = scipy.stats.wilcoxon(MJ_Phase_1N_to_4_comon, MJ_Phase_4N_to_1_comon)
    print('Tried Wilcox Sign Test, Tstat= ',T_sign_1N_4N, 'P value= ',P_sign_1N_4N, 'Degree of freedom = ',degree_1N_4N, 'Accepted if + ',degree_1N_4N - abs(T_sign_1N_4N)  )
else:
    print('1N and 4N Phase accepts the null', T_stat_1N_4N,'P-value', P_val_1N_4N,'Sample size N', N_MJ_Phase_1N_4N)
    print('Tried Wilcox Sign Test, Tstat= ',T_sign_1N_4N, 'P value= ',P_sign_1N_4N, 'Degree of freedom = ',degree_1N_4N, 'Accepted if + ',degree_1N_4N - abs(T_sign_1N_4N)  )
    
    
T_stat_1N_4N_filter, P_val_1N_4N_filter = scipy.stats.ttest_ind(MJ_filter_1N_to_4_comon,MJ_filter_4N_to_1_comon, axis=0, equal_var=True)
degree_1N_4N_filter = (N_MJ_filter_1N_4N -1) *Level_of_confidence
if degree_1N_4N_filter < abs(T_stat_1N_4N_filter):
    print('1N and 4N Filter rejects the null', T_stat_1N_4N_filter,'P-value', P_val_1N_4N_filter,'Sample size N', N_MJ_filter_1N_4N)
else:
    print('1N and 4N Filter accepts the null', T_stat_1N_4N_filter,'P-value', P_val_1N_4N_filter,'Sample size N', N_MJ_filter_1N_4N)
    

T_stat_2N_3N, P_val_2N_3N = scipy.stats.ttest_ind(MJ_Phase_2N_to_3_comon,MJ_Phase_3N_to_2_comon, axis=0, equal_var=True)
degree_2N_3N = (N_MJ_Phase_2N_3N -1) *Level_of_confidence
if degree_2N_3N < abs(T_stat_2N_3N):
    print('2N and 3N Phase rejects the null', T_stat_2N_3N,'P-value', P_val_2N_3N,'Sample size N', N_MJ_Phase_2N_3N)
else:
    print('2N and 3N Phase accepts the null', T_stat_2N_3N,'P-value', P_val_2N_3N,'Sample size N', N_MJ_Phase_2N_3N)
    
T_stat_2N_3N_filter, P_val_2N_3N_filter = scipy.stats.ttest_ind(MJ_filter_2N_to_3_comon,MJ_filter_3N_to_2_comon, axis=0, equal_var=True)
degree_2N_3N_filter = (N_MJ_filter_2N_3N -1) *Level_of_confidence
if degree_2N_3N_filter < abs(T_stat_2N_3N_filter):
    print('2N and 3N Filter rejects the null', T_stat_2N_3N_filter,'P-value', P_val_2N_3N_filter,'Sample size N', N_MJ_filter_2N_3N)
else:
    print('2N and 3N Filter accepts the null', T_stat_2N_3N_filter,'P-value', P_val_2N_3N_filter,'Sample size N', N_MJ_filter_2N_3N)
    
    
T_stat_3N_4N, P_val_3N_4N = scipy.stats.ttest_ind(MJ_Phase_3N_to_4_comon,MJ_Phase_4N_to_3_comon, axis=0, equal_var=True)
degree_3N_4N = (N_MJ_Phase_3N_4N -1) *Level_of_confidence
if degree_3N_4N < abs(T_stat_3N_4N):
    print('3N and 4N Phase rejects the null', T_stat_3N_4N,'P-value', P_val_3N_4N,'Sample size N', N_MJ_Phase_3N_4N)
else:
    print('3N and 4N Phase accepts the null', T_stat_3N_4N,'P-value', P_val_3N_4N,'Sample size N', N_MJ_Phase_3N_4N)
    
T_stat_3N_4N_filter, P_val_3N_4N_filter = scipy.stats.ttest_ind(MJ_filter_3N_to_4_comon,MJ_filter_4N_to_3_comon, axis=0, equal_var=True)
degree_3N_4N_filter = (N_MJ_filter_3N_4N -1) *Level_of_confidence
if degree_3N_4N_filter < abs(T_stat_3N_4N_filter):
    print('3N and 4N Filter rejects the null', T_stat_3N_4N_filter,'P-value', P_val_3N_4N_filter,'Sample size N', N_MJ_filter_3N_4N)
else:
    print('3N and 4N Filter accepts the null', T_stat_3N_4N_filter,'P-value', P_val_3N_4N_filter,'Sample size N', N_MJ_filter_3N_4N)
    
#sns.distplot(Mj_1N_Phase, hist=True, rug=True)
#sns.distplot(Mj_2N_Phase ,hist=True, rug=True)
#sns.distplot(Mj_3N_Phase , hist=True, rug=True)
#sns.distplot(Mj_4N_Phase , hist=True, rug=True)

#plt.show()

Kj_per_sae_no_hood = {'median':[np.median(Mj_1N_Phase),np.median(Mj_2N_Phase),np.median(Mj_3N_Phase),np.median(Mj_4N_Phase)],
                        'Phase':['1n','2n','3n','4n']}

print(pd.DataFrame(Kj_per_sae_no_hood))

Kj_per_sae_filter_no_hood = {'median filter':[np.median(Mj_filter_1N_Phase),np.median(Mj_filter_2N_Phase),np.median(Mj_filter_3N_Phase),np.median(Mj_filter_4N_Phase)],
                        'Phase':['1n','2n','3n','4n']}

print(pd.DataFrame(Kj_per_sae_filter_no_hood))

Kj_per_sae_mean_no_hood = {'mean':[np.mean(Mj_1N_Phase),np.mean(Mj_2N_Phase),np.mean(Mj_3N_Phase),np.mean(Mj_4N_Phase)],
                        'Phase':['1n','2n','3n','4n']}

print(pd.DataFrame(Kj_per_sae_mean_no_hood))

###hood
print('Hood section')
Kj_per_sae_Hood = {'median':[np.median(Mj_1N_Phase),np.median(Mj_2N_Phase),np.median(Mj_3N_Phase),np.median(Mj_4N_Phase)],
                        'Phase':['1n','2n','3n','4n']}

print(pd.DataFrame(Kj_per_sae_Hood))

Kj_per_sae_filter_Hood = {'median filter':[np.median(Mj_filter_1N_Phase),np.median(Mj_filter_2N_Phase),np.median(Mj_filter_3N_Phase),np.median(Mj_filter_4N_Phase)],
                        'Phase':['1n','2n','3n','4n']}

print(pd.DataFrame(Kj_per_sae_filter_Hood))

Kj_per_sae_mean_Hood = {'mean':[np.mean(Mj_1N_Phase),np.mean(Mj_2N_Phase),np.mean(Mj_3N_Phase),np.mean(Mj_4N_Phase)],
                        'Phase':['1n','2n','3n','4n']}
print(pd.DataFrame(Kj_per_sae_mean_Hood))