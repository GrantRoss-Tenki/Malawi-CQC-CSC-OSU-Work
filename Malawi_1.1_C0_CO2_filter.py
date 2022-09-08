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


Source = 'laptop' #input("laptop or Work: ")  # 'work' or 'laptop'
Household = 'HH1' #input("HH1 or HH2... etc:  ")
Stove = '1'#input("1 = TSF, 2 = CQC, 3 = JFK:  ")
CCT_Num = '1'#input("1, 2, or 3: ")

if Source == 'laptop':
    USB = 'D'
else:
    USB = 'E'


CCT_Stove_Path = USB+":/Malawi 1.1/"+Household+"/S- "+Stove+"; CCT-"+CCT_Num
l_files = os.listdir(CCT_Stove_Path)

for file in l_files:

    file_path = f'{CCT_Stove_Path}\\{file}'
    print(file,file_path, file[0] )
    if file[0] == "H":
        if (file[6:10] == '1577') or (file[6:10] == '1558') or (file[6:10] == '3275'):
            Inline_hapex_name = 'HAPEx '+ file[6:10]
            I_H_File = os.getcwd()
            I_H_open = glob.glob((file_path))
            for files in I_H_open:
                with open(files, 'r') as f:
                    csv_reader = csv.reader(f)
                    for idx, row in enumerate(csv_reader):
                        if 'Timestamp' in row:
                            Inline_hapex_csv = pd.read_csv(file_path, skiprows= (idx))
                            I_Hap_Time = Inline_hapex_csv.iloc[:,0]
                            Day_date = Inline_hapex_csv.iloc[0,0][0:10]
                            Inline_Hap_Comp = Inline_hapex_csv.iloc[:,1]
                            Inline_Hap_PM = Inline_hapex_csv.iloc[:,2]
        elif file[1] == "H":
            print('Household')
            #Whole_Household_CSV = pd.read_csv(file_path)
        else:
            Cook_hapex_name = 'HAPEx '+ file[6:10]
            C_H_File = os.getcwd()
            C_H_open = glob.glob((file_path))
            for files in C_H_open:
                with open(files, 'r') as f:
                    csv_reader = csv.reader(f)
                    for idx, row in enumerate(csv_reader):
                        if 'Timestamp' in row:
                            Cook_hapex_csv = pd.read_csv(file_path, skiprows= (idx))
                            C_Hap_Time = Cook_hapex_csv.iloc[:,0]
                            Cook_Hap_Comp = Cook_hapex_csv.iloc[:,1]
                            Cook_Hap_PM = Cook_hapex_csv.iloc[:,2]
            print('Cook hapex: ', Cook_hapex_name)

    elif file[0] == "B":
        Cook_Beacon_name = 'Beacon ' + file[7:11]
        C_Beacon_File = os.getcwd()
        C_Beacon_open = glob.glob((file_path))
        for files in C_Beacon_open:
            with open(files, 'r') as f:
                csv_reader = csv.reader(f)
                for idx, row in enumerate(csv_reader):
                    if 'Timestamp' in row:
                        Cook_Beacon_csv = pd.read_csv(file_path, skiprows=(idx))
                        C_Hap_Time = Cook_Beacon_csv.iloc[:, 0]
                        Cook_Beacon_Move= Cook_Beacon_csv.iloc[:, 1]
                        Cook_Beacon_Accel = Cook_Beacon_csv.iloc[:, 2]
        print('Beacon: ', Cook_Beacon_name)
    elif file[0] == 'U':
        USB_name = 'USBLog ' + file[7:11]
        USB_File = os.getcwd()
        USB_open = glob.glob((file_path))
        for files in USB_open:
            with open(files, 'r') as f:
                csv_reader = csv.reader(f)
                for idx, row in enumerate(csv_reader):
                    if 'Timestamp' in row:
                        USB_CSV = pd.read_csv(file_path, skiprows=(idx))
                        USB_Time = USB_CSV.iloc[:, 0]
                        USB_Battery = USB_CSV.iloc[:, 1]
                        USB_Current = USB_CSV.iloc[:, 2]
                        USB_Voltage = USB_CSV.iloc[:, 3]
                        USB_Power = USB_CSV.iloc[:, 4]
                        USB_Energy  = USB_CSV.iloc[:, 5]
                        USB_Usage = USB_CSV.iloc[:, 6]
                        USB_Proximity_DF = pd.DataFrame(USB_CSV.iloc[:, 6:])
        print('USB: ', USB_name)
    elif file[0] == 'G':
        Gas_name = 'GasSense ' + file[9:13]
        Gas_File = os.getcwd()
        Gas_open = glob.glob((file_path))
        for files in C_Beacon_open:
            with open(files, 'r') as f:
                csv_reader = csv.reader(f)
                for idx, row in enumerate(csv_reader):
                    if 'Timestamp' in row:
                        Gas_csv = pd.read_csv(file_path, skiprows=(idx))
                        Gas_Time = Gas_csv.iloc[:, 0]
                        Gas_Battery = Gas_csv.iloc[:, 1]
                        Gas_CO2 = Gas_csv.iloc[:, 2]
                        Gas_CO = Gas_csv.iloc[:, 3]
                        Gas_Termal = Gas_csv.iloc[:, 4]
                        Gas_T_Bosh = Gas_csv.iloc[:, 5]
                        Gas_T_Sen = Gas_csv.iloc[:, 6]
                        Gas_Pressure = Gas_csv.iloc[:, 7]
                        Gas_RH = Gas_csv.iloc[:, 8]
        print('GASSS: ', Gas_name)


print('Task finished!')