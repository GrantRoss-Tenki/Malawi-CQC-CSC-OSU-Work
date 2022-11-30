import os
import pandas as pd
import numpy as np
import csv
import glob
from datetime import datetime
from csv import reader
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
import csv

import statistics as stat

Path_Stove_1 = "F:/Percentile_CSV.csv"
Path_Stove_2 = "F:/Percentile_CSV_2.csv"

Array_1 = np.array(pd.read_csv(Path_Stove_1, header =0))
Array_2 = np.array(pd.read_csv(Path_Stove_2, header =0))
N_1 = len(Array_1)
N_2 = len(Array_2)
print('the lenngth of array 1:', len(Array_1), 'First-' ,Array_1[0], 'Average-',np.average(Array_1), 'Stedev',np.std(Array_1))
percent_1= np.percentile(Array_1, [25,50,75])
print('percentile for Array 1:',percent_1 )

print('-------------- next array -----------------------------')
print('the lenngth of array 2:', len(Array_2), 'First-' ,Array_2[0], 'Average-',np.average(Array_2), 'Stedev',np.std(Array_2))
percent_2= np.percentile(Array_2, [25,50,75])
print('percentile for Array 2:', np.percentile(Array_2, [25,50,75]))

if np.average(Array_1) > np.average(Array_2):
    
    T_test =  ttest_ind(Array_1,Array_2, equal_var = False, alternative='greater')
elif np.average(Array_1) < np.average(Array_2):
    T_test =  ttest_ind(Array_1,Array_2, equal_var = False, alternative='less')
else:
    T_test =  ttest_ind(Array_1,Array_2, equal_var = False, alternative='two-sided')
    
print('T-test- Score: ',(int(T_test[0] * 1000)/1000), '  P-Value: ', 2*T_test[1], type(T_test),'----' , T_test)
tests = [(int(T_test[0] * 10000)/10000), (int(2*T_test[1] * 10000)/10000)]
tests = [str(a) for a in tests]
print('here is the tests----', tests)
col_1 = (percent_1[0],percent_1[1],percent_1[2], np.average(Array_1),np.std(Array_1),N_1)
col_2 = (percent_2[0],percent_2[1],percent_2[2], np.average(Array_2),np.std(Array_2),N_2)

df = pd.DataFrame({'first': col_1, 'second': col_2})
print(df.head())
df_2 = pd.DataFrame({'tests' : tests})
print(df_2.head())
Path_Raw_Event = "F:/Percentile borred.csv"
df.to_csv(Path_Raw_Event,index=False, mode='a')
df_2.to_csv(Path_Raw_Event,index=False, mode='a')
