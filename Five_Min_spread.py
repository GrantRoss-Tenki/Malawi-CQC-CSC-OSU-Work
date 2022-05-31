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
from itertools import zip_longest


Phase  = "1N"
spread_start = 10
spread_end = 15
if Phase == "1N":
    Event_length_Threshold = 75
elif Phase == "2N":
    Event_length_Threshold = 88
elif Phase == "3N":
    Event_length_Threshold = 68
elif Phase == "4N":
    Event_length_Threshold = 65

House_hold = [1006, 1007, 1009, 1019, 1023, 1025, 1029, 1035]

total_median_Five_array = []
total_median_Five_time = []
total_median_five_household = []
for HH in House_hold:
    print('Household- ', HH)
    path_HH1 = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_1_exact/HH_summary_Event/"+Phase+"_HH_Summary_Event_"+str(HH)+"_1_exact_1.11.csv"
    HH_1 = pd.read_csv(path_HH1, skiprows = 2)
    Event_length = HH_1.iloc[:,6]
    Event_start = HH_1.iloc[:,3]
    Event_end = HH_1.iloc[:,4]
    Day = HH_1.iloc[:,1]

    High_usage_start = []
    High_usage_end = []
    Day_event = []
    Median_Five = []
    Median_length = []
    for row, length in enumerate(Event_length):
        if length > Event_length_Threshold:
            High_usage_start.append(Event_start[row])
            High_usage_end.append(Event_end[row])
            Day_event.append(Day[row])
            total_median_five_household.append(HH)
            

    print(High_usage_start,High_usage_end)

    
    Phase_HH1_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_1_exact/Raw_D_metrics/"+Phase+"_HH_raw_Day_metrics_"+str(HH)+"_1_exact_3.55555.csv"
    Phase_HH1 = pd.read_csv(Phase_HH1_path, skiprows = 2)
    Kitchen_hapex = Phase_HH1.iloc[:,8]
    if Kitchen_hapex[0] != -1 or Kitchen_hapex[0] != 0:
        for end_val, start in enumerate(High_usage_start):
            
            end = High_usage_end[end_val] + spread_end
            hapex_data = Kitchen_hapex[start -spread_start : end]
            divisi_seciton = 0
            Spit_five = 0
            Hepex_needed_breakdown = np.arange(0,int(len(hapex_data)/5),1)
            five_minute_breakdown = []
            

            for prev_spred, spread in enumerate(Hepex_needed_breakdown):
                if prev_spred == 0:
                    five_minute_breakdown.append(np.average(hapex_data[0:5]))
                elif prev_spred == 1:
                    five_minute_breakdown.append(np.average(hapex_data[5:10]))
                else:
                    five_minute_breakdown.append(np.average(hapex_data[((prev_spred-1)*5):(spread*5)+1]))
            if len(hapex_data)/5 - len(Hepex_needed_breakdown) != 0:
                five_minute_breakdown.append(np.average(hapex_data[((Hepex_needed_breakdown[-1]+1)*5):]))
            total_median_Five_time.append(len(hapex_data))
            print('how many splits-- ',len(Hepex_needed_breakdown), 'length of hapex_data-- ',((Hepex_needed_breakdown[-1]+1)*5), len(hapex_data), 'length / 5-- ',len(hapex_data)/5, 'Length of the five minue split array -- ',len(five_minute_breakdown), 'on day -- ',Day_event[end_val],'if length int??== ',
                len(hapex_data)/5 - len(Hepex_needed_breakdown) )
            total_median_Five_array.append(five_minute_breakdown)
    else:
        print('this household has a failed HAPEX', HH)

Output_path_five = "C:/Users/gvros/Desktop/"+Phase+"_Five_Minute_Spread.csv"

with open(Output_path_five,"w+") as f:
    writer = csv.writer(f, delimiter = ',')
    for values in zip_longest(*total_median_Five_array):
        writer.writerow(values)

df_hh = {'HH':total_median_five_household, 'time':total_median_Five_time}
df_hh_time = pd.DataFrame(df_hh)
df_hh_time.to_csv(Output_path_five, index= False, mode='a')