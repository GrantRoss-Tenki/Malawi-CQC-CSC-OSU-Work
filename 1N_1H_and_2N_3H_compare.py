# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 10:32:00 2022

@author: rossgra
"""

import numpy as np
from numpy.core.fromnumeric import std
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu
import scipy
#import statistics as stat

No_hood_MJ_path = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/1N_1H_and_2N_3H_compare.csv" #rossgra or gvros

No_hood_MJ = pd.read_csv(No_hood_MJ_path)

Fuel_1N_1H = [x for x in No_hood_MJ.iloc[:,1] if x != -1]
Fuel_2N_3H = [x for x in No_hood_MJ.iloc[:,5] if x != -1]
print(Fuel_1N_1H, len(Fuel_1N_1H)) 
Fuel_SAE_1N_1H = [x for x in No_hood_MJ.iloc[:,2] if x != -1]
Fuel_SAE_2N_3H = [x for x in No_hood_MJ.iloc[:,6] if x != -1]

MJ_1N_1H = [x for x in No_hood_MJ.iloc[:,3] if x != -1]
MJ_2N_3H = [x for x in No_hood_MJ.iloc[:,7] if x != -1]

T_stat_Fuel, P_Fuel = scipy.stats.ttest_ind(Fuel_1N_1H, Fuel_2N_3H, axis=0, equal_var=True)
T_sign_Fuel, P_sign_Fuel = scipy.stats.wilcoxon(Fuel_1N_1H, Fuel_2N_3H)

T_stat_Fuel_SAE, P_Fuel_SAE = scipy.stats.ttest_ind(Fuel_SAE_1N_1H, Fuel_SAE_2N_3H, axis=0, equal_var=True)
T_sign_Fuel_SAE, P_sign_Fuel_SAE = scipy.stats.wilcoxon(Fuel_SAE_1N_1H, Fuel_SAE_2N_3H)

T_stat_MJ, P_MJ = scipy.stats.ttest_ind(MJ_1N_1H, MJ_2N_3H, axis=0, equal_var=True)
T_sign_MJ, P_sign_MJ = scipy.stats.wilcoxon(MJ_1N_1H, MJ_2N_3H)

df_met =pd.DataFrame({'Metric':['Fuel reduc','fuel pval','fuel pval sign','MJ reduc','mj pval','mj pval sign'], 'Percentatges of hood filter':[(np.median(Fuel_2N_3H)/np.median(Fuel_1N_1H)),
       P_Fuel,P_sign_Fuel,(np.median(MJ_2N_3H)/np.median(MJ_1N_1H)),P_MJ,P_sign_MJ]})
print(df_met)



Cooking_times_path = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/Ratios_COOKINGTIMES_day_event.csv" #rossgra or gvros
cooking_times = pd.read_csv(Cooking_times_path)

event_1N_2 = cooking_times.iloc[:,1]
event_2N_1 = cooking_times.iloc[:,4]
day_1N_2 = cooking_times.iloc[:,2]
day_2N_1 = cooking_times.iloc[:,5]
T_stat_day_1n_2, P_day_1n_2 = scipy.stats.ttest_ind(day_1N_2, day_2N_1, axis=0, equal_var=True)
T_sign_day_1n_2, P_sign_day_1n_2  = scipy.stats.wilcoxon(day_1N_2, day_2N_1)
T_stat_event_1n_2, P_event_1n_2 = scipy.stats.ttest_ind(event_1N_2, event_2N_1, axis=0, equal_var=True)
T_sign_event_1n_2, P_sign_event_1n_2  = scipy.stats.wilcoxon(event_1N_2, event_2N_1)

df_1N_2N =pd.DataFrame({'Metric 2N-1N':['day reduc','day pval','day pval sign','Event reduc','event pval','event pval sign'], 
                      '1N - 2N':[(np.median(day_2N_1)/np.median(day_1N_2)), 
                      P_day_1n_2,P_sign_day_1n_2,(np.median(event_2N_1)/np.median(event_1N_2)),P_event_1n_2,P_sign_event_1n_2]})
print(df_1N_2N)

event_1N_3 = cooking_times.iloc[:,7]
event_3N_1 = cooking_times.iloc[:,10]
day_1N_3 = cooking_times.iloc[:,8]
day_3N_1 = cooking_times.iloc[:,11]
T_stat_day_1n_3, P_day_1n_3 = scipy.stats.ttest_ind(day_1N_3, day_3N_1, axis=0, equal_var=True)
T_sign_day_1n_3, P_sign_day_1n_3  = scipy.stats.wilcoxon(day_1N_3, day_3N_1)
T_stat_event_1n_3, P_event_1n_3 = scipy.stats.ttest_ind(event_1N_3, event_3N_1, axis=0, equal_var=True)
T_sign_event_1n_3, P_sign_event_1n_3  = scipy.stats.wilcoxon(event_1N_3, event_3N_1)

df_1N_3N =pd.DataFrame({'Metric 3N-1N':['day reduc','day pval','day pval sign','Event reduc','event pval','event pval sign'], 
                      '1N - 3N':[(np.median(day_3N_1)/np.median(day_1N_3)), 
                      P_day_1n_3,P_sign_day_1n_3,(np.median(event_3N_1)/np.median(event_1N_3)),P_event_1n_3,P_sign_event_1n_3]})
print(df_1N_3N)


event_1N_4 = [x for x in cooking_times.iloc[:,13] if x != -1]
event_4N_1 = [x for x in cooking_times.iloc[:,16] if x != -1]
day_1N_4 = [x for x in cooking_times.iloc[:,14] if x != -1]
day_4N_1 = [x for x in cooking_times.iloc[:,17] if x != -1]
T_stat_day_1n_4, P_day_1n_4 = scipy.stats.ttest_ind(day_1N_4, day_4N_1, axis=0, equal_var=True)
T_sign_day_1n_4, P_sign_day_1n_4  = scipy.stats.wilcoxon(day_1N_4, day_4N_1)
T_stat_event_1n_4, P_event_1n_4 = scipy.stats.ttest_ind(event_1N_4, event_4N_1, axis=0, equal_var=True)
T_sign_event_1n_4, P_sign_event_1n_4  = scipy.stats.wilcoxon(event_1N_4, event_4N_1)

df_1N_4N =pd.DataFrame({'Metric 4N-1N':['day reduc','day pval','day pval sign','Event reduc','event pval','event pval sign'], 
                      '1N - 4N':[(np.median(day_4N_1)/np.median(day_1N_4)), 
                      P_day_1n_4,P_sign_day_1n_4,(np.median(event_4N_1)/np.median(event_1N_4)),P_event_1n_4,P_sign_event_1n_4]})
print(df_1N_4N)


event_2N_3 = [x for x in cooking_times.iloc[:,19] if x != -1]
event_3N_2 = [x for x in cooking_times.iloc[:,22] if x != -1]
day_2N_3 = [x for x in cooking_times.iloc[:,20] if x != -1]
day_3N_2 = [x for x in cooking_times.iloc[:,23] if x != -1]
T_stat_day_2n_3, P_day_2n_3 = scipy.stats.ttest_ind(day_3N_2, day_2N_3, axis=0, equal_var=True)
T_sign_day_2n_3, P_sign_day_2n_3  = scipy.stats.wilcoxon(day_2N_3, day_3N_2)
T_stat_event_2n_3, P_event_2n_3 = scipy.stats.ttest_ind(event_2N_3, event_3N_2, axis=0, equal_var=True)
T_sign_event_2n_3, P_sign_event_2n_3  = scipy.stats.wilcoxon(event_2N_3, event_3N_2)

df_2N_3N =pd.DataFrame({'Metric 3N-2N':['day reduc','day pval','day pval sign','Event reduc','event pval','event pval sign'], 
                      '3N - 2N':[(np.median(day_3N_2)/np.median(day_2N_3)), 
                      P_day_2n_3,P_sign_day_2n_3,(np.median(event_3N_2)/np.median(event_2N_3)),P_event_2n_3,P_sign_event_2n_3]})
print(df_2N_3N)


event_3N_4 = [x for x in cooking_times.iloc[:,25] if x != -1]
event_4N_3 = [x for x in cooking_times.iloc[:,28] if x != -1]
day_3N_4 = [x for x in cooking_times.iloc[:,26] if x != -1]
day_4N_3 = [x for x in cooking_times.iloc[:,29] if x != -1]
T_stat_day_4n_3, P_day_4n_3 = scipy.stats.ttest_ind(day_3N_4, day_4N_3, axis=0, equal_var=True)
T_sign_day_4n_3, P_sign_day_4n_3  = scipy.stats.wilcoxon(day_4N_3, day_3N_4)
T_stat_event_4n_3, P_event_4n_3 = scipy.stats.ttest_ind(event_4N_3, event_3N_4, axis=0, equal_var=True)
T_sign_event_4n_3, P_sign_event_4n_3  = scipy.stats.wilcoxon(event_4N_3, event_3N_4)

df_4N_3N =pd.DataFrame({'Metric 3N-4N':['day reduc','day pval','day pval sign','Event reduc','event pval','event pval sign'], 
                      '3N - 4N':[(np.median(day_3N_4)/np.median(day_4N_3)), 
                      P_day_4n_3,P_sign_day_4n_3,(np.median(event_3N_4)/np.median(event_4N_3)),P_event_4n_3,P_sign_event_4n_3]})
print(df_4N_3N)


event_2N_4 = [x for x in cooking_times.iloc[:,31] if x != -1]
event_4N_2 = [x for x in cooking_times.iloc[:,34] if x != -1]
day_2N_4 = [x for x in cooking_times.iloc[:,32] if x != -1]
day_4N_2 = [x for x in cooking_times.iloc[:,35] if x != -1]
T_stat_day_4n_2, P_day_4n_2 = scipy.stats.ttest_ind(day_2N_4, day_4N_2, axis=0, equal_var=True)
T_sign_day_4n_2, P_sign_day_4n_2  = scipy.stats.wilcoxon(day_4N_2, day_2N_4)
T_stat_event_4n_2, P_event_4n_2 = scipy.stats.ttest_ind(event_4N_2, event_2N_4, axis=0, equal_var=True)
T_sign_event_4n_2, P_sign_event_4n_2  = scipy.stats.wilcoxon(event_4N_2, event_2N_4)

df_4N_2N =pd.DataFrame({'Metric 2N-4N':['day reduc','day pval','day pval sign','Event reduc','event pval','event pval sign'], 
                      '2N - 4N':[(np.median(day_4N_2)/np.median(day_2N_4)), 
                      P_day_4n_2,P_sign_day_4n_2,(np.median(event_4N_2)/np.median(event_2N_4)),P_event_4n_2,P_sign_event_4n_2]})
print(df_4N_2N)


event_1H_2 = [x for x in cooking_times.iloc[:,37] if x != -1]
event_2H_1 = [x for x in cooking_times.iloc[:,40] if x != -1]
day_1H_2 = [x for x in cooking_times.iloc[:,38] if x != -1]
day_2H_1 = [x for x in cooking_times.iloc[:,41] if x != -1]
T_stat_day_1H_2, P_day_1H_2 = scipy.stats.ttest_ind(day_1H_2, day_2H_1, axis=0, equal_var=True)
T_sign_day_1H_2, P_sign_day_1H_2  = scipy.stats.wilcoxon(day_1H_2, day_2H_1)
T_stat_event_1H_2, P_event_1H_2 = scipy.stats.ttest_ind(event_1H_2, event_2H_1, axis=0, equal_var=True)
T_sign_event_1H_2, P_sign_event_1H_2  = scipy.stats.wilcoxon(event_1H_2, event_2H_1)

df_1H_2H =pd.DataFrame({'Metric 2H-1H':['day reduc','day pval','day pval sign','Event reduc','event pval','event pval sign'], 
                      '2H - 1H':[(np.median(day_2H_1)/np.median(day_1H_2)), 
                      P_day_1H_2,P_sign_day_1H_2,(np.median(event_2H_1)/np.median(event_1H_2)),P_event_1H_2,P_sign_event_1H_2]})
print(df_1H_2H)


event_1H_3 = [x for x in cooking_times.iloc[:,43] if x != -1]
event_3H_1 = [x for x in cooking_times.iloc[:,46] if x != -1]
day_1H_3 = [x for x in cooking_times.iloc[:,44] if x != -1]
day_3H_1 = [x for x in cooking_times.iloc[:,47] if x != -1]
T_stat_day_1H_3, P_day_1H_3 = scipy.stats.ttest_ind(day_1H_3, day_3H_1, axis=0, equal_var=True)
T_sign_day_1H_3, P_sign_day_1H_3  = scipy.stats.wilcoxon(day_1H_3, day_3H_1)
T_stat_event_1H_3, P_event_1H_3 = scipy.stats.ttest_ind(event_1H_3, event_3H_1, axis=0, equal_var=True)
T_sign_event_1H_3, P_sign_event_1H_3  = scipy.stats.wilcoxon(event_1H_3, event_3H_1)

df_1H_3H =pd.DataFrame({'Metric 3H-1H':['day reduc','day pval','day pval sign','Event reduc','event pval','event pval sign'], 
                      '3H - 1H':[(np.median(day_3H_1)/np.median(day_1H_3)), 
                      P_day_1H_3,P_sign_day_1H_3,(np.median(event_3H_1)/np.median(event_1H_3)),P_event_1H_3,P_sign_event_1H_3]})
print(df_1H_3H)


event_2H_3 = [x for x in cooking_times.iloc[:,49] if x != -1]
event_3H_2 = [x for x in cooking_times.iloc[:,52] if x != -1]
day_2H_3 = [x for x in cooking_times.iloc[:,50] if x != -1]
day_3H_2 = [x for x in cooking_times.iloc[:,53] if x != -1]
T_stat_day_2H_3, P_day_2H_3 = scipy.stats.ttest_ind(day_2H_3, day_2H_3, axis=0, equal_var=True)
T_sign_day_2H_3, P_sign_day_2H_3  = scipy.stats.wilcoxon(day_2H_3, day_3H_2)
T_stat_event_2H_3, P_event_2H_3 = scipy.stats.ttest_ind(event_2H_3, event_3H_2, axis=0, equal_var=True)
T_sign_event_2H_3, P_sign_event_2H_3  = scipy.stats.wilcoxon(event_2H_3, event_3H_2)

df_2H_3H =pd.DataFrame({'Metric 3H-2H':['day reduc','day pval','day pval sign','Event reduc','event pval','event pval sign'], 
                      '3H - 2H':[(np.median(day_3H_2)/np.median(day_2H_3)), 
                      P_day_2H_3,P_sign_day_2H_3,(np.median(event_3H_2)/np.median(event_2H_3)),P_event_2H_3,P_sign_event_2H_3]})
print(df_2H_3H)


event_1H1N_23 = [x for x in cooking_times.iloc[:,55] if x != -1]
event_3H2N_11 = [x for x in cooking_times.iloc[:,58] if x != -1]
day_1H1N_23 = [x for x in cooking_times.iloc[:,56] if x != -1]
day_3H2N_11 = [x for x in cooking_times.iloc[:,59] if x != -1]
T_stat_day_1N1H_32, P_day_1N1H_32 = scipy.stats.ttest_ind(day_1H1N_23, day_3H2N_11, axis=0, equal_var=True)
T_sign_day_1N1H_32, P_sign_day_1N1H_32  = scipy.stats.wilcoxon(day_1H1N_23, day_3H2N_11)
T_stat_event_1N1H_32, P_event_1N1H_32 = scipy.stats.ttest_ind(event_1H1N_23, event_3H2N_11, axis=0, equal_var=True)
T_sign_event_1N1H_32, P_sign_event_1N1H_32  = scipy.stats.wilcoxon(event_1H1N_23, event_3H2N_11)

df_1N1H_32 =pd.DataFrame({'Metric 1N1H-2N3H':['day reduc','day pval','day pval sign','Event reduc','event pval','event pval sign'], 
                      '1N1H-2N3H':[(np.median(day_3H2N_11)/np.median(day_1H1N_23)), 
                      P_day_1N1H_32,P_sign_day_1N1H_32,(np.median(event_3H2N_11)/np.median(event_1H1N_23)),P_event_1N1H_32,P_sign_event_1N1H_32]})
print(df_1N1H_32)
