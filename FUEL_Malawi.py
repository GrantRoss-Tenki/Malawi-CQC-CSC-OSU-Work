import itertools
import os
import pandas as pd
import numpy as np
import csv
import glob
from decimal import *
from itertools import chain
import statistics as stat
import datetime
from io import StringIO
import matplotlib.pyplot as plt

# What Phase are we in?
Phase = "4N"
#What exact are we looking at? 1 or 2?
Exact_num = "2"



#this file is not going to distinguish between Agricultural Residue and Firewood
# these are for the raw files to average later
T_D_Fuel = []
T_D_KG_removed = []
T_D_Temp = []
T_D_Cook_comp = []
T_D_Cook_PM = []
T_D_Kit_comp = []
T_D_Kit_PM = []
T_d_set_fuel = []
#specfic sensors for each household's metrics
ID_HH_m = []
HH_fuel_removed_for_phase = []

HH_avg_temp = []
HH_avg_cook_comp = []
HH_avg_Kit_comp = []
HH_sum_KIT_PM = []
HH_sum_cook_pm = []
HH_avg_cook_PM =[]
HH_avg_Kit_PM =[]
HH_std_temp = []
HH_std_cook_comp = []
HH_std_Kit_comp = []
HH_std_cook_PM =[]
HH_std_Kit_PM = []
HH_total_time_f_collection = []
#For the Day summary that is to be used later



#Day_met_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/1N/Compiler/Raw_Day/Raw_D_metrics/1N_HH_raw_Day_metrics_1005.csv"
os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+ Phase +"/Compiler_"+Exact_num+"_exact/Raw_D_metrics")
# For Hood portion
#os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/2H/Compiler/Raw_Day/Raw_D_metrics")
# This was for hood portion
Day_met_path = os.getcwd()
csv_R_m = glob.glob(os.path.join(Day_met_path, "*.csv"))

for file in csv_R_m:
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        for idx, row in enumerate(csv_reader):
            if '0' in row:
                id_number_m = (row[1])
                Fuel_type_m = (row[2])
                Exact_stove_m = (row[3])
                Kitchen_Hapex_m = (row[4])
                Cook_hapex_m = (row[5])
            elif 'Fuel Raw Data' in row:
                data_start = idx
                break


        Day_data = pd.read_csv(file, skiprows=data_start)
        Minutes_of_collection = len(Day_data.iloc[:, 1])
        FUEL_removal = Day_data.iloc[:, 1]
        FUEL_SET = []
        count = 0
        for a in FUEL_removal:
            count = count + 1
            if count == Minutes_of_collection:
                break
            elif a != FUEL_removal.iloc[count] or (count+1) == Minutes_of_collection:
                FUEL_SET.append(a)


        #Fuel Collection
        if np.average(Day_data.iloc[:, 0]) != -1:
            HH_KG_removed = FUEL_SET
            T_D_Fuel.extend(Day_data.iloc[:, 0])
            T_D_KG_removed.extend((Day_data.iloc[:, 1]))
            HH_fuel_removed_for_phase.append(sum(HH_KG_removed))
            T_d_set_fuel.extend(set(Day_data.iloc[:, 1]))
        else:
            HH_fuel_removed_for_phase.append(-1)

        #Temperature Collection
        if np.average(Day_data.iloc[:, 4]) != -1:
            T_D_Temp.extend(Day_data.iloc[:, 4])
            HH_avg_temp.append((int((np.average(Day_data.iloc[:, 4])) * 100)) / 100)
            HH_std_temp.append((int((stat.stdev(Day_data.iloc[:, 4])) * 100)) / 100)
        else:
            HH_avg_temp.append(-1)
            HH_std_temp.append(-1)

        #Cook Hapex Collection
        if np.average(Day_data.iloc[:, 7]) != -1:
            T_D_Cook_comp.extend(Day_data.iloc[:, 5])
            T_D_Cook_PM.extend(Day_data.iloc[:, 7])
            HH_avg_cook_comp.append(int(((sum(Day_data.iloc[:, 5])) / Minutes_of_collection) * 100))
            HH_sum_cook_pm.append((int((sum(Day_data.iloc[:, 7])) * 100)) / 100)
            HH_avg_cook_PM.append((int((np.average(Day_data.iloc[:, 7])) * 100)) / 100)
            HH_std_cook_PM.append((int((stat.stdev(Day_data.iloc[:, 7])) * 100)) / 100)
        else:
            HH_sum_cook_pm.append(-1)
            HH_avg_cook_comp.append(-1)
            HH_avg_cook_PM.append(-1)
            HH_std_cook_PM.append(-1)

        #Kitchen HAPEx Collection
        if np.average(Day_data.iloc[:, 8]) != -1:
            T_D_Kit_PM.extend(Day_data.iloc[:, 8])
            T_D_Kit_comp.extend((Day_data.iloc[:,6]))
            HH_avg_Kit_comp.append(int(((sum(Day_data.iloc[:, 8])) / Minutes_of_collection) * 100))
            HH_sum_KIT_PM.append((int((sum(Day_data.iloc[:, 8])) * 100)) / 100)
            HH_avg_Kit_PM.append((int((np.average(Day_data.iloc[:, 8])) * 100)) / 100)
            HH_std_Kit_PM.append((int((stat.stdev(Day_data.iloc[:, 8])) * 100)) / 100)
        else:
            HH_sum_KIT_PM.append(-1)
            HH_avg_Kit_comp.append(-1)
            HH_avg_Kit_PM.append(-1)
            HH_std_Kit_PM.append(-1)

        #Household identifiers
        ID_HH_m.append(id_number_m)
        HH_total_time_f_collection.append(Minutes_of_collection)



# ## Day Summary is next, has fuel removed per day, percentage of movement per day, precentage of kitchen comp moving
# #these are values that are going to be extended throughout the whole code
#
#
KG_Per_Day =[]
PC_Cook_Comp =[]
PC_Kit_com = []

#specfic sensors for each household_only over summary
ID_HH_s = []
Day_tally_s = []
HH_avg_Fuel_removed_per_day = []
HH_avg_Kit_comp_per_day = []
HH_avg_cook_comp_per_day = []
KG_removed_sum = []
#For the Day summary that is to be used later

os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+ Phase +"/Compiler_"+Exact_num+"_exact/Raw_D_summary")
# For Hood portion
#os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/2H/Compiler/Raw_Day/Raw_D_summary")
# For Hood portion
Day_sum_path = os.getcwd()
csv_R_s = glob.glob(os.path.join(Day_sum_path, "*.csv"))

for file_s in csv_R_s:
    with open(file_s, 'r') as f:
        csv_reader = csv.reader(f)
        for idx, row in enumerate(csv_reader):
            if '0' in row:
                id_number_s = ((row[1]))
                Fuel_type_s = (row[2])
                Exact_stove_s = (row[3])
                Kitchen_Hapex_s = (row[4])
                Cook_hapex_s = (row[5])
            elif 'Fuel Removed (FUEL)' in row:
                data_start = idx

                break
    Day_SUM_data = pd.read_csv(file_s, skiprows=data_start)

    #next is for specific day categories
    counting_days = len(Day_SUM_data.iloc[:,0])
    fuel_day_removal = list(set((Day_SUM_data.iloc[:,0])))
    # Fuel Collection
    if np.average(Day_SUM_data.iloc[:,0]) != -1:
        KG_removed_sum.append((int((sum(fuel_day_removal))*100))/100)
        #HH_avg_Fuel_removed_per_day.append(((int((KG_removed_sum) / counting_days)) * 1000) / 1000)
        KG_Per_Day.extend(Day_SUM_data.iloc[:, 0])
    else:
        KG_removed_sum.append(-1)
        #HH_avg_Fuel_removed_per_day.append(-1)

    #Cook HAPEx Collection
    if np.average(Day_SUM_data.iloc[:,1]) != -1:
        Cook_Comp = Day_SUM_data.iloc[:,1]
        PC_Cook_Comp.extend(Day_SUM_data.iloc[:, 1])
        HH_avg_cook_comp_per_day.append(((int(sum(Cook_Comp) / counting_days)) * 1000) / 1000)
    else:
        HH_avg_cook_comp_per_day.append(-1)
    #kitchen HAPEx Collection
    if np.average(Day_SUM_data.iloc[:,2]) != -1:
        KIT_comp = Day_SUM_data.iloc[:,2]
        HH_avg_Kit_comp_per_day.append(((int(sum(KIT_comp) / counting_days)) * 1000) / 1000)
        PC_Kit_com.extend(Day_SUM_data.iloc[:,2])
    else:
        HH_avg_Kit_comp_per_day.append(-1)

    # this is for length of day, this is not taking into effect the installation or removal
    Day_tally_s.append(counting_days)
    #Household identifiers
    ID_HH_s.append(id_number_s)


# making a dictionary, first is for hh and number inside list
## the HH number is to append correct metric to right hh This will have to be inside each csv loop
# this first one is a tester for the first two HH 1001 and 1005




print('-----------------------EVENT TIME-----------------------------')
# this next section is for the event to compile and to compare to others
# metrics to be compared to the others
### event is next
T_E_Fuel = []
T_E_KG_removed = []
T_E_Temp = []
T_E_Cook_comp = []
T_E_Cook_PM = []
T_E_Kit_comp = []
T_E_Kit_PM = []

ID_HH_EM = []
HH_fuel_removed_for_event = []
HH_Num_Events_observed = []
HH_E_avg_temp = []
HH_E_avg_cook_comp = []
HH_E_avg_Kit_comp = []
HH_E_avg_cook_PM =[]
HH_E_avg_Kit_PM =[]
HH_E_std_temp = []
HH_E_std_cook_comp = []
HH_E_std_Kit_comp = []
HH_E_std_cook_PM =[]
HH_E_std_Kit_PM =[]
HH_Cooking_length = []

os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+ Phase +"/Compiler_"+Exact_num+"_exact/Raw_E_metrics")

Event_met_path = os.getcwd()
csv_E_m = glob.glob(os.path.join(Event_met_path, "*.csv"))

for file in csv_E_m:
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        for idx, row in enumerate(csv_reader):
            if '0' in row:
                id_number_E_m = (row[1])
                Fuel_type_E_m = (row[2])
                Exact_stove_m = (row[3])
                Kitchen_Hapex_E_m = (row[4])
                Cook_hapex_E_m = (row[5])
            elif 'Fuel Raw Data' in row:
                data_start = idx
                break
        Event_data = pd.read_csv(file, skiprows=data_start)
        Minutes_of_collection = len(Event_data.iloc[:, 1])
        Cooking_time = sum([a for a in Event_data.iloc[:, 1]])

        # going to use the HH_summary_event data to get a total of all removed kg


        #HH_KG_E_removed = ((int((sum(list(set(Event_data.iloc[:, 1])))) * 100)) / 100)


        #Fuel Collection
        if np.average(Event_data.iloc[:, 0]) != -1:
            T_E_Fuel.extend(Event_data.iloc[:, 0])
            T_E_KG_removed.extend((Event_data.iloc[:, 1]))
            #HH_fuel_removed_for_event.append(sum(HH_KG_E_removed))

        #temperature Collection
        if np.average(Event_data.iloc[:, 2]) != -1:
            T_E_Temp.extend(Event_data.iloc[:, 2])
            HH_E_avg_temp.append((int((np.average(Event_data.iloc[:, 2])) * 100)) / 100)
            HH_E_std_temp.append((int((stat.stdev(Event_data.iloc[:, 2])) * 100)) / 100)
        else:
            HH_E_avg_temp.append(-1)
            HH_E_std_temp.append(-1)

        #Cook HAPEx Collection
        if np.average(Event_data.iloc[:, 3]) != -1:
            T_E_Cook_comp.extend(Event_data.iloc[:, 3])
            T_E_Cook_PM.extend(Event_data.iloc[:, 5])
            HH_E_avg_cook_comp.append(int(((sum(Event_data.iloc[:, 3])) / Minutes_of_collection) * 100))
            HH_E_avg_cook_PM.append((int((np.average(Event_data.iloc[:, 5])) * 100)) / 100)
            HH_E_std_cook_PM.append((int((stat.stdev(Event_data.iloc[:, 5])) * 100)) / 100)
        else:
            HH_E_avg_cook_comp.append(-1)
            HH_E_avg_cook_PM.append(-1)
            HH_E_std_cook_PM.append(-1)

        #Kitchen HAPEx
        if np.average((Event_data.iloc[:, 4])) != -1:
            T_E_Kit_comp.extend((Event_data.iloc[:, 4]))
            T_E_Kit_PM.extend(Event_data.iloc[:, 6])
            HH_E_avg_Kit_comp.append(int(((sum(Event_data.iloc[:, 4])) / Minutes_of_collection) * 100))
            HH_E_avg_Kit_PM.append((int((np.average(Event_data.iloc[:, 6])) * 100)) / 100)
            HH_E_std_Kit_PM.append((int((stat.stdev(Event_data.iloc[:, 6])) * 100)) / 100)
        else:
            HH_E_avg_Kit_comp.append(-1)
            HH_E_avg_Kit_PM.append(-1)
            HH_E_std_Kit_PM.append(-1)

        #household identifers
        ID_HH_EM.append(id_number_E_m)
        HH_Cooking_length.append(Minutes_of_collection)


print(' does the percentage make sense', HH_E_avg_cook_comp)
print(Minutes_of_collection)
print(HH_E_avg_Kit_comp)
print(len(Event_data.iloc[:, 3]))
print(HH_avg_cook_PM)
# this is starting the event summary file that has, length of event, Fuel removed, Removed time,
# inserted time, percentage of cook comp, and kitchen comp

#specifics for household over summary
ID_HH_Event_S = []
Event_Number_tally = []
KG_per_event = []
HH_PE_Cook_Comp =[]
HH_PE_Kit_com = []
HH_Time_Fuel_remove = []
#HH_Time_Fuel_Insert = []
HH_avg_cooking_length = []
# bellow is for the total to be averaged out later for all households
T_E_Length_of_event = []
T_E_Fuel_used_Event = []
T_E_removed_Time = []

os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+ Phase +"/Compiler_"+Exact_num+"_exact/Raw_E_summary")
# For Hood portion
#os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/2H/Compiler/Raw_Event/Raw_E_summary")
# For Hood portion
Event_Sum_path = os.getcwd()
csv_E_S = glob.glob(os.path.join(Event_Sum_path, "*.csv"))

for file_s in csv_E_S:
    with open(file_s, 'r') as f:
        csv_reader = csv.reader(f)
        for idx, row in enumerate(csv_reader):
            if '0' in row:
                id_number_E_s = (row[1])
                Fuel_type_E_s = (row[2])
                Exact_stove_E_s = (row[3])
                Kitchen_Hapex_E_s = (row[4])
                #Cook_hapex_E_s = (row[5])
            elif 'Fuel Removed (FUEL)' in row:
                data_start = idx

                break
    Event_SUM_data = pd.read_csv(file_s, skiprows=data_start)
    #First is a tally of the number of events
    if np.average(Event_SUM_data.iloc[:,0]) != -1:
        how_many_events = len(Event_SUM_data.iloc[:,0])
        HH_avg_cooking_length.append(Event_SUM_data.iloc[:,0])
        Event_Number_tally.append(how_many_events)
        T_E_Length_of_event.extend(Event_SUM_data.iloc[:, 0])
    else:
        Event_Number_tally.append(-1)
        HH_avg_cooking_length.append(-1)

    ID_HH_Event_S.append(id_number_E_s)

    #Fuel Collection

    HH_KG_E_removed = ((int((sum(list(set(Event_SUM_data.iloc[:, 1])))) * 100)) / 100)
    if np.average(Event_SUM_data.iloc[:,1]) != -1:
        Fuel_removed = Event_SUM_data.iloc[:,1]
        KG_per_event.append(((int(sum(Fuel_removed)/how_many_events))*1000)/1000)
        HH_Time_Fuel_remove.append(Event_SUM_data.iloc[:, 1])
        #HH_Time_Fuel_Insert.append(Event_SUM_data.iloc[:, 3])
        T_E_Fuel_used_Event.extend(Fuel_removed)
        T_E_removed_Time.extend(Event_SUM_data.iloc[:, 2])
        HH_fuel_removed_for_event.append((HH_KG_E_removed))
    else:
        KG_per_event.append(-1)
        HH_Time_Fuel_remove.append([0,-1])
        #HH_Time_Fuel_Insert.append(-1)
        HH_fuel_removed_for_event.append(-1)

    #Cook HAPEx Collection
    if np.average(Event_SUM_data.iloc[:,3]) != -1:
        HH_PE_Cook_Comp.append(Event_SUM_data.iloc[:,3])
    else:
        HH_PE_Cook_Comp.append(-1)

    #Kitchen HAPEx Collection
    if np.average(Event_SUM_data.iloc[:,4]) != -1:
        HH_PE_Kit_com.append(Event_SUM_data.iloc[:,4])
    else:
        HH_PE_Kit_com.append(-1)




##lastly, the last csv file is the first five minutes of cooking event
print('----------------five metrics----------')
### we only care about the cook and kitchen PM
ID_Five_Event = []
T_Five_Cook_PM = []
T_Five_KIT_PM = []
HH_Avg_PP_five_cook = []
HH_Avg_PM_five_kit = []
HH_STD_PP_five_cook = []
HH_STD_PM_five_kit = []



os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+ Phase +"/Compiler_"+Exact_num+"_exact/Raw_E_first_five")
# For Hood portion
#os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/2H/Compiler/Raw_Event/Raw_E_first_five")
# For Hood portion
Event_five_path = os.getcwd()
csv_E_5 = glob.glob(os.path.join(Event_five_path, "*.csv"))

for file_5 in csv_E_5:
    with open(file_5, 'r') as f:
        csv_reader = csv.reader(f)
        for idx, row in enumerate(csv_reader):
            if '0' in row:
                id_number_5 = (row[1])
                # #Fuel_type_5 = (row[2])
                # Exact_stove_5 = (row[3])
                # Kitchen_Hapex_5 = (row[4])
                # Cook_hapex_5 = (row[5])
            elif '10 minutes spread (Cook PM)' in row:
                data_start = idx

                break
    Event_5_data = pd.read_csv(file_5, skiprows=data_start)
    #Cook HAPEx Collection
    if np.average(Event_5_data.iloc[:, 0]) != -1:
        HH_Avg_PP_five_cook.append((int((np.average(Event_5_data.iloc[:, 0])) * 100)) / 100)
        HH_STD_PP_five_cook.append((int((stat.stdev(Event_5_data.iloc[:, 0])) * 100)) / 100)
        T_Five_Cook_PM.extend(Event_5_data.iloc[:, 0])
    else:
        HH_Avg_PP_five_cook.append(-1)
        HH_STD_PP_five_cook.append(-1)

    #Kitchen HAPEx Collection
    if np.average(Event_5_data.iloc[:, 1]) != -1:
        HH_Avg_PM_five_kit.append((int((np.average(Event_5_data.iloc[:, 1])) * 100)) / 100)
        HH_STD_PM_five_kit.append((int((stat.stdev(Event_5_data.iloc[:, 1])) * 100)) / 100)
        T_Five_KIT_PM.extend((Event_5_data.iloc[:, 1]))
    else:
        HH_Avg_PM_five_kit.append(-1)
        HH_STD_PM_five_kit.append(-1)

    Event_5_data = pd.read_csv(file_5, skiprows=data_start)
    ID_Five_Event = id_number_5


print('----------------Cooldown----------')
### we only care about the cook and kitchen PM
ID_CoolDown_Event = []
T_CoolDown_Cook_PM = []
T_CoolDown_KIT_PM = []
HH_Avg_PP_CoolDown_cook = []
HH_Avg_PM_CoolDown_kit = []
HH_STD_PP_CoolDown_cook = []
HH_STD_PM_CoolDown_kit = []



os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+ Phase +"/Compiler_"+Exact_num+"_exact/Raw_E_Cooldown")
# For Hood portion
#os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/2H/Compiler/Raw_Event/Raw_E_first_five")
# For Hood portion
Event_five_path = os.getcwd()
csv_E_5 = glob.glob(os.path.join(Event_five_path, "*.csv"))

for file_5 in csv_E_5:
    with open(file_5, 'r') as f:
        csv_reader = csv.reader(f)
        for idx, row in enumerate(csv_reader):
            if '0' in row:
                id_number_5 = (row[1])
                print('here is the ID number before cooldown',id_number_5)
            elif '30 Cooldown spread (Cook PM)' in row:
                data_start = idx

                break
    Event_5_data = pd.read_csv(file_5, skiprows=data_start)
    #Cook HAPEx Collection
    if np.average(Event_5_data.iloc[:, 0]) != -1:
        HH_Avg_PP_CoolDown_cook.append((int((np.average(Event_5_data.iloc[:, 0])) * 100)) / 100)
        HH_STD_PP_CoolDown_cook.append((int((stat.stdev(Event_5_data.iloc[:, 0])) * 100)) / 100)
        T_CoolDown_Cook_PM.extend(Event_5_data.iloc[:, 0])
    else:
        HH_Avg_PP_CoolDown_cook.append(-1)
        HH_STD_PP_CoolDown_cook.append(-1)

    #Kitchen HAPEx Collection
    #print(Event_5_data.iloc[5, 1])
    if Event_5_data.iloc[5, 1] != -1:
        HH_Avg_PM_CoolDown_kit.append((int((np.average(Event_5_data.iloc[:, 1])))))# * 100)) / 100)
        HH_STD_PM_CoolDown_kit.append((int((stat.stdev(Event_5_data.iloc[:, 1])))))# * 100)) / 100)
        T_CoolDown_KIT_PM.extend(Event_5_data.iloc[:, 1])
    else:
        HH_Avg_PM_CoolDown_kit.append(-1)
        HH_STD_PM_CoolDown_kit.append(-1)

    Event_5_data = pd.read_csv(file_5, skiprows=data_start)
    ID_Five_Event = id_number_5

####geting all the metrics compiled
print('------------------metrics summary for day first -----------------------')

HH_dict_day = {}
HH_missing_fuel = 0
for HH_num, HH in enumerate(ID_HH_m):
    if KG_removed_sum[HH_num] != -1:
        FUEL_REMOVED_PER_day = (int(((KG_removed_sum[HH_num])/(Day_tally_s[HH_num]))*100)/100)
    else:
        FUEL_REMOVED_PER_day = -1
        HH_missing_fuel = HH_missing_fuel + 1
    HH_dict_day[HH] = {'Number of days Observed=':Day_tally_s[HH_num],\
                    'Average Temperature=':HH_avg_temp[HH_num],\
                    'STD Temperature=': HH_std_temp[HH_num],\
                    'Sum of Cook PM': HH_sum_cook_pm[HH_num],\
                    'Average Cook PM=': HH_avg_cook_PM[HH_num],\
                    'STD Cook PM=': HH_std_cook_PM[HH_num], \
                    'Sum of Kitchen PM': HH_sum_KIT_PM[HH_num],\
                    'Average Kitchen PM=':HH_avg_Kit_PM[HH_num],\
                    'STD Kitchen PM=': HH_std_Kit_PM[HH_num],\
                    'Compliance for Kitchen=': HH_avg_Kit_comp[HH_num],
                    'Cook Percent Movement for Phase=': HH_avg_cook_comp[HH_num],\
                    'Fuel Removed for phase=':KG_removed_sum[HH_num] ,
                    'Fuel Removed per day=':FUEL_REMOVED_PER_day}

    print('--------------------KG REMoved____', KG_removed_sum[HH_num] )
    print('---------------SUM of cook pm ____', HH_sum_cook_pm[HH_num])

HH_Number_day_metric_dict = {}
HH_range_m = range(len(ID_HH_m))
for n in HH_range_m:
    HH_Number_day_metric_dict[n] = ID_HH_m[n]
# above for loop is important for finding maximums for households


#Ranking the Housholds by metrics
M_C_PM = {}
M_F_PD = {}
M_K_PM = {}
M_K_Comp = {}
M_C_Comp = {}
acp = 0
fupd = 0
akpd = 0
cfk = 0
cfc = 0

for HH, HH_info in HH_dict_day.items():
    for met in HH_info:
        if met == 'Average Cook PM=':
            M_C_PM[acp] = HH_info[met]
            acp = acp + 1
        elif met == 'Fuel Removed for phase=':
            M_F_PD[fupd] = HH_info[met]
            fupd = fupd + 1
        elif met == 'Average Kitchen PM=':
            M_K_PM[akpd] = HH_info[met]
            akpd = akpd + 1
        elif met == 'Compliance for Kitchen=':
            M_K_Comp[cfk] = HH_info[met]
            cfk = cfk + 1
        elif met == 'Cook Percent Movement for Phase=':
            M_C_Comp[cfc] = HH_info[met]
            cfc = cfc + 1


M_F_PD = sorted(M_F_PD.items(), key=lambda x:x[1], reverse=True)
M_C_PM = sorted(M_C_PM.items(), key=lambda x:x[1], reverse=True)
M_K_PM = sorted(M_K_PM.items(), key=lambda x:x[1], reverse=True)
M_K_Comp = sorted(M_K_Comp.items(), key=lambda x:x[1], reverse=True)
M_C_Comp = sorted(M_C_Comp.items(), key=lambda x:x[1], reverse=True)

HH_Max_Fuel_per_day = []
for fuel in M_F_PD:
    HH_Max_Fuel_per_day.append(HH_Number_day_metric_dict[fuel[0]])
HH_Max_Cook_pm = []
for pm in M_C_PM:
    HH_Max_Cook_pm.append(HH_Number_day_metric_dict[pm[0]])
HH_max_Kit_PM = []
for pm in M_K_PM:
    HH_max_Kit_PM.append(HH_Number_day_metric_dict[pm[0]])
HH_max_Kit_comp = []
for comp in M_K_Comp:
    HH_max_Kit_comp.append(HH_Number_day_metric_dict[comp[0]])
HH_max_Cook_comp = []
for comp in M_C_Comp:
    HH_max_Cook_comp.append(HH_Number_day_metric_dict[comp[0]])
print('Household that removed the most fuel', HH_Max_Fuel_per_day)
print('Household cook that had the most PM', HH_Max_Cook_pm)
print('Household kitchen that had the most PM', HH_max_Kit_PM)
print('Household cook that moved the most', HH_max_Cook_comp)
print('Household kitchen which moved the most', HH_max_Kit_comp)
# this is for the total phase metrics for all the households that are within the study
# Also, theses are all averaged using the T_D section above
Phase_fuel_removal = []
for f in KG_removed_sum:
    if f != -1:
        Phase_fuel_removal.append(f)
Total_fuel_removed_for_phase = (int(sum(Phase_fuel_removal)*100)/100)
print('Total Amount of Fuel Removed for all houses in Phase: (KG)', Total_fuel_removed_for_phase)
Total_Amount_of_time_sensed = len(T_D_Kit_PM)
print('Total Amount of minutes that were sensed: (minutes)', Total_Amount_of_time_sensed)
Total_Average_Cook_PM_exposure = (int(np.average(T_D_Cook_PM)*100)/100)
print('Average PM exposure for all cooks (PM)', Total_Average_Cook_PM_exposure)
Total_Average_Kitchen_PM = (int(np.average(T_D_Kit_PM)*100)/100)
print('The total amount of Kitchen Exposure: (PM)', Total_Average_Kitchen_PM)
Total_days_observed = sum(Day_tally_s)
print('The total number of days observed: (days)', Total_days_observed)
Total_days_observed_minus_missing_HH = Total_days_observed - HH_missing_fuel*Day_tally_s[0]
Total_Fuel_Used_per_day = (int((Total_fuel_removed_for_phase/Total_days_observed_minus_missing_HH)*100))/100
print('The total Average fuel removed per day: (KG/day)', Total_Fuel_Used_per_day)
Total_Cook_Comp = (int((sum(T_D_Cook_comp)/len((T_D_Cook_comp)))*100))
print('Total percentage of Cook Compliance (%)',Total_Cook_Comp)
Total_kitchen_comp = (int((sum(T_D_Kit_comp)/len((T_D_Cook_comp)))*100)/100)
print('Total percentage of Kitchen Compliance (%)', Total_kitchen_comp)

#print("why is the fuel removed per event not working!!!!!!!!!!!!!", HH_Time_Fuel_remove[39])
HH_dict_event = {}

#metrics for event
Total_Amount_of_event_time_sensed = []
Total_fuel_removed_for_all_events = []
for HH_num, HH in enumerate(ID_HH_EM):
    if KG_removed_sum[HH_num] != -1:
        Avg_fuel_per_event_used = (int(((KG_removed_sum[HH_num])/(Event_Number_tally[HH_num]))*100)/100)
        Total_fuel_removed_for_all_events.append(KG_removed_sum[HH_num])
        a_v_g_time_fuel_removed = np.average(HH_Time_Fuel_remove[HH_num])

    else:
        Avg_fuel_per_event_used = -1
        a_v_g_time_fuel_removed = -1

    if Event_Number_tally[HH_num] > 2:
        N_Of_events_O = Event_Number_tally[HH_num]
        a_v_g_event_per_day = (int(((Event_Number_tally[HH_num])/(Day_tally_s[HH_num]))*100))/100
        TT_cooking = HH_Cooking_length[HH_num]
        Total_Amount_of_event_time_sensed.append(TT_cooking)

        S_T_D_length_cooking_event = (int((stat.stdev(HH_avg_cooking_length[HH_num]))*100))/100
    else:
        N_Of_events_O = -1
        a_v_g_event_per_day = -1
        TT_cooking = -1
        S_T_D_length_cooking_event = -1
    HH_dict_event[HH] = {'Number of Events Observed':N_Of_events_O,\
                  'Average Events per day (Events/day)':a_v_g_event_per_day,\
                  'Total time cooking (minutes)': TT_cooking,\
                  'Percentage of Cooking per day (minutes)': ((int(((HH_Cooking_length[HH_num])/(HH_total_time_f_collection[HH_num]))*100))/100),
                  'Average length of Each Cooking Event (minutes)': np.average(HH_avg_cooking_length[HH_num]), \
                   'STD length of Each Cooking Event(minutes)': S_T_D_length_cooking_event, \
                    'Average Cook PM Per Event' : HH_E_avg_cook_PM[HH_num],\
                    'STD Cook PM per Event' : HH_E_std_cook_PM[HH_num],
                  'Average Kitchen PM per Event':HH_E_avg_Kit_PM[HH_num],\
                   'STD Kitchen PM per Event': HH_E_std_Kit_PM[HH_num],\
                   'Percentage Compliance for Kitchen Per Event': HH_E_avg_Kit_comp[HH_num],
                  'Percentage Compliance of Cook per Event': HH_E_avg_cook_comp[HH_num],\
                  'Fuel Used for all events':KG_removed_sum[HH_num] ,
                   'Average Fuel Used per event':Avg_fuel_per_event_used,
                  'Average Time Fuel was removed before Cooking (minutes)': a_v_g_time_fuel_removed,
                   'Average Cook PM for Start-Up of Cooking' : HH_Avg_PP_five_cook[HH_num],
                   'STD Cook PM for Start-Up of Cooking' : HH_STD_PP_five_cook[HH_num],
                   'Average Kitchen PM for Start-Up of Cooking' : HH_Avg_PM_five_kit[HH_num],
                   'STD Kitchen PM for Start-Up of Cooking' : HH_STD_PM_five_kit[HH_num], 
                   'Average Cook PM for Cooldown of Cooking' : HH_Avg_PP_CoolDown_cook[HH_num],
                   'STD Cook PM for Cooldown of Cooking' : HH_STD_PP_CoolDown_cook[HH_num],
                   'Average Kitchen PM for Cooldown of Cooking' : HH_Avg_PM_CoolDown_kit[HH_num],
                  'STD Kitchen PM for Cooldown of Cooking' : HH_STD_PM_CoolDown_kit[HH_num]}



HH_Number_Event_metric_dict = {}
HH_range_Event = range(len(ID_HH_EM))
for n in HH_range_Event:
    HH_Number_Event_metric_dict[n] = ID_HH_EM[n]
# above for loop is important for finding maximums for households


#Ranking the Housholds by metrics
N_E_O = {}
Avg_E_PD = {}
T_T_C = {}
Avg_C_PM_E = {}
Avg_K_PM_E = {}
P_C_C_E = {}
Avg_F_E ={}
Avg_T_F_B_C = {}
Avg_C_PM_F_F = {}
Avg_K_PM_F_F = {}

Neo = 0
Aepd = 0
Ttc = 0
Acpme = 0
Akpme = 0
Pcce = 0
Afe = 0
Atfbc = 0
Acpmff = 0
Akpmff = 0
for HH, HH_info in HH_dict_event.items():
    for met in HH_info:
        if met == 'Number of Events Observed':
            N_E_O[Neo] = HH_info[met]
            Neo = Neo + 1
        elif met == 'Average Events per day (Events/day)':
            Avg_E_PD[Aepd] = HH_info[met]
            Aepd = Aepd + 1
        elif met == 'Total time cooking (minutes)':
            T_T_C[Ttc] = HH_info[met]
            Ttc = Ttc + 1
        elif met == 'Average Cook PM Per Event':
            Avg_C_PM_E[Acpme] = HH_info[met]
            Acpme = Acpme + 1
        elif met == 'Average Kitchen PM per Event':
            Avg_K_PM_E[Akpme] = HH_info[met]
            Akpme = Akpme + 1
        elif met == 'Percentage Compliance of Cook per Event':
            P_C_C_E[Pcce] = HH_info[met]
            Pcce = Pcce + 1
        elif met == 'Average Fuel Used per event':
            Avg_F_E[Afe] = HH_info[met]
            Afe = Afe + 1
        elif met == 'Average Time Fuel was removed before Cooking (minutes)':
            Avg_T_F_B_C[Atfbc] = HH_info[met]
            Atfbc = Atfbc + 1
        elif met == 'Average Cook PM for First Five minutes of Cooking':
            Avg_C_PM_F_F[Acpmff] = HH_info[met]
            Acpmff = Acpmff + 1
        elif met == 'Average Kitchen PM for First Five minutes of Cooking':
            Avg_K_PM_F_F[Akpmff] = HH_info[met]
            Akpmff = Akpmff + 1
#reorganizing for max and min
N_E_O = sorted(N_E_O.items(), key=lambda x:x[1], reverse=True)
Avg_E_PD = sorted(Avg_E_PD.items(), key=lambda x:x[1], reverse=True)
T_T_C = sorted(T_T_C.items(), key=lambda x:x[1], reverse=True)
Avg_C_PM_E = sorted(Avg_C_PM_E.items(), key=lambda x:x[1], reverse=True)
Avg_K_PM_E = sorted(Avg_K_PM_E.items(), key=lambda x:x[1], reverse=True)
P_C_C_E = sorted(P_C_C_E.items(), key=lambda x:x[1], reverse=True)
Avg_F_E = sorted(Avg_F_E.items(), key=lambda x:x[1], reverse=True)
Avg_T_F_B_C = sorted(Avg_T_F_B_C.items(), key=lambda x:x[1], reverse=True)
Avg_C_PM_F_F = sorted(Avg_C_PM_F_F.items(), key=lambda x:x[1], reverse=True)
Avg_K_PM_F_F = sorted(Avg_K_PM_F_F.items(), key=lambda x:x[1], reverse=True)



HH_Max_Event= []
for z in N_E_O:
    HH_Max_Event.append(HH_Number_Event_metric_dict[z[0]])
HH_Max_event_day = []
for z in Avg_E_PD:
    HH_Max_event_day.append(HH_Number_Event_metric_dict[z[0]])
HH_max_time_cooking = []
for z in T_T_C:
    HH_max_time_cooking.append(HH_Number_Event_metric_dict[z[0]])
HH_max_cook_pm_E = []
for z in Avg_C_PM_E:
    HH_max_cook_pm_E.append(HH_Number_Event_metric_dict[z[0]])
HH_max_Kit_PM_E = []
for z in Avg_K_PM_E:
    HH_max_Kit_PM_E.append(HH_Number_Event_metric_dict[z[0]])
HH_max_Cook_comp_E = []
for z in P_C_C_E:
    HH_max_Cook_comp_E.append(HH_Number_Event_metric_dict[z[0]])
HH_max_Fuel_Event = []
for z in Avg_F_E:
    HH_max_Fuel_Event.append(HH_Number_Event_metric_dict[z[0]])
HH_max_Time_Fuel_removed= []
for z in Avg_T_F_B_C:
    HH_max_Time_Fuel_removed.append(HH_Number_Event_metric_dict[z[0]])
HH_max_Cook_First_PM = []
for z in Avg_C_PM_F_F:
    HH_max_Cook_First_PM.append(HH_Number_Event_metric_dict[z[0]])
HH_max_Kit_First_PM = []
for z in Avg_K_PM_F_F:
    HH_max_Kit_First_PM.append(HH_Number_Event_metric_dict[z[0]])


print('Household that had the most cooking events', HH_Max_Event)
print('Household that had the most cooking events per day', HH_Max_event_day)
print('Household that spent the most minutes cooking', HH_max_time_cooking)
print('Household cook that was exposed to the most PM' , HH_max_cook_pm_E)
print('Household kitchen that was exposed to the most PM', HH_max_Kit_PM_E)
print('Household cook that moved the most', HH_max_Cook_comp_E)
print('Household that burned the most fuel for each event', HH_max_Fuel_Event)
print('Household that had the longest time between fuel removal and cooking', HH_max_Time_Fuel_removed)
print('Household cook that had the highest PM for first five minutes', HH_max_Kit_First_PM)
print('Household kitchen that had the highest PM for first five minutes', HH_max_Kit_First_PM)

## total metrics for all of the house with each event
Total_Amount_of_event_time_sensed = sum(Total_Amount_of_event_time_sensed)
print('Total Amount of minutes for cooking event that was sensed: (minutes)', Total_Amount_of_event_time_sensed)
Total_number_of_Events_sensed = len(T_E_Length_of_event)
print('Total number of events sensed', Total_number_of_Events_sensed)

#Total_fuel_removed_for_all_events = sum(Total_fuel_removed_for_all_events)
print('Total Amount of Fuel Removed for events: (KG)', Total_fuel_removed_for_phase)
Percent_cooking_to_non = int(((Total_Amount_of_event_time_sensed/Total_Amount_of_time_sensed))*100)
print('Percentage of cooking to non-cooking time (%)', Percent_cooking_to_non)
Average_Fuel_used_per_event = Total_fuel_removed_for_phase/Total_number_of_Events_sensed
print('Average Fuel Removed for event (KG)' , (int(Average_Fuel_used_per_event*1000))/1000)
Average_Time_cooking_per_event = Total_Amount_of_event_time_sensed/Total_number_of_Events_sensed
print('Average Time spent on each cooking event (minute)', (int(Average_Time_cooking_per_event *100))/100)
Total_Average_Event_cook_exposure = (int(np.average(T_E_Cook_PM)*100)/100)
print('Average Cook PM exposure per event (PM)', Total_Average_Event_cook_exposure)
Total_Average_Event_Kitchen_PM = (int(np.average(T_E_Kit_PM)*100)/100)
print('Average Kitchen PM Exposure per event (PM)', Total_Average_Event_Kitchen_PM)

Total_Average_first_five_Kit_PM = (int(np.average(T_Five_KIT_PM))) #(((sum(T_Five_KIT_PM)))/(len(T_Five_KIT_PM)))*100)/100)
print('Average Kitchen PM for the 10 Minute Start-Up of cooking (PM)', Total_Average_first_five_Kit_PM)
Total_Average_first_five_Cook_PM = (int(np.average(T_Five_Cook_PM))) #(((sum(T_Five_Cook_PM)))/(len(T_Five_Cook_PM)))*100)/100)
print('Average Cook PM for the 10 Minute Start-Up of cooking (PM)', Total_Average_first_five_Cook_PM)

Total_Average_Cooldown_Kit_PM = (int(np.average(T_CoolDown_KIT_PM)))#(((sum(T_Cooldown_KIT_PM)))/(len(T_Cooldown_KIT_PM)))*100)/100)
print('Average Kitchen PM for the whole Cooldown of cooking (PM)', Total_Average_Cooldown_Kit_PM)
Total_Average_Cooldown_Cook_PM = (int(np .average(T_CoolDown_Cook_PM)))#(((sum(T_CoolDown_Cook_PM)))/(len(T_CoolDown_Cook_PM)))*100)/100)
print('Average Cook PM for the whole Cooldown of cooking (PM)', Total_Average_Cooldown_Cook_PM)

Total_Cook_Comp_Event = (int((sum(T_E_Cook_comp)/len((T_E_Cook_comp)))*100)/100)
print('Total percentage of Cook Compliance while Cooking(%)',(Total_Cook_Comp_Event)*100)
Total_kitchen_comp_Event = (int((sum(T_E_Kit_comp)/len((T_E_Kit_comp)))*100)/100)
print('Total percentage of Kitchen Compliance  while Cooking (%)', Total_kitchen_comp_Event)


# making data frames for the housholds
Household_day = []
HH_day_number_days_observed = []
HH_day_Average_temperature = []
HH_day_Std_temperature = []
HH_day_sum_Cook_PM = []
HH_day_Average_Cook_PM = []
HH_day_STD_Cook_PM = []
HH_day_sum_Kitchen_PM = []
HH_day_Average_Kitchen_PM = []
HH_day_STD_Kitchen_PM =[]
HH_day_Compliance_Cook = []
HH_day_Compliance_Kitchen = []
HH_day_fuel_removed_Phase = []
HH_day_Fuel_removed_per_day = []

for Num, hh in enumerate(HH_dict_day.keys()):
    Household_day.append(hh)
    counting = np.arange(0, 13,1)
    for val in counting:
        if val == 0:
            HH_day_number_days_observed.append(HH_dict_day[hh]['Number of days Observed='])
        elif val == 1:
            HH_day_Average_temperature.append(HH_dict_day[hh]['Average Temperature='])
        elif val == 2:
            HH_day_Std_temperature.append(HH_dict_day[hh]['STD Temperature='])
        elif val == 3:
            HH_day_sum_Cook_PM.append(HH_dict_day[hh]['Sum of Cook PM'])
        elif val == 4:
            HH_day_Average_Cook_PM.append(HH_dict_day[hh]['Average Cook PM='])
        elif val == 5:
            HH_day_STD_Cook_PM.append(HH_dict_day[hh]['STD Cook PM='])
        elif val == 6:
            HH_day_sum_Kitchen_PM.append(HH_dict_day[hh]['Sum of Kitchen PM'])
        elif val == 7:
            HH_day_Average_Kitchen_PM.append(HH_dict_day[hh]['Average Kitchen PM='])
        elif val == 8:
            HH_day_STD_Kitchen_PM.append(HH_dict_day[hh]['STD Kitchen PM='])
        elif val == 9:
            HH_day_Compliance_Kitchen.append(HH_dict_day[hh]['Compliance for Kitchen='])
        elif val == 10:
            HH_day_Compliance_Cook.append(HH_dict_day[hh]['Cook Percent Movement for Phase='])
        elif val == 11:
            HH_day_fuel_removed_Phase.append(HH_dict_day[hh]['Fuel Removed for phase='])
        elif val == 12:
            HH_day_Fuel_removed_per_day.append(HH_dict_day[hh]['Fuel Removed per day='])
print(val)
DataFrame_HH_day = {'Household humber': Household_day,
                    'Number of days Observed=':HH_day_number_days_observed,\
                  'Average Temperature':HH_day_Average_temperature,\
                  'STD Temperature': HH_day_Std_temperature,\
                    'Sum of Cook PM': HH_day_sum_Cook_PM,\
                  'Average Cook PM (PM)': HH_day_Average_Cook_PM,\
                  'STD Cook PM (PM)': HH_day_STD_Cook_PM,\
                    'Sum of Kitchen PM': HH_day_sum_Kitchen_PM,\
                  'Average Kitchen PM (PM)':HH_day_Average_Kitchen_PM,\
                   'STD Kitchen PM (PM)': HH_day_STD_Kitchen_PM,\
                   'Compliance for Kitchen (%)': HH_day_Compliance_Kitchen,\
                  'Compliance Cook(%)': HH_day_Compliance_Cook,\
                  'Fuel Removed for phase (KG)':HH_day_fuel_removed_Phase ,\
                   'Fuel Removed per day (KG)':HH_day_Fuel_removed_per_day}

print('this is the length of avg cook', len(HH_day_Average_Cook_PM))
print('this is the length of sum cook', len(HH_day_sum_Cook_PM))
print('this is the length of sum kit', len(HH_day_sum_Kitchen_PM))
print('this is the length of Number of days', len(HH_day_number_days_observed))
print('this is the length of std cook', len(HH_day_STD_Cook_PM))
print('this is the length of fuel Removed per phase', len(HH_day_fuel_removed_Phase))
DF_HH_day = pd.DataFrame(DataFrame_HH_day)

DataFrame_day = {'Total Amount of Fuel Removed for all houses in Phase: (KG)': Total_fuel_removed_for_phase,
                 'Total Amount of minutes that were sensed: (minutes)': Total_Amount_of_time_sensed,
                 'Average PM exposure for all cooks (PM)': Total_Average_Cook_PM_exposure,
                 'Average amount for all Kitchens: (PM)': Total_Average_Kitchen_PM,
                 'The total number of days observed: (days)': Total_days_observed,
                 'The total Average fuel removed per day: (KG/day)': Total_Fuel_Used_per_day,
                 'Total percentage of Cook Compliance (%)':Total_Cook_Comp,
                 'Total percentage of Kitchen Compliance (%)': Total_kitchen_comp}
index_why = [0]
DF_day = pd.DataFrame(DataFrame_day,index=index_why)

DataFrame_day_rankings ={'Household that removed the most fuel': HH_Max_Fuel_per_day,
                         'Household cook that had the most PM': HH_Max_Cook_pm,
                         'Household kitchen that had the most PM': HH_max_Kit_PM,
                         'Household cook that moved the most': HH_max_Cook_comp,
                         'Household kitchen which moved the most': HH_max_Kit_comp}
DF_day_rankings = pd.DataFrame(DataFrame_day_rankings)


Household_event = []
HH_Event_number_Events_observed = []
HH_Event_Average_Events_day = []
HH_Event_Total_time_cooking = []
HH_Event_percentage_cooking_per_day = []
HH_Event_Average_Cooking_length = []
HH_Event_STD_Cooking_length = []
HH_Event_Average_Cook_PM =[]
HH_Event_STD_Cook_PM = []
HH_Event_Average_Kitchen_PM = []
HH_Event_STD_Kitchen_PM = []
HH_Event_Comp_Kitchen = []
HH_Event_Comp_Cook = []
HH_Event_Fuel_used_all_events = []
HH_Event_Average_fuel_per_event = []
HH_Event_Average_time_fuel_removed_before = []
HH_Event_STD_time_fuel_removed_before = []
HH_Event_Average_five_Cook_PM = []
HH_Event_STD_five_Cook_PM = []
HH_Event_Average_five_Kitchen_PM = []
HH_Event_STD_five_Kithen_PM = []
HH_Event_Average_Cooldown_Cook_PM = []
HH_Event_STD_Cooldown_Cook_PM = []
HH_Event_Average_Cooldown_Kitchen_PM = []
HH_Event_STD_Cooldown_Kithen_PM = []



for Num, hh in enumerate(HH_dict_event.keys()):
    Household_event.append(hh)
    countings = np.arange(0, 24,1)
    for val in countings:
        if val == 0:
            HH_Event_number_Events_observed.append(HH_dict_event[hh]['Number of Events Observed'])
        elif val == 1:
            HH_Event_Average_Events_day.append(HH_dict_event[hh]['Average Events per day (Events/day)'])
        elif val == 2:
            HH_Event_Total_time_cooking.append(HH_dict_event[hh]['Total time cooking (minutes)'])
        elif val == 3:
            HH_Event_percentage_cooking_per_day.append(HH_dict_event[hh]['Percentage of Cooking per day (minutes)'])
        elif val == 4:
            HH_Event_Average_Cooking_length.append(HH_dict_event[hh]['Average length of Each Cooking Event (minutes)'])
        elif val == 5:
            HH_Event_STD_Cooking_length.append(HH_dict_event[hh]['STD length of Each Cooking Event(minutes)'])
        elif val == 6:
            HH_Event_Average_Cook_PM.append(HH_dict_event[hh]['Average Cook PM Per Event'])
        elif val == 7:
            HH_Event_STD_Cook_PM.append(HH_dict_event[hh][ 'STD Cook PM per Event' ])
        elif val == 8:
            HH_Event_Average_Kitchen_PM.append(HH_dict_event[hh]['Average Kitchen PM per Event'])
        elif val == 9:
            HH_Event_STD_Kitchen_PM.append(HH_dict_event[hh]['STD Kitchen PM per Event'])
        elif val == 10:
            HH_Event_Comp_Kitchen.append(HH_dict_event[hh]['Percentage Compliance for Kitchen Per Event'])
        elif val == 11:
            HH_Event_Comp_Cook.append(HH_dict_event[hh]['Percentage Compliance of Cook per Event'])
        elif val == 12:
            HH_Event_Fuel_used_all_events.append(HH_dict_event[hh]['Fuel Used for all events'])
        elif val == 13:
            HH_Event_Average_fuel_per_event.append(HH_dict_event[hh]['Average Fuel Used per event'])
        elif val == 14:
            HH_Event_Average_time_fuel_removed_before.append(HH_dict_event[hh]['Average Time Fuel was removed before Cooking (minutes)'])
        elif val == 15:
            HH_Event_Average_five_Cook_PM.append(HH_dict_event[hh]['Average Cook PM for Start-Up of Cooking'])
        elif val == 16:
            HH_Event_STD_five_Cook_PM.append(HH_dict_event[hh]['STD Cook PM for Start-Up of Cooking'])
        elif val == 17:
            HH_Event_Average_five_Kitchen_PM.append(HH_dict_event[hh]['Average Kitchen PM for Start-Up of Cooking' ])
        elif val == 18:
            HH_Event_STD_five_Kithen_PM.append(HH_dict_event[hh]['STD Kitchen PM for Start-Up of Cooking' ])
        elif val == 19:
            HH_Event_Average_Cooldown_Cook_PM.append(HH_dict_event[hh]['Average Cook PM for Cooldown of Cooking'])
        elif val == 20:
            HH_Event_STD_Cooldown_Cook_PM.append(HH_dict_event[hh]['STD Cook PM for Cooldown of Cooking'])
        elif val == 21:
            HH_Event_Average_Cooldown_Kitchen_PM.append(HH_dict_event[hh]['Average Kitchen PM for Cooldown of Cooking'])
        elif val == 22:
            HH_Event_STD_Cooldown_Kithen_PM.append(HH_dict_event[hh]['STD Kitchen PM for Cooldown of Cooking'])

DataFrame_event_HH = {'Household number': Household_event,'Number of Events Observed':HH_Event_number_Events_observed,\
                  'Average Events per day (Events/day)':HH_Event_Average_Events_day,\
                  'Total time cooking (minutes)': HH_Event_Total_time_cooking,\
                   'Percentage of Cooking per day (minutes)': HH_Event_percentage_cooking_per_day,
                  'Average length of Each Cooking Event (minutes)': HH_Event_Average_Cooking_length, \
                    'STD length of Each Cooking Event(minutes)': HH_Event_STD_Cooking_length, \
                    'Average Cook PM Per Event' : HH_Event_Average_Cook_PM,\
                    'STD Cook PM per Event' : HH_Event_STD_Cook_PM,
                  'Average Kitchen PM per Event':HH_Event_Average_Kitchen_PM,\
                   'STD Kitchen PM per Event': HH_Event_STD_Kitchen_PM,\
                   'Percentage Compliance for Kitchen Per Event': HH_Event_Comp_Kitchen,
                  'Percentage Compliance of Cook per Event': HH_Event_Comp_Cook,\
                  'Fuel Used for all events': HH_Event_Fuel_used_all_events ,
                   'Average Fuel Used per event':HH_Event_Average_fuel_per_event,
                    'Average Time Fuel was removed before Cooking (minutes)': HH_Event_Average_time_fuel_removed_before,
                         'Average Cook PM for Start-up of Cooking' : HH_Event_Average_five_Cook_PM,
                         'STD Cook PM for Start-up of Cooking' : HH_Event_STD_five_Cook_PM,
                         'Average Kitchen PM for Start-up minutes of Cooking' : HH_Event_Average_five_Kitchen_PM,
                         'STD Kitchen PM for Start-up minutes of Cooking' : HH_Event_STD_five_Kithen_PM,

                         'Average Cook PM for Cooldown of Cooking' : HH_Event_Average_Cooldown_Cook_PM,
                         'STD Cook PM for Cooldown of Cooking' : HH_Event_STD_Cooldown_Cook_PM,
                         'Average Kitchen PM for Cooldown of Cooking' : HH_Event_Average_Cooldown_Kitchen_PM,
                         'STD Kitchen PM for Cooldown of Cooking' : HH_Event_STD_Cooldown_Kithen_PM}
DF_event_HH = pd.DataFrame(DataFrame_event_HH)

DataFrame_Event = {'Total Amount of minutes for cooking event that was sensed: (minutes)': Total_Amount_of_event_time_sensed,
                   'Total number of events sensed': Total_number_of_Events_sensed,
                   'Total Amount of Fuel Removed for events: (KG)': Total_fuel_removed_for_phase,
                   'Percentage of cooking to non-cooking time (%)': Percent_cooking_to_non,
                   'Average Fuel Removed for event (KG)' : (int(Average_Fuel_used_per_event*1000))/1000,
                   'Average Time spent on each cooking event (minute)': (int(Average_Time_cooking_per_event *100))/100,
                   'Average Cook PM exposure per event (PM)': Total_Average_Event_cook_exposure,
                   'Average Kitchen PM Exposure per event (PM)': Total_Average_Event_Kitchen_PM,
                   'Average Kitchen PM for the first five minutes of cooking (PM)': Total_Average_first_five_Kit_PM,
                   'Average Cook PM for the first five minutes of cooking (PM)': Total_Average_first_five_Cook_PM,
                   'Total percentage of Cook Compliance while Cooking(%)':(Total_Cook_Comp_Event)*100,
                   'Total percentage of Kitchen Compliance  while Cooking (%)': Total_kitchen_comp_Event}
index_why_s = [0]
DF_Event = pd.DataFrame(DataFrame_Event,index=index_why_s)

DataFrame_Event_rankings = {'Household that had the most cooking events': HH_Max_Event,
                          'Household that had the most cooking events per day' :HH_Max_event_day,
                          'Household that spent the most minutes cooking': HH_max_time_cooking,
                          'Household cook that was exposed to the most PM' : HH_max_cook_pm_E,
                          'Household kitchen that was exposed to the most PM': HH_max_Kit_PM_E,
                          'Household cook that moved the most': HH_max_Cook_comp_E,
                          'Household that burned the most fuel for each event': HH_max_Fuel_Event,
                          'Household that had the longest time between fuel removal and cooking': HH_max_Time_Fuel_removed,
                          'Household cook that had the highest PM for first five minutes': HH_max_Kit_First_PM,
                          'Household kitchen that had the highest PM for first five minutes': HH_max_Kit_First_PM}
#DF_Event_rankings = pd.DataFrame(DataFrame_Event_rankings)

Path_HH_Sum = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase
if Exact_num == "1":
    File_name_phase_Day = str(Path_HH_Sum) + "/"+Phase+"_Summary_Day_"+Exact_num+"_exact"+".csv"
    #DF_day.to_csv(File_name_phase_Day)
    #DF_HH_day.to_csv(File_name_phase_Day,index=False, mode= 'a')
    #File_name_phase_Day_rank = str(Path_HH_Sum) + "/"+Phase+"_Summary_Day_rank_"+Exact_num+"_exact"+".csv"
    #DF_day_rankings.to_csv(File_name_phase_Day_rank,index=False,mode='a')


File_name_phase_Event = str(Path_HH_Sum) + "/"+Phase+"_Summary_Event_"+Exact_num+"_exact"+".csv"
DF_Event.to_csv(File_name_phase_Event,index=False,mode='a')
DF_event_HH.to_csv(File_name_phase_Event,index=False, mode= 'a')
#File_name_phase_Event_rank = str(Path_HH_Sum) + "/"+Phase+"_Summary_Event_rank_"+Exact_num+"_exact"+".csv"
#DF_Event_rankings.to_csv(File_name_phase_Event_rank,index=False, mode= 'a')
