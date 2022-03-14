# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 09:33:11 2022

@author: rossgra
"""

import pandas as pd
import numpy as np
import csv
import glob
import os


Phase = "1H"
Computer = "personal"

if Computer == "work":
    USB = "D"
    os.chdir("C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+ Phase +"/Compiler_1_exact/Raw_Day/Raw_D_metrics")
else:
    os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_1_exact/Raw_D_metrics")
    USB = "E"
    
Pump_Fuel_path = os.getcwd()
csv_Fuel = glob.glob(os.path.join(Pump_Fuel_path, "*.csv"))
HH_count = []
Fuel_Removed_for_24_Hours = []
for file in csv_Fuel:
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        for idx, row in enumerate(csv_reader):
            if idx == 1:
                ID_Number = row[1]
                print(ID_Number)
            elif 'Fuel Raw Data' in row:
                data_start = idx
                
    sensor_data = pd.read_csv(file, skiprows=data_start)
    Fuel_removal = sensor_data.iloc[:, 1]
    #print(len(Fuel_removal), type(Fuel_removal))
    Pump_Metrics_path = USB+ ":/24_hour_pump/"+Phase+"/Pump metrics_"+Phase+"_.csv"
    Pump_information = pd.read_csv(Pump_Metrics_path,delimiter = ',')
    
    #print('hhPump', (Pump_information.iloc[1,1])+(Pump_information.iloc[1,4]))
    HH_pump = Pump_information.iloc[:,0]
    fuel_removal_pump = []
    for num, hh_pump in enumerate(HH_pump):
        
        if hh_pump == int(ID_Number):
            print(ID_Number,'did my numbers start right', Pump_information.iloc[num,1])
            for tv, pump_removal in enumerate(Fuel_removal):
                High_bar = (Pump_information.iloc[num,1] + Pump_information.iloc[num,4])
                if (Pump_information.iloc[num,1]) <= tv <= High_bar:
                    if (pump_removal != -1) and (Pump_information.iloc[num,1] != -1):
                        
                        if (len(Fuel_removal) -1 >= High_bar):
                            if (pump_removal != Fuel_removal[tv+1]):
                                #print('this is high bar:   ',len(Fuel_removal), High_bar)
                                fuel_removal_pump.append(pump_removal)
                                count_tv = tv
                        else:
                            if tv == (len(Fuel_removal) - 1):
                                count_tv = tv
                                break
                            elif (pump_removal != Fuel_removal[tv+1]):
                                #print('this is high bar:   ', High_bar)
                                fuel_removal_pump.append(pump_removal)
                                count_tv = tv
            
    
    print('length of fuel Removal',len(fuel_removal_pump))
    HH_count.append(ID_Number)
    if len(fuel_removal_pump) != 0:  
        if Fuel_removal[count_tv] != fuel_removal_pump[-1]:
            fuel_removal_pump.append(Fuel_removal[count_tv])
        print(count_tv, fuel_removal_pump[-1], Fuel_removal[count_tv])
        Fuel_Removed_for_24_Hours.append(sum(fuel_removal_pump))
    else:
        Fuel_Removed_for_24_Hours.append(-1)

print('-------------------gimmie the lengths----------', len(HH_count), len(Fuel_Removed_for_24_Hours))

DATA_FRame_PUMP = {'Household': HH_count, 'Fuel Removed for Pump Installation (kg)' : Fuel_Removed_for_24_Hours}
d_f_P_24 = pd.DataFrame(DATA_FRame_PUMP, columns=['Household','Fuel Removed for Pump Installation (kg)'])

Path_3 = USB+":/24_hour_pump/"+Phase+"/Fuel_24_hr_pump_"+Phase+"_.csv"
d_f_P_24.to_csv(Path_3, index= False, mode='a')