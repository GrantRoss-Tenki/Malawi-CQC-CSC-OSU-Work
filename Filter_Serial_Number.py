import itertools
import os
import pandas as pd
import numpy as np
import csv
import glob
from decimal import *
from itertools import chain
#import statistics as stat
import datetime
from datetime import datetime
from itertools import islice, cycle
from io import StringIO
import matplotlib.pyplot as plt
import seaborn as sns

# this is for the filter serial number and household with minutes
USB = "D" # or "E"

Pump_information_path  = USB+ ":/PUMP FILES/Gravimetric_Analysis_MALAWI_2_16_2022.csv"
Pump_Household_information = USB +":/PUMP FILES/Phase_HH_SN.csv"

Filter_information = pd.read_csv(Pump_information_path)
Household_information = pd.read_csv(Pump_Household_information)

Filter_SN_information = Filter_information.iloc[:, 0]
Filter_weight = Filter_information.iloc[:, 3]

Filter_SN_Household = Household_information.iloc[:,4]
Household_number = Household_information.iloc[:,0]



print('checking 1N split', Filter_SN_Household[40], Household_number[40])
print('checking 1H split', Filter_SN_Household[56], Household_number[56])
print('checking 2N split', Filter_SN_Household[97], Household_number[97])
print('checking 2H split', Filter_SN_Household[113],Household_number[113])
print('checking 3N split', Filter_SN_Household[154], Household_number[154])
print('checking 3H split', Filter_SN_Household[170], Household_number[170])
print('checking 4N split', Filter_SN_Household[211], Household_number[211])
print('type of each hh', type(Filter_SN_Household))
print('type of each SN', type(Filter_SN_information))



Household_1N = []
Household_1N_SN = []
Difference_1N = []
Time_collection_1N = []
Household_1H = []
Household_1H_SN = []
Difference_1H = []
Time_collection_1H = []
Household_2N = []
Household_2N_SN = []
Difference_2N = []
Full_24_hour_pumps = [1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030]
Time_collection_2N =[]

Household_2H = []
Household_2H_SN = []
Difference_2H = []
Household_3N = []
Household_3N_SN = []
Difference_3N = []
Household_3H = []
Household_3H_SN = []
Difference_3H = []
Household_4N = []
Household_4N_SN = []
Difference_4N = []



for val, SN in enumerate(Filter_SN_information):
    for val_H, HH_SN in enumerate(Filter_SN_Household):
        if SN == int(HH_SN):
            #print('sdfasdfasdfsadfsad')
            if val_H <= 40:
                Household_1N_SN.append(SN)
                Household_1N.append(Household_number[val_H])
                Time_collection_1N.append(Household_information.iloc[val_H, 6])
                if Filter_weight[val] == '#DIV/0!':
                    Difference_1N.append(-1)
                else:
                    Difference_1N.append(Filter_weight[val])
            elif 40 < val_H <= 56:
                Household_1H_SN.append(SN)
                Household_1H.append(Household_number[val_H])
                Time_collection_1H.append(Household_information.iloc[val_H, 6])
                if Filter_weight[val] == '#DIV/0!':
                    Difference_1H.append(-1)
                else:
                    Difference_1H.append(Filter_weight[val])
            elif 56 < val_H <= 97:
                Household_2N_SN.append(SN)
                Household_2N.append(Household_number[val_H])
                Time_collection_2N.append(Household_information.iloc[val_H, 6])
                if Filter_weight[val] == '#DIV/0!':
                    Difference_2N.append(-1)
                else:
                    Difference_2N.append(Filter_weight[val])
            elif 97 < val_H <= 113:
                Household_2H_SN.append(SN)
                Household_2H.append(Household_number[val_H])
                if Filter_weight[val] == '#DIV/0!':
                    Difference_2H.append(-1)
                else:
                    Difference_2H.append(Filter_weight[val])
            elif 113 < val_H <= 154:
                Household_3N_SN.append(SN)
                Household_3N.append(Household_number[val_H])
                if Filter_weight[val] == '#DIV/0!':
                    Difference_3N.append(-1)
                else:
                    Difference_3N.append(Filter_weight[val])
            elif 154 < val_H <= 170:
                Household_3H_SN.append(SN)
                Household_3H.append(Household_number[val_H])
                if Filter_weight[val] == '#DIV/0!':
                    Difference_3H.append(-1)
                else:
                    Difference_3H.append(Filter_weight[val])
            elif 170 < val_H <= 211:
                Household_4N_SN.append(SN)
                Household_4N.append(Household_number[val_H])
                if Filter_weight[val] == '#DIV/0!':
                    Difference_4N.append(-1)
                else:
                    Difference_4N.append(Filter_weight[val])




# creating a csv file that will be taken to another file read
# 1N
phase_1N = {'Household': Household_1N, 'Household SN': Household_1N_SN, 
                  'Weight Difference': Difference_1N, 'Time Collected':Time_collection_1N}
DF_1N = pd.DataFrame(phase_1N, columns= ['Household','Household SN','Weight Difference', 'Time Collected'])
path_1N = USB +":/PUMP FILES/1N_Compress_SN.csv"
DF_1N.to_csv(path_1N, index=False, mode= 'a')
# 1H
phase_1H = {'Household': Household_1H, 'Household SN': Household_1H_SN, 
                  'Weight Difference': Difference_1H, 'Time Collected':Time_collection_1H}
DF_1H = pd.DataFrame(phase_1H, columns= ['Household','Household SN','Weight Difference', 'Time Collected'])
path_1H = USB+":/PUMP FILES/1H_Compress_SN.csv"
DF_1H.to_csv(path_1H, index=False, mode= 'a')
# 2N
phase_2N = {'Household': Household_2N, 'Household SN': Household_2N_SN, 
                  'Weight Difference': Difference_2N, 'Time Collected':Time_collection_2N}
DF_2N = pd.DataFrame(phase_2N, columns= ['Household','Household SN','Weight Difference','Time Collected'])
path_2N = USB +":/PUMP FILES/2N_Compress_SN.csv"
DF_2N.to_csv(path_2N, index=False, mode= 'a')
# 2H
phase_2H = {'Household': Household_2H, 'Household SN': Household_2H_SN, 
                  'Weight Difference': Difference_2H}
DF_2H = pd.DataFrame(phase_2H, columns= ['Household','Household SN','Weight Difference'])
path_2H = USB +":/PUMP FILES/2H_Compress_SN.csv"
DF_2H.to_csv(path_2H, index=False, mode= 'a')
# 3N
phase_3N = {'Household': Household_3N, 'Household SN': Household_3N_SN, 
                  'Weight Difference': Difference_3N}
DF_3N = pd.DataFrame(phase_3N, columns= ['Household','Household SN','Weight Difference'])
path_3N = USB+":/PUMP FILES/3N_Compress_SN.csv"
DF_3N.to_csv(path_3N, index=False, mode= 'a')
# 3H
phase_3H = {'Household': Household_3H, 'Household SN': Household_3H_SN, 
                  'Weight Difference': Difference_3H}
DF_3H = pd.DataFrame(phase_3H, columns= ['Household','Household SN','Weight Difference'])
path_3H = USB +":/PUMP FILES/3H_Compress_SN.csv"
DF_3H.to_csv(path_3H, index=False, mode= 'a')
# 4N
phase_4N = {'Household': Household_4N, 'Household SN': Household_4N_SN, 
                  'Weight Difference': Difference_4N}
DF_4N = pd.DataFrame(phase_4N, columns= ['Household','Household SN','Weight Difference'])
path_4N = USB+":/PUMP FILES/4N_Compress_SN.csv"
DF_4N.to_csv(path_4N, index=False, mode= 'a')
#left overs
#phase_left_over = {'Missing Serial Numbers': Missing_SN, 'Missing Weights' : Missing_weights}
#DF_over = pd.DataFrame(phase_left_over, columns= ['Missing Serial Numbers','Missing Weights'])
#path_over = "E:/PUMP FILES/Missing_Compress_SN.csv"
#DF_over.to_csv(path_over, index=False, mode= 'a')