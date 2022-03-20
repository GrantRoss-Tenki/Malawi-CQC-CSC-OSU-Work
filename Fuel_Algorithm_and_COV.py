# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 17:48:12 2022

@author: rossgra
"""

# this file is to determine the differences in algorithms for fuel

import pandas as pd
import numpy as np
import csv
import os
import glob
import matplotlib.pyplot as plt
import math
import statistics as stat 
#from pathlib import Path
#import satistics as stat

def FUEL_REMOVAL(Raw_fuel, Thresold, min_average_spread):
        Fuel_KG_nf = Raw_fuel


        count = 0
        n = 0
        Fuel_KG = []

        insert = []
        remove = []
        #This works, but there needsis a better way
        
#        previous = Fuel_KG_nf.iloc[(0)]
#        for kg in Fuel_KG_nf:
#            n = n + 1
#            if n+2 == (len(Fuel_KG_nf)):
#                Fuel_KG.append(Fuel_KG_nf.iloc[(n)])
#                Fuel_KG.append(Fuel_KG_nf.iloc[(n+1)])
#                break
#
#            elif (previous < Fuel_KG_nf.iloc[n+2]) and  (Fuel_KG_nf.iloc[(n+2)] < Fuel_KG_nf.iloc[(n)]):
#                Fuel_KG.append(Fuel_KG_nf.iloc[n+2])
#
#            elif Fuel_KG_nf.iloc[n+2] >= previous:
#                 Fuel_KG.append(previous)
#
#            elif (previous > Fuel_KG_nf.iloc[n+2]) and (Fuel_KG_nf.iloc[(n)] < Fuel_KG_nf.iloc[(n+2)]):
#                Fuel_KG.append(Fuel_KG_nf.iloc[n+2])
#
#            else:
#                Fuel_KG.append(Fuel_KG_nf.iloc[(n)])
#            previous = Fuel_KG[-1]
#        
        
        # this is for running average
        Mean_Count_min = [np.mean(Fuel_KG_nf[0:min_average_spread+1])]
        count = 0
        inside_spread = [0]
        for kg in (Fuel_KG_nf):
            if count == min_average_spread:
                median = stat.median(inside_spread)
                Mean_Count_min.append(median)
                inside_spread = []
                count = -1
            else:
                Mean_Count_min.append(Mean_Count_min[-1])
                inside_spread.append(kg)
            count = count + 1
        
        Mean_Count_min.remove(Mean_Count_min[0])
        
        # two in one algorithm taking in the threshold and running average 
        KG_burned = [0]
        insert = []
        for vv, kg in enumerate(Fuel_KG_nf):
            if ((vv % 2) == 0) or (vv == 0):
                KG_burned.append(KG_burned[-1])
                if vv + 3 == len(Fuel_KG_nf):
                    KG_burned.append(KG_burned[-1])
                    KG_burned.append(KG_burned[-1])
                    KG_burned.remove(KG_burned[0])  
                    break
                if (vv == 0):
                    previous = Fuel_KG_nf.iloc[(0)]
                    delta_up = 0
                    delta_down = 0
                else:
                    previous = Fuel_KG_nf.iloc[vv -1]
                    delta_up =  abs(Fuel_KG_nf.iloc[vv +2] -kg)
                    delta_down = abs(kg - Fuel_KG_nf.iloc[vv +2])
                pass
            elif vv + 3 == len(Fuel_KG_nf):
                    KG_burned.append(KG_burned[-1])
                    KG_burned.append(KG_burned[-1])
                    
                    break
            elif  delta_up > Thresold and Fuel_KG_nf[vv +3] > Mean_Count_min[vv]:
                if previous < kg:
                    insert.append(vv)
                    KG_burned.append(KG_burned[-1])
                else:
                    KG_burned.append(KG_burned[-1])
            elif delta_down > Thresold and Fuel_KG_nf.loc[vv +3] < Mean_Count_min[vv]:
                if (kg  < previous) or (kg < Mean_Count_min[vv]) or (Fuel_KG_nf.loc[vv +1] < previous):
                    
                    KG_burned.append(delta_down)
                else:
                    KG_burned.append(KG_burned[-1])
            else:
                KG_burned.append(KG_burned[-1])
        
#        if aray_equal != 0:
#            print('this needs to work,,,,,n ow', aray_equal)
#            #if aray_equal < 0:
#                
#            for a in equate_araray:
#                Mean_Count_min.append(Mean_Count_min[0])
        # threshold fun time
        # first adaptation willl need this
        print('---WILL NEED THE FOLLOWING ------ IT IS NEW ALGO------')
#        count_removals = 0
#        KG_burned = [0]
#        for time_value, weight in enumerate(Fuel_KG):
#            if ((time_value % 2) == 0) or (time_value == 0):
#                KG_burned.append(KG_burned[-1])
#
#                if time_value + 2 == len(Fuel_KG):
#                    KG_burned.append(KG_burned[-1])
#                    KG_burned.append(KG_burned[-1])
#                    print('this the length of mean count array', len(Mean_Count_min))
#                    break
#                pass
#            elif time_value + 2 == len(Fuel_KG):
#                    KG_burned.append(KG_burned[-1])
#                    KG_burned.append(KG_burned[-1])
#                    print('this the length of mean count array', len(Mean_Count_min))
#                    break
#            elif abs(weight - Fuel_KG[time_value+2] > Thresold) or  (abs(Fuel_KG[time_value+2] - weight) > Thresold):
#                up_thresh = abs(Fuel_KG[time_value+2] - weight)
#                low_thresh = abs(weight - Fuel_KG[time_value+2])
#                if (up_thresh > Thresold) and (Fuel_KG[time_value+2] >= Mean_Count_min[time_value]): # the two here can be adjusted
#                    insert.append(up_thresh)
#                    KG_burned.append(KG_burned[-1])
#                elif (low_thresh > Thresold) and (Fuel_KG[time_value+2] <= Mean_Count_min[time_value]): # the two here can be adjusted
#                    KG_burned.append(up_thresh)
#                    count_removals = count_removals + 1
#                else:
#                    KG_burned.append(KG_burned[-1])
#            elif (weight == 0) and (weight -Thresold <  weight  < weight + Thresold):
#                KG_burned.append(0)
#            else:
#                KG_burned.append(KG_burned[-1])
                
         
        
        print('-What are the lengths-------in and out-------', len(KG_burned),len(Raw_fuel))
        
        ##this is the origional and now it does not work
        print('---ORIGIONAL ------ IT IS THE OLD WORKING ALGO------')
#        Fuel_KG.insert(0, Fuel_KG_nf.iloc[0])
#        remove = []
#        remove_kg = []
#        insert = []
#        insert_kg = []
#        v = 0
#        Filter_Fuel = Fuel_KG
#        for weight in Filter_Fuel:
#            v = v + 1
#            #print(weight)
#            if v+1 == (len(Raw_fuel)):
#                break
#            elif Filter_Fuel[v] <= 0 or weight <= 0:
#                if (abs(weight - Filter_Fuel[v]) > Thresold) or (abs(weight + Filter_Fuel[v]) > Thresold):
#                    if weight - Filter_Fuel[v] > Thresold:
#                        remove.append(v)
#                        kg_amount = weight - Filter_Fuel[v]
#                        remove_kg.append((int(kg_amount*1000))/1000)
#                    elif (weight + Filter_Fuel[v] > Thresold):
#                        insert.append(v)
#                        kg_amount = weight + Filter_Fuel[v]
#                        insert_kg.append((int(kg_amount*1000))/1000)
#                else:
#                    pass
#            elif (weight - Filter_Fuel[v]) > Thresold:
#                remove.append(v)
#                remove_kg.append((int((abs(Filter_Fuel[v] - weight))*1000)/1000))
#
#            elif (Filter_Fuel[v] - weight) > Thresold:
#                insert.append(v)
#                insert_kg.append(Filter_Fuel[v] - weight)
     


#        kg = np.arange(0, len(Raw_fuel),1)
#        count = 0
#        KG_burned = []
#        
#        for wei in kg:
#            if (wei) == (len(Raw_fuel)-1):
#                KG_burned.append(KG_burned[-1])
#                break
#            elif remove[-1] == len(KG_burned)-2:
#                KG_burned.append(KG_burned[-1])
#                pass
#            elif wei == remove[count]:
#                KG_burned.append(remove_kg[count])
#                if remove[-1] == wei:
#                    end_bit = np.arange(wei, len(Raw_fuel),1)
#                    for a in end_bit:
#                        KG_burned.append(KG_burned[-1])
#                    break
#                count = count + 1
#            elif wei == 0: #and remove_kg[wei] != 0:
#                KG_burned.append(0)
#            else:
#                KG_burned.append(KG_burned[-1])
#        #print('is this where it breaks?  ', remove, len(KG_burned))
        return KG_burned, Mean_Count_min


Computer = "personal"
Phase = "1N"
Second_Exact = [1,2]
min_average_spread = 5
if Phase== "2N":
    exact_2_hh = [1007]
elif Phase== "3N":
    exact_2_hh = [1001]
elif Phase== "4N":
    exact_2_hh = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1011, 1013, 1014, 1016, 1017, 1018, 1019, 1021, 1022, 1023, 1024, 1025, 1026, 1028, 1029, 1030, 1031, 1032, 1033, 1035, 1036, 1037, 1038, 1039]
elif Phase== "2H":
    exact_2_hh = [2006]
elif Phase== "3H":
    exact_2_hh = [2001, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
else:
    exact_2_hh = [0]
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
PHASE_24_HR_AVG_Min = []
HIGHEST_Fuel_PER_DAY = []
DAY_OF_HIGHEST_Fuel = []
visit_1_min = []
visit_2_min = []
visit_3_min = []

if (Phase  == "1N"):
    Fuel_scale_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/1N/1N_1H_Survey_summary_.csv"
    fuel_scale = pd.read_csv(Fuel_scale_path)
else:
    Fuel_scale_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/"+Phase+"_Survey_summary_.csv"
    fuel_scale = pd.read_csv(Fuel_scale_path)

if Computer == 'work':
    os.chdir("D:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_"+str(Second_Exact[0])+"_exact")
    Moist_SAE_path = "D:/SAE_Moisture_Split/Moisture_SAE_split_1N_.csv"

elif Phase == "1N":
    os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_1_exact/Raw_D_metrics")
    Moist_SAE_path = "E:/SAE_Moisture_Split/Moisture_SAE_split_"+Phase+"_.csv"

else:
    os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_1_exact/Raw_D_metrics")
    Moist_SAE_path = "E:/SAE_Moisture_Split/Moisture_SAE_split_"+Phase+"_.csv"
    
FUEL_sensor = os.getcwd()
FUEL_csv_open = glob.glob(os.path.join(FUEL_sensor, "*.csv"))
MOIST_SAE = pd.read_csv(Moist_SAE_path)
# second Exact Numbers


HH_NUMBER = []
HH_NUMBER_2 = []
HH_NUMBER_Min = []
DAYS_O = []
TIME_START = []
TIME_END = []
PHASE_24_HR_Fuel_AVG = []
HIGHEST_fuel_PER_DAY = []
DAY_OF_HIGHEST_fuel_removal = []
day_1_total_Min= []
day_2_total_Min = []
day_3_total_Min = []
day_4_total_Min = []
day_5_total_Min = []
day_6_total_Min = []
day_7_total_Min = []
day_8_total_Min = []
day_9_total_Min = []
day_10_total_Min = []
day_11_total_Min = []
day_12_total_Min = []
day_13_total_Min = []
day_14_total_Min = []

Day_1_use = []
Day_2_use = []
Day_3_use = []
Day_4_use = []
Day_5_use = []
Day_6_use = []
Day_7_use = []
Day_8_use = []
Day_9_use = []

Day_1_Fuel = []
Day_2_Fuel = []
Day_3_Fuel = []
Day_4_Fuel = []
Day_5_Fuel = []
Day_6_Fuel = []
Day_7_Fuel = []
Day_8_Fuel = []
Day_9_Fuel = []


COV_Whole = []
mean_days_col_array = []
STD_days_Col_array = []
days_counted = []
MJ_SAE_DAY = []
MJ_SAE_DAY_phase = []
days_filtered = []
SAE_PHase = []
fuel_scle_value = []
Phase_cooking_times = []
fuel_removed_for_phase = []
for file in FUEL_csv_open:
    with open(file, 'r') as f:
        csv_reader_fuel = csv.reader(f)
        for idx, row in enumerate(csv_reader_fuel):
            if idx == 1:
                id_number = (row[1])
                print('-=-=-=-=-=-=-=-=-=-=-=-=Household=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-',id_number)
            elif 'Fuel Raw Data' in row:
                skippy = idx
                break

    hhh_survey = fuel_scale.iloc[:,1]
    for row, bed in enumerate(hhh_survey):
        if int(id_number) == int(bed):
            row_survey = int(row)
            print('----row -',row_survey )
            break
    metric_day_data = pd.read_csv(file, skiprows=skippy)
    # introducing Calorfic heating value mj/kg
    # using 20.7 mj/kg for wood and 15.13 mj/kg
    FUEL_SCALE_VALUE =  fuel_scale.iloc[row_survey, 19]
    Average_SAE = fuel_scale.iloc[row_survey,7]
    
    NCV = 20.7*(1-FUEL_SCALE_VALUE) + 15.13*(FUEL_SCALE_VALUE)
    
    for ttt in exact_2_hh:
        Cooking_minute_2 = []
        if int(id_number) == ttt and len(Second_Exact) > 1:
            second_exact_2_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_2_exact/Fire_Finder_usage_2/"+Phase+"_HH_raw_Day_metrics_"+str(id_number)+"_1_exact_seeeecond.csv"
            second_exact_2 = pd.read_csv(second_exact_2_path,  skiprows=2)
            Cooking_minute_2 = second_exact_2.iloc[:,3]
            
        else:
            for zero in metric_day_data.iloc[:,0]:
                Cooking_minute_2.append(0)
    second_exact = 0
    
    Fuel_removal = metric_day_data.iloc[:,0]
    if Fuel_removal[0] == -1:
        continue
    Fuel_removal, Fuel_running_mean = FUEL_REMOVAL(Fuel_removal, 0.005, min_average_spread)
    Cooking_minute = metric_day_data.iloc[:,4]
    
    day_arange = np.arange(0, 14)
    if Computer == 'work':
        Fuel_time_path = "D:/Time_list/1N_"+id_number+"_time_array.csv"
        FF_USage_path_1 = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+Phase+"//FIREFINDER/1 exact/"+id_number+"_FF_1.csv"

    else:
        Fuel_time_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Time_list/"+Phase+"_"+str(id_number)+"_time_array.csv"
        FF_USage_path_1 = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/FIREFINDER/1 exact/"+id_number+"_FF_1.csv"
    
    
    Household_count = 0
    HH_metric_row = np.arange(1001, 1040, 1)
    for HHMR in HH_metric_row:
        if int(id_number) == HHMR:
            Household_count = HHMR -1001
            break
            
    time_vlaue_frame = pd.read_csv(Fuel_time_path)

    ff_use_1 = pd.read_csv(FF_USage_path_1)
    ff_use_1 = ff_use_1.iloc[:,0]
    second_exact_usage = 0
    second_exact_event = 0
    if metric_day_data.iloc[5,1]!= -1:

        day_sum_fuel = []

        Cooking_times_min = []
        count_event_count = []
        day_count = 0
        SAE_PHase.append(Average_SAE)
        fuel_scle_value.append(FUEL_SCALE_VALUE)

        for wood in day_arange:
            fuel_setting = []

            if wood == 0:
                dummy_Fuel = Fuel_removal[5:((24*60)+6)]
                Cooking_sum = int(sum((Cooking_minute[5:((24*60)+6)]))) + int(sum((Cooking_minute_2[5:((24*60)+6)])))
                Cooking_times_min.append(Cooking_sum)
                for tv, anything in enumerate(dummy_Fuel):
                    if tv + 1 == len(dummy_Fuel)-1:
                        if anything != dummy_Fuel[-1]:
                            fuel_setting.append(anything)
                            break
                        else:
                            break
                    elif anything != dummy_Fuel[tv + 1]:
                        
                        fuel_setting.append(anything)
                        
                day_sum_fuel.append(sum(fuel_setting))
            
                
                day_time_end_vlaue  = ((24*60)+5)
                day_count = day_count +1

                
                # getting the events for the days
                Event_for_1 = list(ff_use_1.iloc[5:((24*60)+6)])

                Event_for_sum2 = Event_for_1[-1]

                count_event_count.append(Event_for_sum2)
                
            elif (wood != 0) and ((day_time_end_vlaue + (60*24)) <= len(metric_day_data.iloc[:,0])-1):
                dummy_Fuel = Fuel_removal[day_time_end_vlaue:(day_time_end_vlaue +(24*60))]
                Cooking_sum = int(sum((Cooking_minute[day_time_end_vlaue:(day_time_end_vlaue +(24*60))]))) + int(sum((Cooking_minute_2[day_time_end_vlaue:(day_time_end_vlaue +(24*60))])))
                Cooking_times_min.append(Cooking_sum)

                #print('are the types the same fucking asshole', len(dummy_Fuel),len(dummy_Fuel_2) )
                for tv, anything in enumerate(dummy_Fuel):
                    next_int = tv + 1 #+ day_time_end_vlaue
                    
                    if (tv + 1 == len(dummy_Fuel) -1):
                        if dummy_Fuel[0] == dummy_Fuel[-1]:
                            fuel_setting.append(dummy_Fuel[0])
                        else:
                            fuel_setting.append(fuel_setting[-1])
                        
                        break
                    
                    elif anything != dummy_Fuel[next_int]:
                        fuel_setting.append(anything)
                
                day_sum_fuel.append(sum(fuel_setting))
                #print('is next int correct?',next_int)
               
                
                
                # getting the events for the days
                Event_for_1 = (ff_use_1[day_time_end_vlaue])
                Event_for_sum2 = Event_for_1
                count_event_count.append(Event_for_sum2) 

                day_time_end_vlaue  = day_time_end_vlaue + ((24*60))
                day_count = day_count +1
        #print('here is day count ---------', day_count-1,round(day_count/2)) 
        new_fuel_day = []
        Day_Sum_pre_filter = day_sum_fuel
        for fff in day_sum_fuel:
            new_fuel_day.append(fff/(1 + ((np.average(MOIST_SAE.iloc[row_survey,2:4]))/100)))
        day_sum_fuel = new_fuel_day
        complete_phase_24_Fuel_Sum = (sum(day_sum_fuel)/(day_count))
        fuel_removed_for_phase.append(sum(day_sum_fuel))
        HH_NUMBER.append(id_number)
        HH_NUMBER_Min.append((id_number)+"_m")
        Event_Count.append(count_event_count)
        
        mj_equatoin_SAE = (complete_phase_24_Fuel_Sum*NCV)/ Average_SAE
        MJ_SAE_DAY.append(mj_equatoin_SAE)
        DAYS_O = (day_count)
        TIME_START.append(time_vlaue_frame.iloc[5,0])
        TIME_END.append(time_vlaue_frame.iloc[day_time_end_vlaue,0])
        PHASE_24_HR_AVG.append(complete_phase_24_Fuel_Sum)
        max_fuel_value = max(day_sum_fuel)
        max_fuel_day = [index for index, item in enumerate(day_sum_fuel) if item == max_fuel_value]

        HIGHEST_Fuel_PER_DAY.append(max_fuel_value)
        

        val_integer = max_fuel_day[0]

        if val_integer != 0:
            day_max_value = time_vlaue_frame.iloc[val_integer*24*60, 0]
        else:
            day_max_value = time_vlaue_frame.iloc[5,0]
        
        DAY_OF_HIGHEST_Fuel.append(day_max_value)

    else:
        day_average_fuel = [-1]
        HH_NUMBER.append(id_number)
        fuel_removed_for_phase.append(-1)
        HH_NUMBER_Min.append(str(id_number)+"_m")
        DAYS_O = (-1)
        TIME_START.append(-1)
        TIME_END.append(-1)
        PHASE_24_HR_AVG.append(-1)
        MJ_SAE_DAY.append(-1)
        PHASE_24_HR_AVG_2.append(-1)
        HIGHEST_Fuel_PER_DAY.append(-1)
        DAY_OF_HIGHEST_Fuel.append(-1)

    day_counter = np.arange(0,14)

    if len(Day_Sum_pre_filter) < len(day_counter):
        zero_count = np.arange(0, len(day_counter) - len(Day_Sum_pre_filter))
        for z in zero_count:
            Day_Sum_pre_filter.append(0)
            count_event_count.append(0)
            Cooking_times_min.append(0)

    
    
   # print('here is the Weighted Biomass NCV---------------', NCV)
    #print('are the cooking times right?--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-', Cooking_times_min,day_sum_fuel, MOIST_SAE.iloc[row_survey,2])
#    # Adding moisture and SAE
    Fuel_day_SAE_moist = []
    Fuel_day_SAE_moist_2 = []
    Fuel_day_SAE_moist_min = []
    MJ_SAE_DAY_array = []
    Fuel_dry_WHole_Phase = []
    for day, fuel in enumerate(Day_Sum_pre_filter):
        if fuel == 0 or fuel == -1:# or MOIST_SAE.iloc[Household_count,5] == 0 or MOIST_SAE.iloc[Household_count,13] == 0:
            Fuel_day_SAE_moist.append(0)
            Fuel_day_SAE_moist_2.append(0)
            Fuel_day_SAE_moist_min.append(0)
            Fuel_dry_WHole_Phase.append(0)
        else:
            if day <= round(DAYS_O/2):
                fuel_calc = (fuel / (1 + (MOIST_SAE.iloc[row_survey,2]/100)))
                Fuel_dry_WHole_Phase.append(fuel_calc)
                if day < MOIST_SAE.iloc[day,5]:
                    TOTAL_ref = fuel_calc /count_event_count[day]#/ MOIST_SAE.iloc[row_survey,6]
                    Fuel_day_SAE_moist.append(TOTAL_ref)    
                    TOTAL_ref_min = fuel_calc /Cooking_times_min[day]#/ MOIST_SAE.iloc[row_survey,6]
                    if TOTAL_ref_min <= 0.0384:
                        MJ_SAE_DAY_array.append((int(fuel_calc)* int(NCV))/ (Average_SAE))
                        Fuel_day_SAE_moist_min.append(TOTAL_ref_min)
                    else:
                        Fuel_day_SAE_moist_min.append(-1)
                   
                elif day <= (MOIST_SAE.iloc[row_survey,5] + MOIST_SAE.iloc[row_survey,7]): 
                    TOTAL_ref = fuel_calc/count_event_count[day] # / MOIST_SAE.iloc[row_survey,8]
                    Fuel_day_SAE_moist.append(TOTAL_ref)

                    TOTAL_ref_min = fuel_calc /Cooking_times_min[day]#/ MOIST_SAE.iloc[Household_count,6]
                    if TOTAL_ref_min <= 0.0384:
                        MJ_SAE_DAY_array.append((int(fuel_calc)* int(NCV))/ (Average_SAE))
                        Fuel_day_SAE_moist_min.append(TOTAL_ref_min)
                    else:
                        Fuel_day_SAE_moist_min.append(-1)
                    
                elif day <= (MOIST_SAE.iloc[row_survey,5] + MOIST_SAE.iloc[row_survey,7] + MOIST_SAE.iloc[row_survey,11]): 
                    TOTAL_ref = fuel_calc /count_event_count[day] #/ MOIST_SAE.iloc[row_survey,12]
                    Fuel_day_SAE_moist.append(TOTAL_ref)
                    TOTAL_ref_min = fuel_calc /Cooking_times_min[day] #/ MOIST_SAE.iloc[row_survey,12]

                    if TOTAL_ref_min <= 0.0384:
                        MJ_SAE_DAY_array.append((int(fuel_calc)* int(NCV))/ (Average_SAE))
                        Fuel_day_SAE_moist_min.append(TOTAL_ref_min)
                    else:
                        Fuel_day_SAE_moist_min.append(-1)
                   
                elif day <= (MOIST_SAE.iloc[row_survey,5] + MOIST_SAE.iloc[row_survey,7] + MOIST_SAE.iloc[row_survey,11] + MOIST_SAE.iloc[row_survey,13]): 
                    TOTAL_ref = fuel_calc /count_event_count[day] #/ MOIST_SAE.iloc[row_survey,14]
                    Fuel_day_SAE_moist.append(TOTAL_ref)
                    TOTAL_ref_min = fuel_calc /Cooking_times_min[day] #/ MOIST_SAE.iloc[row_survey,14]

                    if TOTAL_ref_min <= 0.0384:
                        MJ_SAE_DAY_array.append((int(fuel_calc)* int(NCV))/ (Average_SAE))
                        Fuel_day_SAE_moist_min.append(TOTAL_ref_min)
                    else:
                        Fuel_day_SAE_moist_min.append(-1)
                elif day > (MOIST_SAE.iloc[row_survey,5] + MOIST_SAE.iloc[row_survey,7] + MOIST_SAE.iloc[row_survey,11] + MOIST_SAE.iloc[row_survey,13]):
                    Collection = Fuel_day_SAE_moist[-1]
                    Fuel_day_SAE_moist.append(0)
                    Fuel_day_SAE_moist_2.append(0)
                    Fuel_day_SAE_moist_min.append(0)
                    Fuel_dry_WHole_Phase.append(0)
            else:
                fuel_calc = (fuel/ (1 + (MOIST_SAE.iloc[row_survey,3]/100)))
                Fuel_dry_WHole_Phase.append(fuel_calc)
                if day <= (MOIST_SAE.iloc[row_survey,5] + MOIST_SAE.iloc[row_survey,7]): 
                    TOTAL_ref = fuel_calc/count_event_count[day] # / MOIST_SAE.iloc[row_survey,8]
                    Fuel_day_SAE_moist.append(TOTAL_ref)
                    TOTAL_ref_min = fuel_calc /Cooking_times_min[day]#/ MOIST_SAE.iloc[row_survey,6]

                    if TOTAL_ref_min <= 0.0384:
                        MJ_SAE_DAY_array.append((int(fuel_calc)* int(NCV))/ (Average_SAE))
                        Fuel_day_SAE_moist_min.append(TOTAL_ref_min)
                    else:
                        Fuel_day_SAE_moist_min.append(-1)
                elif day <= (MOIST_SAE.iloc[row_survey,5] + MOIST_SAE.iloc[row_survey,7] + MOIST_SAE.iloc[row_survey,11]): 
                    TOTAL_ref = fuel_calc /count_event_count[day] #/ MOIST_SAE.iloc[row_survey,12]
                    Fuel_day_SAE_moist.append(TOTAL_ref)
                    
                    TOTAL_ref_min = fuel_calc /Cooking_times_min[day] #/ MOIST_SAE.iloc[row_survey,12]
                    if TOTAL_ref_min <= 0.0384:
                        MJ_SAE_DAY_array.append((int(fuel_calc)* int(NCV))/ (Average_SAE))
                        Fuel_day_SAE_moist_min.append(TOTAL_ref_min)
                    else:
                        Fuel_day_SAE_moist_min.append(-1)
                elif day <= (MOIST_SAE.iloc[row_survey,5] + MOIST_SAE.iloc[row_survey,7] + MOIST_SAE.iloc[row_survey,11] + MOIST_SAE.iloc[row_survey,13]): 
                    TOTAL_ref = fuel_calc/count_event_count[day] # / MOIST_SAE.iloc[row_survey,14]
                    Fuel_day_SAE_moist.append(TOTAL_ref)

                    TOTAL_ref_min = fuel_calc /Cooking_times_min[day] #/ MOIST_SAE.iloc[row_survey,14]
                    if TOTAL_ref_min <= 0.0384:
                        MJ_SAE_DAY_array.append((int(fuel_calc)* int(NCV))/ (Average_SAE))
                        Fuel_day_SAE_moist_min.append(TOTAL_ref_min)
                    else:
                        Fuel_day_SAE_moist_min.append(-1)
                    Collection = TOTAL_ref
                    Collection_min = TOTAL_ref_min
                    
                elif day > (MOIST_SAE.iloc[row_survey,5] + MOIST_SAE.iloc[row_survey,7] + MOIST_SAE.iloc[row_survey,11] + MOIST_SAE.iloc[row_survey,13]):
                    Fuel_day_SAE_moist.append(0)
                    Fuel_dry_WHole_Phase.append(0)
                    Fuel_day_SAE_moist_min.append(0)
                #print(Fuel_day_SAE_moist)
    
    if (MOIST_SAE.iloc[row_survey,5] + MOIST_SAE.iloc[row_survey,7]) == (0 or 1):
        pump_install = Fuel_day_SAE_moist[0]
        pump_collection = Fuel_day_SAE_moist[1]

        pump_install_min = Fuel_day_SAE_moist_min[0]
        pump_collection_min = Fuel_day_SAE_moist_min[1]
    #elif (MOIST_SAE.iloc[row_survey,5] + MOIST_SAE.iloc[row_survey,7]) > DAYS_O:
    #    pump_install = 0
    else:
        pump_install = Fuel_day_SAE_moist[int((MOIST_SAE.iloc[row_survey,5] + MOIST_SAE.iloc[row_survey,7]) -2)]
        pump_collection = Fuel_day_SAE_moist[int((MOIST_SAE.iloc[row_survey,5] + MOIST_SAE.iloc[row_survey,7])-1)]

        pump_install_min = Fuel_day_SAE_moist_min[int((MOIST_SAE.iloc[row_survey,5] + MOIST_SAE.iloc[row_survey,7]) -2)]
        pump_collection_min = Fuel_day_SAE_moist_min[int((MOIST_SAE.iloc[row_survey,5] + MOIST_SAE.iloc[row_survey,7])-1)]

    if Fuel_day_SAE_moist[0] == 0:
        Collection = 0
        Collection_min = 0
    else: 
        ZERO_Erase = [i for i in Fuel_day_SAE_moist if i != 0]
        Collection = ZERO_Erase[-1]

        ZERO_Erase_min = [g for g in Fuel_day_SAE_moist_min if g != 0]
        Collection_min = ZERO_Erase_min[-1]
        
        #ZERO_Erase_Whole_Fuel = [g for g in Fuel_dry_WHole_Phase if g != 0]

    
    day_1_total_Min.append(Fuel_day_SAE_moist_min[0])
    day_2_total_Min.append(Fuel_day_SAE_moist_min[1])
    day_3_total_Min.append(Fuel_day_SAE_moist_min[2])
    day_4_total_Min.append(Fuel_day_SAE_moist_min[3])
    day_5_total_Min.append(Fuel_day_SAE_moist_min[4])
    day_6_total_Min.append(Fuel_day_SAE_moist_min[5])
    day_7_total_Min.append(Fuel_day_SAE_moist_min[6])
    day_8_total_Min.append(Fuel_day_SAE_moist_min[7])
    day_9_total_Min.append(Fuel_day_SAE_moist_min[8])
    day_10_total_Min.append(Fuel_day_SAE_moist_min[9])
    day_11_total_Min.append(Fuel_day_SAE_moist_min[10])
    day_12_total_Min.append(Fuel_day_SAE_moist_min[11])
    day_13_total_Min.append(Fuel_day_SAE_moist_min[12])
    day_14_total_Min.append(Fuel_day_SAE_moist_min[13])
    visit_1_min.append(pump_install_min)
    visit_2_min.append(pump_collection_min)
    visit_3_min.append(Collection_min)
    days_collected = []
    

    Day_1_use.append(Cooking_times_min[0])
    Day_2_use.append(Cooking_times_min[1])
    Day_3_use.append(Cooking_times_min[2])
    Day_4_use.append(Cooking_times_min[3])
    Day_5_use.append(Cooking_times_min[4])
    Day_6_use.append(Cooking_times_min[5])
    Day_7_use.append(Cooking_times_min[6])
    Day_8_use.append(Cooking_times_min[7])
    Day_9_use.append(Cooking_times_min[8])

    Day_1_Fuel.append(Fuel_dry_WHole_Phase[0])
    Day_2_Fuel.append(Fuel_dry_WHole_Phase[1])
    Day_3_Fuel.append(Fuel_dry_WHole_Phase[2])
    Day_4_Fuel.append(Fuel_dry_WHole_Phase[3])
    Day_5_Fuel.append(Fuel_dry_WHole_Phase[4])
    Day_6_Fuel.append(Fuel_dry_WHole_Phase[5])
    Day_7_Fuel.append(Fuel_dry_WHole_Phase[6])
    Day_8_Fuel.append(Fuel_dry_WHole_Phase[7])
    Day_9_Fuel.append(Fuel_dry_WHole_Phase[8])

    count_em = 0
    for a in Fuel_day_SAE_moist_min:
        #print('-------------------',a)
        if a != 0  and a != np.inf:#(a > 0.0000001 or a < 100000 or a != np.inf):
            days_collected.append(a)
            count_em = count_em + 1
    
    count_em_2 = 0
    median_dayssss_collected = np.median(days_collected)
    up_bound_mean = median_dayssss_collected + (median_dayssss_collected*0.3)
    low_bound_mean = median_dayssss_collected - (median_dayssss_collected*0.3)
    dayss_mean = []
    dayys_mean_with_zero = []

    for mm in days_collected:
        if low_bound_mean < mm < up_bound_mean:
            dayss_mean.append(mm)
            count_em_2 = count_em_2 +1
            dayys_mean_with_zero.append(mm)
        else:
            dayys_mean_with_zero.append(0)

    if count_em_2 > 0:
        mean_days_col = (sum(dayss_mean))/ count_em_2
    else:
        mean_days_col = -1
    STD_days_Col = (np.std(dayss_mean))
    mean_days_col_array.append(mean_days_col)
    STD_days_Col_array.append(STD_days_Col)
    COV_Whole.append(STD_days_Col/mean_days_col)
    if len(MJ_SAE_DAY_array) != 0:
        MJ_SAE_DAY_phase.append(sum(MJ_SAE_DAY_array)/(len(MJ_SAE_DAY_array)))
    else:
        MJ_SAE_DAY_phase.append(-1)
    days_filtered.append(len(MJ_SAE_DAY_array))
    Phase_cooking_times.append(sum(Cooking_times_min))


    days_counted.append((count_em))
    MINUTESSSS= np.arange(0, len(metric_day_data.iloc[:,0]), 1)
    graph_me = {'minutes': MINUTESSSS, 'raw': metric_day_data.iloc[:,0], 'filters removal':Fuel_removal, 'mean run':Fuel_running_mean}
    dfgraphsss = pd.DataFrame(graph_me,columns=['minutes','raw','filters removal', 'mean run'])
    #dfgraphsss.to_csv("D:/ALGORITHM-TEST/tester_avg_spread_"+str(min_average_spread)+"__"+str(id_number)+"_.csv", index=False,mode='a')
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

print('are the lengths real------', len(SAE_PHase), len(PHASE_24_HR_AVG) )
HH_fuel_SAE_Moist_min = {'Household': HH_NUMBER_Min,'Days counted':days_counted ,'24hr Avg _m':PHASE_24_HR_AVG,'Fuel Removed For Phase (24h hour Sprints)':fuel_removed_for_phase, 'avg SAE for Phase': SAE_PHase,'MJ/SAE/day for phase':MJ_SAE_DAY,'MJ/SAE(breakdown)/day for phase Filtered': MJ_SAE_DAY_phase,
                         'Days that were filtered':days_filtered,
                         'Time Cooked':Phase_cooking_times,'Fuel Scale':fuel_scle_value,'COV':COV_Whole,'mean':mean_days_col_array, 'std':STD_days_Col_array,  
                           'Day 1 min': day_1_total_Min,
                           'Day 2 min': day_2_total_Min,
                           'Day 3 min': day_3_total_Min,
                           'Day 4 min': day_4_total_Min,
                           'Day 5 min': day_5_total_Min,
                           'Day 6 min': day_6_total_Min,
                           'Day 7 min': day_7_total_Min, 
                           'Day 8 min': day_8_total_Min,
                           'Day 9 min': day_9_total_Min,
                           'Day 10 min': day_10_total_Min,
                           'Day 11 min': day_11_total_Min,
                           'Day 12 min': day_12_total_Min,
                           'Day 13 min': day_13_total_Min,'Day 14min': day_14_total_Min,
                           'Visit 1 min': visit_1_min , 'Visit 2 min': visit_2_min , 'Visit 3 min':visit_3_min }

df_HH_fuel_SAE_Moist_breakdown_min = pd.DataFrame(HH_fuel_SAE_Moist_min,columns=['Household','Days counted' ,'24hr Avg _m','Fuel Removed For Phase (24h hour Sprints)', 'avg SAE for Phase','MJ/SAE/day for phase','MJ/SAE(breakdown)/day for phase Filtered','Days that were filtered','Time Cooked', 'Fuel Scale','COV','mean', 'std','Day 1 min','Day 2 min',
                                                                           'Day 3 min','Day 4 min','Day 5 min', 
                                                                           'Day 6 min','Day 7 min','Day 8 min',
                                                                           'Day 9 min','Day 10 min','Day 11 min',
                                                                           'Day 12 min','Day 13 min','Day 14 min','Visit 1 min', 'Visit 2 min', 'Visit 3 min' ])
print(df_HH_fuel_SAE_Moist_breakdown_min.iloc[:,4:16])
if Computer == 'work':
    HH_SAE_moist_breakdown_file_path_minute = "D:/1N_Minute_for 24_Household_SAE_Moist_breakdown.csv"
    Fuel_24_hour_file_path = "D:/1N_24_hour_Fuel_removal.csv"
#    HH_breakdown_file_path = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+ Phase +"/"+Phase+"_Household_Fuel_removal_breakdown" +".csv"
#    HH_SAE_moist_breakdown_file_path = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+ Phase +"/"+Phase+"_Household_SAE_Moist_breakdown" +".csv"
else:
    Fuel_24_hour_file_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase +"/"+Phase+"_24_hour_Fuel_removal" +".csv"
#
    HH_SAE_moist_breakdown_file_path_minute = "C:/Users/gvros/Desktop/"+Phase+"_Min_filter_for_24_Household_Moist_CE_breakdown.csv"
#
#df_Fuel_per_24_hour.to_csv(Fuel_24_hour_file_path,index=False,mode='a')
df_HH_fuel_SAE_Moist_breakdown_min.to_csv(HH_SAE_moist_breakdown_file_path_minute, index=False,mode='a')
#print('day sum bull shit and cokign times ', day_sum_fuel[4], Cooking_times_min[4], MOIST_SAE.iloc[Household_count,8], day_1_total_Min,
     # ((day_sum_fuel[4]/(1.16))/MOIST_SAE.iloc[34,6]/Cooking_times_min[4]), int(id_number), type(id_number) )

FUEL_breakdown = {'Household':HH_NUMBER,'day 1': Day_1_use,'day 2': Day_2_use,'day 3': Day_3_use,'day 4': Day_4_use,
                  'day 5': Day_5_use,'day 6': Day_6_use,'day 7': Day_7_use,'day 8': Day_8_use,
                  'day 9': Day_9_use}

USe_breakdown = {'Household':HH_NUMBER, 'day 1': Day_1_Fuel,'day 2': Day_2_Fuel,'day 3': Day_3_Fuel,'day 4': Day_4_Fuel,
                  'day 5': Day_5_Fuel,'day 6': Day_6_Fuel,'day 7': Day_7_Fuel,'day 8': Day_8_Fuel,
                  'day 9': Day_9_Fuel}

df_fuel = pd.DataFrame(FUEL_breakdown,columns=['Household','day 1','day 2',
                                                                           'day 3','day 4','day 5',
                                                                           'day 6','day 7','day 8',
                                                                           'day 9'])

df_use = pd.DataFrame(USe_breakdown,columns=['Household','day 1','day 2',
                                                                           'day 3','day 4','day 5',
                                                                           'day 6','day 7','day 8',
                                                                           'day 9'])

path = "C:/Users/gvros/Desktop/My_algo_Fule_Time.csv"

#print(df_use)
df_fuel.to_csv(path, index=False,mode='a')
df_use.to_csv(path, index=False,mode='a')