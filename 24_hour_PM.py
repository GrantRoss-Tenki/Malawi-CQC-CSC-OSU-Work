# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 16:28:26 2022

@author: rossgra
"""
import pandas as pd
import numpy as np
import csv
import glob 
import os


# THis file is for gathering 24 hour averages 
#Work computer
datafile_path ="C:/Users/rossgra/Box/OSU, CSC, CQC Project files/1N/Collection/Clean_HH_1001_2021-10-01_12-36-06.csv"
#personal computer 
#datafile_path ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/3H/Collection/Clean_HH_2006_2021-11-29_09-58-09.csv"

with open(datafile_path, 'r') as f:
    csv_reader = csv.reader(f)
    for idx, row in enumerate(csv_reader):
        if 'Household ID:' in row:
            id_number = (row[1])
        elif 'Total number of logs:' in  row:
            number_of_days = int(row[1])/(24*60)
        elif 'Timestamp' in row:
            Fueltype = row[1]
            Exact = row[3]
            Usage = row[2]
            K_hapex = row[5]
            C_hapex = row[7]
            data_start = idx

            if len(row) < 9:
                print('There is no second exact')
                break
            elif row[8] == 'Second EXACT Usage':
                Exact_2 = row[9]
                Usage_2 = row[8]
                Second_Exact = 1
                print('--------------Two EXACT-------------')
            break
        

print('kitchen HAPEx', K_hapex)
print('number of days', str(number_of_days))
Sensor_Data = pd.read_csv(datafile_path, skiprows=data_start)
Kitchen_usage = Sensor_Data.iloc[:, 4]
Kitchen_PM = Sensor_Data.iloc[:, 5]

day_arange = np.arange(0,number_of_days+1)
print(day_arange)
Day_Average_PM =[]
complete_24_Hour_SUM = []
day_count = 0
for smoke in day_arange:
    if smoke == 0:
        #I am negating the first 7 minutes of collection time
        Day_Average_PM.append(np.average(Kitchen_PM.iloc[5:((24*60)+5)]))
        day_end_time_value = ((24*60)+5)
        day_count = day_count + 1
        print('time end value after first day',Kitchen_PM.iloc[5:6])#@day_end_time_value,0] )
        print('is the lenght right??', len(Kitchen_PM.iloc[5:((24*60)+5)]))
        
    elif (smoke != 0) and ((day_end_time_value + (60*24)) <= len(Kitchen_PM)):
        Day_Average_PM.append(np.average(Kitchen_PM.iloc[day_end_time_value:(day_end_time_value + (24*60))]))
        day_end_time_value = (day_end_time_value + (24*60))
        day_count = day_count + 1
    
complete_phase_24_Hour_SUM = (sum(Kitchen_PM.iloc[5:day_end_time_value]))/(day_count*24*60)
print('complete 24 hours sum per day;' , complete_phase_24_Hour_SUM)
print(Day_Average_PM)
print(day_end_time_value)
print('time end value',Sensor_Data.iloc[day_end_time_value,0] )
print(day_count)