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

Phase = "3H"
Computer = "work"
# THis file is for gathering 24 hour averages 
#Work computer
#colecting metrics for each household comparison
HH_NUMBER = []
DAYS_O = []
TIME_START = []
TIME_END = []
PHASE_24_HR_AVG = []
HIGHEST_Fuel_PER_DAY = []
DAY_OF_HIGHEST_Fuel = []
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
PHASE_24_HR_Fuel_AVG = []
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
    Fuel_removal = metric_day_data.iloc[:,1]
    day_arange = np.arange(0, 14)
    time_vlaue_frame = pd.read_csv(Fuel_time_path)
    
    
    if metric_day_data.iloc[0,1]!= -1:
        day_average_fuel = []
        day_count = 0

        for wood in day_arange:
            fuel_setting = []

            if wood == 0:
                dummy_Fuel = Fuel_removal[5:((24*60)+5)]
                #print(dummy_Fuel)
                for tv, anything in enumerate(dummy_Fuel):
                    if tv + 1 == len(dummy_Fuel)-6:
                        fuel_setting.append(anything)

                        break
                    elif anything != dummy_Fuel.iloc[tv + 1]:
                        fuel_setting.append(anything)

                #print('fuel setting after wood = 0', fuel_setting)

                day_average_fuel.append(np.average(fuel_setting))
                day_time_end_vlaue  = ((24*60)+5)
                day_count = day_count +1
                
            elif (wood != 0) and ((day_time_end_vlaue + (60*24)) <= len(metric_day_data.iloc[:,1])-1):
                dummy_Fuel = Fuel_removal[day_time_end_vlaue:(day_time_end_vlaue +(24*60))]
                for tv, anything in enumerate(dummy_Fuel):
                    next_int = tv + 1 + day_time_end_vlaue
                    if tv + 1 == len(dummy_Fuel) -1:
                        fuel_setting.append(anything)
                        break
                    elif anything != dummy_Fuel[next_int]:
                        fuel_setting.append(anything)
                day_average_fuel.append(np.average(fuel_setting))
                day_time_end_vlaue  = day_time_end_vlaue + ((24*60))
                day_count = day_count +1
                

        #print(day_average_fuel)
        complete_phase_24_Fuel_Sum = (sum(Fuel_removal.iloc[5:day_time_end_vlaue]))/(day_count*24*60)
        HH_NUMBER.append(id_number)
        DAYS_O.append(day_count)
        TIME_START.append(time_vlaue_frame.iloc[6,0])
        TIME_END.append(time_vlaue_frame.iloc[day_time_end_vlaue,0])
        PHASE_24_HR_AVG.append(complete_phase_24_Fuel_Sum)
        max_fuel_value = max(day_average_fuel)
        max_fuel_day = [index for index, item in enumerate(day_average_fuel) if item == max_fuel_value]

        HIGHEST_Fuel_PER_DAY.append(max_fuel_value)
        

        DAY_OF_HIGHEST_Fuel.append(time_vlaue_frame.iloc[((max_fuel_day[0])*24*60), 0])

    else:
        day_average_fuel = [-1]
        HH_NUMBER.append(id_number)
        DAYS_O.append(-1)
        TIME_START.append(-1)
        TIME_END.append(-1)
        PHASE_24_HR_AVG.append(-1)
        HIGHEST_Fuel_PER_DAY.append(-1)
        DAY_OF_HIGHEST_Fuel.append(-1)

    day_counter = np.arange(0,14)
    if len(day_average_fuel) < len(day_counter):
        zero_count = np.arange(0, len(day_counter) - len(day_average_fuel))
        for z in zero_count:
            day_average_fuel.append(0)
    day_1.append(day_average_fuel[0])
    day_2.append(day_average_fuel[1])
    day_3.append(day_average_fuel[2])
    day_4.append(day_average_fuel[3])
    day_5.append(day_average_fuel[4])
    day_6.append(day_average_fuel[5])
    day_7.append(day_average_fuel[6])
    day_8.append(day_average_fuel[7])
    day_9.append(day_average_fuel[8])
    day_10.append(day_average_fuel[9])
    day_11.append(day_average_fuel[10])
    day_12.append(day_average_fuel[11])
    day_13.append(day_average_fuel[12])
    day_14.append(day_average_fuel[13])

Fuel_per_24_hour = {'Household': HH_NUMBER,
                      'Days Observed': DAYS_O,
                      'Day Start': TIME_START,
                      'Day End': TIME_END,
                      'Phase 24hr Avg (sum of phase/min/day obesrved)' : PHASE_24_HR_AVG,
                      'KG of Highest Fuel removed for one day': HIGHEST_Fuel_PER_DAY,
                      'Day with Highest Fuel Removal' : DAY_OF_HIGHEST_Fuel}

df_Fuel_per_24_hour = pd.DataFrame(Fuel_per_24_hour, columns= ['Household','Days Observed',
                                                                   'Day Start','Day End','KG of Highest Fuel removed for one day',
                                                                   'Day with Highest Fuel Removal','Phase 24hr Avg (sum of phase/min/day obesrved)'])

HH_Fuel_breakdown = {'Household': HH_NUMBER,
                           'Day 1': day_1,
                           'Day 2': day_2,
                           'Day 3': day_3,
                           'Day 4': day_4,
                           'Day 5': day_5,
                           'Day 6': day_6,
                           'Day 7': day_7,
                           'Day 8': day_8,
                           'Day 9': day_9,
                           'Day 10': day_10,
                           'Day 11': day_11,
                           'Day 12': day_12,
                           'Day 13': day_13,'Day 14': day_14}
df_HH_Fuel_breakdown = pd.DataFrame(HH_Fuel_breakdown,columns=['Household','Day 1','Day 2',
                                                                           'Day 3','Day 4','Day 5',
                                                                           'Day 6','Day 7','Day 8',
                                                                           'Day 9','Day 10','Day 11',
                                                                           'Day 12','Day 13','Day 14'])

if Computer == 'work':
    Fuel_24_hour_file_path = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+ Phase +"/"+Phase+"_24_hour_Fuel_removal" +".csv"
    HH_breakdown_file_path = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+ Phase +"/"+Phase+"_Household_Fuel_removal_breakdown" +".csv"

else:
    Fuel_24_hour_file_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase +"/"+Phase+"_24_hour_Fuel_removal" +".csv"
    HH_breakdown_file_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase +"/"+Phase+"_Household_Fuel_removal_breakdown" +".csv"
df_Fuel_per_24_hour.to_csv(Fuel_24_hour_file_path,index=False,mode='a')
df_HH_Fuel_breakdown.to_csv(HH_breakdown_file_path,index=False,mode='a')
