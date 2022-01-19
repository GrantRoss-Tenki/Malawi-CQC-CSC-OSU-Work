# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 16:28:26 2022

@author: rossgra
"""
import pandas as pd
import numpy as np
import csv
import os
import glob


Phase = "3N"
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
    os.chdir("C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+Phase +"/Collection")

else:
    os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+ Phase +"/Collection")

Kitchen_HAPEx = os.getcwd()
Kit_csv_open = glob.glob(os.path.join(Kitchen_HAPEx, "*.csv"))

for file in Kit_csv_open:
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        for idx, row in enumerate(csv_reader):
            if 'Household ID:' in row:
                id_number = (row[1])
                print('Household',id_number)
            elif 'Total number of logs:' in  row:
                number_of_days = int(row[1])/(24*60)
            elif 'Timestamp' in row:
                Fueltype = row[1]
                Exact = row[3]
                Usage = row[2]
                K_hapex = row[5]
                C_hapex = row[7]
                data_start = idx
#    
#                if len(row) < 9:
#                    print('There is no second exact')
#                    break
#                elif row[8] == 'Second EXACT Usage':
#                    Exact_2 = row[9]
#                    Usage_2 = row[8]
#                    Second_Exact = 1
#                    print('--------------Two EXACT-------------')
#                break
#            

    Sensor_Data = pd.read_csv(file, skiprows=data_start)
    if Sensor_Data.iloc[0, 4] != 'NO KITCHEN': 
        Kitchen_usage = Sensor_Data.iloc[:, 4]
        Kitchen_PM = Sensor_Data.iloc[:, 5]
        
        day_arange = np.arange(0,number_of_days+1)
        Day_Average_PM =[]
        complete_24_Hour_SUM = []
        day_count = 0
        for smoke in day_arange:
            if smoke == 0:
                #I am negating the first 7 minutes of collection time
                Day_Average_PM.append(np.average(Kitchen_PM.iloc[5:((24*60)+5)]))
                day_end_time_value = ((24*60)+5)
                day_count = day_count + 1
                
            elif (smoke != 0) and ((day_end_time_value + (60*24)) <= len(Kitchen_PM)):
                Day_Average_PM.append(np.average(Kitchen_PM.iloc[day_end_time_value:(day_end_time_value + (24*60))]))
                day_end_time_value = (day_end_time_value + (24*60))
                day_count = day_count + 1
            
        complete_phase_24_Hour_SUM = (sum(Kitchen_PM.iloc[5:day_end_time_value]))/(day_count*24*60)

        HH_NUMBER.append(id_number)
        DAYS_O.append(day_count)
        TIME_START.append(Sensor_Data.iloc[5,0])
        TIME_END.append(Sensor_Data.iloc[day_end_time_value,0] )
        PHASE_24_HR_AVG.append(complete_phase_24_Hour_SUM)
        max_PM_value = max(Day_Average_PM)
        Max_PM_on_day = [index for index, item in enumerate(Day_Average_PM) if item == max_PM_value]

        HIGHEST_PM_PER_DAY.append((int(max_PM_value*100))/100)

        DAY_OF_HIGHEST_PM.append(Sensor_Data.iloc[((Max_PM_on_day[0])*24*60), 0])
    else: 

        HH_NUMBER.append(id_number)
        DAYS_O.append(str(number_of_days))
        TIME_START.append(Sensor_Data.iloc[0, 0])
        TIME_END.append(Sensor_Data.iloc[0, -1])
        PHASE_24_HR_AVG.append(-1)
        HIGHEST_PM_PER_DAY.append(-1)
        DAY_OF_HIGHEST_PM.append(-1)
        
    day_counter = np.arange(0,14)
    if len(Day_Average_PM) < len(day_counter):
        zero_count = np.arange(0, len(day_counter) - len(Day_Average_PM))
        for z in zero_count:
            Day_Average_PM.append(0)
    day_1.append(Day_Average_PM[0])
    day_2.append(Day_Average_PM[1])
    day_3.append(Day_Average_PM[2])
    day_4.append(Day_Average_PM[3])
    day_5.append(Day_Average_PM[4])
    day_6.append(Day_Average_PM[5])
    day_7.append(Day_Average_PM[6])
    day_8.append(Day_Average_PM[7])
    day_9.append(Day_Average_PM[8])
    day_10.append(Day_Average_PM[9])
    day_11.append(Day_Average_PM[10])
    day_12.append(Day_Average_PM[11])
    day_13.append(Day_Average_PM[12])
    day_14.append(Day_Average_PM[13])
    #Individual_household = pd.DataFrame()
print(len(day_counter))
Kit_PM_per_24_hour = {'Household': HH_NUMBER, 
                      'Days Observed': DAYS_O, 
                      'Day Start': TIME_START, 
                      'Day End': TIME_END, 
                      'Phase 24hr Avg (sum of phase/min/day obesrved)' : PHASE_24_HR_AVG, 
                      'Day with Highest PM Value': HIGHEST_PM_PER_DAY,
                      'Day with Highest PM' : DAY_OF_HIGHEST_PM}

df_Kit_PM_per_24_hour = pd.DataFrame(Kit_PM_per_24_hour, columns= ['Household','Days Observed',
                                                                   'Day Start','Day End','Day with Highest PM Value',
                                                                   'Day with Highest PM','Phase 24hr Avg (sum of phase/min/day obesrved)'])

HH_Kitchen_PM_breakdown = {'Household': HH_NUMBER, 
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
df_HH_Kitchen_PM_breakdown = pd.DataFrame(HH_Kitchen_PM_breakdown,columns=['Household','Day 1','Day 2',
                                                                           'Day 3','Day 4','Day 5',
                                                                           'Day 6','Day 7','Day 8',
                                                                           'Day 9','Day 10','Day 11',
                                                                           'Day 12','Day 13','Day 14'])

if Computer == 'work':
    Kit_PM_24_hour_file_path = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+ Phase +"/"+Phase+"_24_hour_Kitchen_PM" +".csv"
    HH_breakdown_file_path = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+ Phase +"/"+Phase+"_Household_Kitchen_breakdown_PM" +".csv"

else:
    Kit_PM_24_hour_file_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase +"/"+Phase+"_24_hour_Kitchen_PM" +".csv"
    HH_breakdown_file_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase +"/"+Phase+"_Household_Kitchen_breakdown_PM" +".csv"
df_Kit_PM_per_24_hour.to_csv(Kit_PM_24_hour_file_path,index=False,mode='a')
df_HH_Kitchen_PM_breakdown.to_csv(HH_breakdown_file_path,index=False,mode='a')