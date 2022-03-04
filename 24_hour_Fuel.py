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
from pathlib import Path

def FUEL_REMOVAL(Raw_fuel, Filter_Fuel, Thresold):
        remove = []
        remove_kg = []
        insert = []
        insert_kg = []
        v = 0
        for weight in Filter_Fuel:
            v = v + 1
            #print(weight)
            if v+1 == (len(Raw_fuel)):
                break
            elif Filter_Fuel[v] <= 0 or weight <= 0:
                if (abs(weight - Filter_Fuel[v]) > Thresold) or (abs(weight + Filter_Fuel[v]) > Thresold):
                    if weight - Filter_Fuel[v] > Thresold:
                        remove.append(v)
                        kg_amount = weight - Filter_Fuel[v]
                        remove_kg.append((int(kg_amount*1000))/1000)
                    elif (weight + Filter_Fuel[v] > Thresold):
                        insert.append(v)
                        kg_amount = weight + Filter_Fuel[v]
                        insert_kg.append((int(kg_amount*1000))/1000)
                else:
                    pass
            elif (weight - Filter_Fuel[v]) > Thresold:
                remove.append(v)
                remove_kg.append((int((abs(Filter_Fuel[v] - weight))*1000)/1000))

            elif (Filter_Fuel[v] - weight) > Thresold:
                insert.append(v)
                insert_kg.append(Filter_Fuel[v] - weight)
        v = 0


        kg = np.arange(0, len(Raw_fuel),1)
        count = 0
        KG_burned = []
        
        for wei in kg:
            if (wei) == (len(Raw_fuel)-1):
                KG_burned.append(KG_burned[-1])
                break
            elif remove[-1] == len(KG_burned)-2:
                KG_burned.append(KG_burned[-1])
                pass
            elif wei == remove[count]:
                KG_burned.append(remove_kg[count])
                if remove[-1] == wei:
                    end_bit = np.arange(wei, len(Raw_fuel),1)
                    for a in end_bit:
                        KG_burned.append(KG_burned[-1])
                    break
                count = count + 1
            elif wei == 0 and remove_kg[wei] != 0:
                KG_burned.append(0)
            else:
                KG_burned.append(KG_burned[-1])
     
        return KG_burned

Phase = "3N"
Computer = "personal"
# THis file is for gathering 24 hour averages 
#Work computer
#colecting metrics for each household comparison
HH_NUMBER = []
DAYS_O = []
TIME_START = []
TIME_END = []
PHASE_24_HR_AVG = []
Event_Count = []
PHASE_24_HR_AVG_2 = []
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

visit_1 = []
visit_2 = []
visit_3 = []
visit_1_2 = []
visit_2_2 = []
visit_3_2 = []
Moist_SAE_path = "E:/SAE_Moisture_Split/Moisture_SAE_split_"+Phase+"_.csv"
MOIST_SAE = pd.read_csv(Moist_SAE_path)

if Computer == 'work':
    os.chdir("C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+Phase +"/Compiler_1_exact/Raw_Day/Raw_D_metrics")

else:
    os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+ Phase +"/Compiler_1_exact/Raw_D_metrics")


Fuel_time_paths = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase +"/Time_list"


FUEL_sensor = os.getcwd()
FUEL_csv_open = glob.glob(os.path.join(FUEL_sensor, "*.csv"))

# second Exact Numbers
exact_2_2N = [1007]
exact_2_3N = [1001]
exact_2_4N = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1011, 1013, 1014, 1016, 1017, 1018, 1019, 1021, 1022, 1023, 1024, 1025, 1026, 1028, 1029, 1030, 1031, 1032, 1033, 1035, 1036, 1037, 1038, 1039]
if Phase == "3N":
    exac2= exact_2_3N
if Phase == "2N":
    exac2= exact_2_2N
if Phase == "4N":
    exac2= exact_2_4N

HH_NUMBER = []
HH_NUMBER_2 = []
DAYS_O = []
TIME_START = []
TIME_END = []
PHASE_24_HR_Fuel_AVG = []
HIGHEST_fuel_PER_DAY = []
DAY_OF_HIGHEST_fuel_removal = []
day_1_total = []
day_2_total = []
day_3_total = []
day_4_total = []
day_5_total = []
day_6_total = []
day_7_total = []
day_8_total = []
day_9_total = []
day_10_total = []
day_11_total = []
day_12_total = []
day_13_total = []
day_14_total = []
day_1_total_2 = []
day_2_total_2 = []
day_3_total_2 = []
day_4_total_2 = []
day_5_total_2 = []
day_6_total_2 = []
day_7_total_2 = []
day_8_total_2 = []
day_9_total_2 = []
day_10_total_2 = []
day_11_total_2 = []
day_12_total_2 = []
day_13_total_2 = []
day_14_total_2 = []
Household_count = 0
for file in FUEL_csv_open:
    with open(file, 'r') as f:
        csv_reader_fuel = csv.reader(f)
        for idx, row in enumerate(csv_reader_fuel):
            if idx == 1:
                id_number = (row[1])
                print('Household',id_number, type(id_number), str(id_number))
            elif 'Fuel Raw Data' in row:
                skippy = idx
                break
    second_exact = 0
    metric_day_data = pd.read_csv(file, skiprows=skippy)
    Fuel_removal = metric_day_data.iloc[:,1]
    day_arange = np.arange(0, 14)
    Fuel_time_path = Fuel_time_paths +Phase+"_"+id_number+"_time_array.csv"
    Fuel_time_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase +"/Time_list/"+Phase+"_"+id_number+"_time_array.csv"
    FF_USage_path_1 = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase +"/FIREFINDER/1 exact/"+id_number+"_FF_1.csv"
    if Phase == "3N" or Phase == "2N" or Phase == "4N":
        for hhhhhh in exac2:
            if int(id_number) == hhhhhh:
                print('babababaooiiiii')
                FF_USage_path_2 = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase +"/FIREFINDER/2 exact/"+id_number+"_FF_2.csv"
                ff_use_2 = pd.read_csv(FF_USage_path_2)
                ff_use_2 = ff_use_2.iloc[:,0]
                second_exact = 1
    
    
    time_vlaue_frame = pd.read_csv(Fuel_time_path)

    ff_use_1 = pd.read_csv(FF_USage_path_1)
    ff_use_1 = ff_use_1.iloc[:,0]
    second_exact_usage = 0
    second_exact_event = 0
    if metric_day_data.iloc[5,1]!= -1:
        Fuel_2_removal = (FUEL_REMOVAL(metric_day_data.iloc[:,0],metric_day_data.iloc[:,3], 0.02))
        Fuel_2_removal.remove(Fuel_2_removal[-1])
        Fuel_2_removal = pd.Series(Fuel_2_removal)
        day_average_fuel = []
        day_average_fuel_2 = []
        count_event_count = []
        day_count = 0

        for wood in day_arange:
            fuel_setting = []
            fuel_setting_2 = []
            if wood == 0:
                dummy_Fuel = Fuel_removal[5:((24*60)+6)]
                dummy_Fuel_2 = Fuel_2_removal[5:((24*60)+6)]
                

                for tv, anything in enumerate(dummy_Fuel):
                    if tv + 1 == len(dummy_Fuel)-1:
                        fuel_setting.append(anything)
                        break
                    elif anything != dummy_Fuel.iloc[tv + 1]:
                        fuel_setting.append(anything)
                day_average_fuel.append(sum(fuel_setting))
                #now second Alg
                for tv, anything in enumerate(dummy_Fuel_2):
                    if tv + 1 == len(dummy_Fuel_2)-1:
                        fuel_setting_2.append(anything)
                        break
                    elif anything != dummy_Fuel_2.iloc[tv + 1]:
                        fuel_setting_2.append(anything)
                day_average_fuel_2.append(sum(fuel_setting))
                
                day_time_end_vlaue  = ((24*60)+5)
                day_count = day_count +1
                # getting the events for the days
                if second_exact == 0:
                    Event_for_1 = list(ff_use_1.iloc[5:((24*60)+6)])
                    #print('event list--------------', Event_for_1)
                    Event_for_sum2 = Event_for_1[-1]
                else:
                    Event_for_1 = list(ff_use_1.iloc[5:((24*60)+6)])
                    Event_for_2 = list(ff_use_2.iloc[5:((24*60)+6)])
                    Event_for_sum2 = Event_for_2[-1] +Event_for_1[-1]
                count_event_count.append(Event_for_sum2)

            elif (wood != 0) and ((day_time_end_vlaue + (60*24)) <= len(metric_day_data.iloc[:,0])-1):
                dummy_Fuel = Fuel_removal[day_time_end_vlaue:(day_time_end_vlaue +(24*60))]
                dummy_Fuel_2 = Fuel_2_removal[day_time_end_vlaue:(day_time_end_vlaue +(24*60))]
                #print('are the types the same fucking asshole', len(dummy_Fuel),len(dummy_Fuel_2) )
                for tv, anything in enumerate(dummy_Fuel):
                    next_int = tv + 1 + day_time_end_vlaue
                    if tv + 1 == len(dummy_Fuel) -1:
                        fuel_setting.append(anything)
                        break
                    elif anything != dummy_Fuel[next_int]:
                        fuel_setting.append(anything)
                day_average_fuel.append(sum(fuel_setting))
                #print('is next int correct?',next_int)
                #now second Alg
                for tv2, anything2 in enumerate(dummy_Fuel_2):
                    next_int2 = tv2 + 1 + day_time_end_vlaue
                    if tv2 + 1 == len(dummy_Fuel_2) -1:
                        fuel_setting_2.append(anything2)
                        break
                    elif anything2 != dummy_Fuel_2[next_int2]:
                        fuel_setting_2.append(anything2)
                day_average_fuel_2.append(sum(fuel_setting_2))
                
                
                # getting the events for the days
                if second_exact != 1:
                    Event_for_1 = (ff_use_1[day_time_end_vlaue])
                    Event_for_sum2 = Event_for_1
                else:
                    Event_for_1 = (ff_use_1[day_time_end_vlaue])
                    Event_for_2 = (ff_use_2.iloc[day_time_end_vlaue])
                    Event_for_sum2 = Event_for_2 + Event_for_1
                count_event_count.append(Event_for_sum2) 

                day_time_end_vlaue  = day_time_end_vlaue + ((24*60))
                day_count = day_count +1
        print('here is day count ---------', day_count-1,round(day_count/2)) 
        complete_phase_24_Fuel_Sum = (sum(day_average_fuel)/(day_count))
        complete_phase_24_Fuel_Sum_2 = (sum(day_average_fuel_2)/(day_count))
        HH_NUMBER.append(id_number)
        HH_NUMBER_2.append(str(id_number)+"_2")
        Event_Count.append(count_event_count)
        

        DAYS_O = (day_count)
        TIME_START.append(time_vlaue_frame.iloc[5,0])
        TIME_END.append(time_vlaue_frame.iloc[day_time_end_vlaue,0])
        PHASE_24_HR_AVG.append(complete_phase_24_Fuel_Sum)
        PHASE_24_HR_AVG_2.append(complete_phase_24_Fuel_Sum_2)
        max_fuel_value = max(day_average_fuel)
        max_fuel_day = [index for index, item in enumerate(day_average_fuel) if item == max_fuel_value]

        HIGHEST_Fuel_PER_DAY.append(max_fuel_value)
        

        val_integer = max_fuel_day[0]

        if val_integer != 0:
            day_max_value = time_vlaue_frame.iloc[val_integer*24*60, 0]
        else:
            day_max_value = time_vlaue_frame.iloc[5,0]
        
        DAY_OF_HIGHEST_Fuel.append(day_max_value)

    else:
        day_average_fuel = [-1]
        day_average_fuel_2 = [-1]
        HH_NUMBER.append(id_number)
        HH_NUMBER_2.append(id_number+"_2")
        DAYS_O = (-1)
        TIME_START.append(-1)
        TIME_END.append(-1)
        PHASE_24_HR_AVG.append(-1)
        PHASE_24_HR_AVG_2.append(-1)
        HIGHEST_Fuel_PER_DAY.append(-1)
        DAY_OF_HIGHEST_Fuel.append(-1)

    day_counter = np.arange(0,14)
    if len(day_average_fuel) < len(day_counter):
        zero_count = np.arange(0, len(day_counter) - len(day_average_fuel))
        for z in zero_count:
            day_average_fuel.append(0)
            count_event_count.append(0)
            day_average_fuel_2.append(0)
            
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
    
    print('day o is this', int(DAYS_O))
    print(count_event_count, day_average_fuel)
#    # Adding moisture and SAE
    Fuel_day_SAE_moist = []
    Fuel_day_SAE_moist_2 = []
    for day, fuel in enumerate(day_average_fuel):
        if fuel == 0 or fuel == -1:# or MOIST_SAE.iloc[Household_count,5] == 0 or MOIST_SAE.iloc[Household_count,13] == 0:
            Fuel_day_SAE_moist.append(0)
            Fuel_day_SAE_moist_2.append(0)
        #elif day_average_fuel_2[day] == 0 or 
        else:
            if day <= round(DAYS_O/2):
                fuel_calc = fuel / (1 + (MOIST_SAE.iloc[Household_count,2]/100))
                fuel_calc_2 = day_average_fuel_2[day]/ (1 + (MOIST_SAE.iloc[Household_count,2]/100))
                if day < MOIST_SAE.iloc[day,5]:
                    TOTAL_ref = fuel_calc / MOIST_SAE.iloc[Household_count,6]/count_event_count[day]
                    Fuel_day_SAE_moist.append(TOTAL_ref)    

                    TOTAL_ref_2 = fuel_calc_2 / MOIST_SAE.iloc[Household_count,6]/count_event_count[day]
                    Fuel_day_SAE_moist_2.append(TOTAL_ref_2)

                elif day <= (MOIST_SAE.iloc[Household_count,5] + MOIST_SAE.iloc[Household_count,7]): 
                    TOTAL_ref = fuel_calc / MOIST_SAE.iloc[Household_count,8]/count_event_count[day]
                    Fuel_day_SAE_moist.append(TOTAL_ref)

                    TOTAL_ref_2 = fuel_calc_2 / MOIST_SAE.iloc[Household_count,8]/count_event_count[day]
                    Fuel_day_SAE_moist_2.append(TOTAL_ref_2)

                elif day <= (MOIST_SAE.iloc[Household_count,5] + MOIST_SAE.iloc[Household_count,7] + MOIST_SAE.iloc[Household_count,11]): 
                    TOTAL_ref = fuel_calc / MOIST_SAE.iloc[Household_count,12]/count_event_count[day]
                    Fuel_day_SAE_moist.append(TOTAL_ref)
                    TOTAL_ref_2 = fuel_calc_2 / MOIST_SAE.iloc[Household_count,12]/count_event_count[day]
                    Fuel_day_SAE_moist_2.append(TOTAL_ref_2)

                   
                elif day <= (MOIST_SAE.iloc[Household_count,5] + MOIST_SAE.iloc[Household_count,7] + MOIST_SAE.iloc[Household_count,11] + MOIST_SAE.iloc[Household_count,13]): 
                    TOTAL_ref = fuel_calc / MOIST_SAE.iloc[Household_count,14]/count_event_count[day]
                    Fuel_day_SAE_moist.append(TOTAL_ref)
                    TOTAL_ref_2 = fuel_calc_2 / MOIST_SAE.iloc[Household_count,14]/count_event_count[day]
                    Fuel_day_SAE_moist_2.append(TOTAL_ref_2)

                elif day > (MOIST_SAE.iloc[Household_count,5] + MOIST_SAE.iloc[Household_count,7] + MOIST_SAE.iloc[Household_count,11] + MOIST_SAE.iloc[Household_count,13]):
                    Collection = Fuel_day_SAE_moist[-1]
                    Fuel_day_SAE_moist.append(0)
                    Fuel_day_SAE_moist_2.append(0)

            else:
                fuel_calc = fuel / (1 + (MOIST_SAE.iloc[Household_count,3]/100))
                fuel_calc_2 = day_average_fuel_2[day] / (1 + (MOIST_SAE.iloc[Household_count,3]/100))
                if day <= (MOIST_SAE.iloc[Household_count,5] + MOIST_SAE.iloc[Household_count,7]): 
                    TOTAL_ref = fuel_calc / MOIST_SAE.iloc[Household_count,8]/count_event_count[day]
                    Fuel_day_SAE_moist.append(TOTAL_ref)
                    
                    TOTAL_ref_2 = fuel_calc_2 / MOIST_SAE.iloc[Household_count,8]/count_event_count[day]
                    Fuel_day_SAE_moist_2.append(TOTAL_ref_2)

                elif day <= (MOIST_SAE.iloc[Household_count,5] + MOIST_SAE.iloc[Household_count,7] + MOIST_SAE.iloc[Household_count,11]): 
                    TOTAL_ref = fuel_calc / MOIST_SAE.iloc[Household_count,12]/count_event_count[day]
                    Fuel_day_SAE_moist.append(TOTAL_ref)
                    
                    TOTAL_ref_2 = fuel_calc_2 / MOIST_SAE.iloc[Household_count,12]/count_event_count[day]
                    Fuel_day_SAE_moist_2.append(TOTAL_ref_2)

                elif day <= (MOIST_SAE.iloc[Household_count,5] + MOIST_SAE.iloc[Household_count,7] + MOIST_SAE.iloc[Household_count,11] + MOIST_SAE.iloc[Household_count,13]): 
                    TOTAL_ref = fuel_calc / MOIST_SAE.iloc[Household_count,14]/count_event_count[day]
                    Fuel_day_SAE_moist.append(TOTAL_ref)
                    TOTAL_ref_2 = fuel_calc_2 / MOIST_SAE.iloc[Household_count,14]/count_event_count[day]
                    Fuel_day_SAE_moist_2.append(TOTAL_ref_2)
                    Collection = TOTAL_ref
                    Collection_2 = TOTAL_ref_2
                        
                elif day > (MOIST_SAE.iloc[Household_count,5] + MOIST_SAE.iloc[Household_count,7] + MOIST_SAE.iloc[Household_count,11] + MOIST_SAE.iloc[Household_count,13]):
                    Fuel_day_SAE_moist.append(0)
                    Fuel_day_SAE_moist_2.append(0)
                #print(Fuel_day_SAE_moist)
    
    if (MOIST_SAE.iloc[Household_count,5] + MOIST_SAE.iloc[Household_count,7]) == (0 or 1):
        pump_install = Fuel_day_SAE_moist[0]
        pump_collection = Fuel_day_SAE_moist[1]
        pump_install_2 = Fuel_day_SAE_moist_2[0]
        pump_collection_2 = Fuel_day_SAE_moist_2[1]
    #elif (MOIST_SAE.iloc[Household_count,5] + MOIST_SAE.iloc[Household_count,7]) > DAYS_O:
    #    pump_install = 0
    else:
        pump_install = Fuel_day_SAE_moist[int((MOIST_SAE.iloc[Household_count,5] + MOIST_SAE.iloc[Household_count,7]) -2)]
        pump_collection = Fuel_day_SAE_moist[int((MOIST_SAE.iloc[Household_count,5] + MOIST_SAE.iloc[Household_count,7])-1)]
        pump_install_2 = Fuel_day_SAE_moist_2[int((MOIST_SAE.iloc[Household_count,5] + MOIST_SAE.iloc[Household_count,7]) -2)]
        pump_collection_2 = Fuel_day_SAE_moist_2[int((MOIST_SAE.iloc[Household_count,5] + MOIST_SAE.iloc[Household_count,7])-1)]
    
    if Fuel_day_SAE_moist[0] == 0:
        Collection = 0
        Collection_2 = 0
    else: 
        ZERO_Erase = [i for i in Fuel_day_SAE_moist if i != 0]
        Collection = ZERO_Erase[-1]
        ZERO_Erase_2 = [i for i in Fuel_day_SAE_moist_2 if i != 0]
        Collection_2 = ZERO_Erase_2[-1]
    
    
    day_1_total.append(Fuel_day_SAE_moist[0])
    day_2_total.append(Fuel_day_SAE_moist[1])
    day_3_total.append(Fuel_day_SAE_moist[2])
    day_4_total.append(Fuel_day_SAE_moist[3])
    day_5_total.append(Fuel_day_SAE_moist[4])
    day_6_total.append(Fuel_day_SAE_moist[5])
    day_7_total.append(Fuel_day_SAE_moist[6])
    day_8_total.append(Fuel_day_SAE_moist[7])
    day_9_total.append(Fuel_day_SAE_moist[8])
    day_10_total.append(Fuel_day_SAE_moist[9])
    day_11_total.append(Fuel_day_SAE_moist[10])
    day_12_total.append(Fuel_day_SAE_moist[11])
    day_13_total.append(Fuel_day_SAE_moist[12])
    day_14_total.append(Fuel_day_SAE_moist[13])
    day_1_total_2.append(Fuel_day_SAE_moist_2[0])
    day_2_total_2.append(Fuel_day_SAE_moist_2[1])
    day_3_total_2.append(Fuel_day_SAE_moist_2[2])
    day_4_total_2.append(Fuel_day_SAE_moist_2[3])
    day_5_total_2.append(Fuel_day_SAE_moist_2[4])
    day_6_total_2.append(Fuel_day_SAE_moist_2[5])
    day_7_total_2.append(Fuel_day_SAE_moist_2[6])
    day_8_total_2.append(Fuel_day_SAE_moist_2[7])
    day_9_total_2.append(Fuel_day_SAE_moist_2[8])
    day_10_total_2.append(Fuel_day_SAE_moist_2[9])
    day_11_total_2.append(Fuel_day_SAE_moist_2[10])
    day_12_total_2.append(Fuel_day_SAE_moist_2[11])
    day_13_total_2.append(Fuel_day_SAE_moist_2[12])
    day_14_total_2.append(Fuel_day_SAE_moist_2[13])
    visit_1.append(pump_install)
    visit_2.append(pump_collection)
    visit_3.append(Collection)
    visit_1_2.append(pump_install_2)
    visit_2_2.append(pump_collection_2)
    visit_3_2.append(Collection_2)
    
    Household_count = Household_count + 1

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
HH_fuel_SAE_Moist = {'Household': HH_NUMBER,'Phase 24hr Avg (sum of phase/min/day obesrved)':PHASE_24_HR_AVG,
                           'Day 1': day_1_total,
                           'Day 2': day_2_total,
                           'Day 3': day_3_total,
                           'Day 4': day_4_total,
                           'Day 5': day_5_total,
                           'Day 6': day_6_total,
                           'Day 7': day_7_total,
                           'Day 8': day_8_total,
                           'Day 9': day_9_total,
                           'Day 10': day_10_total,
                           'Day 11': day_11_total,
                           'Day 12': day_12_total,
                           'Day 13': day_13_total,'Day 14': day_14_total, 
                           'Visit 1': visit_1 , 'Visit 2': visit_2, 'Visit 3':visit_3 }

df_HH_fuel_SAE_Moist_breakdown = pd.DataFrame(HH_fuel_SAE_Moist,columns=['Household','Phase 24hr Avg (sum of phase/min/day obesrved)','Day 1','Day 2',
                                                                           'Day 3','Day 4','Day 5',
                                                                           'Day 6','Day 7','Day 8',
                                                                           'Day 9','Day 10','Day 11',
                                                                           'Day 12','Day 13','Day 14','Visit 1', 'Visit 2', 'Visit 3' ])
HH_fuel_SAE_Moist_2 = {'Household_2222': HH_NUMBER_2, 'Phase 24hr Avg (sum of phase/min/day obesrved)':PHASE_24_HR_AVG_2,
                           'Day 1': day_1_total_2,
                           'Day 2': day_2_total_2,
                           'Day 3': day_3_total_2,
                           'Day 4': day_4_total_2,
                           'Day 5': day_5_total_2,
                           'Day 6': day_6_total_2,
                           'Day 7': day_7_total_2,
                           'Day 8': day_8_total_2,
                           'Day 9': day_9_total_2,
                           'Day 10': day_10_total_2,
                           'Day 11': day_11_total_2,
                           'Day 12': day_12_total_2,
                           'Day 13': day_13_total_2,'Day 14': day_14_total_2, 
                           'Visit 1': visit_1_2 , 'Visit 2': visit_2_2, 'Visit 3':visit_3_2 }

df_HH_fuel_SAE_Moist_breakdown_2 = pd.DataFrame(HH_fuel_SAE_Moist_2,columns=['Household_2222','Phase 24hr Avg (sum of phase/min/day obesrved)', 'Day 1','Day 2',
                                                                           'Day 3','Day 4','Day 5',
                                                                           'Day 6','Day 7','Day 8',
                                                                           'Day 9','Day 10','Day 11',
                                                                           'Day 12','Day 13','Day 14','Visit 1', 'Visit 2', 'Visit 3' ])

if Computer == 'work':
    Fuel_24_hour_file_path = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+ Phase +"/"+Phase+"_24_hour_Fuel_removal" +".csv"
    HH_breakdown_file_path = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+ Phase +"/"+Phase+"_Household_Fuel_removal_breakdown" +".csv"
    HH_SAE_moist_breakdown_file_path = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+ Phase +"/"+Phase+"_Household_SAE_Moist_breakdown" +".csv"
else:
    Fuel_24_hour_file_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase +"/"+Phase+"_24_hour_Fuel_removal" +".csv"
    HH_breakdown_file_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase +"/"+Phase+"_Household_Fuel_removal_breakdown" +".csv"
    HH_SAE_moist_breakdown_file_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase +"/"+Phase+"_Household_SAE_Moist_breakdown" +".csv"
    Fuel_24_hour_file_path_2 = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase +"/"+Phase+"_second_alg_24_hour_Fuel_removal" +".csv"
    HH_breakdown_file_path_2 = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase +"/"+Phase+"_second_alg_Household_Fuel_removal_breakdown" +".csv"
    HH_SAE_moist_breakdown_file_path_2 = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase +"/"+Phase+"_second_alg_Household_SAE_Moist_breakdown" +".csv"

df_Fuel_per_24_hour.to_csv(Fuel_24_hour_file_path,index=False,mode='a')
df_HH_Fuel_breakdown.to_csv(HH_breakdown_file_path,index=False,mode='a')
df_HH_fuel_SAE_Moist_breakdown.to_csv(HH_SAE_moist_breakdown_file_path, index=False,mode='a')

#df_Fuel_per_24_hour_2.to_csv(Fuel_24_hour_file_path_2,index=False,mode='a')
#df_HH_Fuel_breakdown_2.to_csv(HH_breakdown_file_path_2,index=False,mode='a')
df_HH_fuel_SAE_Moist_breakdown_2.to_csv(HH_SAE_moist_breakdown_file_path_2, index=False,mode='a')

