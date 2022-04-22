
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


# the first step is to get the time Values for a double stove Household.


Phase = "4N"
if Phase== "4N":
    exact_2_hh = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1011, 1013, 1014, 1016, 1017, 1018, 1019, 1021, 1022, 1023, 1024, 1025, 1026, 1028, 1029, 1030, 1031, 1032, 1033, 1035, 1036, 1037, 1038, 1039]

os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+ Phase +"/Compiler_1_exact/HH_summary_Event")

Day_met_path = os.getcwd()
csv_R_m = glob.glob(os.path.join(Day_met_path, "*.csv"))
count_hh = 0
for file in csv_R_m:
    if count_hh != 0:
        break
    else:
        count_hh = 1 + count_hh
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        hh_gimme = reader(f)
        header = next(hh_gimme)
        if header != None:
            for rrrr, rows in enumerate(hh_gimme):
                if rrrr == 0:
                    Household = rows[1]
                    print('the household id number is:  ',  (rows[1]))
        for idx, row in enumerate(csv_reader):
            if '| Event Number |' in row:
                data_start= idx
                break

        
        get_me_data = (pd.read_csv(file, skiprows=2 ))
        #print('-----------------  ',  get_me_data.iloc[0, 3])
        stove_1_start_times = get_me_data.iloc[:, 3]
        stove_1_end_times = get_me_data.iloc[:, 4]

        # Certify that the household is using the second stove

        for ttt in exact_2_hh:
            Cooking_minute_2 = []
            if int(Household) == ttt: 
                stove_2_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+ Phase +"/Compiler_2_exact/HH_summary_Event/"+Phase+"_HH_Summary_Event_"+str(Household)+"_2_exact_1.11.csv"
                second_exact_2 = pd.read_csv(stove_2_path,  skiprows=2)
                stove_2_start_times = second_exact_2.iloc[:, 3]
                stove_2_end_times = second_exact_2.iloc[:, 4]
                break
            else:
                second_exact = 0
        #print('Time vlaues for both starts',stove_1_start_times,stove_2_start_times, 'Time values for both end',stove_1_end_times, stove_2_end_times)

        #Clariffy: Start and end varriables for each stove are the same length. Or, stove 1 and stove 2 can have different overall lengths, but their individaul start and end are the same array lengths 

        if len(stove_1_start_times) > len(stove_2_start_times):
            Greatest_event_stove_start = stove_1_start_times
            Greatest_event_stove_end = stove_1_end_times

            Least_event_stove_start = stove_2_start_times
            Least_event_stove_end = stove_2_end_times
        elif len(stove_1_start_times) < len(stove_2_start_times):
            Greatest_event_stove_start = stove_2_start_times
            Greatest_event_stove_end = stove_2_end_times
            Least_event_stove_start = stove_1_start_times
            Least_event_stove_end = stove_1_end_times
        else:
            Greatest_event_stove_start = stove_1_start_times
            Greatest_event_stove_end = stove_1_end_times
            Least_event_stove_start = stove_2_start_times
            Least_event_stove_end = stove_2_end_times

        #MERGING: if stove cooking events overlay, combine to new Time Value complete stove in variible - "Merged_Stoves_start" and Merged_Stove_end" 
        #New Time Values are going to be used for raw dauly metrics to get complete metrics

        Collection_length = np.arange(0, Greatest_event_stove_end.iloc[-1]+45, 1)

        Greatest_event_stove = []
        Greatest_event_count = 0
        No_more_cooking = 0
        for tv in Collection_length:
            if No_more_cooking == 0:
                if (tv >= int(Greatest_event_stove_start[Greatest_event_count])) and (tv <= int(Greatest_event_stove_end[Greatest_event_count])):
                    Greatest_event_stove.append(1)
                elif (tv > int(Greatest_event_stove_end[Greatest_event_count])) or tv == Greatest_event_stove_end.iloc[-1]:
                    if Greatest_event_count + 1 == len(Greatest_event_stove_end):
                        No_more_cooking = 1
                    elif Greatest_event_count <=  len(Greatest_event_stove_end):
                        Greatest_event_count = Greatest_event_count + 1 
                        Greatest_event_stove.append(1)
                else:
                    Greatest_event_stove.append(0)
            else:
                Greatest_event_stove.append(0)

        print(len(Greatest_event_stove_end),len(Greatest_event_stove), Greatest_event_count)

        Collection_length_least = np.arange(0, Least_event_stove_end.iloc[-1]+45, 1)
        Least_event_stove = []
        Least_event_count = 0
        No_more_cooking = 0
        for tv in Collection_length_least:
            if No_more_cooking == 0:
                if (tv >= int(Least_event_stove_start[Least_event_count])) and (tv <= int(Least_event_stove_end[Least_event_count])):
                    Least_event_stove.append(1)
                elif (tv > int(Least_event_stove_end[Least_event_count])) or tv == Least_event_stove_end.iloc[-1]:
                    if Least_event_count + 1 == len(Least_event_stove_end):
                        No_more_cooking = 1
                    elif Least_event_count <=  len(Least_event_stove_end):
                        Least_event_count = Least_event_count + 1 
                        Least_event_stove.append(1)
                else:
                    Least_event_stove.append(0)
            else:
                Least_event_stove.append(0)

        print(len(Least_event_stove_end),len(Least_event_stove), Least_event_count)

        Merged_Stove_combined_Array = []
        if len(Greatest_event_stove) > len(Least_event_stove):
            Greatest_stove_length = Greatest_event_stove
            least_stove_length = Least_event_stove
        else:
            Greatest_stove_length = Least_event_stove
            least_stove_length = Greatest_event_stove

        Merged_Stove_combined_Array = []
        no_more_less_used_stove = 0
        for tvv, cooking in enumerate(Greatest_stove_length):
            if no_more_less_used_stove == 0:
                if tvv > len(least_stove_length)-1:
                    Merged_Stove_combined_Array.append(cooking)
                    no_more_less_used_stove = 1
                elif cooking == 1:
                    Merged_Stove_combined_Array.append(cooking)
                elif least_stove_length[tvv] == 1:
                    Merged_Stove_combined_Array.append(least_stove_length[tvv])
                else:
                    Merged_Stove_combined_Array.append(cooking)
            else:
                Merged_Stove_combined_Array.append(cooking)
        print('length of the merged stove---', len(Merged_Stove_combined_Array))
        #going to use combined stove to get to the start and end values
        Merged_Stoves_start = []
        Merged_Stoves_end = []
        for nexx, a in enumerate(Merged_Stove_combined_Array):
            if nexx + 1 == len(Merged_Stove_combined_Array) - 1:
                break
            elif a == 0 and Merged_Stove_combined_Array[nexx + 1] == 1:
                Merged_Stoves_start.append(nexx + 1)
            elif a == 1 and  Merged_Stove_combined_Array[nexx + 1] == 0:
                Merged_Stoves_end.append(nexx)

        print(Merged_Stoves_start)
        print(Merged_Stoves_end)


        # getting the raw day metrics for the combined stoves
        RAW_day_Path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+ Phase +"/Compiler_1_exact/Raw_D_metrics/"+Phase+"_HH_raw_Day_metrics_"+str(Household)+"_1_exact_3.55555.csv"
        RAW_day = pd.read_csv(RAW_day_Path,  skiprows=2)
        Fuel_Removed = RAW_day.iloc[:, 1]
        print(Fuel_Removed)