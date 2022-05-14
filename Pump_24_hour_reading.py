# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 15:27:13 2022

@author: rossgra
"""

import itertools
import os
import pandas as pd
import numpy as np
import csv
import glob
from datetime import datetime


Phase  = "3H"
computer = "personal"

if computer == "work":
    USB = "D"
    os.chdir("C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+ Phase +"/Collection")
else:
    os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Collection")
    USB = "E"

Day_met_path = os.getcwd()
csv_R_m = glob.glob(os.path.join(Day_met_path, "*.csv"))

Household_pump_metric = []
Kitchen_Hapex_average = []
Cook_Hapex_average = []
Liters_pumped = []
Time_pumped = []
Cook_Hapex_sensor = []
Kit_Hapex_sensor = []
Fuel_Hapex_sensor = []
Exact_1_sensor = []
Exact_2_sensor = []
time_value_start = []

First_Stove = False
#Cook_Hapex_sensor.append(Cook_HAPEx)
    #Kit_Hapex_sensor.append(Kitchen_HAPEx)
    #Fuel_Hapex_sensor.append(Fuel)
    #Exact_1_sensor.append(EXACT_1)

    #Cook_Hapex_sensor.append(Cook_HAPEx)
for file in csv_R_m:
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        for idx, row in enumerate(csv_reader):
            if 'Household ID:' in row:
                ID_Number = row[1]
                print(ID_Number)
                Household_pump_metric.append(ID_Number)
            elif 'Stove Name:' in row:
                EXACT_1 = row[1]
                Exact_1_sensor.append(EXACT_1)
                First_Stove = True
                
                if row[2] != '':
                    print(len(row))
                    print('this is the exact value', row[2])
                    second_stove = True
                    EXACT_2 = row[2]
                else:
                    second_stove = False
            elif 'PM measurement location:' in row:
                for q in row[1]:
                    if len(row) < 2:
                        break
                    elif q == 'k':
                        Kitchen_HAPEx = row[1]
                        Kit_Hapex_sensor.append(Kitchen_HAPEx)
                        Kit_hapex_sensor = ''
                        for letter, k in enumerate(Kitchen_HAPEx):
                            if letter >= 14:
                                Kit_hapex_sensor = Kit_hapex_sensor + k
                        Cook_HAPEx = row[2]
                        Cook_Hapex_sensor.append(Cook_HAPEx)
                        Cook_hapex_sensor = ''
                        for letter, c in enumerate(Cook_HAPEx):
                            if letter >= 11:
                                Cook_hapex_sensor = Cook_hapex_sensor + c
                    else:
                        Cook_HAPEx = row[1]
                        Cook_Hapex_sensor.append(Cook_HAPEx)
                        Cook_hapex_sensor = ''
                        for letter, c in enumerate(Cook_HAPEx):
                            if letter >= 11:
                                Cook_hapex_sensor = Cook_hapex_sensor + c
                        Kitchen_HAPEx = row[2]
                        Kit_Hapex_sensor.append(Kitchen_HAPEx)
                        Kit_hapex_sensor = ''
                        for letter, k in enumerate(Kitchen_HAPEx):
                            if letter >= 14:
                                Kit_hapex_sensor = Kit_hapex_sensor + k
                
                    print('cook?', Cook_HAPEx,Cook_hapex_sensor )
                    print('Kitchen?', Kitchen_HAPEx, Kit_hapex_sensor)
                    break
            elif 'Fuel type:' in row:
                if len(row) < 2:
                    Fuel_Sensor = False
                    print('NO FUEL Senor')
                    
                    break
                else:
                    Fuel = row[1]
                    Fuel_Hapex_sensor.append(Fuel)
                    Fuel_sensor = ''
                    for letter, f in enumerate(Fuel):
                            if letter >= (14):
                                Fuel_sensor = Fuel_sensor + f
                    print('Fuel Sensor', Fuel_sensor)
            elif 'Timestamp' in row:
                count_one_exact_usage = 0
                for col, sensor in enumerate(row):
                    word_count = 0
                    if row[col].find('Battery') == 8:
                        Pump_col = np.arange(col, col + 9, 1)
                    elif row[col].find('kitchen Compliance') == 0:
                        Kit_comp_col = col
                    elif row[col].find('kitchen PM') == 0:
                        kit_pm_col = col
                    elif row[col].find('cook Compliance') == 0:
                        cool_com_col = col
                    elif row[col].find('cook PM') == 0:
                        cool_pm_col = col
                    elif row[col].find('FUEL') == (13 or 12):
                        fuel_col = col
                    elif (row[col].find('CQC') == 0) or (row[col].find('3') == 0):
                        if second_stove == True and count_one_exact_usage >= 2 and (row[col].find('Second') == 0):
                            exact_usage_col_2 = 8
                            count_one_exact_usage = count_one_exact_usage + 1
                            if count_one_exact_usage >= 3:
                                exact_tem_col_2 = 9
                                print('-------------------------- second exact at this hh', ID_Number)
                        else:
                            exact_usage_col = col
                            count_one_exact_usage = count_one_exact_usage + 1
                            if count_one_exact_usage >= 1:
                                count_one_exact_usage = count_one_exact_usage + 1
                                exact_usage_col = exact_usage_col - 1
                                exact_tem_col = col
                                
                         
                    data_start = idx
                break

    WHOLE_FILE = pd.read_csv(file, skiprows=data_start)
    #print('------------- gimmmeee the exact array-------------', len()
    if WHOLE_FILE.iloc[1,exact_usage_col] == 'NO EXACT':
        No_exact = 1
    else:
        No_exact = 0
        
    os.chdir(USB+":/PUMP FILES/"+ Phase +"/UPump")
    UPump_path = os.getcwd()
    
    upump_m = glob.glob(os.path.join(UPump_path, "*.csv"))
    
    for file in upump_m:
        with open(file, 'r') as j:
            csv_reader_2 = csv.reader(j)
            for idxx, rrow in enumerate(csv_reader_2):
                if 'Household ID:' in rrow:
                    id_number = (rrow[1])
                elif 'Start time:' in rrow:
                    Time_start = rrow[1]
        if id_number == ID_Number:
            failed_uPump = False
            break
        else:
            failed_uPump = True
            pass

    if failed_uPump == True:
        Kitchen_Hapex_average.append(-1)
        Cook_Hapex_average.append(-1)
        Time_pumped.append(-1)
        time_value_start.append(-1)
        Exact_2_sensor.append(-1)
        continue

    if Phase == ("1H")  or Phase == "1N" or Phase == "2N":
        print('is the failed pump true or flase:', failed_uPump)
        Pump_Household_information = USB +":/PUMP FILES/"+Phase+"_Compress_SN.csv"
        Pump_Times = pd.read_csv(Pump_Household_information, delimiter= ',')
        
        non_24_hour_times = Pump_Times.iloc[:, 3]
        HH_non_24_hour_times = Pump_Times.iloc[:, 0]
        for nym,hh in enumerate(HH_non_24_hour_times):
            
            if hh == int(ID_Number):
                print('comon i am so done',nym,hh, (ID_Number))
                time_length = int(non_24_hour_times[nym])
                break
            elif nym+1 == len(HH_non_24_hour_times):
                time_length = 1440
    else:
        time_length = 1440
        
    if (Phase  == ("2N") or Phase == "2H") and (int(ID_Number) == 1003 or int(ID_Number) == 2012):
        print('------------------------- why oh why--------------------')
        #if int(ID_Number) == (1003 or 2012 or 2212):
        print('-----------------------',int(ID_Number),'--------------------')
        formattt = datetime.strptime(Time_start, "%m/%d/%Y %H:%M")
        time_start_format_1 = formattt.strftime("%Y-%m-%d %H:%M")
        time_start_format_2 = formattt.strftime("%m/%d/%Y %H:%M")
    elif (Phase  == ("4N")) and (int(ID_Number) == 1034):
        formattt = datetime.strptime(Time_start, "%Y-%m-%d %H:%M:%S")
        time_start_format_1 = formattt.strftime("%Y-%m-%d %H:%M")
        time_start_format_2 = formattt.strftime("%m/%d/%Y %H:%M")
    else:
        formattt = datetime.strptime(Time_start, "%Y-%m-%d %H:%M:%S")
        time_start_format_1 = formattt.strftime("%Y-%m-%d %H:%M")
        time_start_format_2 = formattt.strftime("%m/%d/%Y %H:%M")
    
    Time_Whole_File = list(WHOLE_FILE.iloc[:,0])
    dformat = ("%m/%d/%Y %H:%M","%Y-%m-%d %H:%M:%S")
    time_of_clean_phase_file = []
    day_of_clean_phase_file = []
    minute_of_clean_phase_file = []
    tv = 0
    for a in Time_Whole_File:
        tv = 0
        for i in dformat:
            #print(tv)
            try:
                 formatarray = datetime.strptime(a, i)#.strftime(i)
                 if tv == 0:
                     day_of_clean_phase_file.append(formatarray.day)
                     minute_of_clean_phase_file.append(formatarray.minute)
                 tv = tv + 1
            except ValueError: 
                pass
        arrayTime = formatarray.strftime("%m/%d/%Y %H:%M")
        time_of_clean_phase_file.append(arrayTime)
        if arrayTime == (time_start_format_2 or time_start_format_1):
            
            pass
    
    Hapex_start_kit_value = -1
    count = 0
    for clean in time_of_clean_phase_file:
        #print(clean,time_start_format_2)
        if clean == time_start_format_2:
            Hapex_start_kit_value = count
        elif clean == time_start_format_1:
            Hapex_start_kit_value = count

        count = count +1
    
    if Hapex_start_kit_value == -1:
        if formattt.day == day_of_clean_phase_file[1]:
            if (minute_of_clean_phase_file[1] - formattt.minute) < 61:
                Hapex_start_kit_value = minute_of_clean_phase_file[1] - formattt.minute

#    for date, a in enumerate(time_of_clean_phase_file):
#                if date == 3:
#                    if a > pump_start_date:
#                        Hapex_start_kit_value = -1

    #Hapex_start_kit_value = tv
    #print('---this is non -------', Hapex_start_kit_value ,'--------',time_length,'------------------')
    #print('---this is non -------', exact_usage_col ,'--------',exact_tem_col,'------------------')
    
    PM_pump_time_kit = []
    Count_Day_ahead =Hapex_start_kit_value + time_length + 1
    for pm in WHOLE_FILE.iloc[Hapex_start_kit_value:Count_Day_ahead,kit_pm_col]:
        if Hapex_start_kit_value != -1:
            PM_pump_time_kit.append(pm)
        else:
            PM_pump_time_kit.append(-1)
    
    PM_pump_time_cook = []
    for pm in WHOLE_FILE.iloc[Hapex_start_kit_value:Count_Day_ahead,cool_pm_col]:
        if Hapex_start_kit_value != -1:
            PM_pump_time_cook.append(pm)
        else:
            PM_pump_time_cook.append(-1) 
    print('------ stove name -----',First_Stove )   
    print('---Pumo Day start',Hapex_start_kit_value, Count_Day_ahead,len(WHOLE_FILE.iloc[:,exact_usage_col]))

    if First_Stove == True:
        
        usage_array = []
        for use in (WHOLE_FILE.iloc[Hapex_start_kit_value:Count_Day_ahead,exact_usage_col]):
            #if Hapex_start_kit_value != -1:
                usage_array.append(use)
        
        temp_aray = []
        for temp in (WHOLE_FILE.iloc[Hapex_start_kit_value:Count_Day_ahead,exact_tem_col]):
            #if Hapex_start_kit_value != -1:
                temp_aray.append(temp)
    else:
        usage_array.append(-1)
        temp_aray.append(-1)
    usage_array_2 = []
    temp_aray_2 = []
    if second_stove == True:
        if Phase == "4N" and int(ID_Number) == 1010:
            for use in (WHOLE_FILE.iloc[Hapex_start_kit_value:-1,8]):
                #if Hapex_start_kit_value != -1:
                    usage_array_2.append(use)
        else:
            for use in (WHOLE_FILE.iloc[Hapex_start_kit_value:Count_Day_ahead,8]):
                #if Hapex_start_kit_value != -1:
                    usage_array_2.append(use)
        
        
        for temp in (WHOLE_FILE.iloc[Hapex_start_kit_value:Count_Day_ahead,9]):
            #if Hapex_start_kit_value != -1:
                temp_aray_2.append(temp)
                
    print(kit_pm_col, type(kit_pm_col))
    print(len(WHOLE_FILE.iloc[:,5]))
    #print('----------',(Hapex_start_kit_value),len(temp_aray),time_length,(Count_Day_ahead), Count_Day_ahead-Hapex_start_kit_value,' ---------------')
    
    #print('-----------Fire Finder Start ---------------')
    df_1 = {'Exact 1 Usage':usage_array, 'Exact 1 Temp':temp_aray}
    FF_1 = pd.DataFrame(df_1, columns=['Exact 1 Temp','Exact 1 Usage'] )
    Path_1 = USB+":/24_hour_pump/"+Phase+"/Raw_pump_Time/Exact_1_"+ID_Number+"_"+Phase+"_.csv"
    FF_1.to_csv(Path_1, index= False, mode='a')
    
    df_2 = {'Exact 2 Usage':usage_array_2, 'Exact 2 Temp':temp_aray_2}
    FF_2 = pd.DataFrame(df_2, columns=['Exact 2 Temp','Exact 2 Usage'])
    Path_2 = USB+":/24_hour_pump/"+Phase+"/Raw_pump_Time/Second_stove/Exact_2_"+ID_Number+"_"+Phase+"_.csv"
    FF_2.to_csv(Path_2, index= False, mode='a')
    
    
    #Household_pump_metric.append(ID_Number)
    Kitchen_Hapex_average.append(np.average([float(a) for a in PM_pump_time_kit]))
    Cook_Hapex_average.append(np.average([float(a) for a in PM_pump_time_cook]))
    Time_pumped.append(time_length)
    #Cook_Hapex_sensor.append(Cook_HAPEx)
    #Kit_Hapex_sensor.append(Kitchen_HAPEx)
    #Fuel_Hapex_sensor.append(Fuel)
    #Exact_1_sensor.append(EXACT_1)
    time_value_start.append(Hapex_start_kit_value)
    
    if second_stove == True:
        Exact_2_sensor.append(EXACT_2)
    else:
        Exact_2_sensor.append(-1)
    print('lengths of arrays hh, pump tv, kit hap, cook hap, time pumped, sensor, exact 2',len(Household_pump_metric),
          len(time_value_start),len(Kitchen_Hapex_average),len(Cook_Hapex_average),len(Time_pumped), len(Fuel_Hapex_sensor), len(Exact_2_sensor)  )


df_3 = {'Household':Household_pump_metric, 'Start Time Value for Pump install':time_value_start,
        'Kitchen_Hapex_average ':Kitchen_Hapex_average,
        'Cook Hapex Average':Cook_Hapex_average,
        'Time Pumped':Time_pumped,'Cook Hapex Sensor':Cook_Hapex_sensor, 'Kitchen Hapex Sensor':Kit_Hapex_sensor,
        'Fuel Sensor':Fuel_Hapex_sensor, 
        'Exact 1 Sensor':Exact_1_sensor, 'Exact 2 Sensor':Exact_2_sensor}
FF_3 = pd.DataFrame(df_3, columns=['Household','Start Time Value for Pump install','Kitchen_Hapex_average ','Cook Hapex Average',
                                   'Time Pumped','Cook Hapex Sensor','Kitchen Hapex Sensor','Fuel Sensor','Exact 1 Sensor','Exact 2 Sensor'])

Path_3 = USB+":/24_hour_pump/"+Phase+"/pump metrics_"+Phase+"_.csv"
#FF_3.to_csv(Path_3, index= False, mode='a')