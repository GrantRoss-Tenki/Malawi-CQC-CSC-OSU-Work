import os
from turtle import shape
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

Household_Number = 'HH6' #input("HH1 or HH2... etc:  ")
Source = 'laptop' #input("laptop or Work: ")  # 'work' or 'laptop'
KPT_NUM = '1'
Start_Up_Spread = 10
Cooldown_Spread = 30
Log_rate_per_min = 15

if Source == 'laptop':
    USB_D = 'D'
elif Source != 'laptop':
    USB_D = 'F'

# sorting out the missing data
USB_time_place = False
Fuel_time_place = False
if Household_Number == 'HH1':
    One_time = True
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
    One_time = True
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
    One_time = True
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
    One_time = True
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
    One_time = False
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
    One_time = False
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
    One_time = False
    Cook_beacon = '3407'
    Child_beacon = '3400'
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
    Fuel_2_place = False
    USB_name_place = True

# Fire finder metrics for jet flame and CQC stove
cooking_threshold = 7
length_decrease = 40
start_threshold = 1
end_threshold = -5
merge_CE_threshold = 40
min_CE_length = 15
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
                        print('here is the timestamp :', idx)
                        WHOLE_CSV = pd.read_csv(file_path, skiprows=(idx), encoding='unicode_escape')
                        
                        if One_time == False:
                            First_time = WHOLE_CSV.iloc[:,0]
                            First_time_Clean = [item for item in First_time if not(pd.isnull(item)) == True]
                            Minute_log_length = (len(First_time_Clean))
                            Decrease_to_min_log_length = First_time_Clean
                        elif One_time == True:
                            First_time_Clean = WHOLE_CSV.iloc[:,0]
                            step_coutner = np.arange(1, len(First_time_Clean), Log_rate_per_min)
                            Minute_log_length = len(step_coutner)
                            Decrease_to_min_log_length = []
                            for step in step_coutner:
                                Decrease_to_min_log_length.append(First_time_Clean[step])
                            
                        for Column, Metric in enumerate(row):
                            if Metric[-6:-1] == Fuel_1 and Fuel_1_place == True and Metric[0:13] == 'Battery level' :
                                Fuel_1_Battery = WHOLE_CSV.iloc[:,Column]
                                Fuel_1_T = WHOLE_CSV.iloc[:,Column+1]
                                Fuel_1_KG = WHOLE_CSV.iloc[:,Column+2]
                                KG_burned_1, KG_1_mean = Functions_malawi.FUEL_REMOVAL(Fuel_1_KG, 0.03, Log_rate_per_min, True, 30)
                                
                            elif Metric[-6:-1] == Fuel_2 and Fuel_2_place == True and Metric[0:13] =='Battery level' :
                                Fuel_2_Battery = WHOLE_CSV.iloc[:,Column]
                                Fuel_2_T = WHOLE_CSV.iloc[:,Column+1]
                                Fuel_2_KG = WHOLE_CSV.iloc[:,Column+2]
                                KG_burned_2, KG_2_mean = Functions_malawi.FUEL_REMOVAL(Fuel_2_KG, 0.03, Log_rate_per_min, True, 30)
                               
                            elif (Metric[-6:-1] == Kitchen_Hapex) and (Kitchen_Hapex_place == True) and (Metric[0:18] =='kitchen Compliance'):
                                if One_time == True:
                                    Kitchen_Hapex_Comp = []
                                    Kitchen_Hapex_PM = []
                                    for step in step_coutner:
                                        Kitchen_Hapex_Comp.append(WHOLE_CSV.iloc[step,Column])
                                        Kitchen_Hapex_PM.append(WHOLE_CSV.iloc[step,Column+1])
                                    Kitchen_Hapex_Comp = pd.Series(Kitchen_Hapex_Comp)
                                    Kitchen_Hapex_PM = pd.Series(Kitchen_Hapex_PM)
                                else:
                                    Kitchen_Hapex_Comp = WHOLE_CSV.iloc[0:Minute_log_length,Column]
                                    Kitchen_Hapex_PM = WHOLE_CSV.iloc[0:Minute_log_length,Column+1]

                            elif Metric[-6:-1] == Cook_Hapex and Cook_Hapex_place == True and Metric[0:Log_rate_per_min] =='cook Compliance':
                                if One_time == True:
                                    CooK_Hapex_Comp = []
                                    Cook_Hapex_PM = []
                                    for step in step_coutner:
                                        CooK_Hapex_Comp.append(WHOLE_CSV.iloc[step,Column])
                                        Cook_Hapex_PM.append(WHOLE_CSV.iloc[step,Column+1])
                                    CooK_Hapex_Comp = pd.Series(CooK_Hapex_Comp)
                                    Cook_Hapex_PM = pd.Series(Cook_Hapex_PM)
                                else:
                                    CooK_Hapex_Comp = WHOLE_CSV.iloc[0:Minute_log_length,Column]
                                    Cook_Hapex_PM = WHOLE_CSV.iloc[0:Minute_log_length,Column+1]
                                
                            elif Metric[-6:-1] == Exact_1 and Exact_1_place == True and Metric[0:6] ==' Usage':
                                if One_time == True:
                                    Exact_1_Usage = []
                                    Exact_1_Temp = []
                                    for step in step_coutner:
                                        Exact_1_Usage.append(WHOLE_CSV.iloc[step,Column])
                                        Exact_1_Temp.append(WHOLE_CSV.iloc[step,Column+1])
                                    Exact_1_Usage = pd.Series(Exact_1_Usage[:])
                                    Exact_1_Temp = pd.Series(Exact_1_Temp[:])
                                else:    
                                    Exact_1_Usage = WHOLE_CSV.iloc[0:Minute_log_length,Column]
                                    Exact_1_Temp = WHOLE_CSV.iloc[0:Minute_log_length,Column+1]
                                #print('Why would data fram be so small ?',Household_Number,'____',Minute_log_length, type(WHOLE_CSV.iloc[:,0]), type(Decrease_to_min_log_length))
                            elif Metric[-6:-1] == Exact_2 and Exact_2_place == True and Metric[0:6] ==' Usage':
                                if One_time == True:
                                    Exact_2_Usage = []
                                    Exact_2_Temp = [] 
                                    for step in step_coutner:
                                        Exact_2_Usage.append(WHOLE_CSV.iloc[step,Column])
                                        Exact_2_Temp.append(WHOLE_CSV.iloc[step,Column+1])
                                    Exact_2_Usage = pd.Series(Exact_2_Usage)
                                    Exact_2_Temp = pd.Series(Exact_2_Temp)
                                else:
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
                                Proxmimity_column_count = np.arange(Column + 6, len(row), 1)
                                print('~~~~~~~USB first values ~~~~~',USB_Battery[0], USB_Energy[0],USB_Current[29290],sum(USB_Usage[2641:2655]), USB_Power[29290]   )
                                for prox in Proxmimity_column_count:
                                    row_Name = row[prox]
                                    if row_Name[0:17] == ('RSSI Beacon  ' + Cook_beacon):

                                        print('There is a proximity BEacon to USB logger !!')
                                        Beacon_proximity = WHOLE_CSV.iloc[:,prox]
                                        IS_there_a_Cook_beacon_proximity = True 
                                        break
                                    else:
                                        IS_there_a_Cook_beacon_proximity = False
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
# if there is not a split of time values, Going to have to convert Hapex, Exact to minute sets

#print('------Battery ', len(USB_Battery), '----- Exact 1---', len(Exact_1_Temp), len(Kitchen_Hapex_PM))
#print('Decrease to min decrease log length: ', len(Decrease_to_min_log_length), len(First_gtime_Clean),Decrease_to_min_log_length[0:5])

if USB_time_place == False and Fuel_time_place == False:
    USB_time = First_time_Clean
    Fuel_time = First_time_Clean
    
elif USB_time_place == False and Fuel_time_place == True:
    USB_time = Fuel_time

# Next, the Exact and Hapex need to be extended to reach the 4 seconds for HH 4, 5, 6
if (Household_Number == 'HH4') or (Household_Number == 'HH5') or (Household_Number == 'HH6'):
    if Exact_1_place == True:
        Exact_1_Usage_ext = Functions_malawi.Add_repeated_values(Exact_1_Usage, Log_rate_per_min, len(USB_time))
        Exact_1_Temp_ext = Functions_malawi.Add_repeated_values(Exact_1_Temp, Log_rate_per_min, len(USB_time))
        EXACT_1_FF_usage, EXACT_1_fire_start, EXACT_1_fire_end = Functions_malawi.FireFinder(Exact_1_Temp, Exact_1_Usage, Exact_1_place, cooking_threshold, length_decrease, start_threshold, end_threshold, merge_CE_threshold, min_CE_length, window_slope)
    if Exact_2_place == True:
        Exact_2_Usage_ext = Functions_malawi.Add_repeated_values(Exact_2_Usage, Log_rate_per_min, len(USB_time))
        Exact_2_Temp_ext = Functions_malawi.Add_repeated_values(Exact_2_Temp, Log_rate_per_min, len(USB_time))
        EXACT_2_FF_usage, EXACT_2_fire_start, EXACT_2_fire_end = Functions_malawi.FireFinder(Exact_2_Temp,Exact_2_Usage, Exact_2_place, cooking_threshold, length_decrease, start_threshold,end_threshold, merge_CE_threshold, min_CE_length, window_slope)
    if Kitchen_Hapex_place == True:
        Kitchen_Hapex_Comp_ext = Functions_malawi.Add_repeated_values(Kitchen_Hapex_Comp, Log_rate_per_min, len(USB_time))
        Kitchen_Hapex_PM_ext = Functions_malawi.Add_repeated_values(Kitchen_Hapex_PM, Log_rate_per_min, len(USB_time))
    if Cook_Hapex_place == True:
        CooK_Hapex_Comp_ext = Functions_malawi.Add_repeated_values(CooK_Hapex_Comp, Log_rate_per_min, len(USB_time))
        Cook_Hapex_PM_ext = Functions_malawi.Add_repeated_values(Cook_Hapex_PM, Log_rate_per_min, len(USB_time))
else:
    if Exact_1_place == True:
        EXACT_1_FF_usage, EXACT_1_fire_start, EXACT_1_fire_end = Functions_malawi.FireFinder(Exact_1_Temp, Exact_1_Usage, Exact_1_place,cooking_threshold, length_decrease, start_threshold, end_threshold, merge_CE_threshold, min_CE_length, window_slope)
    if Exact_2_place == True:
        EXACT_2_FF_usage, EXACT_2_fire_start, EXACT_2_fire_end = Functions_malawi.FireFinder(Exact_2_Temp, Exact_2_Usage, Exact_2_place,cooking_threshold, length_decrease, start_threshold, end_threshold, merge_CE_threshold, min_CE_length, window_slope)
    if Kitchen_Hapex_place == True and len(Kitchen_Hapex_Comp) != len(USB_Usage):
        Kitchen_Hapex_Comp_ext = Functions_malawi.Add_repeated_values(Kitchen_Hapex_Comp, Log_rate_per_min, len(USB_time))
        Kitchen_Hapex_PM_ext = Functions_malawi.Add_repeated_values(Kitchen_Hapex_PM, Log_rate_per_min, len(USB_time))
    if Cook_Hapex_place == True and len(CooK_Hapex_Comp) != len(USB_Usage):
        CooK_Hapex_Comp_ext = Functions_malawi.Add_repeated_values(CooK_Hapex_Comp, Log_rate_per_min, len(USB_time))
        Cook_Hapex_PM_ext = Functions_malawi.Add_repeated_values(Cook_Hapex_PM, Log_rate_per_min, len(USB_time))
    
#Getting Metrics For the events and collection
#Combining stove usage

if (Exact_1_place == True) and (Exact_2_place == True):
    Combined_Stove, Combined_events, Two_stove_once = Functions_malawi.Squish_usage('2N', 1007, EXACT_1_FF_usage, EXACT_2_FF_usage, min_CE_length)
    Combined_Stove_ext = Functions_malawi.Add_repeated_values(Combined_Stove, Log_rate_per_min, len(USB_time))

    count_onez_and_zeros = 0
    Combined_Cooking_start = []
    Combined_Cooking_end = []
    Cooking = False
    for Fire in Combined_Stove:
        count_onez_and_zeros = count_onez_and_zeros + 1
        if (count_onez_and_zeros + min_CE_length == len(Combined_Stove)-1):
            break
        elif (Fire == 0) and (Combined_Stove[count_onez_and_zeros] == 1) and (Combined_Stove[count_onez_and_zeros+ min_CE_length] == 1):
            Combined_Cooking_start.append(count_onez_and_zeros)
            Cooking = True
        elif (Fire == 1) and (Combined_Stove[count_onez_and_zeros] == 0) and (Cooking == True):
            Combined_Cooking_end.append(count_onez_and_zeros-1)
            Cooking = False
    if len(Combined_Cooking_start) > len(Combined_Cooking_end):
        Combined_Cooking_end.append(count_onez_and_zeros)

print('----FF Start----------',Combined_Cooking_start)
print('----FF End------------',Combined_Cooking_end)
print('length of minute log: ',len(USB_time),'Length of log rate: ', len(EXACT_1_FF_usage))

if (Exact_1_place == True) and (Exact_2_place == False):
    Combined_Cooking_start.append(EXACT_1_fire_start)
    Combined_Cooking_end.append(EXACT_1_fire_end)

if (Exact_1_place == False) and (Exact_2_place == True):
    Combined_Cooking_start.append(EXACT_2_fire_start)
    Combined_Cooking_end.append(EXACT_2_fire_end)




Event_counter = np.arange(0,len(Combined_Cooking_start), 1)
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
Event_End_time = []

Event_Average_USB_Current = []; Event_Avergage_Cook_Beacon_Acceleration = []
Event_Median_USB_Current = []; Event_Average_Child_Beacon_Acceleration = []
Event_StDeV_USB_Current = []; Event_Average_Child_Beacon_Movement = []
Event_RAW_Beacon_Cook_accel = []; Event_RAW_Child_Beacon_Acceleration= []; Event_RAW_Child_Beacon_Movement = []
Event_RAW_USB_Current = []
Event_Average_USB_Voltage = []
Event_Median_USB_Voltage = []
Event_StDeV_USB_Voltage = []
Event_RAW_USB_Voltage = []
Event_jet_flame_percent = []
Event_jet_flame_start_min = []
Event_jet_flame_end_min = []
Event_jet_flame_time_on = []
Event_Watt_R_1 = []; Event_Watt_R_2 = []; Event_Watt_R_3 = []; Event_Watt_R_4 = []; Event_Watt_R_5 = []; Event_Watt_R_6 = []
Event_Watt_R_7 = [];  Event_Watt_R_8 = []; 

prev_fuel_bound_1 = [0]
prev_fuel_bound_2 = [0]

#Beacon Proximity
Beacon_Use_event_number = []
Length_of_time_at_stove = []
length_of_time_away_from_stove = []
Adjusting_the_jet_flame = []
Percentage_away_from_stove_CE = []
Time_at_stove = []
for Event in Event_counter:
    #print('|||Event||', Event, '|||Cooking start||', Event_RAW_USB_Voltage )
    #first Fuel
    if Fuel_1_place == True:
        fuel_bounds_1 = list(set(KG_burned_1[((Combined_Cooking_start[Event]-(Start_Up_Spread*Log_rate_per_min))*Log_rate_per_min):(Combined_Cooking_end[Event]*Log_rate_per_min)]))
        if (Event != 0) and (fuel_bounds_1 != []):
            #print('Fuel Bounds 1----', Event, sum(fuel_bounds_1),'last fuel bound--',prev_fuel_bound_1)
            #print('--- are they the same?----', ((prev_fuel_bound_1)*10000),'==',((fuel_bounds_1[0])*10000))
            if ((prev_fuel_bound_1)*10000) != ((fuel_bounds_1[0])*10000):
                Event_KG_Removed_Fuel_1.append((int((sum(fuel_bounds_1))*1000)/1000))
                prev_fuel_bound_1 = fuel_bounds_1[-1]
                #print('!=!=!=!=!= Non Equal !=!=!=!=!=!=')
            elif ((prev_fuel_bound_1)*10000) == ((fuel_bounds_1[0])*10000):
                Event_KG_Removed_Fuel_1.append((int((sum(fuel_bounds_1[1:]))*1000)/1000))
                prev_fuel_bound_1 = fuel_bounds_1[-1]
                #print('===== Equal =======')
            else:
                Event_KG_Removed_Fuel_1.append((int((sum(fuel_bounds_1))*1000)/1000))
                prev_fuel_bound_1 = fuel_bounds_1[-1]
        elif Event == 0 or fuel_bounds_1 == []:
            Event_KG_Removed_Fuel_1.append((int((sum(fuel_bounds_1))*1000)/1000))
            prev_fuel_bound_1 = 0
        else:
            Event_KG_Removed_Fuel_1.append((int((sum(fuel_bounds_1))*1000)/1000))
            prev_fuel_bound_1 = fuel_bounds_1[-1]
        
    else:
        Event_KG_Removed_Fuel_1.append("")
    #Second Fuel
    if Fuel_2_place == True:
        
        fuel_bounds_2 = list(set(KG_burned_2[((Combined_Cooking_start[Event]-(Start_Up_Spread*Log_rate_per_min))*Log_rate_per_min):(Combined_Cooking_end[Event]*Log_rate_per_min)]))
        #print('Fuel Bounds 2----', Event, sum(fuel_bounds_2),'last fuel bound--')
        if Event != 0 and fuel_bounds_2 != []:
            if ((prev_fuel_bound_2)*10000) != ((fuel_bounds_2[0])*10000):
                Event_KG_Removed_Fuel_2.append((int((sum(fuel_bounds_2))*1000)/1000))
                
            elif ((prev_fuel_bound_2)*10000) == ((fuel_bounds_2[0])*10000):
                Event_KG_Removed_Fuel_2.append((int((sum(fuel_bounds_2[1:]))*1000)/1000))
            else:
                Event_KG_Removed_Fuel_2.append((int((sum(fuel_bounds_2))*1000)/1000))
                prev_fuel_bound_2 = fuel_bounds_2[-1]
        elif Event == 0 or fuel_bounds_2 == []:
            Event_KG_Removed_Fuel_2.append((int((sum(fuel_bounds_2))*1000)/1000))
            prev_fuel_bound_2 = fuel_bounds_2
        else:
            Event_KG_Removed_Fuel_2.append((int((sum(fuel_bounds_2))*1000)/1000))
            prev_fuel_bound_2 = fuel_bounds_2[-1]
    else:
        Event_KG_Removed_Fuel_2.append(-1)

    if Fuel_2_place == True and Fuel_1_place == True:
        Event_KG_Combined_Fuel.append((Event_KG_Removed_Fuel_1[-1] + Event_KG_Removed_Fuel_2[-1]))
    else:
        Event_KG_Combined_Fuel.append("")

    if Kitchen_Hapex_place == True:
        Event_Average_Kitchen_Compliance.append((int((np.average([a for a in Kitchen_Hapex_Comp[(Combined_Cooking_start[Event]):(Combined_Cooking_end[Event])]]))*100))/100)
        Event_Average_Kitchen_PM.append((int((np.average([a for a in Kitchen_Hapex_PM[(Combined_Cooking_start[Event]):(Combined_Cooking_end[Event])]]))*100))/100)
        Event_Median_Kitchen_PM.append((int((np.median([a for a in Kitchen_Hapex_PM[(Combined_Cooking_start[Event]):(Combined_Cooking_end[Event])]]))*100))/100)
        Event_StDeV_Kitchen_PM.append((int((stat.stdev(Kitchen_Hapex_PM[(Combined_Cooking_start[Event]):(Combined_Cooking_end[Event])])) * 100)) / 100)
    else:
        Event_Average_Kitchen_Compliance.append("");Event_Average_Kitchen_PM.append("")
        Event_Median_Kitchen_PM.append("");Event_StDeV_Kitchen_PM.append("")

    Event_Length.append((Combined_Cooking_end[Event])-(Combined_Cooking_start[Event]))
    Event_start_time.append(Decrease_to_min_log_length[(Combined_Cooking_start[Event])])
    Event_End_time.append(Decrease_to_min_log_length[(Combined_Cooking_end[Event])])
    #print('==== Event Start Time =====', Event_start_time)
    if Cook_Hapex_place == True:
        Event_Average_Cook_Compliance.append((int((np.average([a for a in CooK_Hapex_Comp[(Combined_Cooking_start[Event]):(Combined_Cooking_end[Event])]]))*100))/100)
        
        Event_Average_Cook_PM.append((int((np.average([a for a in Cook_Hapex_PM[(Combined_Cooking_start[Event]):(Combined_Cooking_end[Event])]]))*100))/100)
        Event_Median_Cook_PM.append((int((np.median([a for a in Cook_Hapex_PM[(Combined_Cooking_start[Event]):(Combined_Cooking_end[Event])]]))*100))/100)
        Event_StDeV_Cook_PM.append((int((stat.stdev(Cook_Hapex_PM[(Combined_Cooking_start[Event]):(Combined_Cooking_end[Event])])) * 100)) / 100)
    else:
        Event_Average_Cook_Compliance.append("");Event_Average_Cook_PM.append("")
        Event_Median_Cook_PM.append("");Event_StDeV_Cook_PM.append("")

    if USB_name_place == True and sum(USB_Usage[(Combined_Cooking_start[Event]*Log_rate_per_min):(Combined_Cooking_end[Event]*Log_rate_per_min)]) != 0:
        JFK_percent, JFK_start, JFK_end, jet_flame_on = Functions_malawi.FF_to_jet_flame_usage((Combined_Cooking_start[Event]*Log_rate_per_min),(Combined_Cooking_end[Event]*Log_rate_per_min),USB_Usage[(Combined_Cooking_start[Event]*Log_rate_per_min):(Combined_Cooking_end[Event]*Log_rate_per_min)])
        Jet_flame_Start = (Combined_Cooking_start[Event]*Log_rate_per_min) + JFK_start
        Jet_flame_End = (Combined_Cooking_end[Event] *Log_rate_per_min) - JFK_end
        print('/\/\/\/\\/\/\ ',Jet_flame_Start, Jet_flame_End, (Jet_flame_End-Jet_flame_Start))
        Event_Average_USB_Current.append(np.average(list((USB_Current.loc[Jet_flame_Start:Jet_flame_End]))))
        EVENT_CURRENT_CHECK = np.average(list((USB_Current.loc[Jet_flame_Start:Jet_flame_End])))
        Event_Median_USB_Current.append(np.median(list((USB_Current.loc[Jet_flame_Start:Jet_flame_End]))))
        Event_StDeV_USB_Current.append((int((stat.stdev(USB_Current.loc[Jet_flame_Start:Jet_flame_End])) * 100)) / 100)
        Event_RAW_USB_Current.append(USB_Current.loc[Jet_flame_Start:Jet_flame_End])
        Event_Average_USB_Voltage.append(np.average(list(set(USB_Voltage.loc[Jet_flame_Start:Jet_flame_End]))))
        Event_Median_USB_Voltage.append(np.median(list(set(USB_Voltage.loc[Jet_flame_Start:Jet_flame_End]))))
        Event_StDeV_USB_Voltage.append((int((stat.stdev(USB_Voltage.loc[Jet_flame_Start:Jet_flame_End])) * 100)) / 100)
        Event_RAW_USB_Voltage.append(USB_Voltage.loc[Jet_flame_Start:Jet_flame_End])
        
        Event_jet_flame_percent.append((JFK_percent))
        Event_jet_flame_start_min.append(int(JFK_start/Log_rate_per_min))
        Event_jet_flame_end_min.append(int(JFK_end/Log_rate_per_min))
        Event_jet_flame_time_on.append(round((jet_flame_on/Log_rate_per_min)))
         # I want to make a new algorithm for USB power meter and breakdown
        Raw_JFK_Current = pd.Series(list((USB_Current.loc[(Jet_flame_Start-JFK_start):(Jet_flame_End + JFK_end)])))
        Raw_JFK_Voltage = pd.Series(list((USB_Voltage.loc[(Jet_flame_Start-JFK_start):(Jet_flame_End + JFK_end)])))
        Raw_Kitchen_PM = pd.Series(list( (Kitchen_Hapex_PM_ext[(Jet_flame_Start-JFK_start):(Jet_flame_End + JFK_end+1)])))
        Raw_Cook_PM = pd.Series(list( (Cook_Hapex_PM_ext[(Jet_flame_Start-JFK_start):(Jet_flame_End + JFK_end+1)])))
        Raw_Cook_Com = pd.Series(list((CooK_Hapex_Comp_ext[(Jet_flame_Start-JFK_start):(Jet_flame_End + JFK_end+1)])))

        print('array check: ',len(USB_Current) ,len(CooK_Hapex_Comp_ext),len(Raw_Cook_PM), len(Raw_JFK_Current), Raw_Cook_PM.shape, Raw_JFK_Current.shape,Raw_Cook_PM[0:5],Raw_JFK_Current[0:5] )


        JFK_event_matrix =  {'Event': Event, 'JFK start':Jet_flame_Start, 'JFK end':Jet_flame_End, 'jfk %': JFK_percent, 'JFLK on': jet_flame_on}
        Raw_Event_matrix = {'JFK current': (Raw_JFK_Current), 'JFK voltage':(Raw_JFK_Voltage), 'Kitchen PM': (Raw_Kitchen_PM),'Cook PM':(Raw_Cook_PM), 'Cook Comp':(Raw_Cook_Com)}
        
        Df_JFK_event_matrix = pd.DataFrame(JFK_event_matrix, index= [0])
        DF_Raw_Event_matrix = pd.DataFrame(Raw_Event_matrix)
        print('lengths of the event exports  ',Event, JFK_start,'Size of dataframe: ',Df_JFK_event_matrix.shape, DF_Raw_Event_matrix.shape)

        HH_event_raw_timescale_path = USB_D+":/Malawi 1.1/"+Household_Number+"/Raw Event/"+str(Event)+"_Breakdown.csv"
        
        Df_JFK_event_matrix.to_csv(HH_event_raw_timescale_path,index=False, mode='a')
        DF_Raw_Event_matrix.to_csv(HH_event_raw_timescale_path,index=False, mode='a')

        raw_wattage = list((USB_Power.loc[Jet_flame_Start:Jet_flame_End]))
        Wattage_running_average = Functions_malawi.Running_Average(raw_wattage, 20)
        print('-=-=-=-=-=lengths of the event exports  ', Jet_flame_Start, raw_wattage[0:5],np.average(USB_Power),np.average(raw_wattage), len(raw_wattage),type(Wattage_running_average), type(raw_wattage), type(USB_Energy))
        for tv, a in enumerate(Wattage_running_average): 
            if a < 0: 
                Wattage_running_average[tv] = 0

        r_1, r_2, r_3, r_4, r_5, r_6, r_7, r_8 = Functions_malawi.Counting_regions(Wattage_running_average, max(Wattage_running_average))
        Event_Watt_R_1.append(r_1); Event_Watt_R_2.append(r_2); Event_Watt_R_3.append(r_3)
        Event_Watt_R_4.append(r_4); Event_Watt_R_5.append(r_5); Event_Watt_R_6.append(r_6)
        Event_Watt_R_7.append(r_7);  Event_Watt_R_8.append(r_8) 


        if (IS_there_a_Cook_beacon_proximity == True) and (EVENT_CURRENT_CHECK != 0):
            Beacon_Use_event_number.append(Event)
            #print('==-=-=proximity -- Start Time Value -=-', (Combined_Cooking_start[Event]))
            At_stove,Jet_flame_adjust ,Time_away_from_stove,zero_to_one, zero_to_one_tv, Reaching_to_stove_tv, Going_away_from_stove, Going_away_from_stove_tv = Functions_malawi.Beacon_Movement_change((Combined_Cooking_start[Event]*Log_rate_per_min),Beacon_proximity.loc[(Combined_Cooking_start[Event]*Log_rate_per_min):(Combined_Cooking_end[Event]*Log_rate_per_min)])
            #print('==-=-=proximity-=-=-=-', At_stove, Time_away_from_stove, Reaching_to_stove_tv, Going_away_from_stove, Going_away_from_stove_tv )
            if Event_Length[-1] == Time_away_from_stove/Log_rate_per_min:
                Length_of_time_at_stove.append('No Cook Beacon')
                length_of_time_away_from_stove.append('No Cook Beacon')
                Adjusting_the_jet_flame.append('No Cook Beacon')
                Percentage_away_from_stove_CE.append('No Cook Beacon')
            else:
                Length_of_time_at_stove.append(At_stove/Log_rate_per_min)
                length_of_time_away_from_stove.append(Time_away_from_stove/Log_rate_per_min)
                #Time_at_stove.append(Fuel_time[Reaching_to_stove_tv])
                Adjusting_the_jet_flame.append(Jet_flame_adjust)
                Percentage_away_from_stove_CE.append((int(((length_of_time_away_from_stove[-1])/(Event_Length[-1]))*100)))
    else:
        Event_Average_USB_Current.append("");Event_Median_USB_Voltage.append("")
        Event_Median_USB_Current.append(""); Event_StDeV_USB_Voltage.append("")
        Event_StDeV_USB_Current.append(""); Event_RAW_USB_Voltage.append("")
        Event_RAW_USB_Current.append("");Event_Average_USB_Voltage.append("")
        Event_jet_flame_percent.append("");Event_jet_flame_start_min.append("")
        Event_jet_flame_end_min.append("")
        Time_at_stove.append("")
        Beacon_Use_event_number.append(Event)
        length_of_time_away_from_stove.append("")
        Length_of_time_at_stove.append("")
        Event_jet_flame_time_on.append("")
        Adjusting_the_jet_flame.append("")
        Percentage_away_from_stove_CE.append("")
        Event_Watt_R_1.append(""); Event_Watt_R_2.append(""); Event_Watt_R_3.append("")
        Event_Watt_R_4.append(""); Event_Watt_R_5.append(""); Event_Watt_R_6.append("")
        Event_Watt_R_7.append("");  Event_Watt_R_8.append("") 

    if Cook_Beacon_place == True:
        Event_Avergage_Cook_Beacon_Acceleration.append(np.average(list(set(Cook_Beacon_accel[(Combined_Cooking_start[Event]*Log_rate_per_min):(Combined_Cooking_end[Event]*Log_rate_per_min)]))))
        Event_RAW_Beacon_Cook_accel.append(Cook_Beacon_accel[(Combined_Cooking_start[Event]*Log_rate_per_min):(Combined_Cooking_end[Event]*Log_rate_per_min)])
    else:
        Event_Avergage_Cook_Beacon_Acceleration.append("")
        Event_RAW_Beacon_Cook_accel.append("")

    if Child_Beacon_place == True:
        Event_Average_Child_Beacon_Acceleration.append(np.average(list(set(Child_Beacon_accel[(Combined_Cooking_start[Event]*Log_rate_per_min):(Combined_Cooking_end[Event]*Log_rate_per_min)]))))
        Event_Average_Child_Beacon_Movement.append(np.average(list(set(Child_Beacon_move[(Combined_Cooking_start[Event]*Log_rate_per_min):(Combined_Cooking_end[Event]*Log_rate_per_min)]))))
        Event_RAW_Child_Beacon_Acceleration.append(Child_Beacon_accel[(Combined_Cooking_start[Event]*Log_rate_per_min):(Combined_Cooking_end[Event]*Log_rate_per_min)])
        Event_RAW_Child_Beacon_Movement.append(Child_Beacon_move[(Combined_Cooking_start[Event]*Log_rate_per_min):(Combined_Cooking_end[Event]*Log_rate_per_min)])

    else:
        Event_Average_Child_Beacon_Acceleration.append("")
        Event_Average_Child_Beacon_Movement.append("")
        Event_RAW_Child_Beacon_Acceleration.append("")
        Event_RAW_Child_Beacon_Movement.append("")

   


    #print('<<<<<<<<<<<<<<<<<<<<<<<<<<<',Event,'-----',Event_KG_Removed_Fuel_1[-1],'-----',sum(fuel_bounds_1),' Next Event>>>>>>>>>>>>>>>>>>>>>>>>>>',prev_fuel_bound_1,'+++++',fuel_bounds_1)
    #print('-')
# need to see the averages for the Kitchen Hapex and Firefinder start
#print('-------Before startup metric finder ---', Event_Average_Kitchen_PM, ' <-Kit Hapex PM --- Combing CE Start->' ,Combined_Cooking_start)
#print('Current RAW--', np.average(Event_RAW_USB_Current[3]))
#print('--- Fuel USed for event fuel 1--', len(Event_KG_Removed_Fuel_1), len(Event_KG_Removed_Fuel_2))
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

Approaching_stove  = []
Approaching_stove_tv = []


for Event in Event_counter:
    # If the startup is too large betwene sensor launch and event start, need to modify the first start up event to account for this change
    Start_too_soon = False
    if Event == 0 and (Combined_Cooking_start[Event] - Start_Up_Spread) < 0:
        Startup_place_holder = Start_Up_Spread
        Start_Up_Spread = Combined_Cooking_start[Event]
        Start_too_soon = True
    elif Start_too_soon == True:
        Start_Up_Spread = Startup_place_holder
    else:
        Start_Up_Spread = Start_Up_Spread
    if Kitchen_Hapex_place == True:
        Startup_Average_Kitchen_Compliance.append((int((np.average([a for a in Kitchen_Hapex_Comp[(Combined_Cooking_start[Event]-((Start_Up_Spread))):(Combined_Cooking_start[Event]+1)]]))*100))/100)
        Startup_Average_Kitchen_PM.append((int((np.average([a for a in Kitchen_Hapex_PM[(Combined_Cooking_start[Event]-((Start_Up_Spread))):(Combined_Cooking_start[Event]+1)]]))*100))/100)
        Startup_Median_Kitchen_PM.append((int((np.median([a for a in Kitchen_Hapex_PM[(Combined_Cooking_start[Event]-((Start_Up_Spread))):(Combined_Cooking_start[Event]+1)]]))*100))/100)
        Startup_StDeV_Kitchen_PM.append((int((stat.stdev(Kitchen_Hapex_PM[(Combined_Cooking_start[Event]-((Start_Up_Spread))):(Combined_Cooking_start[Event]+1)])) * 100)) / 100)
    else:
        Startup_Average_Kitchen_Compliance.append(""); Startup_Average_Kitchen_PM.append("")
        Startup_Median_Kitchen_PM.append("");Startup_StDeV_Kitchen_PM.append("")

    if Cook_Hapex_place == True:
        Startup_Average_Cook_Compliance.append((int((np.average([a for a in CooK_Hapex_Comp[(Combined_Cooking_start[Event]-((Start_Up_Spread))):(Combined_Cooking_start[Event]+1)]]))*100))/100)
        Startup_Average_Cook_PM.append((int((np.average([a for a in Cook_Hapex_PM[(Combined_Cooking_start[Event]-((Start_Up_Spread))):(Combined_Cooking_start[Event]+1)]]))*100))/100)
        Startup_Median_Cook_PM.append((int((np.median([a for a in Cook_Hapex_PM[(Combined_Cooking_start[Event]-((Start_Up_Spread))):(Combined_Cooking_start[Event]+1)]]))*100))/100)
        Startup_StDeV_Cook_PM.append((int((stat.stdev(Cook_Hapex_PM[(Combined_Cooking_start[Event]-((Start_Up_Spread))):(Combined_Cooking_start[Event]+1)])) * 100)) / 100)
    else:
        Startup_Average_Cook_Compliance.append(""); Startup_Average_Cook_PM.append("")
        Startup_Median_Cook_PM.append("");Startup_StDeV_Cook_PM.append("")

    if USB_name_place == True:

        Startup_Average_USB_Current.append(np.average(list((USB_Current[((Combined_Cooking_start[Event]*Log_rate_per_min)-(Start_Up_Spread*Log_rate_per_min)):((Combined_Cooking_start[Event]*Log_rate_per_min)+1)]))))
        Startup_Median_USB_Current.append(np.median(list(USB_Current[((Combined_Cooking_start[Event]*Log_rate_per_min)-(Start_Up_Spread*Log_rate_per_min)):((Combined_Cooking_start[Event]*Log_rate_per_min)+1)])))
        Startup_StDeV_USB_Current.append((int((stat.stdev(USB_Current[((Combined_Cooking_start[Event]*Log_rate_per_min)-(Start_Up_Spread*Log_rate_per_min)):((Combined_Cooking_start[Event]*Log_rate_per_min)+1)])) * 100)) / 100)
        Startup_RAW_USB_Current.append(USB_Current[((Combined_Cooking_start[Event]*Log_rate_per_min)-(Start_Up_Spread*Log_rate_per_min)):((Combined_Cooking_start[Event]*Log_rate_per_min)+1)])
        Startup_Average_USB_Voltage.append(np.average(list(set(USB_Voltage[((Combined_Cooking_start[Event]*Log_rate_per_min)-(Start_Up_Spread*Log_rate_per_min)):((Combined_Cooking_start[Event]*Log_rate_per_min)+1)]))))
        Startup_Median_USB_Voltage.append(np.median(list(set(USB_Voltage[((Combined_Cooking_start[Event]*Log_rate_per_min)-(Start_Up_Spread*Log_rate_per_min)):((Combined_Cooking_start[Event]*Log_rate_per_min)+1)]))))
        Startup_StDeV_USB_Voltage.append((int((stat.stdev(USB_Voltage[((Combined_Cooking_start[Event]*Log_rate_per_min)-(Start_Up_Spread*Log_rate_per_min)):((Combined_Cooking_start[Event]*Log_rate_per_min)+1)])) * 100)) / 100)
        Startup_RAW_USB_Voltage.append(USB_Voltage[((Combined_Cooking_start[Event]*Log_rate_per_min)-(Start_Up_Spread*Log_rate_per_min)):((Combined_Cooking_start[Event]*Log_rate_per_min)+1)])
    else: 
        Startup_Average_USB_Current.append("");Startup_Median_USB_Current.append("")
        Startup_StDeV_USB_Current.append(""); Startup_RAW_USB_Current.append(-1)
        Startup_Average_USB_Voltage.append(""); Startup_Median_USB_Voltage.append("")
        Startup_StDeV_USB_Voltage.append("");Startup_RAW_USB_Voltage.append("")

    if Cook_Beacon_place == True:
        Startup_Avergage_Cook_Beacon_Acceleration.append(np.average(list(set(Cook_Beacon_accel[((Combined_Cooking_start[Event]*Log_rate_per_min)-(Start_Up_Spread*Log_rate_per_min)):((Combined_Cooking_start[Event]*Log_rate_per_min)+1)]))))
        Startup_RAW_Cook_Beacon_Acceleration.append(Cook_Beacon_accel[((Combined_Cooking_start[Event]*Log_rate_per_min)-(Start_Up_Spread*Log_rate_per_min)):((Combined_Cooking_start[Event]*Log_rate_per_min)+1)])
    else:
        Startup_Avergage_Cook_Beacon_Acceleration.append("")
        Startup_RAW_Cook_Beacon_Acceleration.append("")
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
        Cooldown_Average_Kitchen_Compliance.append("");Cooldown_Average_Kitchen_PM.append("")
        Cooldown_Median_Kitchen_PM.append("");Cooldown_StDeV_Kitchen_PM.append("")
    if Cook_Hapex_place == True:
        Cooldown_Average_Cook_Compliance.append((int((np.average([a for a in CooK_Hapex_Comp[(Combined_Cooking_end[Event]):(Combined_Cooking_end[Event]+Cooldown_Spread)]]))*100))/100)
        Cooldown_Average_Cook_PM.append((int((np.average([a for a in Cook_Hapex_PM[(Combined_Cooking_end[Event]):(Combined_Cooking_end[Event]+Cooldown_Spread)]]))*100))/100)
        Cooldown_Median_Cook_PM.append((int((np.median([a for a in Cook_Hapex_PM[(Combined_Cooking_end[Event]):(Combined_Cooking_end[Event]+Cooldown_Spread)]]))*100))/100)
        Cooldown_StDeV_Cook_PM.append((int((stat.stdev(Cook_Hapex_PM[(Combined_Cooking_end[Event]):(Combined_Cooking_end[Event]+Cooldown_Spread)])) * 100)) / 100)
    else: 
        Cooldown_Average_Cook_Compliance.append("");Cooldown_Average_Cook_PM.append("")
        Cooldown_Median_Cook_PM.append("");Cooldown_StDeV_Cook_PM.append("")
    if USB_name_place == True:
        Cooldown_Average_USB_Current.append(np.average(list((USB_Current[(Combined_Cooking_end[Event]*Log_rate_per_min):((Combined_Cooking_end[Event]*Log_rate_per_min)+(Cooldown_Spread*Log_rate_per_min))]))))
        Cooldown_Median_USB_Current.append(np.median(list(USB_Current[(Combined_Cooking_end[Event]*Log_rate_per_min):((Combined_Cooking_end[Event]*Log_rate_per_min)+(Cooldown_Spread*Log_rate_per_min))])))
        Cooldown_StDeV_USB_Current.append((int((stat.stdev(USB_Current[(Combined_Cooking_end[Event]*Log_rate_per_min):((Combined_Cooking_end[Event]*Log_rate_per_min)+(Cooldown_Spread*Log_rate_per_min))])) * 100)) / 100)
        Cooldown_RAW_USB_Current.append(USB_Current[(Combined_Cooking_end[Event]*Log_rate_per_min):((Combined_Cooking_end[Event]*Log_rate_per_min)+(Cooldown_Spread*Log_rate_per_min))])
        Cooldown_Average_USB_Voltage.append(np.average(list(set(USB_Voltage[(Combined_Cooking_end[Event]*Log_rate_per_min):((Combined_Cooking_end[Event]*Log_rate_per_min)+(Cooldown_Spread*Log_rate_per_min))]))))
        Cooldown_Median_USB_Voltage.append(np.median(list(set(USB_Voltage[(Combined_Cooking_end[Event]*Log_rate_per_min):((Combined_Cooking_end[Event]*Log_rate_per_min)+(Cooldown_Spread*Log_rate_per_min))]))))
        Cooldown_StDeV_USB_Voltage.append((int((stat.stdev(USB_Voltage[(Combined_Cooking_end[Event]*Log_rate_per_min):((Combined_Cooking_end[Event]*Log_rate_per_min)+(Cooldown_Spread*Log_rate_per_min))])) * 100)) / 100)
        Cooldown_RAW_USB_Voltage.append(USB_Voltage[(Combined_Cooking_end[Event]*Log_rate_per_min):((Combined_Cooking_end[Event]*Log_rate_per_min)+(Cooldown_Spread*Log_rate_per_min))])
    else:
        Cooldown_Average_USB_Current.append("");Cooldown_Median_USB_Current.append("")
        Cooldown_StDeV_USB_Current.append(""); Cooldown_RAW_USB_Current.append("")
        Cooldown_Average_USB_Voltage.append(""); Cooldown_Median_USB_Voltage.append("")
        Cooldown_StDeV_USB_Voltage.append("");Cooldown_RAW_USB_Voltage.append("")

    # Next- Day Breakdown for Each metric

Munute_Day_breakdown = (int(Minute_log_length/(60*24))) * 60*24
Fast_log_rate_day_breakdown = int(len(USB_time)/ (60*24*Log_rate_per_min)) * 60*24*Log_rate_per_min
how_many_days = (int(Minute_log_length/(60*24)))
Day_counter = np.arange(1,how_many_days+1,1)
Minute_Day_Start_TV= np.arange(0,Munute_Day_breakdown+1, (60*24))
Fast_log_rate_day_Start_TV = np.arange(0,Fast_log_rate_day_breakdown, (60*24*Log_rate_per_min))

Minute_Day_End_TV= np.arange((60*24),Munute_Day_breakdown+1+(60*24), (60*24))
Fast_log_rate_day_End_TV = np.arange((60*24*Log_rate_per_min),Fast_log_rate_day_breakdown+1, (60*24*Log_rate_per_min))


# print('are these the minute breakdowns', how_many_days, Minute_Day_Start_TV, Fast_log_rate_day_Start_TV)
# print('are these the minute breakdowns', Day_counter, Minute_Day_End_TV, Fast_log_rate_day_End_TV)
# print('envent numbers',Combined_Cooking_start, Combined_Cooking_end )
Event_per_Day = []
Average_length_of_CE = []
Day_date = []
Event_number_With_JFK = []

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
    JFK_count_E = 0
    #print('Day Breakdowns', Day,Munute_Day_breakdown, Fast_log_rate_day_breakdown, Minute_Day_Start_TV,Minute_Day_End_TV,Minute_log_length)
    Day_date.append(Decrease_to_min_log_length[Minute_Day_Start_TV[Day-1]])
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
    Wattage_column = []
    for E in Event_counter:
        Fuel_title_column.append('----FUEL----')
        HAPEX_title_column.append('----HAPEx----')
        USB_title_column.append('----USB----')
        Beacon_title_column.append('----BEACON----')
        Wattage_column.append('--Wattage--')
        if (Combined_Cooking_end[E] < Minute_Day_End_TV[Day-1]) and (Combined_Cooking_end[E] >  Minute_Day_Start_TV[Day-1]):
            Event_per_Day_count = Event_per_Day_count +1
            EVENT_LENGTH_count.append(Combined_Cooking_end[E]-Combined_Cooking_start[E])
            
            Fuel_1_Event.append(Event_KG_Removed_Fuel_1[E]); Fuel_2_Event.append(Event_KG_Removed_Fuel_2[E])
            if Fuel_2_place == True and Fuel_1_place == True:
                Combined_Fuel.append(Event_KG_Removed_Fuel_1[E]+Event_KG_Removed_Fuel_2[E])
            else:
                Combined_Fuel.append("")
            if Cook_Hapex_place == True:
                Cook_Comp_event.extend(CooK_Hapex_Comp[Combined_Cooking_start[E]:Combined_Cooking_end[E]])
                Cook_PM_event.extend(Cook_Hapex_PM[Combined_Cooking_start[E]:Combined_Cooking_end[E]])
                Cook_Comp_startup.extend(CooK_Hapex_Comp[(Combined_Cooking_start[E]-(Start_Up_Spread)):(Combined_Cooking_start[E]+1)])
                Cook_PM_startup.extend(Cook_Hapex_PM[(Combined_Cooking_start[E]-((Start_Up_Spread))):(Combined_Cooking_start[E]+1)])
                Cook_Comp_Cooldown.extend(CooK_Hapex_Comp[(Combined_Cooking_end[E]):(Combined_Cooking_end[E]+Cooldown_Spread)])
                Cook_PM_Cooldown.extend(Cook_Hapex_PM[(Combined_Cooking_end[E]):(Combined_Cooking_end[E]+Cooldown_Spread)])
            else:
                Cook_Comp_event.extend(""); Cook_PM_event.extend(""); Cook_Comp_startup.extend(""); Cook_PM_startup.extend(""); Cook_Comp_Cooldown.extend(""); Cook_PM_Cooldown.extend("")

            if Kitchen_Hapex_place == True:
                Kit_Comp_event.extend(Kitchen_Hapex_Comp[Combined_Cooking_start[E]:Combined_Cooking_end[E]])
                Kit_PM_event.extend(Kitchen_Hapex_PM[Combined_Cooking_start[E]:Combined_Cooking_end[E]])
                Kit_Comp_startup.extend(Kitchen_Hapex_Comp[(Combined_Cooking_start[E]-((Start_Up_Spread))):(Combined_Cooking_start[E]+1)])
                Kit_PM_startup.extend(Kitchen_Hapex_PM[(Combined_Cooking_start[E]-((Start_Up_Spread))):(Combined_Cooking_start[E]+1)])
                Kit_Comp_Cooldown.extend(Kitchen_Hapex_Comp[(Combined_Cooking_end[E]):(Combined_Cooking_end[Event]+Cooldown_Spread)])
                Kit_PM_Cooldown.extend(Kitchen_Hapex_PM[(Combined_Cooking_end[E]):(Combined_Cooking_end[E]+Cooldown_Spread)])
            else:
                Kit_Comp_event.extend(""); Kit_PM_event.extend(""); Kit_Comp_startup.extend(""); Kit_PM_startup.extend(""); Kit_Comp_Cooldown.extend(""); Kit_PM_Cooldown.extend("")      
            
            if (USB_name_place == True) and (Event_Average_USB_Current[E] != 0):
                USB_Current_Event.extend(Event_RAW_USB_Current[E]); USB_Voltage_Event.extend(Event_RAW_USB_Voltage[E])
                USB_Current_Startup.extend(Startup_RAW_USB_Current[E])  ; USB_Voltage_Startup.extend(Startup_RAW_USB_Voltage[E])
                USB_Current_Cooldown.extend(Cooldown_RAW_USB_Current[E]) ; USB_Voltage_Cooldown.extend(Cooldown_RAW_USB_Voltage[E])
                JFK_count_E = JFK_count_E + 1
            else:
                USB_Current_Event.extend(""); USB_Voltage_Event.extend(""); USB_Current_Startup.extend(""); USB_Voltage_Startup.extend("");USB_Current_Cooldown.extend("");USB_Voltage_Cooldown.extend("")

            if Cook_Beacon_place == True:
                Beacon_Cook_accel_Event.extend(Event_RAW_Beacon_Cook_accel[E])
                #Beacon_Cook_move_Event.extend(Event_RAW_Child_Beacon_Movement[E])
            else:
                Beacon_Cook_accel_Event.extend("");# Beacon_Cook_move_Event = ""
            if Child_Beacon_place == True:
                Beacon_Cook_accel_startup.extend(Startup_RAW_Cook_Beacon_Acceleration[E])
                Beacon_Child_accel_Event.extend(Event_RAW_Child_Beacon_Acceleration[E])
            else:
                Beacon_Cook_accel_startup.extend(""); Beacon_Child_accel_Event.extend("")

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
        Average_Cook_PM_per_day.append("")
        Average_Cook_Comp_per_day.append("")


    if Kitchen_Hapex_place == True:
        Average_Kitchen_Comp_per_day.append(np.average(Kitchen_Hapex_Comp[Minute_Day_Start_TV[Day-1]:Minute_Day_End_TV[Day-1]]))
        Average_Kitchen_PM_per_day.append(np.average(Kitchen_Hapex_PM[Minute_Day_Start_TV[Day-1]:Minute_Day_End_TV[Day-1]]))
    else:
        Average_Kitchen_Comp_per_day.append("")
        Average_Kitchen_PM_per_day.append("")

    #Hapex Compliance for Start up and Cooldown
    Average_Kitchen_Comp_per_day_per_startup.append(np.average(Kit_Comp_startup)) ; Average_Cook_Comp_per_day_per_startup.append(np.average(Cook_Comp_startup)) 
    Average_Kitchen_Comp_per_day_per_cooldown.append(np.average(Kit_Comp_Cooldown)); Average_Cook_Comp_per_day_per_cooldown.append(np.average(Cook_Comp_Cooldown))
    #Hapex PM for Startup and Cooldown
    Average_Kitchen_PM_per_day_per_startup.append(np.average(Kit_PM_startup)) ; Average_Cook_PM_per_day_per_startup.append(np.average(Cook_PM_startup)) 
    Average_Kitchen_PM_per_day_per_cooldown.append(np.average(Kit_PM_Cooldown)); Average_Cook_PM_per_day_per_cooldown.append(np.average(Cook_PM_Cooldown))
    #Fuel Metrics
    #First Fuel
    if Fuel_1_place == True:
        fuel_bounds_Day_1 = list(set(KG_burned_1[(Minute_Day_Start_TV[Day-1]*Log_rate_per_min):(Minute_Day_End_TV[Day-1]*Log_rate_per_min)]))
        if Day !=1:
            if fuel_bounds_Day_1[0] == Previous_day_fuel_1:
                Sum_Fuel_1_removed_per_day_per_event.append(sum(Fuel_1_Event[1:]))
                Fuel_1_Removed_per_day.append((int((sum(fuel_bounds_Day_1[1:])) * 1000) / 1000))
            else:
                Sum_Fuel_1_removed_per_day_per_event.append(sum(Fuel_1_Event))
                Fuel_1_Removed_per_day.append((int((sum(fuel_bounds_Day_1)) * 1000) / 1000))
        else:
            Sum_Fuel_1_removed_per_day_per_event.append(sum(Fuel_1_Event))
            Fuel_1_Removed_per_day.append((int((sum(fuel_bounds_Day_1)) * 1000) / 1000))
        Previous_day_fuel_1 = fuel_bounds_Day_1[-1]
    else:
        Fuel_1_Removed_per_day.append("")
        Sum_Fuel_1_removed_per_day_per_event.append("")
    #Second Fuel
    if Fuel_2_place == True:
        fuel_bounds_Day_2 = list(set(KG_burned_2[(Minute_Day_Start_TV[Day-1]*Log_rate_per_min):(Minute_Day_End_TV[Day-1]*Log_rate_per_min)]))
        if Day !=1:
            if fuel_bounds_Day_2[0] == Previous_day_fuel_2:
                Sum_Fuel_2_removed_per_day_per_event.append(sum(Fuel_2_Event[1:]))
                Fuel_2_Removed_per_day.append((int((sum(fuel_bounds_Day_2[1:])) * 1000) / 1000))
            else:
                Sum_Fuel_2_removed_per_day_per_event.append(sum(Fuel_2_Event))
                Fuel_2_Removed_per_day.append((int((sum(fuel_bounds_Day_2)) * 1000) / 1000))
        else:
            Sum_Fuel_2_removed_per_day_per_event.append(sum(Fuel_2_Event))
            Fuel_2_Removed_per_day.append((int((sum(fuel_bounds_Day_2)) * 1000) / 1000))
        Previous_day_fuel_2 = fuel_bounds_Day_2[-1]
    else:
        Fuel_2_Removed_per_day.append("")
        Sum_Fuel_2_removed_per_day_per_event.append("")
    #Combine Fuel
    if Fuel_2_place == True and Fuel_1_place == True:
        Sum_Combined_Fuel_removed_per_day_per_event.append(sum(Fuel_1_Event)+sum(Fuel_2_Event))  ; Combined_Fuel_Removed_per_day.append(Fuel_2_Removed_per_day[-1]+Fuel_1_Removed_per_day[-1])
    else:
        Sum_Combined_Fuel_removed_per_day_per_event.append(""); Combined_Fuel_Removed_per_day.append("")

    #USB Power meter
    Average_USB_Current_per_Event.append(np.average(USB_Current_Event)) ; Average_USB_Voltage_per_Event.append(np.average(USB_Voltage_Event))
    Average_USB_Current_per_Startup.append(np.average(USB_Current_Startup)) ; Average_USB_Voltage_per_Startup.append(np.average(USB_Voltage_Startup))
    Average_USB_Current_per_Cooldown.append(np.average(USB_Current_Cooldown)) ; Average_USB_Voltage_per_cooldown.append(np.average(USB_Voltage_Cooldown))
    if USB_Current_Event != 0:
        Event_number_With_JFK.append(JFK_count_E)
    else:
        Event_number_With_JFK.append("")
    #Beacon
    Average_Beacon_Cook_Accel_per_day_per_event.append(np.average(Beacon_Cook_accel_Event))
    Average_Beacon_Child_Accel_per_day_per_event.append(np.average(Beacon_Child_accel_Event))
    Average_Beacon_Child_Move_per_day_per_event.append(np.average(Beacon_Cook_move_Event))
    Average_Beacon_Cook_Accel_per_startup.append(np.average(Beacon_Cook_accel_startup))
    if Child_Beacon_place == True:
        Average_Beacon_Child_Accel_per_Day.append(np.average(Child_Beacon_accel[((Minute_Day_Start_TV[Day-1])*Log_rate_per_min):((Minute_Day_End_TV[Day-1])*Log_rate_per_min)]))
        Average_Beacon_Child_Move_per_Day.append(np.average(Child_Beacon_move[((Minute_Day_Start_TV[Day-1])*Log_rate_per_min):((Minute_Day_End_TV[Day-1])*Log_rate_per_min)]))
    else:
        Average_Beacon_Child_Accel_per_Day.append("")
        Average_Beacon_Child_Move_per_Day.append("")
    if Cook_Beacon_place == True:
        Average_Beacon_Cook_Accel_per_Day.append(np.average(Cook_Beacon_accel[((Minute_Day_Start_TV[Day-1])*Log_rate_per_min):((Minute_Day_End_TV[Day-1])*Log_rate_per_min)]))
    else:
        Average_Beacon_Cook_Accel_per_Day.append("")

# print('events per day---------',Event_per_Day )

#Exporting Metrics to CSV
Dict_sensors = {'~Exact 1~': [Exact_1], '~Exact 2~':[Exact_2], '~Cook HAPEx~':[Cook_Hapex], 
'~Kitchen HAPEx~':[Kitchen_Hapex], '~Fuel 1~':[Fuel_1], '~Fuel 2~':[Fuel_2],'~USB~':[USB_name], '~Cook Beacon~':[Cook_beacon],'~Child Beacon~':[Child_beacon]}
DF_Dict_sensors = pd.DataFrame(Dict_sensors)

Dict_Event = {'|Event|': Event_counter, '|Start Time|':Event_start_time, '|End Time|':Event_End_time,'|Length of Event|':Event_Length,'----FUEL----':Fuel_title_column[0:(len(Event_counter)+1)],'|Fuel 1 Removed|': Event_KG_Removed_Fuel_1, 
'|Fuel 2 Removed|': Event_KG_Removed_Fuel_2, '|Combined Fuel Removed|':Event_KG_Combined_Fuel, '----HAPEx----':HAPEX_title_column[0:(len(Event_counter)+1)],'|Avg. Kitchen Comp|':Event_Average_Kitchen_Compliance,'|Avg. Cook Comp|':Event_Average_Cook_Compliance,
   '|Average Kitchen PM|':Event_Average_Kitchen_PM, '|Average Cook PM|':Event_Average_Cook_PM,'|Median Kitchen PM|':Event_Median_Kitchen_PM,
   '|Median Cook PM|':Event_Median_Cook_PM, '|StDev Kitchen PM|':Event_StDeV_Kitchen_PM, '|StDev Cook PM|':Event_StDeV_Cook_PM,'|Cook Beacon Acceleration|':Event_Avergage_Cook_Beacon_Acceleration,
   '----BEACON----':Beacon_title_column[0:(len(Event_counter)+1)],'|Child Beacon Accleration|': Event_Average_Child_Beacon_Acceleration, '|Child Beacon Movement|':Event_Average_Child_Beacon_Movement, '----USB----':USB_title_column[0:(len(Event_counter)+1)],'|Avg. USB Current|':Event_Average_USB_Current,
   '|Median USB Current|':Event_Median_USB_Current, '|StDev USB Current|':Event_StDeV_USB_Current,'|Avg. USB Voltage|':Event_Average_USB_Voltage,
    '|Median USB Voltage|':Event_Median_USB_Voltage, '|StDev USB Voltage|':Event_StDeV_USB_Voltage,'|Jet Flame on for ~(min)|':Event_jet_flame_time_on,'|Jet Flame Percentage(%)|':Event_jet_flame_percent,
    '|Jet Flame Start from Fire (min)|':Event_jet_flame_start_min, '|Jet Flame End from Fire end (min)|':Event_jet_flame_end_min,'|Time at Stove (Min)|': Length_of_time_at_stove,'|Time Away from Stove (Min)|':length_of_time_away_from_stove, 
    '|# of times adjusting the Jet flame|':Adjusting_the_jet_flame, '|Percent away from stove durring FF CE|':Percentage_away_from_stove_CE, '--Wattage--':Wattage_column[0:(len(Event_counter)+1)],'|0.75 - 1|':Event_Watt_R_1, '|1 - 1.5|':Event_Watt_R_2,
    '|1.5 - 1.75|':Event_Watt_R_3, '|1.75 - 2|':Event_Watt_R_4, '|2 - 2.25|':Event_Watt_R_5, '|2.25 - 2.5|':Event_Watt_R_6, '|2.5 - 2.75|':Event_Watt_R_7, '|2.75 - 3|':Event_Watt_R_8}


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

Dict_Day = {'|Day|': Day_counter,'|Day Date|':Day_date,'|Number of Events for the day|':Event_per_Day,'|Jet Flame Use For Number of Events|':Event_number_With_JFK,'|Average length of Cooking Length (min)|':Average_length_of_CE,'----FUEL----':Fuel_title_column[0:(len(Day_counter))],
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
DF_Dict_Day= pd.DataFrame(Dict_Day)
# print('-------len check -----', HAPEX_title_column[0:(len(Day_counter))], len(Day_date), len(Beacon_title_column[0:(len(Day_counter))]), len(Average_Cook_Comp_per_day), USB_title_column[0:(len(Day_counter))], len(Average_Cook_Comp_per_day_per_startup),len(Fuel_title_column[0:(len(Day_counter))]))
Event_Proximity = {'|Time date at Stove|':Time_at_stove}

#'|Event Number|':Beacon_Use_event_number, 
#
#print('proximity dtatframe', Event_Proximity)
#print('Time Vlaue for tending: ', Time_at_stove)
Df_Event_Proximity = pd.DataFrame(Event_Proximity)
print('DONE WITH FILE.....')




Path_Raw_Events = USB_D+":/Malawi 1.1/"+Household_Number+"_KPT_Summary_with_Wattage_useage"+KPT_NUM+".csv"
Path_Proximity = USB_D+":/Malawi 1.1/"+Household_Number+"_KPT_Beacon_Proximity_"+KPT_NUM+".csv"
#Path_Raw_Event = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_"+str(q)+"_exact"
#File_event_Raw_metrics = str(Path_Raw_Event) + "/Raw_E_metrics/"+Phase+"_HH_raw_Event_metrics_"+str(id_number)+"_"+str(q)+"_exact_1.11"+".csv"
# Df_sensor.to_csv(File_event_Raw_metrics)
# Df_raw_event.to_csv(File_event_Raw_metrics,index=False,mode='a')


# DF_Dict_sensors.to_csv(Path_Raw_Events,index=False, mode='a')
DF_Dict_Event.to_csv(Path_Raw_Events,index=False, mode='a')
# #Df_Event_Proximity.to_csv(Path_Proximity,index=False, mode='a')
# DF_Dict_Startup.to_csv(Path_Raw_Events,index=False, mode='a')
# DF_Dict_Cooldown.to_csv(Path_Raw_Events,index=False, mode='a')
# DF_Dict_Day.to_csv(Path_Raw_Events,index=False, mode='a')