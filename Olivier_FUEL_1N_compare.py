# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 10:52:01 2022

@author: rossgra
"""

import pandas as pd
import numpy as np
import math

OLivier_1N_Path = "C:/Users/rossgra/Box/1n_Fuel_time_Compare.csv"
Olivier_1N = pd.read_csv(OLivier_1N_Path)
print((Olivier_1N.iloc[2,0]))

Household_Usage = 1
Household_Fuel = 2

Length = len(Olivier_1N.iloc[1,:])
print(Length)

Day_cooking_Times = []
Total_Cooking_Times = []
Total_Fuel_Removed = []
Day_Fuel_Removed = []
day_1_Use = []
day_2_Use = []
day_3_Use = []
day_4_Use = []
day_5_Use = []
day_6_Use = []
day_7_Use = []
day_8_Use = []
day_9_Use = []
Use_Nine_sum = []
day_1_Fuel = []
day_2_Fuel = []
day_3_Fuel = []
day_4_Fuel = []
day_5_Fuel = []
day_6_Fuel = []
day_7_Fuel = []
day_8_Fuel = []
day_9_Fuel = []
Fuel_nine_sum = []

Household_count = 0
Household_array = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020]
for HHHHH in Household_array:
    Usage_total_Array = Olivier_1N.iloc[1:,Household_Usage]
    Usage_total_Array = (Usage_total_Array.tolist())
    Usage_total = [float(f) for f in Usage_total_Array if f != 'nan']
            
    Fuel_total_Array = Olivier_1N.iloc[1:,Household_Fuel]
    Fuel_total_Array = Fuel_total_Array.tolist()
    Fuel_total = [float(f) for f in Fuel_total_Array if f != 'nan']
    Total_Fuel_Removed.append(sum(Fuel_total))
    Total_Cooking_Times.append(sum(Usage_total))
    Household_Usage = Household_Usage + 2
    Household_Fuel = Household_Fuel + 2
    
    day_nin = np.arange(1, 10 , 1)
    #print(day_nin)
    day_start = 0
    day_end = 60*24
    Day_fuel = []
    Day_usage = []
    for d in day_nin:
        Day_fuel.append(sum(Fuel_total[day_start:day_end]))
        Day_usage.append(sum(Usage_total[day_start:day_end]))
        day_start = day_end
        day_end = (d+1)*(60*24)
    print(Day_usage)
    
    day_1_Use.append(Day_usage[0])
    day_2_Use.append(Day_usage[1])
    day_3_Use.append(Day_usage[2])
    day_4_Use.append(Day_usage[3])
    day_5_Use.append(Day_usage[4])
    day_6_Use.append(Day_usage[5])
    day_7_Use.append(Day_usage[6])
    day_8_Use.append(Day_usage[7])
    day_9_Use.append(Day_usage[8])
    
    Use_Nine_sum.append(sum(Day_usage))
    
    day_1_Fuel.append(Day_fuel[0])
    day_2_Fuel.append(Day_fuel[1])
    day_3_Fuel.append(Day_fuel[2])
    day_4_Fuel.append(Day_fuel[3])
    day_5_Fuel.append(Day_fuel[4])
    day_6_Fuel.append(Day_fuel[5])
    day_7_Fuel.append(Day_fuel[6])
    day_8_Fuel.append(Day_fuel[7])
    day_9_Fuel.append(Day_fuel[8])
    
    Fuel_nine_sum.append(sum(Day_fuel))
    
print(Total_Cooking_Times)

FUEL_breakdown = {'Household':Household_array,'Phase Total':Total_Cooking_Times,'Total Fuel for nine days':Use_Nine_sum,
                  'day 1': day_1_Use,'day 2': day_2_Use,'day 3': day_3_Use,'day 4': day_4_Use,
                  'day 5': day_5_Use,'day 6': day_6_Use,'day 7': day_7_Use,'day 8': day_8_Use,
                  'day 9': day_9_Use}

USe_breakdown = {'Household':Household_array,'Phase Total':Total_Fuel_Removed,'Total time for nine days':Fuel_nine_sum,
                  'day 1': day_1_Fuel,'day 2': day_2_Fuel,'day 3': day_3_Fuel,'day 4': day_4_Fuel,
                  'day 5': day_5_Fuel,'day 6': day_6_Fuel,'day 7': day_7_Fuel,'day 8': day_8_Fuel,
                  'day 9': day_9_Fuel}

df_fuel = pd.DataFrame(FUEL_breakdown,columns=['Household','Phase Total', 'Total Fuel for nine days','day 1','day 2',
                                                                           'day 3','day 4','day 5',
                                                                           'day 6','day 7','day 8',
                                                                           'day 9'])

df_use = pd.DataFrame(USe_breakdown,columns=['Household','Phase Total', 'Total time for nine days','day 1','day 2',
                                                                           'day 3','day 4','day 5',
                                                                           'day 6','day 7','day 8',
                                                                           'day 9'])

path = "C:/Users/rossgra/Box/Oliver_s_algo_Fule_Time.csv"

#print(df_use)
df_fuel.to_csv(path, index=False,mode='a')
df_use.to_csv(path, index=False,mode='a')
