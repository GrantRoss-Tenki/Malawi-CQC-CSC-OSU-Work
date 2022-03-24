
#import itertools
import os
import pandas as pd
import numpy as np
import csv
import glob
import statistics as stat
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path, PureWindowsPath
import Functions_malawi

Phase = input("What Phase are we in? --type 1N-- ")
print('Phase Number', Phase)

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
Folder_path_1 = Path(input("-Copy down the path of your -1N- folder  - Format should work for either Mac or Windows- "))
path_on_windows_1 = PureWindowsPath(Folder_path_1)

Folder_path_2 = Path(input("-Copy down the path for - 1N_1H_Survey_summary_.csv - Format should work for either Mac or Windows "))
path_on_windows_22 = PureWindowsPath(Folder_path_2)
path_on_windows_2 = os.path.join(path_on_windows_22, '1N_1H_Survey_summary_.csv')
# this is just for 1H
if Phase == "1H":
    os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+ Phase +"/Collection Hapex Stich")
else:
    os.chdir(path_on_windows_1)

Day_met_path = os.getcwd()
csv_R_m = glob.glob(os.path.join(Day_met_path, "*.csv"))

Whole_hh = []
Whole_num_events = []
Whole_time_cooked = []
Whole_PM_event = []
Whole_Cook_comp_event = []
Whole_cook_comp_phase = []
Whole_Fuel_removed_phase = []
Whole_Fuel_per_event = []
Whole_SAE = []
Whole_Fuel_used_scale = []
Whole_kitchen_volume = []

Second_Exact = 0
for file in csv_R_m:
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        for idx, row in enumerate(csv_reader):
            if 'Household ID:' in row:
                id_number = (row[1])
                print('The household ID number is:  ',  (id_number))
            elif 'Timestamp' in row:
                Fueltype = row[1]
                Exact = row[3]
                Usage = row[2]
                K_hapex = row[5]
                C_hapex = row[7]
                data_start = idx

                if len(row) < 9:
                    print('There is no second exact')
                    Second_Exact = 0
                    Two_exact = [1]
                    break
                elif row[8] == 'Second EXACT Usage':
                    Exact_2 = row[9]
                    Usage_2 = row[8]
                    Second_Exact = 1
                    Two_exact = [1,2]
                    print('--------------Two EXACT-------------')
                break

    # this is so far from heather and her "Data Processing Instructions" Using fire Finder algorithm
    #Survey_path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/1N/1N_1H_Survey_summary_.csv"
    Survey_path = path_on_windows_2
    Survey_read = pd.read_csv(Survey_path)
    hhh_survey = Survey_read.iloc[:,1]
    for row, bed in enumerate(hhh_survey):
        if int(id_number) == int(bed):
            row_survey = int(row)
            break
    sensor_data = pd.read_csv(file, skiprows=data_start)

    No_fuel = 0
    No_exact = 0
    No_kitchen = 0
    No_cook = 0
    if sensor_data.iloc[0,1] == 'NO FUEL':
        print('There is no FUEL DATA')
        No_fuel = 1
    if sensor_data.iloc[0,2] == 'NO EXACT':
        print('There is no EXACT DATA')
        No_exact = 1
    if sensor_data.iloc[0,4] == 'NO KITCHEN':
        print('There is no kitchen HAPEx DATA')
        No_kitchen = 1
    if sensor_data.iloc[0,6] == 'NO COOK':
        print('There is no cook HAPEx DATA')
        No_cook = 1


    if No_exact != 1 and Second_Exact != 1:
        Usage, Fire_start_1, Fire_end_1 = Functions_malawi.FireFinder(sensor_data.iloc[:,3],sensor_data.iloc[:,2], cooking_threshold, length_decrease, start_threshold, end_threshold, merge_CE_threshold, min_CE_length, window_slope)
        temp = sensor_data.iloc[:,3]
    elif No_exact != 1 and Second_Exact == 1:
        Usage, Fire_start_1, Fire_end_1 = Functions_malawi.FireFinder(sensor_data.iloc[:,3],sensor_data.iloc[:,2], cooking_threshold, length_decrease, start_threshold, end_threshold, merge_CE_threshold, min_CE_length, window_slope)
        temp = sensor_data.iloc[:,3]
        Usage_2, Fire_start_2, Fire_end_2 = Functions_malawi.FireFinder(sensor_data.iloc[:,9],sensor_data.iloc[:,8], cooking_threshold, length_decrease, start_threshold, end_threshold, merge_CE_threshold, min_CE_length, window_slope)
        temp_2 = sensor_data.iloc[:,9]
    else:
        Fire_start_2 = 0
        Fire_end_2 = 0
        continue
    Fuel_KG_nf = sensor_data.iloc[:,1]

    KG_burned, Fuel_KG = Functions_malawi.FUEL_REMOVAL(Fuel_KG_nf, 0.005, 5, No_fuel)
    Fuel_removal_countdown = Functions_malawi.FuelRemovalTime(KG_burned,No_fuel)

    TimeStamp = (sensor_data.iloc[:,0])
    Cook_comp = sensor_data.iloc[:,6]
    Cook_PM = sensor_data.iloc[:,7]
    Kitchen_Comp = sensor_data.iloc[:, 4]
    Kitcen_PM = sensor_data.iloc[:, 5]


    event_T = []
    day = []
    day_test = []
    fmt_1 = '%Y-%m-%d %H:%M:%S'
    fmt_2 = '%m/%d/%Y %H:%M'
    format = "%m/%d"

    def try_parsing_date(test):
        for fmt in ('%m/%d/%Y %H:%M', '%Y-%m-%d %H:%M:%S'):
            try:
                return datetime.strptime(test, fmt)
            except ValueError:
                pass
        raise ValueError('no valid date format found')


    for d in TimeStamp:
        if int(id_number) != 2006:
            dayyy = '{:%m/%d}'.format(datetime.strptime(d,'%m/%d/%Y %H:%M'))
        else:
             dayyy = '{:%m/%d}'.format(datetime.strptime(d,'%m/%d/%Y %H:%M'))
            #   '%Y-%m-%d %H:%M:%S'   if there is an issue '%m/%d/%Y %H:%M'
        day.append(dayyy)
        Timeeee = datetime.strptime(d,'%m/%d/%Y %H:%M')
        event_T.append(Timeeee)
    for q in Two_exact:
        if No_exact == 0:
            if q == 1:
                Fire_start = Fire_start_1
                Fire_end = Fire_end_1
                temp = temp
            elif q == 2:
                Fire_start = Fire_start_2
                Fire_end = Fire_end_2
                temp = temp_2
                Usage = Usage_2 
        else:
            Fire_start = [-1, -1]
            Fire_end = [-1, -1]

        print('Gathering metrics to be anylized')
        E_Time_Start = []
        E_Time_End = []
        E_Event_length = []
        E_AVG_Temp = []
        E_STD_Temp = []
        ##Event Fuel
        E_Fuel_Used = []
        E_Time_Fuel_Remove = [] #how much time was fuel removed until fire started
        Fire_Start_Array = []
        Fire_End_Array = []
        ##Event Cook PM
        E_Avg_Cook_PM = []
        E_Med_Cook_PM = []
        E_STD_Cook_PM = []
        E_PC_Cook_Move =[]
        E_Spread_Cook_PM =[] #in order to get the average you need to extend to 5 and RAW
        E_Spread_AVG_Cook_PM = []
        E_CoolDown_Cook_PM = []
        E_CoolDoown_AVG_Cook_PM = []
        ##Event Kitchen PM
        E_Avg_Kit_PM = []
        E_Med_Kit_PM = []
        E_STD_Kit_PM = []
        E_PC_Kit_PM = []
        E_Spread_Kit_PM = [] #in order to get the average you need to extend to 5 and RAW
        E_Spread_AVG_Kit_PM = []
        E_CoolDown_Kit_PM = []
        E_CoolDoown_AVG_Kit_PM = []
        ##raw files needed to average whole phase
        Raw_E_Cook_PM = []
        Raw_E_Cook_Comp = []
        Raw_E_Kit_PM = []
        Raw_E_Kit_Comp = []
        Raw_E_Temp = []
        Raw_E_Fuel = []
        Raw_E_Fuel_removed = []
        Raw_Spread_Cook = []
        Raw_Spread_Kit = []
        Raw_CoolDown_Cook = []
        Raw_CoolDown_Kit = []
        filler_spread_values = np.full(shape=10,fill_value=-1)


        ##Gathering Metrics for the event

        for tv,st in enumerate(Fire_start):

            #if No_exact == 0:
                #Give the raw files a -1 to iterate over
                Value = np.arange(st, Fire_end[tv])
                filler_value = []
                for v in Value:
                    filler_value.append(-1)
                if No_exact == 1:
                    E_Time_Start.append(-1)
                    E_Time_End.append(-1)
                    E_Event_length.append(-1)
                    E_AVG_Temp.append(-1)
                    E_STD_Temp.append(-1)
                    Raw_E_Temp.extend(filler_value)
                    Fire_Start_Array.append(1)
                    Fire_End_Array.append(-1)
                else:
                    E_Time_Start.append(event_T[st])
                    E_Time_End.append(event_T[Fire_end[tv]])
                    E_Event_length.append((Fire_end[tv]-st))
                    E_AVG_Temp.append((int((np.average([a for a in temp[st:Fire_end[tv]]]))*10))/10)
                    E_STD_Temp.append((int((stat.stdev(temp[st:Fire_end[tv]]))*100))/100)
                    Raw_E_Temp.extend([a for a in temp[st:Fire_end[tv]]])
                    Fire_Start_Array.append(st)
                    Fire_End_Array.append(Fire_end[tv])
                    ##Starting Fuel Useage
                if No_fuel == 0 and No_exact == 0:
                    fuel_bounds = list(set(KG_burned[st:Fire_end[tv]]))
                    E_Fuel_Used.append((int((sum(fuel_bounds))*1000)/1000))
                    E_Time_Fuel_Remove.append(Fuel_removal_countdown[st])
                    #raw metrics
                    Raw_E_Fuel.extend([a for a in Fuel_KG_nf[st:Fire_end[tv]]])
                    Raw_E_Fuel_removed.extend(KG_burned[st:Fire_end[tv]])

                else:
                    E_Fuel_Used.append(-1)
                    E_Time_Fuel_Remove.append(-1)
                    Raw_E_Fuel.extend(filler_value)
                    Raw_E_Fuel_removed.extend(filler_value)
                ### Cook HAPEx
                if No_cook == 0 and No_exact == 0:
                    E_Avg_Cook_PM.append((int((np.average([a for a in Cook_PM[st:Fire_end[tv]]]))*100))/100)
                    E_Med_Cook_PM.append((int((np.median([a for a in Cook_PM[st:Fire_end[tv]]])) * 100)) / 100)
                    E_STD_Cook_PM.append((int((stat.stdev(Cook_PM[st:Fire_end[tv]])) * 100)) / 100)
                    E_PC_Cook_Move.append((int(((sum(Cook_comp[st:Fire_end[tv]]))/(Fire_end[tv]-st))*100)))
                    E_Cook_S_before = (list([a for a in Cook_PM[(st - 10):st]]))
                    E_cook_spread_combo = E_Cook_S_before + Cook_PM[st]
                    E_Spread_Cook_PM.extend(E_cook_spread_combo)
                    E_Spread_AVG_Cook_PM.append(np.average(E_Spread_Cook_PM))
                    #raw values for total compare
                    Raw_E_Cook_PM.extend([a for a in Cook_PM[st:Fire_end[tv]]])
                    Raw_E_Cook_Comp.extend([a for a in Cook_comp[st:Fire_end[tv]]])
                    Raw_Spread_Cook = E_Spread_Cook_PM
                    E_Cook_S_after = (list([a for a in Cook_PM[Fire_end[tv]:(st + 30)]]))
                    E_CoolDown_Cook_PM.extend(E_Cook_S_after)
                    E_CoolDoown_AVG_Cook_PM.append(np.average(E_Cook_S_after))
                    Raw_CoolDown_Cook = E_CoolDown_Cook_PM
                else:
                    E_Avg_Cook_PM.append(-1)
                    E_Med_Cook_PM.append(-1)
                    E_STD_Cook_PM.append(-1)
                    E_PC_Cook_Move.append(-1)
                    E_Spread_AVG_Cook_PM.append(-1)
                    Raw_E_Cook_PM.extend(filler_value)
                    Raw_E_Cook_Comp.extend(filler_value)
                    Raw_Spread_Cook.extend(filler_spread_values)
                    E_CoolDown_Cook_PM.append(-1)
                    E_CoolDoown_AVG_Cook_PM.append(-1)

                    Raw_CoolDown_Cook.extend(filler_spread_values)

                
                # Kitchen HAPEx
                if No_kitchen == 0 and No_exact == 0:
                    E_Avg_Kit_PM.append((int((np.average([a for a in Kitcen_PM[st:Fire_end[tv]]]))*100))/100)
                    E_Med_Kit_PM.append((int((np.median([a for a in Kitcen_PM[st:Fire_end[tv]]])) * 100)) / 100)
                    E_STD_Kit_PM.append((int((stat.stdev(Kitcen_PM[st:Fire_end[tv]])) * 100)) / 100)
                    E_PC_Kit_PM.append((int((sum(Kitchen_Comp[st:Fire_end[tv]]))/(len(Kitchen_Comp[st:Fire_end[tv]]))*100)))

                    E_Kit_S_before = (list([a for a in Kitcen_PM[(st - 10):st]]))
                    E_Kit_spread_combo = E_Kit_S_before  + Kitcen_PM[st]
                    E_Spread_Kit_PM.extend(E_Kit_spread_combo)
                    E_Spread_AVG_Kit_PM.append(np.average(E_Spread_Kit_PM))

                    E_Kit_S_after = (list([a for a in Kitcen_PM[Fire_end[tv]:(Fire_end[tv] + 30)]]))
                    E_CoolDoown_AVG_Kit_PM.append(np.average(E_Kit_S_after))
                    E_CoolDown_Kit_PM.extend(E_Kit_S_after)
                    # raw values for total compare
                    Raw_E_Kit_PM.extend([a for a in Kitcen_PM[st:Fire_end[tv]]])
                    Raw_E_Kit_Comp.extend([a for a in Kitchen_Comp[st:Fire_end[tv]]])
                    Raw_Spread_Kit = E_Spread_Kit_PM
                    Raw_CoolDown_Kit = E_CoolDown_Kit_PM
                else:
                    E_Avg_Kit_PM.append(-1)
                    E_Med_Kit_PM.append(-1)
                    E_STD_Kit_PM.append(-1)
                    E_PC_Kit_PM.append(-1)
                    E_CoolDoown_AVG_Kit_PM.append(-1)
                    E_Spread_AVG_Kit_PM.append(-1)
                    Raw_CoolDown_Kit.append(filler_value)
                    Raw_E_Kit_PM.extend(filler_value)
                    Raw_E_Kit_Comp.extend(filler_value)
                    Raw_Spread_Kit.extend(filler_spread_values)


        Event_num = np.arange(1,len(E_Event_length)+1,1)
        print('------------------------ Length of spread, cooldown kit, cooldown cook, time value, event number', len(E_Spread_AVG_Kit_PM), len(E_CoolDoown_AVG_Kit_PM),len(E_CoolDoown_AVG_Cook_PM), len(Fire_Start_Array), len(Event_num))
        Data_event = {'| Event Number |' : Event_num,
                          '| Event Start |' : E_Time_Start,
                           '| Event Stop |' : E_Time_End,
                           'Start Time Value':Fire_Start_Array, 'End Time Vlaue':Fire_End_Array,
                          '| Removed Fuel Before Start (min) |' : E_Time_Fuel_Remove,
                           '| Length of Event (min)|': E_Event_length,
                           '| Fuel Used (FUEL) |' : E_Fuel_Used,
                           '| Average Temperature for Event (EXACT) |' : E_AVG_Temp,
                           '| Std of Event Temperature |' : E_AVG_Temp,
                           '| Average PM for Cook in Event (HAPEx) |' : E_Avg_Cook_PM,
                           '| Median PM for Cook in Event (HAPEx) |': E_Med_Cook_PM,
                           '| Std of Cook PM |' : E_STD_Cook_PM,'30 Minute Cooldown Cook':E_CoolDoown_AVG_Cook_PM,
                          '| 10 minutes spread Cook Exposure|' : E_Spread_AVG_Cook_PM,
                           '| Percentage Cook Compliance for Event (HAPEx) |': E_PC_Cook_Move,
                           '| Average PM in Kitchen for Event (HAPEx) |' : E_Avg_Kit_PM,
                           '| Median PM in Kitchen for Event (HAPEx) |' : E_Med_Kit_PM,
                           '| Std of Kitchen PM |' : E_STD_Kit_PM,
                           '30 Minute Cooldown Kitchen':E_CoolDoown_AVG_Kit_PM,
                           '| 10 minutes spread Kitchen PM |' : E_Spread_AVG_Kit_PM,
                           '| Percentage Kitchen Compliance for Event (HAPEx) |' : E_PC_Kit_PM}

        df_event = pd.DataFrame(Data_event)

            # getting the RAW data into csv to compare to other households
        if No_exact == 0:
            Raw_E_Fuel = Raw_E_Fuel
            Raw_E_Fuel_removed = Raw_E_Fuel_removed
            Raw_E_Temp = Raw_E_Temp
            Raw_E_Cook_Comp = Raw_E_Cook_Comp
            Raw_E_Kit_Comp = Raw_E_Kit_Comp
            Raw_E_Cook_PM = Raw_E_Cook_PM
            Raw_E_Kit_PM = Raw_E_Kit_PM
        else:
            Raw_E_Fuel = [-1, -1]
            Raw_E_Fuel_removed = [-1, -1]
            Raw_E_Temp = [-1, -1]
            Raw_E_Cook_Comp = [-1, -1]
            Raw_E_Kit_Comp = [-1, -1]
            Raw_E_Cook_PM = [-1, -1]
            Raw_E_Kit_PM = [-1, -1]

        RAW_event = {'Fuel Raw Data': Raw_E_Fuel, 'Fuel Removed (kg change)': Raw_E_Fuel_removed,
                     'Temperature per event': Raw_E_Temp,
                     'Cook Compliance': Raw_E_Cook_Comp,
                     'Kitchen Compliance': Raw_E_Kit_Comp,
                     'Cook PM': Raw_E_Cook_PM, 'Kitchen PM': Raw_E_Kit_PM}

        RAW_Spread_PM = {'10 minutes spread (Cook PM)': Raw_Spread_Cook,'10 minutes spread (Kitchen PM)': Raw_Spread_Kit}
        Raw_Cool_down_pm = { '30 Cooldown spread (Cook PM)': Raw_Spread_Cook,'30 Cooldown spread (Kitchen PM)': Raw_CoolDown_Kit}
        Df_raw_event = pd.DataFrame(RAW_event)
        Df_first_five = pd.DataFrame(RAW_Spread_PM)
            # Taking some metrics that need to be compared to each other, will be in own CSV file
            # these metrics are to be compared to other households, there are no averages inside here
            # these are repeated, but want to have a separate file to easily gather

        Summary_event = {'Length of Event':E_Event_length,'Fuel Used (FUEL)' : E_Fuel_Used,
                             'Removed Fuel Before Start (min)': E_Time_Fuel_Remove,
                             'Percentage Cook Compliance for Event (HAPEx)': E_PC_Cook_Move,
                             'Percentage Kitchen Compliance for Event (HAPEx)' : E_PC_Kit_PM }

        Df_Summary_Event = pd.DataFrame(Summary_event)

        index_sensors = [0]
        Sensors_used = {'Household Number' : str(id_number),
                            'Fuel Sensor and Type' : Fueltype,
                            'Exact Sensor and Stove Type' : Exact,
                            'Kitchen HAPEx': K_hapex,
                            'Cook HAPEx' : C_hapex}

        Df_sensor = pd.DataFrame(Sensors_used, index=index_sensors)


        ### iterate over the day

        Day_start = []
        Day_end = []
        Date_day = []
        count = 0

        for stamp in day:
            if count +1 == len(day):
                Day_end.append(((len(day))-1))
                Date_day.append(stamp)
                break
            elif stamp != day[count+1]:
                Day_end.append(count)
                Date_day.append(stamp)
                Day_start.append(count +1)
            count = count +1


        Day_start[:0] = [0]
        ## starting with day metrics
        ##Day Fuel
        D_Fuel_Used = []
        D_AVG_Temp = []
        D_STD_Temp = []

        ##Day Cook PM
        D_Avg_Cook_PM = []
        D_Med_Cook_PM = []
        D_STD_Cook_PM = []
        D_PC_Cook_Move =[]

        ##Day Kitchen PM
        D_Avg_Kit_PM = []
        D_Med_Kit_PM = []
        D_STD_Kit_PM = []
        D_PC_Kit_PM = []

        ##raw files needed to average whole phase
        Raw_D_Cook_PM = []
        Raw_D_Cook_Comp = []
        Raw_D_Kit_PM = []
        Raw_D_Kit_Comp = []
        Raw_D_Temp = []
        Raw_D_Fuel = []
        Raw_D_Fuel_removed = []
        FUEL_filter = []
        Alg_2_KG_Burned = []
        ff_usage = []
        d_count = 1
        for tv, ds in enumerate(Day_start):
            # Give the raw files a -1 to iterate over
            Value = np.arange(ds, Day_end[tv])
            filler_value = []
            for v in Value:
                filler_value.append(-1)
            ## Cooking Characteristics
            fuel_per_day = []
            if No_fuel == 0:
                for val, a in  enumerate(KG_burned[ds:Day_end[tv]]):
                    if val+1 == len(KG_burned[ds:Day_end[tv]]):
                        fuel_per_day.append(a)
                        continue
                    elif a != KG_burned[ds + val + 1]:
                        fuel_per_day.append(a)
                #fuel_per_day = list(set([a for a in KG_burned[ds:Day_end[tv]]]))
                D_Fuel_Used.append((int((sum(fuel_per_day))*1000)/1000))
                
                Raw_D_Fuel.extend(Fuel_KG_nf[ds:Day_end[tv]])
                Raw_D_Fuel_removed.extend(KG_burned[ds:Day_end[tv]])
                FUEL_filter.extend(Fuel_KG[ds:Day_end[tv]])
                
            else:
                D_Fuel_Used.append(-1)
                Raw_D_Fuel.extend(filler_value)
                Raw_D_Fuel_removed.extend(filler_value)
                FUEL_filter.extend(filler_value)
                Alg_2_KG_Burned.extend(filler_value)

            #temperature and exact characteristics
            if No_exact == 0:
                DAY_TEMP = [a for a in temp[ds:Day_end[tv]]]
                D_AVG_Temp.append((int((np.average(DAY_TEMP)*10))/10))
                D_STD_Temp.append((int((stat.stdev(DAY_TEMP)) * 100)) / 100)
                Raw_D_Temp.extend(temp[ds:Day_end[tv]])
                ff_usage.extend(Usage[ds:Day_end[tv]])
            else:
                D_AVG_Temp.append(-1)
                D_STD_Temp.append(-1)
                Raw_D_Temp.extend(filler_value)
                ff_usage.extend(filler_value)
            #Finding the Cook's
            if No_cook == 0:
                D_Cook_PM = ([a for a in Cook_PM[tv:Day_end[tv]]])
                D_Avg_Cook_PM.append((int((np.average(D_Cook_PM))*100))/100)
                D_Med_Cook_PM.append((int((np.median(D_Cook_PM))*100))/100)
                D_STD_Cook_PM.append((int((stat.stdev(D_Cook_PM)) * 100)) / 100)
                D_PC_Cook_Move.append((int((sum(Cook_comp[ds:Day_end[tv]]))/(len(Cook_comp[ds:Day_end[tv]]))*100)))
                Raw_D_Cook_PM.extend(Cook_PM[ds:Day_end[tv]])
                Raw_D_Cook_Comp.extend(Cook_comp[ds:Day_end[tv]])
            else:
                D_Avg_Cook_PM.append(-1)
                D_Med_Cook_PM.append(-1)
                D_STD_Cook_PM.append(-1)
                D_PC_Cook_Move.append(-1)
                Raw_D_Cook_PM.extend(filler_value)
                Raw_D_Cook_Comp.extend(filler_value)
            # Finding the Kitchen's
            if No_kitchen == 0:
                D_Kit_PM = ([a for a in Kitcen_PM[tv:Day_end[tv]]])
                D_Avg_Kit_PM.append((int((np.average(D_Kit_PM))*100))/100)
                D_Med_Kit_PM.append((int((np.median(D_Kit_PM))*100))/100)
                D_STD_Kit_PM.append((int((stat.stdev(D_Kit_PM)) * 100)) / 100)
                D_PC_Kit_PM.append((int((sum(Kitchen_Comp[ds:Day_end[tv]]))/(len(Kitchen_Comp[ds:Day_end[tv]]))*100)))
                Raw_D_Kit_PM.extend(Kitcen_PM[ds:Day_end[tv]])
                Raw_D_Kit_Comp.extend(Kitchen_Comp[ds:Day_end[tv]])
            else:
                D_Avg_Kit_PM.append(-1)
                D_Med_Kit_PM.append(-1)
                D_STD_Kit_PM.append(-1)
                D_PC_Kit_PM.append(-1)
                Raw_D_Kit_PM.extend(filler_value)
                Raw_D_Kit_Comp.extend(filler_value)
            ## Raw files to be used for phase averages


            d_count = d_count +  1
            if d_count == len(Day_start)+1:
                break

        Data_day = {'| DAY |' : Date_day, '| Fuel Removed (FUEL) |' : D_Fuel_Used,
                    '| Average Temperature (EXACT) |' : D_AVG_Temp,
                    '| Std Temperature |' : D_STD_Temp,
                    '| Average PM for Cook (HAPEx) |' : D_Avg_Cook_PM,
                    '| Median PM for Cook (HAPEx) |': D_Med_Cook_PM,
                    '| Std of Cook exposure |' : D_STD_Cook_PM,
                    '| Percentage Cook Movement(HAPEx) |':D_PC_Cook_Move,
                    '| Average PM in Kitchen for day (HAPEx) |' : D_Avg_Kit_PM,
                    '| Median PM in Kitchen for day (HAPEx) |' : D_Med_Kit_PM,
                    '| Std of Kitchen exposure |' : D_STD_Kit_PM,
                    '| Percentage Kitchen sensor moving (HAPEx) |' : D_PC_Kit_PM}


        Df_day = pd.DataFrame(Data_day)

        
        RAW_day = {'Fuel Raw Data': Raw_D_Fuel, 'Fuel Removed (kg change)': Raw_D_Fuel_removed,'Fuel Filterd':FUEL_filter, 'ff Usage':ff_usage,
                     'Temperature per day': Raw_D_Temp,
                    'Cook Compliance': Raw_D_Cook_Comp,
                     'Kitchen Compliance': Raw_D_Kit_Comp,
                    'Cook PM': Raw_D_Cook_PM, 'Kitchen PM': Raw_D_Kit_PM}
        Df_raw_day = pd.DataFrame(RAW_day)
        
        # summary of day is values that are going to be compared to other phases
        Summary_day = {'Fuel Removed (FUEL)' : D_Fuel_Used,
                         'Percentage Cook Compliance for Event (HAPEx)': D_PC_Cook_Move,
                         'Percentage Kitchen Compliance for Event (HAPEx)' : D_PC_Kit_PM }

        Df_Summary_day = pd.DataFrame(Summary_day)

        #if int(id_number) == 1034:
        #    minute_count = np.arange(0,len(Raw_D_Fuel), 1)
        #    #print('minute and graph lengths', len(minute_count), len(Raw_D_Fuel))
        #    fig = go.Figure()
        #    fig.add_trace(go.Scatter(x=minute_count, y=Raw_D_Fuel,
        #                        mode='lines',
        #                        name='Raw Fuel Sensor'))
        #    fig.add_trace(go.Scatter(x=minute_count, y=Raw_D_Fuel_removed,
        #                        mode='lines',
        #                        name='Fuel Removed'))
        #    fig.add_trace(go.Scatter(x=minute_count, y=FUEL_filter,
        #                        mode='lines', name='Fuel Filter'))
        #    fig.add_trace(go.Scatter(x=minute_count, y=Raw_D_Temp,
        #                        mode='lines', name='Temperature'))
        #    fig.add_trace(go.Scatter(x=minute_count, y=Alg_2_KG_Burned,
        #                        mode='lines', name='Pre Removal Spiked Filter'))
        #    fig.update_layout(title=Phase+'_'+id_number+'_Fuel Data Cleaning',
        #                       xaxis_title='Threshold',
        #                       yaxis_title='Fuel Removed')
        #    fig.show()
        print('Exporting to csv format...')
        # making all different CSV files for all metrics (This spit out 6 different files)
        ###first is the Specific summary metrics for Household
        Path_HH_Sum_event = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_"+str(q)+"_exact/HH_summary_Event"
        File_name_HH_sum_Event = str(Path_HH_Sum_event) + "/"+ Phase +"_HH_Summary_Event_"+str(id_number)+"_"+str(q)+"_exact_2.2"+".csv"
        #Df_sensor.to_csv(File_name_HH_sum_Event)
        #df_event.to_csv(File_name_HH_sum_Event,index=False,mode='a')

        Path_HH_Sum_day = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_"+str(q)+"_exact/HH_summary_Day"
        File_name_HH_sum_Day = str(Path_HH_Sum_day) + "/"+ Phase+"_HH_Summary_Day_"+str(id_number)+"_"+str(q)+"_exact_2.2"+".csv"
        #Df_sensor.to_csv(File_name_HH_sum_Day)
        #Df_day.to_csv(File_name_HH_sum_Day,index=False, mode= 'a')

        Path_Raw_Event = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_"+str(q)+"_exact"
        File_event_Raw_metrics = str(Path_Raw_Event) + "/Raw_E_metrics/"+Phase+"_HH_raw_Event_metrics_"+str(id_number)+"_"+str(q)+"_exact_2.2"+".csv"
        #Df_sensor.to_csv(File_event_Raw_metrics)
        #Df_raw_event.to_csv(File_event_Raw_metrics,index=False,mode='a')

        File_event_Raw_summary = str(Path_Raw_Event) + "/Raw_E_summary/"+Phase+"_HH_raw_Event_summary_"+str(id_number)+"_"+str(q)+"_exact_2.2"+".csv"
        #Df_sensor.to_csv(File_event_Raw_summary)
        #Df_Summary_Event.to_csv(File_event_Raw_summary,index=False,mode='a')

        File_event_Raw_first_five = str(Path_Raw_Event) + "/Raw_E_first_five/"+ Phase+"_HH_Event_first_five_"+str(id_number)+"_"+str(q)+"_exact_2.2"+".csv"
        #Df_sensor.to_csv(File_event_Raw_first_five)
        #Df_first_five.to_csv(File_event_Raw_first_five,index=False,mode='a')

        Path_Raw_Day = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_"+str(q)+"_exact"
        File_Day_Raw_metrics = str(Path_Raw_Day) + "/Raw_D_metrics/"+Phase+"_HH_raw_Day_metrics_"+str(id_number)+"_"+str(q)+"_exact_3.55555"+".csv"
        
        #Df_sensor.to_csv(File_Day_Raw_metrics)
        
        #Df_raw_day.to_csv(File_Day_Raw_metrics, index=False,mode='a')

        File_Day_Raw_summary = str(Path_Raw_Day) + "/Raw_D_summary/"+ Phase+ "_HH_raw_Day_summary_"+str(id_number)+"_"+str(q)+"_exact_2.5"+".csv"
        #Df_sensor.to_csv(File_Day_Raw_summary)
        #Df_Summary_day.to_csv(File_Day_Raw_summary, index=False,mode='a')

        # metrics for whole 


        Whole_hh.append(str(id_number))
        Whole_num_events.append(len(Event_num))
        Whole_time_cooked.append(sum(Usage))
        Whole_PM_event.append((np.average(Raw_E_Kit_Comp)))
        Whole_Cook_comp_event.append((sum(Raw_E_Cook_Comp))/(len(Raw_E_Cook_Comp)))
        Whole_cook_comp_phase.append((sum(Raw_D_Cook_Comp))/(len(Raw_D_Cook_Comp)))
        Whole_Fuel_removed_phase.append(sum(D_Fuel_Used))
        Whole_Fuel_per_event.append((sum(D_Fuel_Used))/(len(Event_num)))
        Whole_SAE.append(Survey_read.iloc[row_survey,7])
        Whole_Fuel_used_scale.append(Survey_read.iloc[row_survey,19])
        Whole_kitchen_volume.append(Survey_read.iloc[row_survey,15])

Metric_compare = {'Household':Whole_hh, 'Number of Events':Whole_num_events, 'Time Cooked':Whole_time_cooked, 'Avg Kitchen PM per event': Whole_PM_event,
 '% Cook moving for Cooking':Whole_Cook_comp_event, '% Cook moving for Phase': Whole_cook_comp_phase, 'Fuel Used per Phase':Whole_Fuel_removed_phase,
 'Fuel used per Event':Whole_Fuel_per_event, 'Average People fed':Whole_SAE, '0 = wood, 1= Residue':Whole_Fuel_used_scale, 'Kitchen Volume (m^3)':Whole_kitchen_volume}
DF_Metric_compare = pd.DataFrame(Metric_compare)
#print(DF_Metric_compare)

# sns.set(style='ticks')
# f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios":(0.15, 0.85)})
# sns.boxplot(Whole_kitchen_volume, ax=ax_box, color='g')
# sns.histplot(Whole_kitchen_volume, ax=ax_hist, color='g')
# ax_box.set(yticks=[])
# sns.despine(ax=ax_hist)
# sns.despine(ax=ax_box, left=True)
# plt.title('1N Kitchen Volume')
# plt.ylim(top=8)
# plt.ylim(bottom=0)
