import os
import pandas as pd
import numpy as np
import csv
import glob
import statistics as stat
from datetime import datetime
from csv import reader
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import Functions_malawi
import itertools  

#HH1 has a file error

Household_Number = 'HH3' #input("HH1 or HH2... etc:  ")
Source = 'laptop' #input("laptop or Work: ")  # 'work' or 'laptop'
KPT_NUM = '1'
Start_Up_Spread = 10
Cooldown_Spread = 30

if Source == 'laptop':
    USB_D = 'D'
elif Source != 'laptop':
    USB_D = 'E'

# sorting out the missing data
USB_time_place = False
Fuel_time_place = False
if Household_Number == 'HH1':
    Cook_beacon = '3409'
    Child_beacon = '3408'
    Cook_Beacon_place = False
    Child_Beacon_place = False
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
    Cook_Beacon_place = False
    Child_Beacon_place = False
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
    Cook_Beacon_place = False
    Child_Beacon_place = False
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
    Cook_Beacon_place = False
    Child_Beacon_place = False
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
    Cook_Beacon_place = False
    Child_Beacon_place = False
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
    Cook_Beacon_place = False
    Child_Beacon_place = False
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
    Cook_Beacon_place = False
    Child_Beacon_place = False
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
                                

                            elif Metric[-6:-1] == USB_name and USB_name_place == True and Metric[0:8]==' Battery' :
                                print('-----usb---',USB_name, row[Column+5], '-',Cook_beacon ,'-' ,Metric[-6:-1], '-', len(Metric[-6:-1]) )
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
                            elif (Metric[-5:-1] == Cook_beacon) and (Metric[0:9] == ' Movement'):
                                print('-----Cook Beacon ----', Cook_beacon)
                                Cook_Beacon_move = WHOLE_CSV.iloc[:,Column]
                                Cook_Beacon_accel = WHOLE_CSV.iloc[:,Column+1]
                                Cook_Beacon_place = True 
                            elif (Metric[-5:-1] == Child_beacon) and (Metric[0:9] == ' Movement'):
                                print('-----Child Beacon ----', Child_beacon)
                                Child_Beacon_move = WHOLE_CSV.iloc[:,Column]
                                Child_Beacon_accel = WHOLE_CSV.iloc[:,Column+1]
                                Child_Beacon_place = True 
                                    
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
Event_KG_Combined_Fuel = []

Event_Average_Kitchen_Compliance = []; Event_Average_Cook_Compliance = []
Event_Average_Kitchen_PM = []; Event_Average_Cook_PM = []
Event_Median_Kitchen_PM = []; Event_Median_Cook_PM = []
Event_StDeV_Kitchen_PM = []; Event_StDeV_Cook_PM = []
Event_Length = []
Event_start_time = []

Event_Average_USB_Current = []; Event_Avergage_Cook_Beacon_Acceleration = []
Event_Median_USB_Current = []; Event_Average_Child_Beacon_Acceleration = []
Event_StDeV_USB_Current = []; Event_Average_Child_Beacon_Movement = []
Event_RAW_Beacon_Cook_accel = []; Event_RAW_Child_Beacon_Acceleration= []; Event_RAW_Child_Beacon_Movement = []
Event_RAW_USB_Current = []
Event_Average_USB_Voltage = []
Event_Median_USB_Voltage = []
Event_StDeV_USB_Voltage = []
Event_RAW_USB_Voltage = []

for Event in Event_counter:
    if Fuel_1_place == True:
        fuel_bounds = list(set(KG_burned_1[((Combined_Cooking_start[Event]-(Start_Up_Spread*15))*15):(Combined_Cooking_end[Event]*15)]))
        Event_KG_Removed_Fuel_1.append((int((sum(fuel_bounds))*1000)/1000))
    else:
        Event_KG_Removed_Fuel_1.append(-1)
    if Fuel_2_place == True:
        fuel_bounds = list(set(KG_burned_2[((Combined_Cooking_start[Event]-(Start_Up_Spread*15))*15):(Combined_Cooking_end[Event]*15)]))
        Event_KG_Removed_Fuel_2.append((int((sum(fuel_bounds)) * 1000) / 1000))
    else:
        Event_KG_Removed_Fuel_2.append(-1)

    if Fuel_2_place == True and Fuel_1_place == True:
        Event_KG_Combined_Fuel.append((Event_KG_Removed_Fuel_1[-1] + Event_KG_Removed_Fuel_2[-1]))
    else:
        Event_KG_Combined_Fuel.append(-1)

    if Kitchen_Hapex_place == True:
        Event_Average_Kitchen_Compliance.append((int((np.average([a for a in Kitchen_Hapex_Comp[(Combined_Cooking_start[Event]):(Combined_Cooking_end[Event])]]))*100))/100)
        Event_Average_Kitchen_PM.append((int((np.average([a for a in Kitchen_Hapex_PM[(Combined_Cooking_start[Event]):(Combined_Cooking_end[Event])]]))*100))/100)
        Event_Median_Kitchen_PM.append((int((np.median([a for a in Kitchen_Hapex_PM[(Combined_Cooking_start[Event]):(Combined_Cooking_end[Event])]]))*100))/100)
        Event_StDeV_Kitchen_PM.append((int((stat.stdev(Kitchen_Hapex_PM[(Combined_Cooking_start[Event]):(Combined_Cooking_end[Event])])) * 100)) / 100)
    else:
        Event_Average_Kitchen_Compliance.append(-1);Event_Average_Kitchen_PM.append(-1)
        Event_Median_Kitchen_PM.append(-1);Event_StDeV_Kitchen_PM.append(-1)

    Event_Length.append((Combined_Cooking_end[Event])-(Combined_Cooking_start[Event]))
    Event_start_time.append(First_time_Clean[(Combined_Cooking_start[Event])])

    if Cook_Hapex_place == True:
        Event_Average_Cook_Compliance.append((int((np.average([a for a in CooK_Hapex_Comp[(Combined_Cooking_start[Event]):(Combined_Cooking_end[Event])]]))*100))/100)
        
        Event_Average_Cook_PM.append((int((np.average([a for a in Cook_Hapex_PM[(Combined_Cooking_start[Event]):(Combined_Cooking_end[Event])]]))*100))/100)
        Event_Median_Cook_PM.append((int((np.median([a for a in Cook_Hapex_PM[(Combined_Cooking_start[Event]):(Combined_Cooking_end[Event])]]))*100))/100)
        Event_StDeV_Cook_PM.append((int((stat.stdev(Cook_Hapex_PM[(Combined_Cooking_start[Event]):(Combined_Cooking_end[Event])])) * 100)) / 100)
    else:
        Event_Average_Cook_Compliance.append(-1);Event_Average_Cook_PM.append(-1)
        Event_Median_Cook_PM.append(-1);Event_StDeV_Cook_PM.append(-1)

    if USB_name_place == True:
        Event_Average_USB_Current.append(np.average(list((USB_Current[(Combined_Cooking_start[Event]*15):(Combined_Cooking_end[Event]*15)]))))
        Event_Median_USB_Current.append(np.median(list((USB_Current[(Combined_Cooking_start[Event]*15):(Combined_Cooking_end[Event]*15)]))))
        Event_StDeV_USB_Current.append((int((stat.stdev(USB_Current[(Combined_Cooking_start[Event]*15):(Combined_Cooking_end[Event]*15)])) * 100)) / 100)
        Event_RAW_USB_Current.append(USB_Current[(Combined_Cooking_start[Event]*15):(Combined_Cooking_end[Event]*15)])
        Event_Average_USB_Voltage.append(np.average(list(set(USB_Voltage[(Combined_Cooking_start[Event]*15):(Combined_Cooking_end[Event]*15)]))))
        Event_Median_USB_Voltage.append(np.median(list(set(USB_Voltage[(Combined_Cooking_start[Event]*15):(Combined_Cooking_end[Event]*15)]))))
        Event_StDeV_USB_Voltage.append((int((stat.stdev(USB_Voltage[(Combined_Cooking_start[Event]*15):(Combined_Cooking_end[Event]*15)])) * 100)) / 100)
        Event_RAW_USB_Voltage.append(USB_Voltage[(Combined_Cooking_start[Event]*15):(Combined_Cooking_end[Event]*15)])
    else:
        Event_Average_USB_Current.append(-1);Event_Median_USB_Voltage.append(-1)
        Event_Median_USB_Current.append(-1); Event_StDeV_USB_Voltage.append(-1)
        Event_StDeV_USB_Current.append(-1); Event_RAW_USB_Voltage.append(-1)
        Event_RAW_USB_Current.append(-1);Event_Average_USB_Voltage.append(-1)

    if Cook_Beacon_place == True:
        Event_Avergage_Cook_Beacon_Acceleration.append(np.average(list(set(Cook_Beacon_accel[(Combined_Cooking_start[Event]*15):(Combined_Cooking_end[Event]*15)]))))
        Event_RAW_Beacon_Cook_accel.append(Cook_Beacon_accel[(Combined_Cooking_start[Event]*15):(Combined_Cooking_end[Event]*15)])
    else:
        Event_Avergage_Cook_Beacon_Acceleration.append(-1)
        Event_RAW_Beacon_Cook_accel.append(-1)

    if Child_Beacon_place == True:
        Event_Average_Child_Beacon_Acceleration.append(np.average(list(set(Child_Beacon_accel[(Combined_Cooking_start[Event]*15):(Combined_Cooking_end[Event]*15)]))))
        Event_Average_Child_Beacon_Movement.append(np.average(list(set(Child_Beacon_move[(Combined_Cooking_start[Event]*15):(Combined_Cooking_end[Event]*15)]))))
        Event_RAW_Child_Beacon_Acceleration.append(Child_Beacon_accel[(Combined_Cooking_start[Event]*15):(Combined_Cooking_end[Event]*15)])
        Event_RAW_Child_Beacon_Movement.append(Child_Beacon_move[(Combined_Cooking_start[Event]*15):(Combined_Cooking_end[Event]*15)])

    else:
        Event_Average_Child_Beacon_Acceleration.append(-1)
        Event_Average_Child_Beacon_Movement.append(-1)
        Event_RAW_Child_Beacon_Acceleration.append(-1)
        Event_RAW_Child_Beacon_Movement.append(-1)
# Event Startup

Startup_Average_Kitchen_Compliance = []; Startup_Average_Cook_Compliance = []
Startup_Average_Kitchen_PM = []; Startup_Average_Cook_PM = []
Startup_Median_Kitchen_PM = []; Startup_Median_Cook_PM = []
Startup_StDeV_Kitchen_PM = []; Startup_StDeV_Cook_PM = []

Startup_Average_USB_Current = []; Startup_Avergage_Cook_Beacon_Acceleration =[]; Startup_RAW_Cook_Beacon_Acceleration = []
Startup_Median_USB_Current = []
Startup_StDeV_USB_Current = []
Startup_RAW_USB_Current = []
Startup_Average_USB_Voltage = []
Startup_Median_USB_Voltage = []
Startup_StDeV_USB_Voltage = []
Startup_RAW_USB_Voltage = []

for Event in Event_counter:
    if Kitchen_Hapex_place == True:
        Startup_Average_Kitchen_Compliance.append((int((np.average([a for a in Kitchen_Hapex_Comp[(Combined_Cooking_start[Event]-((Start_Up_Spread))):(Combined_Cooking_start[Event]+1)]]))*100))/100)
        Startup_Average_Kitchen_PM.append((int((np.average([a for a in Kitchen_Hapex_PM[(Combined_Cooking_start[Event]-((Start_Up_Spread))):(Combined_Cooking_start[Event]+1)]]))*100))/100)
        Startup_Median_Kitchen_PM.append((int((np.median([a for a in Kitchen_Hapex_PM[(Combined_Cooking_start[Event]-((Start_Up_Spread))):(Combined_Cooking_start[Event]+1)]]))*100))/100)
        Startup_StDeV_Kitchen_PM.append((int((stat.stdev(Kitchen_Hapex_PM[(Combined_Cooking_start[Event]-((Start_Up_Spread))):(Combined_Cooking_start[Event]+1)])) * 100)) / 100)
    else:
        Startup_Average_Kitchen_Compliance.append(-1); Startup_Average_Kitchen_PM.append(-1)
        Startup_Median_Kitchen_PM.append(-1);Startup_StDeV_Kitchen_PM.append(-1)

    if Cook_Hapex_place == True:
        Startup_Average_Cook_Compliance.append((int((np.average([a for a in CooK_Hapex_Comp[(Combined_Cooking_start[Event]-((Start_Up_Spread))):(Combined_Cooking_start[Event]+1)]]))*100))/100)
        Startup_Average_Cook_PM.append((int((np.average([a for a in Cook_Hapex_PM[(Combined_Cooking_start[Event]-((Start_Up_Spread))):(Combined_Cooking_start[Event]+1)]]))*100))/100)
        Startup_Median_Cook_PM.append((int((np.median([a for a in Cook_Hapex_PM[(Combined_Cooking_start[Event]-((Start_Up_Spread))):(Combined_Cooking_start[Event]+1)]]))*100))/100)
        Startup_StDeV_Cook_PM.append((int((stat.stdev(Cook_Hapex_PM[(Combined_Cooking_start[Event]-((Start_Up_Spread))):(Combined_Cooking_start[Event]+1)])) * 100)) / 100)
    else:
        Startup_Average_Cook_Compliance.append(-1); Startup_Average_Cook_PM.append(-1)
        Startup_Median_Cook_PM.append(-1);Startup_StDeV_Cook_PM.append(-1)
    if USB_name_place == True:
        Startup_Average_USB_Current.append(np.average(list((USB_Current[((Combined_Cooking_start[Event]*15)-(Start_Up_Spread*15)):((Combined_Cooking_start[Event]*15)+1)]))))
        Startup_Median_USB_Current.append(np.median(list(USB_Current[((Combined_Cooking_start[Event]*15)-(Start_Up_Spread*15)):((Combined_Cooking_start[Event]*15)+1)])))
        Startup_StDeV_USB_Current.append((int((stat.stdev(USB_Current[((Combined_Cooking_start[Event]*15)-(Start_Up_Spread*15)):((Combined_Cooking_start[Event]*15)+1)])) * 100)) / 100)
        Startup_RAW_USB_Current.append(USB_Current[((Combined_Cooking_start[Event]*15)-(Start_Up_Spread*15)):((Combined_Cooking_start[Event]*15)+1)])
        Startup_Average_USB_Voltage.append(np.average(list(set(USB_Voltage[((Combined_Cooking_start[Event]*15)-(Start_Up_Spread*15)):((Combined_Cooking_start[Event]*15)+1)]))))
        Startup_Median_USB_Voltage.append(np.median(list(set(USB_Voltage[((Combined_Cooking_start[Event]*15)-(Start_Up_Spread*15)):((Combined_Cooking_start[Event]*15)+1)]))))
        Startup_StDeV_USB_Voltage.append((int((stat.stdev(USB_Voltage[((Combined_Cooking_start[Event]*15)-(Start_Up_Spread*15)):((Combined_Cooking_start[Event]*15)+1)])) * 100)) / 100)
        Startup_RAW_USB_Voltage.append(USB_Voltage[((Combined_Cooking_start[Event]*15)-(Start_Up_Spread*15)):((Combined_Cooking_start[Event]*15)+1)])
    else: 
        Startup_Average_USB_Current.append(-1);Startup_Median_USB_Current.append(-1)
        Startup_StDeV_USB_Current.append(-1); Startup_RAW_USB_Current.append(-1)
        Startup_Average_USB_Voltage.append(-1); Startup_Median_USB_Voltage.append(-1)
        Startup_StDeV_USB_Voltage.append(-1);Startup_RAW_USB_Voltage.append(-1)

    if Cook_Beacon_place == True:
        Startup_Avergage_Cook_Beacon_Acceleration.append(np.average(list(set(Cook_Beacon_accel[((Combined_Cooking_start[Event]*15)-(Start_Up_Spread*15)):((Combined_Cooking_start[Event]*15)+1)]))))
        Startup_RAW_Cook_Beacon_Acceleration.append(Cook_Beacon_accel[((Combined_Cooking_start[Event]*15)-(Start_Up_Spread*15)):((Combined_Cooking_start[Event]*15)+1)])
    else:
        Startup_Avergage_Cook_Beacon_Acceleration.append(-1)
        Startup_RAW_Cook_Beacon_Acceleration.append(-1)
# Cooldown

Cooldown_Average_Kitchen_Compliance = []; Cooldown_Average_Cook_Compliance = []
Cooldown_Average_Kitchen_PM = []; Cooldown_Average_Cook_PM = []
Cooldown_Median_Kitchen_PM = []; Cooldown_Median_Cook_PM = []
Cooldown_StDeV_Kitchen_PM = []; Cooldown_StDeV_Cook_PM = []

Cooldown_Average_USB_Current = []
Cooldown_Median_USB_Current = []
Cooldown_StDeV_USB_Current = []
Cooldown_RAW_USB_Current = []
Cooldown_Average_USB_Voltage = []
Cooldown_Median_USB_Voltage = []
Cooldown_StDeV_USB_Voltage = []
Cooldown_RAW_USB_Voltage = []

for Event in Event_counter:
    if Kitchen_Hapex_place == True:
        Cooldown_Average_Kitchen_Compliance.append((int((np.average([a for a in Kitchen_Hapex_Comp[(Combined_Cooking_end[Event]):(Combined_Cooking_end[Event]+Cooldown_Spread)]]))*100))/100)
        Cooldown_Median_Kitchen_PM.append((int((np.median([a for a in Kitchen_Hapex_PM[(Combined_Cooking_end[Event]):(Combined_Cooking_end[Event]+Cooldown_Spread)]]))*100))/100)
        Cooldown_StDeV_Kitchen_PM.append((int((stat.stdev(Kitchen_Hapex_PM[(Combined_Cooking_end[Event]):(Combined_Cooking_end[Event]+Cooldown_Spread)])) * 100)) / 100)
        Cooldown_Average_Kitchen_PM.append((int((np.average([a for a in Kitchen_Hapex_PM[(Combined_Cooking_end[Event]):(Combined_Cooking_end[Event]+Cooldown_Spread)]]))*100))/100)
    else:
        Cooldown_Average_Kitchen_Compliance.append(-1);Cooldown_Average_Kitchen_PM.append(-1)
        Cooldown_Median_Kitchen_PM.append(-1);Cooldown_StDeV_Kitchen_PM.append(-1)
    if Cook_Hapex_place == True:
        Cooldown_Average_Cook_Compliance.append((int((np.average([a for a in CooK_Hapex_Comp[(Combined_Cooking_end[Event]):(Combined_Cooking_end[Event]+Cooldown_Spread)]]))*100))/100)
        Cooldown_Average_Cook_PM.append((int((np.average([a for a in Cook_Hapex_PM[(Combined_Cooking_end[Event]):(Combined_Cooking_end[Event]+Cooldown_Spread)]]))*100))/100)
        Cooldown_Median_Cook_PM.append((int((np.median([a for a in Cook_Hapex_PM[(Combined_Cooking_end[Event]):(Combined_Cooking_end[Event]+Cooldown_Spread)]]))*100))/100)
        Cooldown_StDeV_Cook_PM.append((int((stat.stdev(Cook_Hapex_PM[(Combined_Cooking_end[Event]):(Combined_Cooking_end[Event]+Cooldown_Spread)])) * 100)) / 100)
    else: 
        Cooldown_Average_Cook_Compliance.append(-1);Cooldown_Average_Cook_PM.append(-1)
        Cooldown_Median_Cook_PM.append(-1);Cooldown_StDeV_Cook_PM.append(-1)
    if USB_name_place == True:
        Cooldown_Average_USB_Current.append(np.average(list((USB_Current[(Combined_Cooking_end[Event]*15):((Combined_Cooking_end[Event]*15)+(Cooldown_Spread*15))]))))
        Cooldown_Median_USB_Current.append(np.median(list(USB_Current[(Combined_Cooking_end[Event]*15):((Combined_Cooking_end[Event]*15)+(Cooldown_Spread*15))])))
        Cooldown_StDeV_USB_Current.append((int((stat.stdev(USB_Current[(Combined_Cooking_end[Event]*15):((Combined_Cooking_end[Event]*15)+(Cooldown_Spread*15))])) * 100)) / 100)
        Cooldown_RAW_USB_Current.append(USB_Current[(Combined_Cooking_end[Event]*15):((Combined_Cooking_end[Event]*15)+(Cooldown_Spread*15))])
        Cooldown_Average_USB_Voltage.append(np.average(list(set(USB_Voltage[(Combined_Cooking_end[Event]*15):((Combined_Cooking_end[Event]*15)+(Cooldown_Spread*15))]))))
        Cooldown_Median_USB_Voltage.append(np.median(list(set(USB_Voltage[(Combined_Cooking_end[Event]*15):((Combined_Cooking_end[Event]*15)+(Cooldown_Spread*15))]))))
        Cooldown_StDeV_USB_Voltage.append((int((stat.stdev(USB_Voltage[(Combined_Cooking_end[Event]*15):((Combined_Cooking_end[Event]*15)+(Cooldown_Spread*15))])) * 100)) / 100)
        Cooldown_RAW_USB_Voltage.append(USB_Voltage[(Combined_Cooking_end[Event]*15):((Combined_Cooking_end[Event]*15)+(Cooldown_Spread*15))])
    else:
        Cooldown_Average_USB_Current.append(-1);Cooldown_Median_USB_Current.append(-1)
        Cooldown_StDeV_USB_Current.append(-1); Cooldown_RAW_USB_Current.append(-1)
        Cooldown_Average_USB_Voltage.append(-1); Cooldown_Median_USB_Voltage.append(-1)
        Cooldown_StDeV_USB_Voltage.append(-1);Cooldown_RAW_USB_Voltage.append(-1)

    # Next- Day Breakdown for Each metric

Munute_Day_breakdown = (int(Minute_log_length/(60*24))) * 60*24
Fast_log_rate_day_breakdown = int(len(USB_time)/ (60*24*15)) * 60*24*15
how_many_days = (int(Minute_log_length/(60*24)))
Day_counter = np.arange(1,5,1)
Minute_Day_Start_TV= np.arange(0,Munute_Day_breakdown, (60*24))
Fast_log_rate_day_Start_TV = np.arange(0,Fast_log_rate_day_breakdown, (60*24*15))

Minute_Day_End_TV= np.arange((60*24),Munute_Day_breakdown+1, (60*24))
Fast_log_rate_day_End_TV = np.arange((60*24*15),Fast_log_rate_day_breakdown+1, (60*24*15))

print('Day Breakdowns', Munute_Day_breakdown, Fast_log_rate_day_breakdown)
print('are these the minute breakdowns', how_many_days, Minute_Day_Start_TV, Fast_log_rate_day_Start_TV)
print('are these the minute breakdowns', Day_counter, Minute_Day_End_TV, Fast_log_rate_day_End_TV)
print('envent numbers',Combined_Cooking_start, Combined_Cooking_end )
Event_per_Day = []
Average_length_of_CE = []
Day_date = []
# Fuel
Sum_Fuel_1_removed_per_day_per_event = []; Fuel_1_Removed_per_day = []
Sum_Fuel_2_removed_per_day_per_event = []; Fuel_2_Removed_per_day = []
Sum_Combined_Fuel_removed_per_day_per_event = []; Combined_Fuel_Removed_per_day = []
# Hapex Compliance
Average_Kitchen_Comp_per_day_per_event = []; Average_Kitchen_Comp_per_day = []
Average_Cook_Comp_per_day_per_event = []; Average_Cook_Comp_per_day = []
Average_Kitchen_Comp_per_day_per_startup = []; Average_Cook_Comp_per_day_per_startup = []
Average_Kitchen_Comp_per_day_per_cooldown = []; Average_Cook_Comp_per_day_per_cooldown = []
# Hapex PM
Average_Kitchen_PM_per_day_per_event = []; Median_Kitchen_PM_per_day_per_event = []; Average_Kitchen_PM_per_day = []
Average_Cook_PM_per_day_per_event = []; Median_Cook_PM_per_day_per_event = []; Average_Cook_PM_per_day = []
Average_Kitchen_PM_per_day_per_startup = []; Average_Cook_PM_per_day_per_startup = []
Average_Kitchen_PM_per_day_per_cooldown = []; Average_Cook_PM_per_day_per_cooldown = []
#USB Metrics
Average_USB_Current_per_Event = []; Average_USB_Voltage_per_Event = []
Average_USB_Current_per_Startup = []; Average_USB_Voltage_per_Startup = []
Average_USB_Current_per_Cooldown = []; Average_USB_Voltage_per_cooldown = []
#beacon Informaiton
Average_Beacon_Cook_Accel_per_day_per_event = []; Average_Beacon_Child_Accel_per_day_per_event = []
Average_Beacon_Child_Move_per_day_per_event = []
Average_Beacon_Cook_Accel_per_startup = []
Average_Beacon_Cook_Accel_per_Day = []; Average_Beacon_Child_Accel_per_Day = []
Average_Beacon_Child_Move_per_Day = []




for Day in Day_counter:
    Event_per_Day_count = 0
    Day_date.append(First_time_Clean[Minute_Day_Start_TV[Day-1]])
    EVENT_LENGTH_count = []
    Fuel_1_Event = []; Fuel_2_Event = []
    Kit_Comp_event =[]; Cook_Comp_event = []
    Kit_PM_event  = []; Cook_PM_event = []
    Kit_Comp_startup =[]; Cook_Comp_startup = []
    Kit_PM_startup  = []; Cook_PM_startup = []
    Kit_Comp_Cooldown =[]; Cook_Comp_Cooldown = []
    Kit_PM_Cooldown  = []; Cook_PM_Cooldown = []
    USB_Current_Event = []; USB_Voltage_Event = []
    USB_Current_Startup = []; USB_Voltage_Startup = []
    USB_Current_Cooldown = []; USB_Voltage_Cooldown = []
    Beacon_Cook_accel_Event = []; Beacon_Child_accel_Event = []; Beacon_Cook_move_Event = []
    Beacon_Cook_accel_startup = []
    Combined_Fuel = []
    Fuel_title_column  =[] 
    HAPEX_title_column = []
    USB_title_column = []
    Beacon_title_column = [] 
    for E in Event_counter:
        Fuel_title_column.append('----FUEL----')
        HAPEX_title_column.append('----HAPEx----')
        USB_title_column.append('----USB----')
        Beacon_title_column.append('----BEACON----')
        if (Combined_Cooking_end[E] < Minute_Day_End_TV[Day-1]) and (Combined_Cooking_end[E] >  Minute_Day_Start_TV[Day-1]):
            Event_per_Day_count = Event_per_Day_count +1
            EVENT_LENGTH_count.append(Combined_Cooking_end[E]-Combined_Cooking_start[E])
            
            Fuel_1_Event.append(Event_KG_Removed_Fuel_1[E]); Fuel_2_Event.append(Event_KG_Removed_Fuel_2[E])
            if Fuel_2_place == True and Fuel_1_place == True:
                Combined_Fuel.append(Event_KG_Removed_Fuel_1[E]+Event_KG_Removed_Fuel_2[E])
            else:
                Combined_Fuel.append(-1)
            if Cook_Hapex_place == True:
                Cook_Comp_event.extend(CooK_Hapex_Comp[Combined_Cooking_start[E]:Combined_Cooking_end[E]])
                Cook_PM_event.extend(Cook_Hapex_PM[Combined_Cooking_start[E]:Combined_Cooking_end[E]])
                Cook_Comp_startup.extend(CooK_Hapex_Comp[(Combined_Cooking_start[E]-(Start_Up_Spread)):(Combined_Cooking_start[E]+1)])
                Cook_PM_startup.extend(Cook_Hapex_PM[(Combined_Cooking_start[E]-((Start_Up_Spread))):(Combined_Cooking_start[E]+1)])
                Cook_Comp_Cooldown.extend(CooK_Hapex_Comp[(Combined_Cooking_end[E]):(Combined_Cooking_end[E]+Cooldown_Spread)])
                Cook_PM_Cooldown.extend(Cook_Hapex_PM[(Combined_Cooking_end[E]):(Combined_Cooking_end[E]+Cooldown_Spread)])
            else:
                Cook_Comp_event = [-1, -1]; Cook_PM_event = [-1, -1]; Cook_Comp_startup = [-1, -1]; Cook_PM_startup = [-1, -1]; Cook_Comp_Cooldown = [-1, -1]; Cook_PM_Cooldown = [-1, -1]

            if Kitchen_Hapex_place == True:
                Kit_Comp_event.extend(Kitchen_Hapex_Comp[Combined_Cooking_start[E]:Combined_Cooking_end[E]])
                Kit_PM_event.extend(Kitchen_Hapex_PM[Combined_Cooking_start[E]:Combined_Cooking_end[E]])
                Kit_Comp_startup.extend(Kitchen_Hapex_Comp[(Combined_Cooking_start[E]-((Start_Up_Spread))):(Combined_Cooking_start[E]+1)])
                Kit_PM_startup.extend(Kitchen_Hapex_PM[(Combined_Cooking_start[E]-((Start_Up_Spread))):(Combined_Cooking_start[E]+1)])
                Kit_Comp_Cooldown.extend(Kitchen_Hapex_Comp[(Combined_Cooking_end[E]):(Combined_Cooking_end[Event]+Cooldown_Spread)])
                Kit_PM_Cooldown.extend(Kitchen_Hapex_PM[(Combined_Cooking_end[E]):(Combined_Cooking_end[E]+Cooldown_Spread)])
            else:
                Kit_Comp_event= [-1, -1]; Kit_PM_event = [-1, -1]; Kit_Comp_startup = [-1, -1]; Kit_PM_startup = [-1, -1]; Kit_Comp_Cooldown = [-1, -1]; Kit_PM_Cooldown = [-1, -1]      
            if USB_name_place == True:
                USB_Current_Event.extend(Event_RAW_USB_Current[E]); USB_Voltage_Event.extend(Event_RAW_USB_Voltage[E])
                USB_Current_Startup.extend(Startup_RAW_USB_Current[E])  ; USB_Voltage_Startup.extend(Startup_RAW_USB_Voltage[E])
                USB_Current_Cooldown.extend(Cooldown_RAW_USB_Current[E]) ; USB_Voltage_Cooldown.extend(Cooldown_RAW_USB_Voltage[E])
            else:
                USB_Current_Event = [-1, -1]; USB_Voltage_Event = [-1, -1]; USB_Current_Startup = [-1, -1]; USB_Voltage_Startup = [-1, -1];USB_Current_Cooldown = [-1, -1];USB_Voltage_Cooldown = [-1, -1]

            if Cook_Beacon_place == True:
                Beacon_Cook_accel_Event.extend(Event_RAW_Beacon_Cook_accel[E])
                #Beacon_Cook_move_Event.extend(Event_RAW_Child_Beacon_Movement[E])
            else:
                Beacon_Cook_accel_Event = [-1, -1]; Beacon_Cook_move_Event = [-1, -1]
            if Child_Beacon_place == True:
                Beacon_Cook_accel_startup.extend(Startup_RAW_Cook_Beacon_Acceleration[E])
                Beacon_Child_accel_Event.extend(Event_RAW_Child_Beacon_Acceleration[E])
            else:
                Beacon_Cook_accel_startup = [-1, -1]; Beacon_Child_accel_Event = [-1, -1]

    Event_per_Day.append(Event_per_Day_count)
    Average_length_of_CE.append(np.average(EVENT_LENGTH_count))


    #Kitchen and Cook Hapex
    Average_Kitchen_Comp_per_day_per_event.append(np.average(Kit_Comp_event)); Average_Cook_Comp_per_day_per_event.append(np.average(Cook_Comp_event))
    Average_Kitchen_PM_per_day_per_event.append(np.average(Kit_PM_event)); Median_Kitchen_PM_per_day_per_event.append(np.median(Kit_PM_event))
    Average_Cook_PM_per_day_per_event.append(np.average(Cook_PM_event)); Median_Cook_PM_per_day_per_event.append(np.median(Cook_PM_event))
    if Cook_Hapex_place == True:
        Average_Cook_PM_per_day.append(np.average(Cook_Hapex_PM[Minute_Day_Start_TV[Day-1]:Minute_Day_End_TV[Day-1]]))
        Average_Cook_Comp_per_day.append(np.average(CooK_Hapex_Comp[Minute_Day_Start_TV[Day-1]:Minute_Day_End_TV[Day-1]]))
    else:
        Average_Cook_PM_per_day.append(-1)
        Average_Cook_Comp_per_day.append(-1)


    if Kitchen_Hapex_place == True:
        Average_Kitchen_Comp_per_day.append(np.average(Kitchen_Hapex_Comp[Minute_Day_Start_TV[Day-1]:Minute_Day_End_TV[Day-1]]))
        Average_Kitchen_PM_per_day.append(np.average(Kitchen_Hapex_PM[Minute_Day_Start_TV[Day-1]:Minute_Day_End_TV[Day-1]]))
    else:
        Average_Kitchen_Comp_per_day.append(-1)
        Average_Kitchen_PM_per_day.append(-1)

    #Hapex Compliance for Start up and Cooldown
    Average_Kitchen_Comp_per_day_per_startup.append(np.average(Kit_Comp_startup)) ; Average_Cook_Comp_per_day_per_startup.append(np.average(Cook_Comp_startup)) 
    Average_Kitchen_Comp_per_day_per_cooldown.append(np.average(Kit_Comp_Cooldown)); Average_Cook_Comp_per_day_per_cooldown.append(np.average(Cook_Comp_Cooldown))
    #Hapex PM for Startup and Cooldown
    Average_Kitchen_PM_per_day_per_startup.append(np.average(Kit_PM_startup)) ; Average_Cook_PM_per_day_per_startup.append(np.average(Cook_PM_startup)) 
    Average_Kitchen_PM_per_day_per_cooldown.append(np.average(Kit_PM_Cooldown)); Average_Cook_PM_per_day_per_cooldown.append(np.average(Cook_PM_Cooldown))
    #Fuel Metrics
    if Fuel_1_place == True:
        fuel_bounds_1 = list(set(KG_burned_1[Minute_Day_Start_TV[Day-1]:Minute_Day_End_TV[Day-1]])); Fuel_1_Removed_per_day.append((int((sum(fuel_bounds_1)) * 1000) / 1000))
        Sum_Fuel_1_removed_per_day_per_event.append(sum(Fuel_1_Event))
    else:
        Fuel_1_Removed_per_day.append(-1)
        Sum_Fuel_1_removed_per_day_per_event.append(-1)
    if Fuel_2_place == True:
        fuel_bounds_2 = list(set(KG_burned_2[Minute_Day_Start_TV[Day-1]:Minute_Day_End_TV[Day-1]])); Fuel_2_Removed_per_day.append((int((sum(fuel_bounds_2)) * 1000) / 1000))
        Sum_Fuel_2_removed_per_day_per_event.append(sum(Fuel_2_Event))
    else:
        Fuel_2_Removed_per_day.append(-1)
        Sum_Fuel_2_removed_per_day_per_event.append(-1)

    if Fuel_2_place == True and Fuel_1_place == True:
        Sum_Combined_Fuel_removed_per_day_per_event.append(sum(Fuel_1_Event)+sum(Fuel_2_Event))  ; Combined_Fuel_Removed_per_day.append(Fuel_2_Removed_per_day[-1]+Fuel_1_Removed_per_day[-1])
    else:
        Sum_Combined_Fuel_removed_per_day_per_event.append(-1); Combined_Fuel_Removed_per_day.append(-1)

    #USB Power meter
    Average_USB_Current_per_Event.append(np.average(USB_Current_Event)) ; Average_USB_Voltage_per_Event.append(np.average(USB_Voltage_Event))
    Average_USB_Current_per_Startup.append(np.average(USB_Current_Startup)) ; Average_USB_Voltage_per_Startup.append(np.average(USB_Voltage_Startup))
    Average_USB_Current_per_Cooldown.append(np.average(USB_Current_Cooldown)) ; Average_USB_Voltage_per_cooldown.append(np.average(USB_Voltage_Cooldown))
    #Beacon
    Average_Beacon_Cook_Accel_per_day_per_event.append(np.average(Beacon_Cook_accel_Event))
    Average_Beacon_Child_Accel_per_day_per_event.append(np.average(Beacon_Child_accel_Event))
    Average_Beacon_Child_Move_per_day_per_event.append(np.average(Beacon_Cook_move_Event))
    Average_Beacon_Cook_Accel_per_startup.append(np.average(Beacon_Cook_accel_startup))
    if Child_Beacon_place == True:
        Average_Beacon_Child_Accel_per_Day.append(np.average(Child_Beacon_accel[((Minute_Day_Start_TV[Day-1])*15):((Minute_Day_End_TV[Day-1])*15)]))
        Average_Beacon_Child_Move_per_Day.append(np.average(Child_Beacon_move[((Minute_Day_Start_TV[Day-1])*15):((Minute_Day_End_TV[Day-1])*15)]))
    else:
        Average_Beacon_Child_Accel_per_Day.append(-1)
        Average_Beacon_Child_Move_per_Day.append(-1)
    if Cook_Beacon_place == True:
        Average_Beacon_Cook_Accel_per_Day.append(np.average(Cook_Beacon_accel[((Minute_Day_Start_TV[Day-1])*15):((Minute_Day_End_TV[Day-1])*15)]))
    else:
        Average_Beacon_Cook_Accel_per_Day.append(-1)

print('events per day---------',Event_per_Day )

#Exporting Metrics to CSV
Dict_sensors = {'~Exact 1~': [Exact_1], '~Exact 2~':[Exact_2], '~Cook HAPEx~':[Cook_Hapex], 
'~Kitchen HAPEx~':[Kitchen_Hapex], '~Fuel 1~':[Fuel_1], '~Fuel 2~':[Fuel_2],'~USB~':[USB_name], '~Cook Beacon~':[Cook_beacon],'~Child Beacon~':[Child_beacon]}
DF_Dict_sensors = pd.DataFrame(Dict_sensors)

Dict_Event = {'|Event|': Event_counter, '|Start Time|':Event_start_time, '|Length of Event|':Event_Length,'----FUEL----':Fuel_title_column[0:(len(Event_counter)+1)],'|Fuel 1 Removed|': Event_KG_Removed_Fuel_1, 
'|Fuel 2 Removed|': Event_KG_Removed_Fuel_2, '|Combined Fuel Removed|':Event_KG_Combined_Fuel, '----HAPEx----':HAPEX_title_column[0:(len(Event_counter)+1)],'|Avg. Kitchen Comp|':Event_Average_Kitchen_Compliance,'|Avg. Cook Comp|':Event_Average_Cook_Compliance,
   '|Average Kitchen PM|':Event_Average_Kitchen_PM, '|Average Cook PM|':Event_Average_Cook_PM,
   '|Median Cook PM|':Event_Median_Cook_PM, '|StDev Kitchen PM|':Event_StDeV_Kitchen_PM, '|StDev Cook PM|':Event_StDeV_Cook_PM,'|Cook Beacon Acceleration|':Event_Avergage_Cook_Beacon_Acceleration,
   '----BEACON----':Beacon_title_column[0:(len(Event_counter)+1)],'|Child Beacon Accleration|': Event_Average_Child_Beacon_Acceleration, '|Child Beacon Movement|':Event_Average_Child_Beacon_Movement, '----USB----':USB_title_column[0:(len(Event_counter)+1)],'|Avg. USB Current|':Event_Average_USB_Current,
   '|Median USB Current|':Event_Median_USB_Current, '|StDev USB Current|':Event_StDeV_USB_Current,'|Avg. USB Voltage|':Event_Average_USB_Voltage,
    '|Median USB Voltage|':Event_Median_USB_Voltage, '|StDev USB Voltage|':Event_StDeV_USB_Voltage}


DF_Dict_Event = pd.DataFrame(Dict_Event)

Dict_Startup = {'|Event|': Event_counter,'|Length of Event|':Event_Length,'----HAPEx----':HAPEX_title_column[0:(len(Event_counter)+1)],'|Startup Avg. Kitchen Comp|':Startup_Average_Kitchen_Compliance, '|Startup Avg. Cook Comp|':Startup_Average_Cook_Compliance,
'|Startup Avg. Kitchen PM|':Startup_Average_Kitchen_PM, '|Startup Median Kitchen PM|':Startup_Median_Kitchen_PM,'|Startup StDev Kitchen PM|':Startup_StDeV_Kitchen_PM,
 '|Startup Avg. Cook PM|':Startup_Average_Cook_PM,'|Startup Median Cook PM|':Startup_Median_Cook_PM, '|Startup StDev Cook PM|':Startup_StDeV_Cook_PM,'----BEACON----':Beacon_title_column[0:(len(Event_counter)+1)],
 '|Startup Cook Beacon Acceleration|':Startup_Avergage_Cook_Beacon_Acceleration,'----USB----':USB_title_column[0:(len(Event_counter)+1)],'|Startup Avg. USB Current|':Startup_Average_USB_Current,
    '|Startup Median USB Current|':Startup_Median_USB_Current, '|Startup StDev USB Current|':Startup_StDeV_USB_Current,
  '|Startup Avg. USB Voltage|':Startup_Average_USB_Voltage,    '|Startup Median USB Voltage|':Startup_Median_USB_Voltage, '|Startup StDev USB Voltage|':Startup_StDeV_USB_Voltage}
DF_Dict_Startup = pd.DataFrame(Dict_Startup)

Dict_Cooldown = {'|Event|': Event_counter,'|Length of Event|':Event_Length,'----HAPEx----':HAPEX_title_column[0:(len(Event_counter)+1)],'|Cooldown Avg. Kitchen Comp|':Cooldown_Average_Kitchen_Compliance, '|Cooldown Avg. Cook Comp|':Cooldown_Average_Cook_Compliance,
'|Cooldown Avg. Kitchen PM|':Cooldown_Average_Kitchen_PM, '|Cooldown Median Kitchen PM|':Cooldown_Median_Kitchen_PM,'|Cooldown StDev Kitchen PM|':Cooldown_StDeV_Kitchen_PM,
 '|Cooldown Avg. Cook PM|':Cooldown_Average_Cook_PM,'|Cooldown Median Cook PM|':Cooldown_Median_Cook_PM, '|Cooldown StDev Cook PM|':Cooldown_StDeV_Cook_PM,'----USB----':USB_title_column[0:(len(Event_counter)+1)],
 '|Cooldown Avg. USB Current|':Cooldown_Average_USB_Current,'|Cooldown Median USB Current|':Cooldown_Median_USB_Current, '|Cooldown StDev USB Current|':Cooldown_StDeV_USB_Current,
  '|Cooldown Avg. USB Voltage|':Cooldown_Average_USB_Voltage,    '|Cooldown Median USB Voltage|':Cooldown_Median_USB_Voltage, '|Cooldown StDev USB Voltage|':Cooldown_StDeV_USB_Voltage}

DF_Dict_Cooldown = pd.DataFrame(Dict_Cooldown)
#---------------------------------

Dict_Day = {'|Day|': Day_counter,'|Day Date|':Day_date,'|Number of Events for the day|':Event_per_Day,'|Average length of Cooking Length (min)|':Average_length_of_CE,'----FUEL----':Fuel_title_column[0:(len(Day_counter))],
'|Fuel 1 - Removed for Whole Day|':Fuel_1_Removed_per_day, '|Fuel 2 - Removed for Whole Day|':Fuel_2_Removed_per_day, '|Sum of Fuel Removed for Whole Day|':Combined_Fuel_Removed_per_day,
'|Fuel 1 - Sum of Fuel For Each Event|':Sum_Fuel_1_removed_per_day_per_event,'|Fuel 2 - Sum of Fuel For Each Event|':Sum_Fuel_2_removed_per_day_per_event,
'|Fuel Combined - Removed for Each Event|':Sum_Combined_Fuel_removed_per_day_per_event,'----HAPEx----':HAPEX_title_column[0:(len(Day_counter))],

'|Kitchen Compliance for Events|':Average_Kitchen_Comp_per_day_per_event, '|Kitchen Compliance for Day|':Average_Kitchen_Comp_per_day,
'|Cook Compliance for Events|':Average_Cook_Comp_per_day_per_event, '|Cook Compliance for Day|':Average_Cook_Comp_per_day,

'|Kitchen Startup Compliance for Events|':Average_Kitchen_Comp_per_day_per_startup, '|Cook Startup Compliance for Events|':Average_Cook_Comp_per_day_per_startup,
'|Kitchen Cooldown Compliance for Events|':Average_Kitchen_Comp_per_day_per_cooldown, '|Cook Cooldown Compliance for Events|':Average_Cook_Comp_per_day_per_cooldown,

 '|Average Kitchen PM for Events|':Average_Kitchen_PM_per_day_per_event,'|Median Kitchen PM for Events|':Median_Kitchen_PM_per_day_per_event,'|Average Kitchen PM for Day|':Average_Kitchen_PM_per_day,
 '|Average Cook PM for Events|':Average_Cook_PM_per_day_per_event,'|Median Cook PM for Events|':Median_Cook_PM_per_day_per_event,'|Average Cook PM for Day|':Average_Cook_PM_per_day,

 '|Average Kitchen PM for Startup|':Average_Kitchen_PM_per_day_per_startup,'|Average Cook PM for Startup|':Average_Cook_PM_per_day_per_startup,
  '|Average Kitchen PM for Cooldown|':Average_Kitchen_PM_per_day_per_cooldown,'|Average Cook PM for Cooldown|':Average_Cook_PM_per_day_per_cooldown,'----USB----':USB_title_column[0:(len(Day_counter))],


 '|Average JetFlame Current for Events|':Average_USB_Current_per_Event,'|Average JetFlame Voltage for Events|':Average_USB_Voltage_per_Event,
 '|Average JetFlame Current for Startup|':Average_USB_Current_per_Startup,'|Average JetFlame Voltage for Startup|':Average_USB_Voltage_per_Startup,
 '|Average JetFlame Current for Cooldown|':Average_USB_Current_per_Cooldown,'|Average JetFlame Voltage for Cooldown|':Average_USB_Voltage_per_cooldown,'----BEACON----':Beacon_title_column[0:(len(Day_counter))],

 '|Average (Beacon) Cook Acceleration for Events|':Average_Beacon_Cook_Accel_per_day_per_event, '|Average (Beacon) Child Acceleration for Events|':Average_Beacon_Child_Accel_per_day_per_event,

 '|Average (Beacon) Child Movement for Events|':Average_Beacon_Child_Move_per_day_per_event,'|Average (Beacon) Cook Acceleration for Startup|':Average_Beacon_Cook_Accel_per_startup, 

 '|Average (Beacon) Cook Acceleration for Day|':Average_Beacon_Cook_Accel_per_Day,'|Average (Beacon) Child Acceleration for Day|':Average_Beacon_Child_Accel_per_Day, 
    '|Average (Beacon) Child Movement for Day|':Average_Beacon_Child_Move_per_Day 

}
print('-------len check -----', HAPEX_title_column[0:(len(Day_counter))], len(Day_date), len(Beacon_title_column[0:(len(Day_counter))]), len(Average_Cook_Comp_per_day), USB_title_column[0:(len(Day_counter))], len(Average_Cook_Comp_per_day_per_startup),len(Fuel_title_column[0:(len(Day_counter))]))
print(Dict_Day)

DF_Dict_Day= pd.DataFrame(Dict_Day)
Path_Raw_Events = USB_D+":/Malawi 1.1/"+Household_Number+"_KPT_Summary.csv"
# Path_Raw_Event = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_"+str(q)+"_exact"
# File_event_Raw_metrics = str(Path_Raw_Event) + "/Raw_E_metrics/"+Phase+"_HH_raw_Event_metrics_"+str(id_number)+"_"+str(q)+"_exact_1.11"+".csv"
        #Df_sensor.to_csv(File_event_Raw_metrics)
        #Df_raw_event.to_csv(File_event_Raw_metrics,index=False,mode='a')
DF_Dict_sensors.to_csv(Path_Raw_Events,index=False, mode='a')
DF_Dict_Event.to_csv(Path_Raw_Events,index=False, mode='a')
DF_Dict_Startup.to_csv(Path_Raw_Events,index=False, mode='a')
DF_Dict_Cooldown.to_csv(Path_Raw_Events,index=False, mode='a')
DF_Dict_Day.to_csv(Path_Raw_Events,index=False, mode='a')