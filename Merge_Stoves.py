
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
        print('-----------------  ',  get_me_data.iloc[0, 3])
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
        print('Time vlaues for both starts',stove_1_start_times,stove_2_start_times, 'Time values for both end',stove_1_end_times, stove_2_end_times)

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

        Merged_Stoves_start = []
        Merged_Stoves_end = []
        Least_stove_counter = 0
        Greatest_stove_counter = 0

        for event, Greatest_start_tv in enumerate(Greatest_event_stove_start):


            least_start_tv = Least_event_Least_event_stove_start[Least_stove_counter]

            Least_end_tv = Least_event_Least_event_stove_end[Least_stove_counter]
            Greatest_end_tv = Greatest_event_stove_end[Greatest_stove_counter]

            elif Greatest_start_tv < least_start_tv  < Greatest_end_tv:
                Merged_Stoves.append(Greatest_start_tv)

                if Least_end_tv > Greatest_end_tv and Least_end_tv > Greatest_start_tv:
                    Merged_Stoves_end.append(Least_end_tv)
                elif:  Least_end_tv < Greatest_end_tv:
                    Merged_Stoves_end.append(Greatest_end_tv)

                print(Merged_Stoves_end)
