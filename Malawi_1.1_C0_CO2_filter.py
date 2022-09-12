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

HH_Number_array = ['HH1', 'HH2', 'HH3', 'HH4', 'HH5','HH6']
Stove_array = ['1','2','3']
CCT_array = ['1','2','3', '4']

Source = 'laptop' #input("laptop or Work: ")  # 'work' or 'laptop'
Household = 'HH4' #input("HH1 or HH2... etc:  ")
Stove = '3'#input("1 = TSF, 2 = CQC, 3 = JFK:  ")
CCT_Num = '1'#input("CCT Number - 1, 2, or 3: ")
Running_Average_length = 8#int(input(" Enter Number for running length (8 would be ~ half a minute):  "))
if Source == 'laptop':
    USB = 'D'
else:
    USB = 'E'
# getting the metrics and times
CCT_TIMES_METRICS = pd.read_csv(USB+":/Malawi 1.1 CCT Fire Start Times.csv")
identifyer = Household+' - CCT-'+ CCT_Num
if Stove == '1':
    for rows, name in enumerate(CCT_TIMES_METRICS.iloc[:,0]):
        if name == identifyer:
            Fire_Start = CCT_TIMES_METRICS.iloc[rows,1]
            Fuel_change = CCT_TIMES_METRICS.iloc[rows,2]
            Fuel_MJ = CCT_TIMES_METRICS.iloc[rows, 3]
            Boil_time = CCT_TIMES_METRICS.iloc[rows, 4]
            Coking_Length = CCT_TIMES_METRICS.iloc[rows, 5]
if Stove == '2':
    for rows, name in enumerate(CCT_TIMES_METRICS.iloc[:,6]):
        if name == identifyer:
            Fire_Start = CCT_TIMES_METRICS.iloc[rows,7]
            Fuel_change = CCT_TIMES_METRICS.iloc[rows,8]
            Fuel_MJ = CCT_TIMES_METRICS.iloc[rows, 9]
            Boil_time = CCT_TIMES_METRICS.iloc[rows, 10]
            Coking_Length = CCT_TIMES_METRICS.iloc[rows, 11]
if Stove == '3':
    for rows, name in enumerate(CCT_TIMES_METRICS.iloc[:,12]):
        if name == identifyer:
            Fire_Start = CCT_TIMES_METRICS.iloc[rows,13]
            Fuel_change = CCT_TIMES_METRICS.iloc[rows,14]
            Fuel_MJ = CCT_TIMES_METRICS.iloc[rows, 15]
            Boil_time = CCT_TIMES_METRICS.iloc[rows, 16]
            Coking_Length = CCT_TIMES_METRICS.iloc[rows, 17]


CCT_Stove_Path = USB+":/Malawi 1.1/"+Household+"/S- "+Stove+"; CCT-"+CCT_Num
l_files = os.listdir(CCT_Stove_Path)

for file in l_files:

    file_path = f'{CCT_Stove_Path}\\{file}'
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
                            print('inline')
                            Inline_hapex_csv = pd.read_csv(file_path, skiprows= (idx))
                            I_Hap_Time = (Inline_hapex_csv.iloc[:,0])
                            Day_date = Inline_hapex_csv.iloc[0,0][0:10]
                            Inline_Hap_Comp = Inline_hapex_csv.iloc[:,1]
                            Inline_Hap_PM = Inline_hapex_csv.iloc[:,2]
                            for tv, f in enumerate(I_Hap_Time):
                                if f[11:16] == Fire_Start[9:] or str(f[10:16]) == Fire_Start[10:]:
                                    Inline_Hapex_FIRE_START_TV = tv
                                    break
        elif file[1] == "H":
            print('Household')
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
                            #print('TEEESTER', str(C_Hap_Time[0][11:16]),Fire_Start[9:] )
                            for tv, f in enumerate(C_Hap_Time):
                                if f[9:16] == Fire_Start[9:] or str(f[11:16]) == Fire_Start[10:] or str(f[11:16]) == Fire_Start[9:]:
                                    Cook_hapex_FIRE_START_TV = tv
                                    break

    elif file[0] == "B":
        Cook_Beacon_name = 'Beacon ' + file[7:11]
        C_Beacon_File = os.getcwd()
        C_Beacon_open = glob.glob((file_path))
        for files in C_Beacon_open:
            with open(files, 'r') as f:
                csv_reader = csv.reader(f)
                for idx, row in enumerate(csv_reader):
                    if 'Timestamp' in row:
                        Beacon_Failure = False
                        Cook_Beacon_csv = pd.read_csv(file_path, skiprows=(idx))
                        Cook_Beacon_Time = Cook_Beacon_csv.iloc[:, 0]
                        Cook_Beacon_Move= Cook_Beacon_csv.iloc[:, 1]
                        Cook_Beacon_Accel = Cook_Beacon_csv.iloc[:, 2]
                        #print('TEEESTER' ,str(Cook_Beacon_Time))#,Fire_Start[9:], str(Cook_Beacon_Time[0][10:16]), Fire_Start[10:])
                        for tv, f in enumerate(Cook_Beacon_Time):
                            if f[11:16] == Fire_Start[9:] or str(f[10:16]) == Fire_Start[10:]:
                                Beacon_FIRE_START_TV = tv
                                break
    elif file[0] == 'U':
        USB_name = 'USBLog ' + file[7:11]
        USB_File = os.getcwd()
        USB_open = glob.glob((file_path))
        for files in USB_open:
            with open(files, 'r') as f:
                csv_reader = csv.reader(f)
                for idx, row in enumerate(csv_reader):
                    if 'Timestamp' in row:
                        USB_Failure = False
                        USB_CSV = pd.read_csv(file_path, skiprows=(idx))
                        USB_Time = USB_CSV.iloc[:, 0]
                        USB_Battery = USB_CSV.iloc[:, 1]
                        USB_Current = USB_CSV.iloc[:, 2]
                        USB_Voltage = USB_CSV.iloc[:, 3]
                        USB_Power = USB_CSV.iloc[:, 4]
                        USB_Energy  = USB_CSV.iloc[:, 5]
                        USB_Usage = USB_CSV.iloc[:, 6]
                        USB_Proximity_DF = pd.DataFrame(USB_CSV.iloc[:, 6:])
                        for tv, f in enumerate(USB_Time):
                            if f[11:16] == Fire_Start[9:] or str(f[10:16]) == Fire_Start[10:]:
                                USB_FIRE_START_TV = tv
                                break
    elif file[0] == 'G':
        Gas_name = 'GasSense ' + file[9:13]
        Gas_File = os.getcwd()
        Gas_open = glob.glob((file_path))
        for files in Gas_open:
            with open(files, 'r') as f:
                csv_reader = csv.reader(f)
                for idx, row in enumerate(csv_reader):
                    if 'Timestamp' in row:
                        GasSense_Failure = False
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
                        #finding fire start time value
                        print('~~~~~', Gas_Time[0][9:16], Fire_Start[10:])
                        for tv, f in enumerate(Gas_Time):
                            if f[11:16] == Fire_Start[9:] or str(f[10:16]) == Fire_Start[10:] or str(f[9:16]) == Fire_Start[10:]:
                                GAS_FIRE_START_TV = tv
                                break
    elif file[0] != 'B':
        Beacon_Failure = True
        print('There is no Beacon data')
    elif file[0] != 'U':
        USB_Failure = True
        print('There is no USB data')
    elif file[0] != 'G':
        GasSense_Failure = True
        print('There is no GasSense data')


co2_filter = [Gas_CO2[0]]
count_four = 0
running_average = []
co2_lengh = len(Gas_CO2)
for tv, c in enumerate(Gas_CO2):
    count_four = count_four + 1
    running_average.append(c)
    if count_four == Running_Average_length:
        co2_filter.append(np.average(running_average))
        count_four = 0
        running_average = []
    elif tv +1 ==  co2_lengh:
        break
    else:
        co2_filter.append(co2_filter[-1])


co_filter = [Gas_CO[0]]
co_lengh = len(Gas_CO)
running_average_co = []
for tv, co in enumerate(Gas_CO):
    count_four = count_four + 1
    running_average_co.append(co)
    if count_four == Running_Average_length:
        co_filter.append(np.average(running_average_co))
        count_four = 0
        running_average_co = []
    elif tv +1 ==  co_lengh:
        break
    else:
        co_filter.append(co_filter[-1])



# Finding the fire start and starting with gas

print('----Plotting Gas Sense----')
x = np.linspace(0.0, len(co2_filter), int(len(co2_filter)/(15*5)))
xval = []
for tt in x:
    xval.append(int(tt/15))
fig, ax = plt.subplots()
labels = [x]
plt.title('CO2 Filter')
plt.ylabel("CO2- PPM")
plt.xlabel("Minutes")
plt.plot(Gas_CO2, label='Orginal CO2', color='green')
plt.plot(co2_filter, label='CO2 Filter', color='r')
plt.axvline(GAS_FIRE_START_TV,label='Fire Start', color='blue',linestyle = '--')
if Boil_time != '-1':
    Gas_boil = (GAS_FIRE_START_TV) + (15*int(Boil_time))
    plt.axvline(Gas_boil, label='Boil Time', color='blue', linestyle=':')
    if GasSense_Failure == False:
        Avg_Fire_CO2_Start_to_boil = np.average(co2_filter[GAS_FIRE_START_TV:Gas_boil +1])
        Median_Fire_CO2_Start_to_boil = np.median(co2_filter[GAS_FIRE_START_TV:Gas_boil +1])
        print('Average CO2 PPM from Start - Boil:  ', int(Avg_Fire_CO2_Start_to_boil))
        print('Median CO2 PPM from Start - Boil:  ', int(Median_Fire_CO2_Start_to_boil))


if Coking_Length != '-1':
    Gas_CE = (GAS_FIRE_START_TV) + (15 * int(Coking_Length))
    plt.axvline(Gas_CE, label='Cooking End', color='blue')
    if GasSense_Failure == False:
        Avg_CO2_Cooking_length = np.average(co2_filter[GAS_FIRE_START_TV:Gas_CE+1])
        Median_CO2_Boil_to_Cooking_end = np.median(co2_filter[GAS_FIRE_START_TV:Gas_CE +1])
        print('Average CO2 PPM for Cooking Length:  ', int(Avg_CO2_Cooking_length))
        print('Median CO2 PPM for Cooking Length:  ',int(Median_CO2_Boil_to_Cooking_end) )

if Coking_Length != '-1' and Boil_time != '-1':
    if GasSense_Failure == False:
        Avg_CO2_Boil_to_Cooking_end = np.average(co2_filter[Gas_boil: Gas_CE+1])
        Median_CO2_Boil_to_Cooking_end = np.median(co2_filter[Gas_boil: Gas_CE+1])
        print('Average CO2 PPM from Boil - Cooking End:  ', int(Avg_CO2_Boil_to_Cooking_end))
        print('Median CO2 PPM from Boil - Cooking End:  ', int(Median_CO2_Boil_to_Cooking_end))

plt.xticks(x, xval)
plt.legend()
#plt.show()


fig, ax = plt.subplots()
labels2 = [x]
plt.title('CO Filter')
plt.ylabel("CO - PPM")
plt.xlabel("Minutes")
plt.plot(Gas_CO, label='Orginal CO', color='green')
plt.plot(co_filter, label='CO Filter', color='r')
plt.axvline(GAS_FIRE_START_TV,label='Fire Start', color='blue',linestyle = '--')
if Boil_time != '-1':
    Gas_boil = (GAS_FIRE_START_TV) + (15*int(Boil_time))
    plt.axvline(Gas_boil, label='Boil Time', color='blue', linestyle=':')
    if GasSense_Failure == False:
        Avg_Fire_CO_Start_to_boil = np.average(Gas_CO[GAS_FIRE_START_TV:Gas_boil +1])
        Median_Fire_CO_Start_to_boil = np.median(Gas_CO[GAS_FIRE_START_TV:Gas_boil +1])
        print('Average CO PPM from Start - Boil:  ', int(Avg_Fire_CO_Start_to_boil))
        print('Median CO PPM from Start - Boil:  ', int(Median_Fire_CO_Start_to_boil))


if Coking_Length != '-1':
    Gas_CE = (GAS_FIRE_START_TV) + (15 * int(Coking_Length))
    plt.axvline(Gas_CE, label='Cooking End', color='blue')
    if GasSense_Failure == False:
        Avg_CO_Cooking_length = np.average(Gas_CO[GAS_FIRE_START_TV:Gas_CE+1])
        Median_CO_Boil_to_Cooking_end = np.median(Gas_CO[GAS_FIRE_START_TV:Gas_CE +1])
        print('Average CO PPM for Cooking Length:  ', int(Avg_CO_Cooking_length))
        print('Median CO PPM for Cooking Length:  ',int(Median_CO_Boil_to_Cooking_end) )

if Coking_Length != '-1' and Boil_time != '-1':
    if GasSense_Failure == False:
        Avg_CO_Boil_to_Cooking_end = np.average(Gas_CO[Gas_boil: Gas_CE+1])
        Median_CO_Boil_to_Cooking_end = np.median(Gas_CO[Gas_boil: Gas_CE+1])
        print('Average CO PPM from Boil - Cooking End:  ', int(Avg_CO_Boil_to_Cooking_end))
        print('Median CO PPM from Boil - Cooking End:  ', int(Median_CO_Boil_to_Cooking_end))

plt.xticks(x, xval)
plt.legend()
plt.show()


