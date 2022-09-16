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
import itertools  

#HH1 has a file error

Household_Number = 'HH4' #input("HH1 or HH2... etc:  ")
Source = 'laptop' #input("laptop or Work: ")  # 'work' or 'laptop'
KPT_NUM = '1'

if Source == 'laptop':
    USB_D = 'D'
else:
    USB_D = 'E'

# sorting out the missing data
USB_time_place = False
Fuel_time_place = False
if Household_Number == 'HH1':
    Cook_beacon = '3409'
    Child_beacon = '3408'
    Cook_Beacon = False
    Child_Beacon = False
    Hapex = True
    Exact = True
    Fuel = False
    Exact_1_place = True
    Exact_2_place = True
    Cook_Hapex_place = True
    Kitchen_Hapex_place = True
    Fuel_1_place = False
    Fuel_2_place = False
    USB_name_place = True 
if Household_Number == 'HH2' and KPT_NUM == '1' :
    Cook_beacon = '3404'
    Child_beacon = '3414'
    Cook_Beacon = False
    Child_Beacon = False
    Hapex = True
    Exact = True
    Fuel = True
    Exact_1_place = True
    Exact_2_place = True
    Cook_Hapex_place = True
    Kitchen_Hapex_place = True
    Fuel_1_place = True
    Fuel_2_place = True
    USB_name_place = True
    print('********NEED TO RUN TWICE FOR THE TWO DOWNLOADS, change -KPT_NUM to 2 *********************')
if Household_Number == 'HH2' and KPT_NUM == '2' :
    Cook_beacon = '3404'
    Child_beacon = '3414'
    Cook_Beacon = False
    Child_Beacon = False
    Hapex = True
    Exact = True
    Fuel = True
    Exact_1_place = True
    Exact_2_place = True
    Cook_Hapex_place = True
    Kitchen_Hapex_place = True
    Fuel_1_place = True
    Fuel_2_place = True
    USB_name_place = True
if Household_Number == 'HH3'and KPT_NUM == '1' :
    Cook_beacon = '3405'
    Child_beacon = '3416'
    Cook_Beacon = False
    Child_Beacon = False
    Hapex = True
    Exact = True
    Fuel = True
    Exact_1_place = True
    Exact_2_place = True
    Cook_Hapex_place = False
    Kitchen_Hapex_place = True
    Fuel_1_place = True
    Fuel_2_place = False
    USB_name_place = True
    print('********THERE IS A SECOND, BUT DOES NOT WORK AND IS SHORTER FOR THE SAME DAYS *********************')
if Household_Number == 'HH4':
    Cook_beacon = '3415'
    Child_beacon = '3413'
    Cook_Beacon = False
    Child_Beacon = False
    Hapex = True
    Exact = True
    Fuel = True
    Exact_1_place = True
    Exact_2_place = True
    Cook_Hapex_place = True
    Kitchen_Hapex_place = True
    Fuel_1_place = True
    Fuel_2_place = True
    USB_name_place = True
if Household_Number == 'HH5':
    Cook_beacon = '3401'
    Child_beacon = '3393'
    Cook_Beacon = False
    Child_Beacon = False
    Hapex = True
    Exact = True
    Fuel = False
    Exact_1_place = True
    Exact_2_place = True
    Cook_Hapex_place = True
    Kitchen_Hapex_place = True
    Fuel_1_place = False
    Fuel_2_place = False
    USB_name_place = True
if Household_Number == 'HH6':
    Cook_beacon = '3407'
    Child_beacon = '3400'
    Cook_Beacon = False
    Child_Beacon = False
    Hapex = True
    Exact = True
    Fuel = False
    Exact_1_place = True
    Exact_2_place = True
    Cook_Hapex_place = True
    Kitchen_Hapex_place = True
    Fuel_1_place = False
    Fuel_2_place = False
    USB_name_place = True

# Fire finder metrics for jet flame and CQC stove
cooking_threshold = 5
length_decrease = 40
start_threshold = 1
end_threshold = -5
merge_CE_threshold = 60
min_CE_length = 5
window_slope = 8


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
            with open(files, 'r', errors='ignore') as f:
                csv_reader = csv.reader(f)
                for idx, row in enumerate(csv_reader):
                    if 'Stove Name:' in row and Exact == True:
                        Exact_1 = row[1][-5:]
                        Exact_2 = row[2][-5:]
                        print('exact Numbers', Exact_1, Exact_2)
                    elif 'PM measurement location:' in row and Hapex == True:
                        if row[1][0] == 'c' and Cook_Hapex_place == True:
                            if Kitchen_Hapex_place == False:
                                Cook_Hapex = row[1][-5:]
                                Kitchen_Hapex = Kitchen_Hapex_place
                            else:
                                Kitchen_Hapex = row[2][-5:]
                                Cook_Hapex = row[1][-5:]
                        elif row[1][0] == 'k'and Kitchen_Hapex_place == True:
                            if Cook_Hapex_place == False:
                                Kitchen_Hapex = row[1][-5:]
                                Cook_Hapex = Cook_Hapex_place
                            else:
                                Cook_Hapex = row[2][-5:]
                                Kitchen_Hapex = row[1][-5:]
                        print('Hapex Numbers- Cook', Cook_Hapex,'-Kitchen-', Kitchen_Hapex)
                    elif 'Fuel type:' in row and Fuel == True:
                        Fuel_1 = row[1][-5:]
                        if Fuel_2_place == True:
                            Fuel_2 = row[2][-5:]
                            print('Fuel names', Fuel_1, Fuel_2)
                        else:
                            Fuel_2 = False
                            print('Fuel_1 names', Fuel_1)
                    elif 'Fuel type:' in row and Fuel == False:
                        Fuel_1 = False
                        Fuel_2 = False
                    elif 'Location: ' in row and len(row) == 1:
                        continue
                    elif 'Location: ' in row and USB_name_place == True and row[1][0:2] == ' U':
                        USB_name = row[1][-5:]
                        print('USB Logger',USB_name, type(USB_name))

                    elif 'Timestamp' in row:
                        WHOLE_CSV = pd.read_csv(file_path, skiprows=(idx))
                        First_time = WHOLE_CSV.iloc[:,0]
                        First_time_Clean = [item for item in First_time if not(pd.isnull(item)) == True]
                        Minute_log_length = int(len(First_time_Clean))
                        #print('Time',First_time[0:6])
                        for Column, Metric in enumerate(row):
                            if Metric[-6:-1] == Fuel_1 and Fuel_1_place == True and Metric[0:13] == 'Battery level' :
                                Fuel_1_Battery = WHOLE_CSV.iloc[:,Column]
                                Fuel_1_T = WHOLE_CSV.iloc[:,Column+1]
                                Fuel_1_KG = WHOLE_CSV.iloc[:,Column+2]
                                KG_burned_1, KG_1_mean = Functions_malawi.FUEL_REMOVAL(Fuel_1_KG, 0.05, 15, True, 10)
                                
                            elif Metric[-6:-1] == Fuel_2 and Fuel_2_place == True and Metric[0:13] =='Battery level' :
                                Fuel_2_Battery = WHOLE_CSV.iloc[:,Column]
                                Fuel_2_T = WHOLE_CSV.iloc[:,Column+1]
                                Fuel_2_KG = WHOLE_CSV.iloc[:,Column+2]
                                KG_burned_2, KG_2_mean = Functions_malawi.FUEL_REMOVAL(Fuel_2_KG, 0.05, 15, True, 10)
                               
                            elif (Metric[-6:-1] == Kitchen_Hapex) and (Kitchen_Hapex_place == True) and (Metric[0:18] =='kitchen Compliance'):
                                Kitchen_Hapex_Comp = WHOLE_CSV.iloc[0:Minute_log_length,Column]
                                Kitchen_Hapex_PM = WHOLE_CSV.iloc[0:Minute_log_length,Column+1]

                            elif Metric[-6:-1] == Cook_Hapex and Cook_Hapex_place == True and Metric[0:15] =='cook Compliance':
                                CooK_Hapex_Comp = WHOLE_CSV.iloc[0:Minute_log_length,Column]
                                Cook_Hapex_PM = WHOLE_CSV.iloc[0:Minute_log_length,Column+1]
                                
                            elif Metric[-6:-1] == Exact_1 and Exact_1_place == True and Metric[0:6] ==' Usage':
                                Exact_1_Usage = WHOLE_CSV.iloc[0:Minute_log_length,Column]
                                Exact_1_Temp = WHOLE_CSV.iloc[0:Minute_log_length,Column+1]
                                
                            elif Metric[-6:-1] == Exact_2 and Exact_2_place == True and Metric[0:6] ==' Usage':
                                Exact_2_Usage = WHOLE_CSV.iloc[0:Minute_log_length,Column]
                                Exact_2_Temp = WHOLE_CSV.iloc[0:Minute_log_length,Column+1]
                                

                            elif Metric[-6:-1] == USB_name and USB_name_place == True and Metric[0:7]=='Battery' :
                                print('-----usb---',USB_name, row[Column+5])
                                USB_Battery = WHOLE_CSV.iloc[:,Column]
                                USB_Current = WHOLE_CSV.iloc[:,Column+1]
                                USB_Voltage = WHOLE_CSV.iloc[:,Column+2]
                                USB_Power = WHOLE_CSV.iloc[:,Column+3]
                                USB_Energy = WHOLE_CSV.iloc[:,Column+4]
                                USB_Usage = WHOLE_CSV.iloc[:,Column+5]
                                
                            elif 'Timestamp Fuel' == Metric:
                                Fuel_time = WHOLE_CSV.iloc[:,Column]
                                Fuel_time_place = True
                            elif 'Timestamp USB' == Metric:
                                USB_time = WHOLE_CSV.iloc[:,Column]
                                USB_time_place = True
                            elif Metric[-6:-1] == Cook_beacon:
                                Cook_Beacon_move = WHOLE_CSV.iloc[:,Column]
                                Cook_Beacon_accel = WHOLE_CSV.iloc[:,Column+1]
                                Cook_Beacon = True 
                            elif Metric[-6:-1] == Child_beacon:
                                Child_Beacon_move = WHOLE_CSV.iloc[:,Column]
                                Child_Beacon_accel = WHOLE_CSV.iloc[:,Column+1]
                                Child_Beacon = True 
                                    
# I have all of the values and organizaiton done.
# Next, the Exact and Hapex need to be extended to reach the 4 seconds for HH 4, 5, 6
if (Household_Number == 'HH4') or (Household_Number == 'HH5') or (Household_Number == 'HH6'):
    if Exact_1_place == True:
        Exact_1_Usage_ext = Functions_malawi.Add_repeated_values(Exact_1_Usage, 15, len(USB_time))
        Exact_1_Temp_ext = Functions_malawi.Add_repeated_values(Exact_1_Temp, 15, len(USB_time))
        EXACT_1_FF_usage, EXACT_1_fire_start, EXACT_1_fire_end = Functions_malawi.FireFinder(Exact_1_Temp, Exact_1_Usage, cooking_threshold, length_decrease, start_threshold, end_threshold, merge_CE_threshold, min_CE_length, window_slope)
    if Exact_2_place == True:
        Exact_2_Usage_ext = Functions_malawi.Add_repeated_values(Exact_2_Usage, 15, len(USB_time))
        Exact_2_Temp_ext = Functions_malawi.Add_repeated_values(Exact_2_Temp, 15, len(USB_time))
        EXACT_2_FF_usage, EXACT_2_fire_start, EXACT_2_fire_end = Functions_malawi.FireFinder(Exact_2_Temp,Exact_2_Usage, cooking_threshold, length_decrease, start_threshold,end_threshold, merge_CE_threshold, min_CE_length, window_slope)
    if Kitchen_Hapex_place == True:
        Kitchen_Hapex_Comp_ext = Functions_malawi.Add_repeated_values(Kitchen_Hapex_Comp, 15, len(USB_time))
        Kitchen_Hapex_PM_ext = Functions_malawi.Add_repeated_values(Kitchen_Hapex_PM, 15, len(USB_time))
    if Cook_Hapex_place == True:
        CooK_Hapex_Comp_ext = Functions_malawi.Add_repeated_values(CooK_Hapex_Comp, 15, len(USB_time))
        Cook_Hapex_PM_ext = Functions_malawi.Add_repeated_values(Cook_Hapex_PM, 15, len(USB_time))
else:
    EXACT_1_FF_usage, EXACT_1_fire_start, EXACT_1_fire_end = Functions_malawi.FireFinder(Exact_1_Temp, Exact_1_Usage, cooking_threshold, length_decrease, start_threshold, end_threshold, merge_CE_threshold, min_CE_length, window_slope)
    EXACT_2_FF_usage, EXACT_2_fire_start, EXACT_2_fire_end = Functions_malawi.FireFinder(Exact_2_Temp, Exact_2_Usage, cooking_threshold, length_decrease, start_threshold, end_threshold, merge_CE_threshold, min_CE_length, window_slope)
#Getting Metrics For the events and collection
#Combining stove usage

if (Exact_1_place == True) and (Exact_2_place == True):
    Combined_Stove, Combined_events, Two_stove_once = Functions_malawi.Squish_usage('2N', 1007, EXACT_1_FF_usage, EXACT_2_FF_usage, min_CE_length)
    Combined_Stove_ext = Functions_malawi.Add_repeated_values(Combined_Stove, 15, len(USB_time))

    count_onez_and_zeros = 0
    Combined_Cooking_start = []
    Combined_Cooking_end = []
    for Fire in Combined_Stove:
        count_onez_and_zeros = count_onez_and_zeros + 1
        if count_onez_and_zeros == len(Combined_Stove):
            break
        elif (Fire == 0) and (Combined_Stove[count_onez_and_zeros] == 1):
            Combined_Cooking_start.append(count_onez_and_zeros)
        elif (Fire == 1) and Combined_Stove[count_onez_and_zeros] == 0:
            Combined_Cooking_end.append(count_onez_and_zeros-1)




if (Exact_1_place == True) and (Exact_2_place == False):
    Combined_Cooking_start.append(EXACT_1_fire_start)
    Combined_Cooking_end.append(EXACT_1_fire_end)

if (Exact_1_place == False) and (Exact_2_place == True):
    Combined_Cooking_start.append(EXACT_2_fire_start)
    Combined_Cooking_end.append(EXACT_2_fire_end)

print('# events - stove 1:',EXACT_1_fire_start)
print('# events - stove 2:',EXACT_2_fire_start)
print('# events - stove 1:',len(EXACT_1_fire_start),'# events - stove 2:',len(EXACT_2_fire_start),'# events - combined:',Combined_events, 'Combined Stove:',Combined_Cooking_start)
#finding new event start and stop




Event_counter = np.arange(0,Combined_events, 1)
#Event Metrics that I need to gather
Event_KG_Removed_Fuel_1 = []
Event_KG_Removed_Fuel_2 =[]

Event_Average_Kitchen_Compliance = []
Event_Median_Kitchen_Compliance = []
Event_StDeV_Kitchen_Compliance = []
Event_Average_Kitchen_PM = []
Event_Median_Kitchen_PM = []
Event_StDeV_Kitchen_PM = []

Event_Average_Cook_Compliance = []
Event_Median_Cook_Compliance = []
Event_StDeV_Cook_Compliance = []
Event_Average_Cook_PM = []
Event_Median_Cook_PM = []
Event_StDeV_Cook_PM = []

Event_Average_USB_Current = []
Event_Median_USB_Current = []
Event_StDeV_USB_Current = []
Event_Average_USB_Voltage = []
Event_Median_USB_Voltage = []
Event_StDeV_USB_Voltage = []

# for TVE, Metric in enumerate(Event_counter):
#     if Fuel_1_place == True
#         fuel_bounds = list(set(KG_burned_1[st:Fire_end[tv]]))
#         Event_KG_Removed_Fuel_1.append()
#     if Fuel_2_place == True
#         Event_KG_Removed_Fuel_2.append()
#
#     Event_Average_Kitchen_Compliance = []
#     Event_Median_Kitchen_Compliance = []
#     Event_StDeV_Kitchen_Compliance = []
#     Event_Average_Kitchen_PM = []
#     Event_Median_Kitchen_PM = []
#     Event_StDeV_Kitchen_PM = []
#
#     Event_Average_Cook_Compliance = []
#     Event_Median_Cook_Compliance = []
#     Event_StDeV_Cook_Compliance = []
#     Event_Average_Cook_PM = []
#     Event_Median_Cook_PM = []
#     Event_StDeV_Cook_PM = []
#
#     Event_Average_USB_Current = []
#     Event_Median_USB_Current = []
#     Event_StDeV_USB_Current = []
#     Event_Average_USB_Voltage = []
#     Event_Median_USB_Voltage = []
#     Event_StDeV_USB_Voltage = []