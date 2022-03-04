# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 16:08:40 2022

@author: rossgra
"""
import pandas as pd
import numpy as np
import csv
import os
import glob


Phase = "1H"
Computer = "personal"
if Computer == 'work':
    os.chdir("C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+Phase +"/Collection")

else:
    if Phase == "1H":
        os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+ Phase +"/Collection With first two days")
    else:
        os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+ Phase +"/Collection")

Kitchen_HAPEx = os.getcwd()
Kit_csv_open = glob.glob(os.path.join(Kitchen_HAPEx, "*.csv"))

count = 0
for file in Kit_csv_open:
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        for idx, row in enumerate(csv_reader):
            if 'Household ID:' in row:
                id_number = (row[1])
                #print('Household',id_number)
            elif 'Total number of logs:' in  row:
                number_of_days = int(row[1])/(24*60)
            elif 'Timestamp' in row:
                Fueltype = row[1]
                Exact = row[3]
                Usage = row[2]
                K_hapex = row[5]
                C_hapex = row[7]
                data_start = idx
                
    Sensor_Data = pd.read_csv(file, skiprows=data_start)
    
    Time_array = Sensor_Data.iloc[:,0]
    dataframe_1 = pd.DataFrame({id_number: Time_array})
    

    if Computer == 'work':
        Time_array_path = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+ Phase +"/Time_list/"+Phase+"_"+id_number+"_time_array.csv"
    
    
    else:
        Time_array_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase +"/Time_list/"+Phase+"_"+id_number+"_time_array.csv"
  
    dataframe_1.to_csv(Time_array_path,index=False,mode='a')