# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:51:45 2022

@author: rossgra
"""

import pandas as pd
import numpy as np
import csv
import os
import glob

Phase = "1N"
Computer = "work"
# THis file is for gathering 24 hour averages 
#Work computer
#colecting metrics for each household comparison
HH_NUMBER = []
DAYS_O = []
TIME_START = []
TIME_END = []
PHASE_24_HR_AVG = []
HIGHEST_PM_PER_DAY = []
DAY_OF_HIGHEST_PM = []
day_1 = []
day_2 = []
day_3 = []
day_4 = []
day_5 = []
day_6 = []
day_7 = []
day_8 = []
day_9 = []
day_10 = []
day_11 = []
day_12 = []
day_13 = []
day_14 = []
if Computer == 'work':
    os.chdir("C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+Phase +"/Compiler_1_exact/Raw_Day/Raw_D_metrics")

else:
    os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+ Phase +"/Compiler_1_exact/Raw_Day/Raw_D_metrics")


FUEL_sensor = os.getcwd()
FUEL_csv_open = glob.glob(os.path.join(FUEL_sensor, "*.csv"))




HH_NUMBER = []
DAYS_O = []
TIME_START = []
TIME_END = []
PHASE_24_HR_AVG = []
HIGHEST_fuel_PER_DAY = []
DAY_OF_HIGHEST_fuel_removal = []
day_1 = []
day_2 = []
day_3 = []
day_4 = []
day_5 = []
day_6 = []
day_7 = []
day_8 = []
day_9 = []
day_10 = []
day_11 = []
day_12 = []
day_13 = []
day_14 = []

for file in FUEL_csv_open:
    with open(file, 'r') as f:
        csv_reader_fuel = csv.reader(f)
        for idx, row in enumerate(csv_reader_fuel):
            if idx == 1:
                id_number = (row[1])
                print('Household',id_number)

    if Computer == 'work':
        Fuel_time_path = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+Phase +"/Time_list/"+Phase+"_"+id_number+"_time_array.csv"

    else:
        Fuel_time_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase +"/Time_list/"+Phase+"_"+id_number+"_time_array.csv"

    metric_day_data = pd.read_csv(file, skiprows=2)
    day_count = np.arange(0, 14)
    time_vlaue_frame = pd.read_csv(Fuel_time_path)
    
    
    if metric_day_data.iloc[0,1]!= -1:
        for wood in day_count:
            day_average_fuel = []
            day_count  = 0
            fuel_setting = []
            if wood == 0:
                dummy_time = time_vlaue_frame[5:((24*60)+5)]
                for tv, anything in enumerate(dummy_time):
                    if tv + 1 == len(dummy_time):
                        fuel_setting.append(anything)
                        continue
                    elif anything != dummy_time[tv + 1]:
                        fuel_setting.append(anything)
                day_average_fuel.append(np.average(fuel_setting))
                day_time_end_vlaue  = ((24*60)+5)
                day_count = day_count +1
                
            elif (wood != 0) and ((day_time_end_vlaue + (60*24)) <= len(metric_day_data.iloc[:,1])-1):
                dummy_time = time_vlaue_frame[day_time_end_vlaue:(day_time_end_vlaue +(24*60))]
                for tv, anything in enumerate(dummy_time):
                    if tv + 1 == len(time_vlaue_frame[day_time_end_vlaue:(day_time_end_vlaue +(24*60))]):
                        fuel_setting.append(anything)
                        continue
                    elif anything != time_vlaue_frame[tv +1]:
                        fuel_setting.append(anything)
                day_average_fuel.append(np.average(fuel_setting))
                day_time_end_vlaue  = day_time_end_vlaue + ((24*60)+5)
                day_count = day_count +1
