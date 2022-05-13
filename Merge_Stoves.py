
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
from pathlib import Path, PureWindowsPath
import Functions_malawi

# the first step is to get the time Values for a double stove Household.


Phase = "4N"
start_spread = 10
cooldown_Length = 30

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


if Phase  == ("2N") or Phase == "3N" or Phase == "3N" or Phase == "4N":
    cooking_threshold = 5
    length_decrease = 40
    start_threshold = 1
    end_threshold = -5
    merge_CE_threshold = 60
    min_CE_length = 5
    window_slope = 8
else:
    cooking_threshold = 1
    length_decrease = 10
    start_threshold = 1
    end_threshold = -5
    merge_CE_threshold = 40
    min_CE_length = 8
    window_slope = 12

os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+ Phase +"/Compiler_1_exact/HH_summary_Event")

Day_met_path = os.getcwd()
csv_R_m = glob.glob(os.path.join(Day_met_path, "*.csv"))

Hosuehold = []
total_cooking_time = []
Average_events_per_day = []
Percentage_cooking = []
Average_Event_length = []
Number_of_events = []

Total_Average_Cook_PM_per_Event = []
Total_Average_Kitchen_PM_per_Event = []
Total_Medain_Cook_PM_per_Event = []
Total_Median_Kitchen_PM_per_Event = []
Total_STD_Cook_PM_per_Event = []
Total_STD_Kitchen_PM_per_Event = []
Total_Percentage_Cook_Compliance = []
Total_Percentage_Kitchen_Compliance =[]


Total_Fuel_Used_for_events_Non_filtered = []
Total_Fuel_removed_before_event = []
#Start up
Total_Median_Kitchen_Start_up_PM = []
Total_Average_Kitchen_Startup_PM = [] 
Total_Std_Kitchen_Start_Up_PM = []
Total_Median_Cook_Start_up_PM = []
Total_Average_Cook_Startup_PM = [] 
Total_Std_Cook_Start_Up_PM = []
#coolDown
Total_Median_Kitchen_Cooldown_PM = []
Total_Average_Kitchen_Cooldown_PM = []
Total_STD_Kitchen_Cooldown_PM = []
Total_Median_Cook_Cooldown_PM = []
Total_Average_Cook_Cooldown_PM = []
Total_STD_Cook_Cooldown_PM = []

Total_Start_Up_minutes_Collected = []
Total_Cooldown_minutes_Collected = []

Total_Sum_Start_up_Kitchen = []
Total_Sum_Start_up_Cook = []

Total_Sum_Cooldown_Cook = []
Total_Sum_Cooldown_Kitchen = []

Spacer_for_data_frame = []

count_hh = 0
for file in csv_R_m:
    count_hh = 1 + count_hh
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        hh_gimme = reader(f)
        header = next(hh_gimme)
        if header != None:
            for rrrr, rows in enumerate(hh_gimme):
                if rrrr == 0:
                    Household = rows[1]
                    print('the household id number is:  ',  (rows[1]))
        for idx, row in enumerate(csv_reader):
            if '| Event Number |' in row:
                data_start= idx
                break

        
        get_me_data = (pd.read_csv(file, skiprows=2 ))
        #print('-----------------  ',  get_me_data.iloc[0, 3])
        stove_1_start_times = get_me_data.iloc[:, 3]
        stove_1_end_times = get_me_data.iloc[:, 4]

        # Certify that the household is using the second stove

        for ttt in exact_2_hh:
            Cooking_minute_2 = []
            if int(Household) == ttt: 
                stove_2_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+ Phase +"/Compiler_2_exact/HH_summary_Event/"+Phase+"_HH_Summary_Event_"+str(Household)+"_2_exact_1.11.csv"
                second_exact_2 = pd.read_csv(stove_2_path,  skiprows=2)
                stove_2_start_times = second_exact_2.iloc[:, 3]
                stove_2_end_times = second_exact_2.iloc[:, 4]
                second_exact = 1
                break
            else:
                second_exact = 0
                stove_2_start_times = []
        #print('Time vlaues for both starts',stove_1_start_times,stove_2_start_times, 'Time values for both end',stove_1_end_times, stove_2_end_times)

        #Clariffy: Start and end varriables for each stove are the same length. Or, stove 1 and stove 2 can have different overall lengths, but their individaul start and end are the same array lengths 
        if second_exact != 0:
            if len(stove_1_start_times) > len(stove_2_start_times):
                Greatest_event_stove_start = stove_1_start_times
                Greatest_event_stove_end = stove_1_end_times

                Least_event_stove_start = stove_2_start_times
                Least_event_stove_end = stove_2_end_times
            elif len(stove_1_start_times) < len(stove_2_start_times):
                Greatest_event_stove_start = stove_2_start_times
                Greatest_event_stove_end = stove_2_end_times
                Least_event_stove_start = stove_1_start_times
                Least_event_stove_end = stove_1_end_times
            else:
                Greatest_event_stove_start = stove_1_start_times
                Greatest_event_stove_end = stove_1_end_times
                Least_event_stove_start = stove_2_start_times
                Least_event_stove_end = stove_2_end_times
        else:
            Greatest_event_stove_start = stove_1_start_times
            Greatest_event_stove_end = stove_1_end_times

        #MERGING: if stove cooking events overlay, combine to new Time Value complete stove in variible - "Merged_Stoves_start" and Merged_Stove_end" 
        #New Time Values are going to be used for raw dauly metrics to get complete metrics

        Collection_length = np.arange(0, Greatest_event_stove_end.iloc[-1]+cooldown_Length +1, 1)

        
        if second_exact != 0:
            Greatest_event_stove = []
            Greatest_event_count = 0
            No_more_cooking = 0
            for tv in Collection_length:
                if No_more_cooking == 0:
                    if (tv >= int(Greatest_event_stove_start[Greatest_event_count])) and (tv <= int(Greatest_event_stove_end[Greatest_event_count])):
                        Greatest_event_stove.append(1)
                    elif (tv > int(Greatest_event_stove_end[Greatest_event_count])) or tv == Greatest_event_stove_end.iloc[-1]:
                        if Greatest_event_count + 1 == len(Greatest_event_stove_end):
                            No_more_cooking = 1
                        elif Greatest_event_count <=  len(Greatest_event_stove_end):
                            Greatest_event_count = Greatest_event_count + 1 
                            Greatest_event_stove.append(1)
                    else:
                        Greatest_event_stove.append(0)
                else:
                    Greatest_event_stove.append(0)

            #print(len(Greatest_event_stove_end),len(Greatest_event_stove), Greatest_event_count)

            Collection_length_least = np.arange(0, Least_event_stove_end.iloc[-1]+cooldown_Length +1, 1)
            Least_event_stove = []
            Least_event_count = 0
            No_more_cooking = 0
            for tv in Collection_length_least:
                if No_more_cooking == 0:
                    if (tv >= int(Least_event_stove_start[Least_event_count])) and (tv <= int(Least_event_stove_end[Least_event_count])):
                        Least_event_stove.append(1)
                    elif (tv > int(Least_event_stove_end[Least_event_count])) or tv == Least_event_stove_end.iloc[-1]:
                        if Least_event_count + 1 == len(Least_event_stove_end):
                            No_more_cooking = 1
                        elif Least_event_count <=  len(Least_event_stove_end):
                            Least_event_count = Least_event_count + 1 
                            Least_event_stove.append(1)
                    else:
                        Least_event_stove.append(0)
                else:
                    Least_event_stove.append(0)

            #print(len(Least_event_stove_end),len(Least_event_stove), Least_event_count)

            Merged_Stove_combined_Array = []
            if len(Greatest_event_stove) > len(Least_event_stove):
                Greatest_stove_length = Greatest_event_stove
                least_stove_length = Least_event_stove
            else:
                Greatest_stove_length = Least_event_stove
                least_stove_length = Greatest_event_stove

            Merged_Stove_combined_Array = []
            no_more_less_used_stove = 0
            for tvv, cooking in enumerate(Greatest_stove_length):
                if no_more_less_used_stove == 0:
                    if tvv > len(least_stove_length)-1:
                        Merged_Stove_combined_Array.append(cooking)
                        no_more_less_used_stove = 1
                    elif cooking == 1:
                        Merged_Stove_combined_Array.append(cooking)
                    elif least_stove_length[tvv] == 1:
                        Merged_Stove_combined_Array.append(least_stove_length[tvv])
                    else:
                        Merged_Stove_combined_Array.append(cooking)
                else:
                    Merged_Stove_combined_Array.append(cooking)
        else: 
            Merged_Stove_combined_Array = []
            Greatest_event_count = 0
            No_more_cooking = 0
            for tv in Collection_length:
                if No_more_cooking == 0:
                    if (tv >= int(Greatest_event_stove_start[Greatest_event_count])) and (tv <= int(Greatest_event_stove_end[Greatest_event_count])):
                        Merged_Stove_combined_Array.append(1)
                    elif (tv > int(Greatest_event_stove_end[Greatest_event_count])) or tv == Greatest_event_stove_end.iloc[-1]:
                        if Greatest_event_count + 1 == len(Greatest_event_stove_end):
                            No_more_cooking = 1
                        elif Greatest_event_count <=  len(Greatest_event_stove_end):
                            Greatest_event_count = Greatest_event_count + 1 
                            Merged_Stove_combined_Array.append(1)
                    else:
                        Merged_Stove_combined_Array.append(0)
                else:
                    Merged_Stove_combined_Array.append(0)




        print('length of the merged stove---', len(Merged_Stove_combined_Array))
        #going to use combined stove to get to the start and end values
        Merged_Stoves_start = []
        Merged_Stoves_end = []
        for nexx, a in enumerate(Merged_Stove_combined_Array):
            if nexx + 1 == len(Merged_Stove_combined_Array) - 1:
                break
            elif a == 0 and Merged_Stove_combined_Array[nexx + 1] == 1:
                Merged_Stoves_start.append(nexx + 1)
            elif a == 1 and  Merged_Stove_combined_Array[nexx + 1] == 0:
                Merged_Stoves_end.append(nexx)


        # getting the raw day metrics for the combined stoves
        RAW_day_Path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+ Phase +"/Compiler_1_exact/Raw_D_metrics/"+Phase+"_HH_raw_Day_metrics_"+str(Household)+"_1_exact_3.55555.csv"
        RAW_day = pd.read_csv(RAW_day_Path,  skiprows=2)
        Fuel = RAW_day.iloc[:, 0]
        Temperature = RAW_day.iloc[:,4]
        Cook_compliance = RAW_day.iloc[:, 5]
        Kitchen_Compliance = RAW_day.iloc[:, 6]
        Cook_PM = RAW_day.iloc[:, 7]
        Kitchen_PM = RAW_day.iloc[:, 8]

        if Fuel[3] == -1:
            no_fuel = 1
        else:
            no_fuel = 0

        Fuel_Removed, mean_count_Fuel = Functions_malawi.FUEL_REMOVAL(Fuel, 0.005, 5, no_fuel)
        Fuel_removal_countdown = Functions_malawi.FuelRemovalTime(Fuel_Removed,no_fuel)
        print('cook pm', Cook_PM[4])
        
        
        Average_Cook_PM_per_Event = []
        Average_Kitchen_PM_per_Event = []
        Medain_Cook_PM_per_Event = []
        Median_Kitchen_PM_per_Event = []
        STD_Cook_PM_per_Event = []
        STD_Kitchen_PM_per_Event = []
        Percentage_Cook_Compliance = []
        Percentage_Kitchen_Compliance =[]


        Fuel_Used_for_events_Non_filtered = []

        #Start up
        Median_Kitchen_Start_up_PM = []
        Average_Kitchen_Startup_PM = [] 
        Std_Kitchen_Start_Up_PM = []
        Median_Cook_Start_up_PM = []
        Average_Cook_Startup_PM = [] 
        Std_Cook_Start_Up_PM = []
        #coolDown
        Median_Kitchen_Cooldown_PM = []
        Average_Kitchen_Cooldown_PM = []
        STD_Kitchen_Cooldown_PM = []
        Median_Cook_Cooldown_PM = []
        Average_Cook_Cooldown_PM = []
        STD_Cook_Cooldown_PM = []

        Start_Up_minutes_Collected = []
        Cooldown_minutes_Collected = []
        length_of_event = []
        Sum_Start_up_Kitchen = []
        Sum_Start_up_Cook = []

        Sum_Cooldown_Cook = []
        Sum_Cooldown_Kitchen = []

        RAW_EVENT_KITCHEN_PM = []
        RAW_EVENT_Cook_PM = [] 
        Raw_Tempterature_event = []
        Raw_Kitchen_start_up = []
        Raw_Cook_start_up = []
        Raw_Kitchen_cooldown = []
        Raw_Cook_cooldown = []
        

        Raw_Combined_Kitchen_Hapex = []
        Raw_Combined_Temperature = []
        Raw_Fuel_removal_Events_combined = []
        Raw_Cook_Compliance = []
        Raw_Kitchen_Compliance = []


        Whole_Kitchen_hapex_Min_tv = []
        Whole_Kitchen_hapex_Min_count = []
        Whole_Kitchen_hapex_Max_tv = []
        Whole_Kitchen_hapex_Max_count = []

        Whole_Temperture_Min_tv = []
        Whole_Temperture_Min_count = []
        Whole_Temperture_Max_tv = []
        Whole_Temperture_Max_count = []

        Fuel_removed_before_firefinder = []
        Raw_Fuel_removed_before_event = []
        event_num = 0
        for time_value, start in enumerate(Merged_Stoves_start):

            Average_Cook_PM_per_Event.append((int((np.average([a for a in Cook_PM[start:Merged_Stoves_end[time_value]]]))*10))/10)
            Average_Kitchen_PM_per_Event.append((int((np.average([a for a in Kitchen_PM[start:Merged_Stoves_end[time_value]]]))*10))/10)
            Medain_Cook_PM_per_Event.append((int((np.median([a for a in Cook_PM[start:Merged_Stoves_end[time_value]]]))*10))/10)
            Median_Kitchen_PM_per_Event.append((int((np.median([a for a in Kitchen_PM[start:Merged_Stoves_end[time_value]]]))*10))/10)
            STD_Cook_PM_per_Event.append((int((np.std([a for a in Cook_PM[start:Merged_Stoves_end[time_value]]]))*10))/10)
            STD_Kitchen_PM_per_Event.append((int((np.std([a for a in Kitchen_PM[start:Merged_Stoves_end[time_value]]]))*10))/10)
            Percentage_Cook_Compliance.append((int(((sum([a for a in Cook_compliance[start:Merged_Stoves_end[time_value]]]))/(Merged_Stoves_end[time_value]-start))*100)))
            Percentage_Kitchen_Compliance.append((int(((sum([a for a in Kitchen_Compliance[start:Merged_Stoves_end[time_value]]]))/(Merged_Stoves_end[time_value]-start))*100)))
            count_fuel = []
           
            end_event = 0
            if no_fuel != 1:
                EVENT_FUEL_REMOVED = list(Fuel_Removed[(start - start_spread):Merged_Stoves_end[time_value]])
                Raw_Fuel_removed_before_event.append(Fuel_removal_countdown[(start - start_spread)])
                for f_tv, f in enumerate(EVENT_FUEL_REMOVED):
                    if f_tv + 1 == len(EVENT_FUEL_REMOVED):
                        if f != EVENT_FUEL_REMOVED[-1]:
                            count_fuel.append(f)
                            end_event = 1
                        break
                    elif f != EVENT_FUEL_REMOVED[f_tv+1] and end_event == 0:
                        count_fuel.append(f)
                Fuel_Used_for_events_Non_filtered.append(sum(count_fuel))
            else:
                count_fuel.append(-1)
                Raw_Fuel_removed_before_event.append(-1)
                Fuel_Used_for_events_Non_filtered.append(-1)
            
            #Start up
            Median_Kitchen_Start_up_PM.append((int((np.median([a for a in Kitchen_PM[(start - start_spread): start]]))*10))/10)
            Average_Kitchen_Startup_PM.append((int((np.average([a for a in Kitchen_PM[(start - start_spread): start]]))*10))/10)
            length_of_event.append(Merged_Stoves_end[time_value]-start)
            
            Std_Kitchen_Start_Up_PM.append(np.std([a for a in Kitchen_PM[(start - start_spread): start]]))
            Median_Cook_Start_up_PM.append(np.median([a for a in Cook_PM[(start - start_spread): start]]))
            Average_Cook_Startup_PM.append(np.average([a for a in Cook_PM[(start - start_spread): start]]))
            Std_Cook_Start_Up_PM.append(np.std([a for a in Cook_PM[(start - start_spread): start]]))
            #CoolDown
            Median_Kitchen_Cooldown_PM.append(np.median([a for a in Kitchen_PM[Merged_Stoves_end[time_value]:(Merged_Stoves_end[time_value] + cooldown_Length)]]))
            Average_Kitchen_Cooldown_PM.append(np.average([a for a in Kitchen_PM[Merged_Stoves_end[time_value]:(Merged_Stoves_end[time_value] + cooldown_Length)]]))
            STD_Kitchen_Cooldown_PM.append(np.std([a for a in Kitchen_PM[Merged_Stoves_end[time_value]:(Merged_Stoves_end[time_value] + cooldown_Length)]]))
            Median_Cook_Cooldown_PM.append(np.median([a for a in Cook_PM[Merged_Stoves_end[time_value]:(Merged_Stoves_end[time_value] + cooldown_Length)]]))
            Average_Cook_Cooldown_PM.append(np.average([a for a in Cook_PM[Merged_Stoves_end[time_value]:(Merged_Stoves_end[time_value] + cooldown_Length)]]))
            STD_Cook_Cooldown_PM.append(np.std([a for a in Cook_PM[Merged_Stoves_end[time_value]:(Merged_Stoves_end[time_value] + cooldown_Length)]]))

            RAW_EVENT_KITCHEN_PM.extend([a for a in Kitchen_PM[start:Merged_Stoves_end[time_value]]])
            RAW_EVENT_Cook_PM.extend([a for a in Cook_PM[start:Merged_Stoves_end[time_value]]])
            Raw_Tempterature_event.extend([a for a in Temperature[start:Merged_Stoves_end[time_value]]])

            Raw_Kitchen_start_up.extend(Kitchen_PM[(start - start_spread): start])
            Raw_Cook_start_up.extend([a for a in Cook_PM[(start - start_spread): start]])
            Raw_Kitchen_cooldown.extend([a for a in Kitchen_PM[Merged_Stoves_end[time_value]:(Merged_Stoves_end[time_value] + cooldown_Length)]])
            Raw_Cook_cooldown.extend([a for a in Cook_PM[Merged_Stoves_end[time_value]:(Merged_Stoves_end[time_value] + cooldown_Length)]])

            Raw_Combined_Kitchen_Hapex.extend(([a for a in Kitchen_PM[(start - start_spread):  (Merged_Stoves_end[time_value] + cooldown_Length)]]))
            Raw_Combined_Temperature.extend([a for a in Temperature[(start - start_spread):  (Merged_Stoves_end[time_value] + cooldown_Length)]])
            Raw_Fuel_removal_Events_combined.extend(Fuel_Used_for_events_Non_filtered)
            Raw_Cook_Compliance.extend([a for a in Cook_compliance[start:Merged_Stoves_end[time_value]]])
            Raw_Kitchen_Compliance.extend([a for a in Kitchen_Compliance[start:Merged_Stoves_end[time_value]]])


            #this section is for steady state and max value --- going to have to be put in later or next

            Start_Up_minutes_Collected.append(len(Kitchen_PM[(time_value - start_spread): time_value]))
            Cooldown_minutes_Collected.append(len(Kitchen_PM[Merged_Stoves_end[time_value]:(Merged_Stoves_end[time_value] + cooldown_Length)]))
        
            Sum_Start_up_Kitchen.append(sum(Kitchen_PM[(time_value - start_spread): time_value]))
            Sum_Start_up_Cook.append(sum(Cook_PM[(time_value - start_spread): time_value]))
            if no_fuel != 1:
                Fuel_removed_before_firefinder.append(Fuel_removal_countdown[start])
            else:
                Fuel_removed_before_firefinder.append(-1)

            Sum_Cooldown_Cook.append(sum(Kitchen_PM[Merged_Stoves_end[time_value]:(Merged_Stoves_end[time_value] + cooldown_Length)]))
            Sum_Cooldown_Kitchen.append(sum(Cook_PM[Merged_Stoves_end[time_value]:(Merged_Stoves_end[time_value] + cooldown_Length)]))

            #print('median startup- ',Median_Kitchen_Start_up_PM[event_num],'-Average Startup-', Average_Kitchen_Startup_PM[event_num],'-average event pm-',
                  #Average_Kitchen_PM_per_Event[event_num],'median event pm-',Median_Kitchen_PM_per_Event[event_num], 'length of event-',length_of_event[event_num],
                  #'min--Median cooldown-',Median_Kitchen_Cooldown_PM[event_num],'Average Cooldown-',Average_Kitchen_Startup_PM[event_num])
            #print('--------next event------',K_H_MIN_tv,'min- TV -max' ,K_H_MAX_tv ,K_H_MIN_Count[-1] ,'Min- array last value -Max',K_H_MAX_Count[-1], 'Startup max tv', K_Hapex_Startup_max, 'Startup next min',K_Hapex_Next_Startup_min)
            event_num = event_num + 1

        Event_number_tally = np.arange(0, event_num,1)
    #print('count fuel',Fuel_Used_for_events_Non_filtered, sum(Fuel_Used_for_events_Non_filtered))
    
    Hosuehold.append(Household)
    total_cooking_time.append(sum(Merged_Stove_combined_Array))
    Number_of_events.append(len(Merged_Stoves_end))
    Average_events_per_day.append(len(Merged_Stoves_start)/ ((len(Merged_Stove_combined_Array))/(24*60)))
    Percentage_cooking.append(int((sum(Merged_Stove_combined_Array)/ len(Merged_Stove_combined_Array))*100))
    Average_Event_length.append(sum(Merged_Stove_combined_Array)/ len(Merged_Stoves_start)) 

    Total_Average_Cook_PM_per_Event.append(np.average(RAW_EVENT_Cook_PM))
    Total_Average_Kitchen_PM_per_Event.append(np.average(RAW_EVENT_KITCHEN_PM))
    Total_Medain_Cook_PM_per_Event.append(np.median(RAW_EVENT_Cook_PM))
    Total_Median_Kitchen_PM_per_Event.append(np.median(RAW_EVENT_KITCHEN_PM))
    Total_STD_Cook_PM_per_Event.append(np.std(RAW_EVENT_Cook_PM))
    Total_STD_Kitchen_PM_per_Event.append(np.std(RAW_EVENT_KITCHEN_PM))
    Total_Percentage_Cook_Compliance.append(int((sum(Raw_Cook_Compliance))/(len(Raw_Cook_Compliance))*100))
    Total_Percentage_Kitchen_Compliance.append(int((sum(Raw_Kitchen_Compliance))/(len(Raw_Kitchen_Compliance))*100))

    if no_fuel != 1:
        Total_Fuel_Used_for_events_Non_filtered.append(sum(Fuel_Used_for_events_Non_filtered))
        Total_Fuel_removed_before_event.append(np.average(Raw_Fuel_removed_before_event))
    else:
        Total_Fuel_Used_for_events_Non_filtered.append(-1)
        Total_Fuel_removed_before_event.append(-1)
    #Start up
    Total_Median_Kitchen_Start_up_PM.append(np.median(Raw_Kitchen_start_up))
    Total_Average_Kitchen_Startup_PM.append(np.average(Raw_Kitchen_start_up))
    Total_Std_Kitchen_Start_Up_PM.append(np.std(Raw_Kitchen_start_up))

    Total_Median_Cook_Start_up_PM.append(np.median(Raw_Cook_start_up))
    Total_Average_Cook_Startup_PM.append(np.average(Raw_Cook_start_up))
    Total_Std_Cook_Start_Up_PM.append(np.std(Raw_Cook_start_up))
    #coolDown
    Total_Median_Kitchen_Cooldown_PM.append(np.median(Raw_Kitchen_cooldown))
    Total_Average_Kitchen_Cooldown_PM.append(np.average(Raw_Kitchen_cooldown))
    Total_STD_Kitchen_Cooldown_PM.append(np.std(Raw_Kitchen_cooldown))

    Total_Median_Cook_Cooldown_PM.append(np.median(Raw_Cook_cooldown))
    Total_Average_Cook_Cooldown_PM.append(np.average(Raw_Cook_cooldown))
    Total_STD_Cook_Cooldown_PM.append(np.std(Raw_Cook_cooldown))

    Total_Start_Up_minutes_Collected.append(len(Raw_Kitchen_start_up))
    Total_Cooldown_minutes_Collected.append(len(Raw_Kitchen_cooldown))
        
    Total_Sum_Start_up_Kitchen.append(sum(Raw_Kitchen_start_up))
    Total_Sum_Start_up_Cook.append(sum(Raw_Cook_start_up))

    Total_Sum_Cooldown_Cook.append(sum(Raw_Cook_cooldown))
    Total_Sum_Cooldown_Kitchen.append(sum(Raw_Kitchen_cooldown))

    Spacer_for_data_frame.append('-')

Combined_stove_whole_metric = {'Household': Hosuehold, 'Total Cooking times (minues)':total_cooking_time,
                               'Number of Events':Number_of_events, 'Events per day': Average_events_per_day,
                               'Percentage Cooking per Day':Percentage_cooking, 'Event Metrics':Spacer_for_data_frame,
                               'Average Event Length (minutes)':Average_Event_length,
                               'Average Cook PM per Event':Total_Average_Cook_PM_per_Event, 
                              'Average Kitchen PM per Event': Total_Average_Kitchen_PM_per_Event,
                              'Median Cook PM per Event':Total_Medain_Cook_PM_per_Event,
                             'Median Kitchen PM per Event': Total_Median_Kitchen_PM_per_Event, 
                             'STD Cook PM per Event':Total_STD_Cook_PM_per_Event,
                             'STD Kitchen PM per Event': Total_STD_Kitchen_PM_per_Event,
                             '(%) Cook Compliance per Event': Total_Percentage_Cook_Compliance,
                             '(%) Kitchen Compliance per Event': Total_Percentage_Kitchen_Compliance,
                             'Sum of Fuel removed for each Event': Total_Fuel_Used_for_events_Non_filtered,
                             'Average Time Fuel was removed before event (min)':Total_Fuel_removed_before_event,
                             'Startup': Spacer_for_data_frame, 'Median Kitchen Start up':Total_Median_Kitchen_Start_up_PM,
                             'Average Kitchen Start up':Total_Average_Kitchen_Startup_PM, 
                             'STD Kitchen Start up':Total_Std_Kitchen_Start_Up_PM,'Kitchen Start up Sum':Total_Sum_Start_up_Kitchen,
                             'Median Cook Start up':Total_Median_Cook_Start_up_PM,
                             'Average Cook Start up':Total_Average_Cook_Startup_PM,
                             'STD Cook Start up': Total_Std_Cook_Start_Up_PM,'Cook Start up Sum':Total_Sum_Start_up_Cook,
                             'Minutes Start up Collected':Total_Start_Up_minutes_Collected,
                             'CoolDown':Spacer_for_data_frame, 'Median Kitchen Cooldown':Total_Median_Kitchen_Cooldown_PM,
                             'Average Kitchen Cooldown': Total_Average_Kitchen_Cooldown_PM,
                             'STD Kitchen Cooldown':Total_STD_Kitchen_Cooldown_PM, 
                             'Kitchen Cooldown Sum': Total_Sum_Cooldown_Kitchen, 
                             'Median Cook Cooldown':Total_Median_Cook_Cooldown_PM,
                             'Average Cook Cooldown': Total_Average_Cook_Cooldown_PM,
                             'STD Cook Cooldown':Total_STD_Cook_Cooldown_PM,
                            'Cook Cooldown Sum':Total_Sum_Cooldown_Cook,
                            'Minutes Cooldown Collected': Total_Cooldown_minutes_Collected}

DF_Combined_stove_whole_metric = pd.DataFrame(Combined_stove_whole_metric)

Path_export_combined_stove = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Combined_Stove_Whole_"+Phase+".csv"
DF_Combined_stove_whole_metric.to_csv(Path_export_combined_stove, index=False, mode='a')
