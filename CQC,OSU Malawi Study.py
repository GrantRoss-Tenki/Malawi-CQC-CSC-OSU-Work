import itertools
import os
import pandas as pd
import numpy as np
import csv
from itertools import chain
import statistics as stat
import datetime
from io import StringIO
import matplotlib.pyplot as plt


datafile_path ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/HH_1023_2021-09-24_11-45-04.csv"
#file = pd.read_csv('C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/HH_1023_2021-09-24_11-45-04.csv')
#house_ID = file.iloc[5:1]                    tester_no_pump.csv
#print(house_ID)

with open(datafile_path, 'r') as f:
    csv_reader = csv.reader(f)
    for idx, row in enumerate(csv_reader):
        if 'Household ID:' in row:
            id_number = int(row[1])
            print("this is the number of iterations")
        elif 'Timestamp' in row:
            data_start= idx
            break

# this is so far from heather and her "Data Processing Instructions"

sensor_data = pd.read_csv(datafile_path, skiprows=data_start)
print(sensor_data)
print('The household ID number is: ......',  id_number)
#print(sensor_data.iloc[:,1])

#Filtering out FUEl this is using the same process derived by Heather and her thesis
Fuel_KG_nf = sensor_data.iloc[:,1]

n  = 0
Fuel_KG = []
Thres_fuel = 0.14
insert = []
remove = []
previous = 0
for kg in Fuel_KG_nf:
    n = n + 1
    if n+1 == (len(Fuel_KG_nf)):
        Fuel_KG.append(Fuel_KG_nf.iloc[(n)])
        break
    elif (Fuel_KG_nf.iloc[(n)] - Fuel_KG_nf.iloc[(n+1)]) > Thres_fuel:
        Fuel_KG.append(Fuel_KG_nf.iloc[n])
        insert.append(n)
    elif (Fuel_KG_nf.iloc[(n)]) < 0:
        Fuel_KG.append(0)
    elif (Fuel_KG_nf.iloc[(n+1)] - Fuel_KG_nf.iloc[(n)]) > Thres_fuel:
        Fuel_KG.append(Fuel_KG_nf.iloc[n])
        remove.append(n)
    elif previous < Fuel_KG_nf.iloc[n] and Fuel_KG_nf.iloc[(n)] > Fuel_KG_nf.iloc[(n+1)]:
        Fuel_KG.append(previous)
    elif previous < Fuel_KG_nf.iloc[n] and Fuel_KG_nf.iloc[(n)] > Fuel_KG_nf.iloc[(n+1)] and previous < Fuel_KG_nf.iloc[(n+1)]:
        Fuel_KG.append(Fuel_KG_nf.iloc[(n+1)])
    else:
        Fuel_KG.append(Fuel_KG_nf.iloc[(n)])
    previous = Fuel_KG[-1]

Fuel_KG.insert(0, Fuel_KG_nf.iloc[0])
print(Fuel_KG)

remove_2 = []
remove_2_kg = []
insert_2 = []
insert_2_kg = []
v = 0
for weight in Fuel_KG:
    v = v + 1
    #print(weight)
    if v+1 == (len(Fuel_KG_nf)):
        break
    elif (weight - Fuel_KG[v]) > Thres_fuel:
        remove_2.append(v)
        remove_2_kg.append(abs(Fuel_KG[v] - weight))
    elif (Fuel_KG[v] - weight) > Thres_fuel:
        insert_2.append(v)
        insert_2_kg.append(Fuel_KG[v] - weight)
v = 0

print('Removing the fuel at this timestamp value' , remove_2)
#print('inserting the fuel at this timestamp value' , insert_2)

Fuel_removed = [((int(i*100))/100) for i in remove_2_kg]
print('Fuel Changes in kilogram remove_2_kg', [((int(i*100))/100) for i in remove_2_kg])
print('----- length Fuel Changes in kilogram remove_2_kg', len(Fuel_removed))
print('----- length Fuel Changes in kilogram remove_2_kg', len(remove_2))

#this is trying to find the time at each fuel removal
Fuel_time_removal = []
for t in remove_2:
    Fuel_time_removal.append(sensor_data.iloc[t,0])
print('Time the fuel was removed', Fuel_time_removal)
Fuel_time_insert = []
for t in insert_2:
    Fuel_time_insert.append(sensor_data.iloc[t,0])
#print('Time the fuel was inserted', Fuel_time_insert)


between_Fuel_removal = []
v = 0
for b in remove_2:
    v = v + 1
    if (v) == len(remove_2):
        break
    between_Fuel_removal.append(((remove_2[v]) - b))

print(' this is the amount of minutes between Fuel Removal',  between_Fuel_removal)

between_Fuel_Insert = []
v = 0
for b in insert_2:
    v = v + 1
    if (v) == len(insert_2):
        break
    between_Fuel_Insert.append(((insert_2[v]) - b))

print(' ----------this is the amount of minutes between Fuel insert',  between_Fuel_Insert)
# lastly This is for finding the timestamp value for fuel used in a fire

print(len(Fuel_KG_nf))
kg = np.arange(0, len(Fuel_KG_nf),1)
remove_2[:0] = [0]
Fuel_removed[:0] = [0]
print(remove_2)
print(Fuel_removed)
print(kg)
print(len(kg))
count = 0
KG_burned =[]
for wei in kg:
#    print(len(remove_2))
    if (wei) == (len(Fuel_KG_nf)-1):
        KG_burned.append(KG_burned[-1])
        break
    elif remove_2[-1] == len(KG_burned)-2:
        KG_burned.append(KG_burned[-1])
        pass
    elif wei == remove_2[count]:
        KG_burned.append(Fuel_removed[count])
        if remove_2[-1] == wei:
            end_bit = np.arange(wei, len(Fuel_KG_nf),1)
            for a in end_bit:
                KG_burned.append(KG_burned[-1])
            break
        count = count + 1
    else:
        KG_burned.append(KG_burned[-1])


print('this is the fuel KG_burned for whole timestamp' , KG_burned[-2])
print(len(KG_burned))

#--------------- finding cooking event------------------
print('--------------- finding cooking event------------------')

#
# # print('Fire End Stamp',Fire_end)
# # #this is to finally filter out the times of cooking event
# # cooking_event = list(zip(sensor_data.iloc[Fire_start,0],sensor_data.iloc[Fire_end,0]))
# # print('time of start and stop of cooking event', cooking_event)
# # Cooking_Event_length = [a - b for a, b in zip(Fire_end, Fire_start)]
# # print('Minutes for cooking event', Cooking_Event_length)
# #
# # # --- here is trying to find the amount of fuel and other things used per cooking event----
# # prec_movement = []
# # EVENT_FUEL_CHANGE = []
# # Cook_CE_exposure = []
# # Median_cook_exposure = []
# # STD_cook_exp = []
# # Temp_CE_average = []
# # STD_Temp = []
# # Kitchen_movement_precent = []
# # Avg_kitchen_PM = []
# # STD_Avg_Kit_pm = []
# Median_kitche_PM = []
# Length_of_event = []
# raw_cook_pm_event =[]
# raw_Kitchen_pm_event = []
# raw_cook_comp_event = []
# raw_temp_event = []
# raw_fuel_event = []
# First_20_kpm = []
# First_20_kpm_avg = []
# First_20_Cpm = []
# First_20_Cpm_avg = []
# Cook_comp = sensor_data.iloc[:,6]
# Cook_PM = sensor_data.iloc[:,7]
# Stove_temp = sensor_data.iloc[:, 3]
# Kitchen_Comp = sensor_data.iloc[:, 4]
# Kitcen_PM = sensor_data.iloc[:, 5]
# print('length of kg', len(KG_burned))
# print('length of kichen pm', len(Kitcen_PM))
# ############_______________________________________________________
# for ev,st in enumerate(Fire_start):
#    if (KG_burned[st-40] == KG_burned[st] or KG_burned[0] == KG_burned[st]) and KG_burned[(st+1)] != KG_burned[st]:
#        event_2 = list(set(KG_burned[st:Fire_end[ev]]))
#    elif KG_burned[(st-40)] != KG_burned[st] or KG_burned[0] != KG_burned[st]:
#         if KG_burned[(st-20)] != KG_burned[st] or KG_burned[0] != KG_burned[st]:
#             event_2 = list(set(KG_burned[(st+2):Fire_end[ev]]))
#         elif KG_burned[(st-10)] != KG_burned[st] or KG_burned[0] != KG_burned[st]:
#             event_2 = list(set(KG_burned[(st + 2):Fire_end[ev]]))
#
#    EVENT_FUEL_CHANGE.append((int((sum(event_2))*100)/100))
#    raw_fuel_event.extend([a for a in KG_burned[st:Fire_end[ev]]])#need for raw
#    prec_movement.append((int(((sum(Cook_comp[st:Fire_end[ev]]))/(Fire_end[ev]-st))*100)))
#    raw_cook_comp_event.extend([a for a in Cook_comp[st:Fire_end[ev]]])#need for raw
#    Cook_CE_exposure.append((int((np.average([a for a in Cook_PM[st:Fire_end[ev]]]))*100))/100)
#    raw_cook_pm_event.extend([a for a in Cook_PM[st:Fire_end[ev]]])#need for raw
#    First_20_Cpm.extend([a for a in Cook_PM[st:(st+20)]])#need for raw
#    First_20_Cpm_avg.append(np.average(First_20_Cpm))
#    Median_cook_exposure.append((int((np.median([a for a in Cook_PM[st:Fire_end[ev]]])) * 100)) / 100)
#    Temp_CE_average.append((int((np.average([a for a in Stove_temp[st:Fire_end[ev]]]))*10))/10)
#    raw_temp_event.extend([a for a in Stove_temp[st:Fire_end[ev]]])#need for raw
#    Kitchen_movement_precent.append((int((sum(Kitchen_Comp[st:Fire_end[ev]]))/(len(Kitchen_Comp[st:Fire_end[ev]]))*100)))
#    Avg_kitchen_PM.append((int((np.average([a for a in Kitcen_PM[st:Fire_end[ev]]])) * 100)) / 100)
#    Median_kitche_PM.append((int((np.median([a for a in Kitcen_PM[st:Fire_end[ev]]])) * 100)) / 100)
#    raw_Kitchen_pm_event.extend([a for a in Kitcen_PM[st:Fire_end[ev]]])#need for raw
#    First_20_kpm.extend([a for a in Kitcen_PM[st:(st +20)]])#need for raw
#    First_20_kpm_avg.append(np.average(First_20_kpm))
#    Length_of_event.append(Fire_end[ev]-st) #need for raw
#    STD_Temp.append((int((stat.stdev(Stove_temp[st:Fire_end[ev]]))*100))/100)
#    STD_Avg_Kit_pm.append((int((stat.stdev(Kitcen_PM[st:Fire_end[ev]])) * 100)) / 100)
#    STD_cook_exp.append((int((stat.stdev(Cook_PM[st:Fire_end[ev]])) * 100)) / 100)
#
#
# time_start = enumerate(sensor_data.iloc[Fire_start,0])
# time_end =enumerate(sensor_data.iloc[Fire_end,0])
#
# Event_number = np.arange(1, len(Median_kitche_PM)+1,1)
# Data_event = {'| Cooking Start |' : time_start,
#               '| Cooking Stop |' : time_end,
#               '| Length of event (min)|': Length_of_event,
#               '| Fuel Used (FUEL) |' : EVENT_FUEL_CHANGE,
#               '| Average Temperature for Event (EXACT) |' : Temp_CE_average,
#               '| Std of event temperature |' : STD_Temp,
#               '| Average PM for Cook for Event (HAPEx) |' : Cook_CE_exposure,
#               '| Median PM for Cook for Event (HAPEx) |': Median_cook_exposure,
#               '| Std of Cook exposure |' : STD_cook_exp,'| First 20 minutes cook PM avg |' : First_20_Cpm_avg,
#               '| Percentage Cook Movement while cooking (HAPEx) |':prec_movement,
#               '| Average PM in Kitchen for Event (HAPEx) |' : Avg_kitchen_PM,
#               '| Median PM in Kitchen for Event (HAPEx) |' : Median_kitche_PM,
#               '| Std of Kitchen exposure |' : STD_Avg_Kit_pm,
#               '| First 20 minutes kitchen PM avg |' : First_20_kpm_avg,
#               '| Percentage Kitchen sensor moving while cooking (HAPEx) |' : Kitchen_movement_precent}
# df_event = pd.DataFrame(Data_event)#, index=Event_number)
#
# print(len(raw_fuel_event))
# print(len(raw_cook_pm_event))
# print(len(raw_cook_comp_event))
# print(len(raw_temp_event))
# print(len(raw_Kitchen_pm_event))
# ## raw event data set
# Raw_event = {'RAW cook pm ': raw_cook_pm_event,
#              'RAW cook Compliance': raw_cook_comp_event,
#              'RAW Temperature ':raw_temp_event,
#              'RAW Kitchen PM ': raw_Kitchen_pm_event,
#              'RAW fuel changes': raw_fuel_event}
#
#
# df_raw_event = pd.DataFrame(Raw_event)
#
# # this is to see how much in a day
# print('------------ iterate over a day----------')
# one = (sensor_data.iloc[:,0])
# print(one)
#
# time = []
# for d in one:
#     onee = '{:%d}'.format(datetime.datetime.strptime(d, '%m/%d/%Y %H:%M'))
#     time.append(onee)
#
#
# print(day)
# days_observed = len(list(set(day)))
# print(days_observed, 'days were observed')
#
# day_start = []
# day_end = []
# count = 0
# for stamp in day:
#     if count + 1 == len(day):
#         day_end.append((len(day))-1)
#         break
#     elif stamp != day[count +1]:
#         day_end.append(count)
#         day_start.append(count+1)
#     count = count + 1
#
# Start_day = day_start
# day_start[:0] = [0]
#
# Day_prec_movement = []
# Day_FUEL_CHANGE = []
# Day_Cook_exposure = []
# Day_Median_cook_exposure = []
# STD_day_cook_exp = []
# Day_Temp_average = []
# STD_day_temp =[]
# Day_Kitchen_movement_precent = []
# Day_Avg_kitchen_PM = []
# Day_Median_kitche_PM = []
# STD_day_k_pm = []
# raw_cook_pm_day =[]
# raw_Kitchen_pm_day = []
# raw_cook_comp_day = []
# raw_temp_day = []
# raw_fuel_day = []
# day_Cook_comp = sensor_data.iloc[:,6]
# day_Cook_PM = sensor_data.iloc[:,7]
# day_Stove_temp = sensor_data.iloc[:, 3]
# day_Kitchen_Comp = sensor_data.iloc[:, 4]
# day_Kitcen_PM = sensor_data.iloc[:, 5]
#
# count = 0
# for ev,st in enumerate(day_start):
#     if count + 2 == len(day_start)+1:
#         break
#     fuel_per_day = list(set([a for a in KG_burned[st:day_end[ev]]]))
#     Day_FUEL_CHANGE.append((int((sum(fuel_per_day))*100)/100))
#     raw_fuel_day.extend([a for a in KG_burned[st:day_end[ev]]])#need for raw
#     Day_prec_movement.append((int((sum(Cook_comp[st:day_end[ev]]))/(len(Cook_comp[st:day_end[ev]]))*100)))
#     raw_cook_comp_day.extend((Cook_comp[st:day_end[ev]]))#need for raw
#     Day_Kitchen_movement_precent.append((int((sum(Kitchen_Comp[st:day_end[ev]]))/(len(Kitchen_Comp[st:day_end[ev]]))*100)))
#     DCPM = ([a for a in Cook_PM[st:day_end[ev]]])
#     raw_cook_pm_day.extend(DCPM)#need for raw
#     Day_Cook_exposure.append((int((np.average(DCPM))*100))/100)
#     Day_Median_cook_exposure.append((int((np.median(DCPM)) * 100)) / 100)
#     TEMP_DAY = [a for a in Stove_temp[st:day_end[ev]]]
#     raw_temp_day.extend(TEMP_DAY)#need for raw
#     Day_Temp_average.append((int((np.average(TEMP_DAY)*10))/10))
#     DKPM = ([a for a in Kitcen_PM[st:day_end[ev]]])
#     raw_Kitchen_pm_day.extend(DKPM)#need for raw
#     Day_Avg_kitchen_PM.append((int((np.average(DKPM))*100))/100)
#     Day_Median_kitche_PM.append((int((np.median(DKPM))*100))/100)
#     STD_day_cook_exp.append((int((stat.stdev(DCPM)) * 100)) / 100)
#     STD_day_k_pm.append((int((stat.stdev(DKPM)) * 100)) / 100)
#     STD_day_temp.append((int((stat.stdev(TEMP_DAY)) * 100)) / 100)
#
#
# Day_time = sensor_data.iloc[Start_day[0:-1],0]
# stt = Start_day[0:-1]
# eddd = day_end[0:-1]
# stt.insert(len(stt),len(Fuel_KG_nf)-1)
# day_time = (sensor_data.iloc[stt,0])
#
#
# Day_number = np.arange(1, len(Day_Median_kitche_PM)+1,1)
# Data_day = {'| DAY and Time |' : day_time, '| Fuel removed (FUEL) |' : Day_FUEL_CHANGE,
#             '| Average Temperature for day (EXACT) |' : Day_Temp_average,
#             '| Std of day temperature |' : STD_day_temp,
#             '| Average PM for Cook for day (HAPEx) |' : Day_Cook_exposure,
#             '| Median PM for Cook for day (HAPEx) |': Day_Median_cook_exposure,
#             '| Std of Cook exposure |' : STD_day_cook_exp,
#             '| Percentage Cook Movement(HAPEx) |':Day_prec_movement,
#             '| Average PM in Kitchen for day (HAPEx) |' : Day_Avg_kitchen_PM,
#             '| Median PM in Kitchen for day (HAPEx) |' : Day_Median_kitche_PM,
#             '| Std of Kitchen exposure |' : STD_day_k_pm,
#             '| Percentage Kitchen sensor moving (HAPEx) |' : Day_Kitchen_movement_precent}
#
# df_day = pd.DataFrame(Data_day)
#
#
# Path_folder = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files"
# File_name_compiler = str(Path_folder) + "/1N_summary_hh_"+str(id_number)+".csv"
# df_event.to_csv(File_name_compiler)#, index=False)
# df_day.to_csv(File_name_compiler,index=False,mode='a')
#
# File_Raw_event = str(Path_folder) + "/1N_event_raw_hh_"+str(id_number)+".csv"
#
#
# num_events = {'Events': list(Event_number), 'Length of event (min)': Length_of_event}
# first_20_frame_event = {'RAW first 20 min kitchen PM': First_20_kpm,
#                         'RAW first 20 min cook PM': First_20_Cpm}
# Df_event = pd.DataFrame(num_events)
# Df_first_20 = pd.DataFrame(first_20_frame_event)
# #num_events.to_csv(File_Raw_event)
# #pd.concat([df_raw_event,Df_first_20,Df_event],axis=1).to_csv(File_Raw_event,index=False)
# File_Raw_day = str(Path_folder) + "/1N_day_raw_hh_"+str(id_number)+".csv"
#
# RAW_day = {'Fuel removed per day': raw_fuel_day, 'Cook day exposure': raw_cook_pm_day,
#            'cook compliance per day': raw_cook_comp_day, 'Temperature per day': raw_temp_day,
#            'Kitchen exp': raw_Kitchen_pm_day}
# df_day = pd.DataFrame(RAW_day)
# df_day.to_csv(File_Raw_day)