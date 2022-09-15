import os
import pandas as pd
import numpy as np
import csv
import glob
from datetime import datetime
from csv import reader
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import Functions_malawi

#HH1 has a file error

Household_Number = 'HH2' #input("HH1 or HH2... etc:  ")
Source = 'laptop' #input("laptop or Work: ")  # 'work' or 'laptop'
KPT_NUM = '1'

if Source == 'laptop':
    USB_D = 'D'
else:
    USB_D = 'E'

# sorting out the missing data
Beacon = True 
USB = True
Hapex = True
Exact = True

if Household_Number == '5':
    Fuel = False

    #USB+":/Malawi 1.1/"+Household+"/S- "+Stove+"; CCT-"+CCT_Num
KPT_Stove_Path = USB_D+":/Malawi 1.1/"+Household_Number+"/KPT/KPT - "+KPT_NUM
l_files = os.listdir(KPT_Stove_Path)

for file in l_files:
    file_path = f'{KPT_Stove_Path}\\{file}'
    if file[0:2] == "HH":# and file[1] == "H":
        print('here is the file', file)
        I_H_File = os.getcwd()
        I_H_open = glob.glob((file_path))
        for files in I_H_open:
            with open(files, 'r') as f:
                csv_reader = csv.reader(f)
                for idx, row in enumerate(csv_reader):
                    if 'Stove Name:' in row and Exact == True:
                        Exact_1 = row[1][6:]
                        Exact_2 = row[2][6:]
                    elif 'PM measurement location:' in row and Hapex == True:
                        #HAPEx_summary = pd.read_csv(file_path, skiprows= (idx))
                        for g in row[1]:
                            if g == 'c':
                               Cook_Hapex = row[1]
                               Kitchen_Hapex = row[2]
                            elif g == 'k':
                                Cook_Hapex = row[2]
                                Kitchen_Hapex = row[1]
                    elif 'Fuel type:' in row and Fuel == True:
                        Fuel_name = pd.read_csv(file_path, skiprows= (idx))
                        Fuel_1 = USB_summary.iloc[1:0]
                        Fuel_2 = USB_summary.iloc[2:0]
                        print('fuel names', Fuel_1, )
                    elif 'Location: ' in row and USB == True:
                        USB_summary = pd.read_csv(file_path, skiprows= (idx))
                        USB_name = USB_summary.iloc[1:0]
                        print(USB_name)

                    elif 'Timestamp' in row:
                        Inline_hapex_csv = pd.read_csv(file_path, skiprows= (idx))
                        I_Hap_Time = (Inline_hapex_csv.iloc[:,0])
                        Day_date = Inline_hapex_csv.iloc[0,0][0:10]
                        Inline_Hap_Comp = Inline_hapex_csv.iloc[:,1]
                        Inline_Hap_PM = Inline_hapex_csv.iloc[:,2]

                     