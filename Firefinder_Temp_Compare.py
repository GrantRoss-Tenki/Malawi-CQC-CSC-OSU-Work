import itertools
import os
import pandas as pd
import numpy as np
import csv
import glob
from decimal import *
from itertools import chain
#import statistics as stat
import datetime
from datetime import datetime
from itertools import islice, cycledfas
import matplotlib.pyplot as plt
import seaborn as sns

Phase  = input("What phase? -1N or 2N or 3N or 4N - ") 
computer = input("personal or work computer - ")

if computer == "work":
    USB = "D"
    #os.chdir("C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+ Phase +"/Collection")
else:
    os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Collection")
    USB = "D"
Household_FF = []
Cooking_Time = []
Num_of_Events = []
Cooking_Time_2 = []
Num_of_Events_2 = []
Second_Exact = 0
#os.chdir(USB+":/24_hour_pump/"+Phase+"/Collection")

Day_met_path = os.getcwd()
csv_R_m = glob.glob(os.path.join(Day_met_path, "*.csv"))

second_exact_is_for_the_second_stove = 0
Household_count = 0
for file in csv_R_m:
    Household_count = Household_count + 1
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        for idx, row in enumerate(csv_reader):
            if 'Household ID:' in row:
                id_number = (row[1])
                print('------- ID Number------', id_number)
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
                    break
                elif row[8] == 'Second EXACT Usage':
                    Exact_2 = row[9]
                    Usage_2 = row[8]
                    Second_Exact = 1
                    print('--------------Two EXACT-------------')
                break

    # this is so far from heather and her "Data Processing Instructions" Using fire Finder algorithm

    sensor_data = pd.read_csv(file, skiprows=data_start)
    #print('Type of fuel used:  ',Fueltype)
    #print('Type of exact used:  ',Exact)
    #print('Type of Kitchen Hapex:  ',(K_hapex))
    #print('Type of Cook Hapex:  ',(C_hapex))
    print('The household ID number is:  ',  (id_number))

    #print('this is the exact row ', Exact)
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

    second_exact_is_for_the_second_stove = 0
    count = 1
    Two_exact = [1]
    if No_exact == 0:
        if Second_Exact == 1:
            Two_exact.append(2)

        for q in Two_exact:
            if q == 1 and second_exact_is_for_the_second_stove == 0 :
                Usage = sensor_data.iloc[:,2]
                temp = sensor_data.iloc[:,3]
                Testing_end_thresh = np.arange(0, 1, 1)
                Is_thresh_good = []
            elif q ==2 and len(Two_exact)>1 and Second_Exact== 1:
                Usage = sensor_data.iloc[:,8]
                temp = sensor_data.iloc[:,9]
                Testing_end_thresh = np.arange(0, 1, 1)
                second_exact_is_for_the_second_stove = 1
                print('==============second_exact_is_for_the_second_stove================',second_exact_is_for_the_second_stove)
                Is_thresh_good = []
            else:

                break
            for tet in Testing_end_thresh:
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

                n = len(Usage) - 1
                Temp_slope = []
                print('n length', n)
                count = 1
                for t, us in enumerate(Usage):
                    if window_slope < (n+1) - t:
                        actual_slope = window_slope
                    #elif n == t: 
                    #    Temp_slope.append(0)
                    #    actual_slope = n - 2
                    #    break
                    else:
                        actual_slope = (n+1) - t
                    if t < window_slope - 1:
                        Temp_slope.append(0)
                    elif n > t + actual_slope:
                        f1 = temp[actual_slope + t] - temp[t]
                        Temp_slope.append((f1/actual_slope))
                    elif n <= t + actual_slope:
                        Temp_slope.append(0)
                        
                print('length of usage', len(Usage))
                print('length of temp slope', len(Temp_slope))


                ## this is to get out the singe times in midst of burning event

                neg_slope = 0
                for t,s in enumerate(Temp_slope):
                    if s <= 1:
                        if temp[t] < 127:# and temp[t] > cooking_threshold:
                            neg_slope = neg_slope +1

                        else:
                            neg_slope = 0
                    else:
                        neg_slope = 0
                    if neg_slope > length_decrease:   
                        Usage[t - length_decrease: t+1] = 0


                for t,s in enumerate(Temp_slope):
                    if s <= end_threshold and temp[t] != 127:
                        Usage[t] = 0
                    elif s > start_threshold:
                        Usage[t] = 1
                
                        
                CE_time = 0
                time_since_no_cooking = 0
                ISCOOKING = False

                for v,f in enumerate(Usage):
                    if f == 0:
                        time_since_no_cooking = time_since_no_cooking + 1
                        ISCOOKING = False
                    elif f == 1:
                        if (ISCOOKING == False) and (time_since_no_cooking < merge_CE_threshold) and (CE_time > 0):
                            tsnc = np.arange(0, time_since_no_cooking+1, 1)
                            for c,g in enumerate(tsnc):
                                Usage[v-c] = 1
                        ISCOOKING = True
                        time_since_no_cooking  = 0
                        CE_time = CE_time +1


                CE_time = 0
                ISCOOKING = False
                nb_cooking_ev = 0
                nb_minute_cook = 0
                nb_minute_inter = 0
                ff_start = []
                ff_end = []
                start_cooking = []
                for t,c in enumerate(Usage):
                    nb_minute_inter = nb_minute_inter + 1
                    if c  == 1:
                        CE_time = CE_time + 1
                        ISCOOKING = True
                        start_cooking.append(t)
                    elif c == 0:
                        if (ISCOOKING == True) and (CE_time < min_CE_length):
                            ce_tme_span = np.arange(0,CE_time,1)
                            for i, te in enumerate(ce_tme_span):
                                Usage[t-i-1] = 0
                            start_cooking = []

                        elif (ISCOOKING == True) and CE_time > min_CE_length:
                            nb_cooking_ev = nb_cooking_ev +1
                            nb_minute_cook = nb_minute_cook + CE_time
                            nb_minute_inter = 0
                            split_dif_sum = sum([a for a in Usage[start_cooking[0]:t]])
                            split_diff = t - start_cooking[0]
                            if (split_dif_sum/split_diff) > 0.75:
                                ff_start.append(start_cooking[0])
                                ff_end.append(t)

                            start_cooking = []
                        ISCOOKING = False
                        CE_time = 0
                Cooking_Time_sumation = np.sum(Usage)
                Fire_start = ff_start
                Fire_end = ff_end
                Is_thresh_good.append(len(Fire_start))
                #if statment counting for the second stove and exact sensor
                if Second_Exact == 1 and q == 2:
                    Fire_start_2 = Fire_start
                    Fire_end_2 = Fire_end
                    break
                elif Second_Exact == 0 or q == 1:
                    Fire_start_1 = Fire_start
                    Fire_end_1 = Fire_end
                else:
                    count = count + 1

            Temp_counter = np.arange(0, len(sensor_data.iloc[:,3]),1)
            # first is to change the cooking to 7 or greater 
            if No_exact == 0:
                if second_exact_is_for_the_second_stove == 0:
                    Temperature_filter = []
                    for te in sensor_data.iloc[:,3]:
                        if te >= cooking_threshold:
                            Temperature_filter.append(te)
                        else:
                            Temperature_filter.append(0)


                    #print(Fire_start[0])
                    Fire_Finder_Cooking = []
                    Event_Count = 0
                    for val in Temp_counter:
                        if Event_Count > len(Fire_start)-1: # or Event_Count > 20:
                            Fire_Finder_Cooking.append(0)
                            cut_off = val + 1

                        elif val == Fire_start[Event_Count]:
                            Fire_Finder_Cooking.append(cooking_threshold)
                        elif val <= Fire_end[Event_Count] and val > Fire_start[Event_Count]:
                            Fire_Finder_Cooking.append(cooking_threshold)
                            if val == Fire_end[Event_Count]:
                                Event_Count = Event_Count +1
                        else: 
                            Fire_Finder_Cooking.append(0)
                else:
                    Temperature_filter = []
                    for te in sensor_data.iloc[:,3]:
                        if te >= cooking_threshold:
                            Temperature_filter.append(te)
                        else:
                            Temperature_filter.append(0)


                    #print(Fire_start[0])
                    Fire_Finder_Cooking = []
                    Event_Count = 0
                    for val in Temp_counter:
                        if Event_Count > len(Fire_start)-1: # or Event_Count > 20:
                            Fire_Finder_Cooking.append(0)
                            cut_off = val + 1

                        elif val == Fire_start[Event_Count]:
                            Fire_Finder_Cooking.append(cooking_threshold)
                        elif val <= Fire_end[Event_Count] and val > Fire_start[Event_Count]:
                            Fire_Finder_Cooking.append(cooking_threshold)
                            if val == Fire_end[Event_Count]:
                                Event_Count = Event_Count +1
                        else: 
                            Fire_Finder_Cooking.append(0)
            else:
                Usage = 0
                Event_Count = 0
        

            if len(Two_exact) > 1 and second_exact_is_for_the_second_stove == 1:
                Cooking_Time_2.append(Cooking_Time_sumation)
                Household_FF.append(id_number)
                Num_of_Events_2.append(len(Fire_start))
                Num_of_Events.append(-1)
                Cooking_Time.append(-1)
                print('----this is the HH number 1', len(Household_FF),Household_FF)
                print('----this is cooking time 1', len(Cooking_Time),Cooking_Time)
                print('----this is cooking time 2', len(Cooking_Time_2),Cooking_Time_2)
                print('----this is event number 1', len(Num_of_Events),Num_of_Events)
                print('----this is event number 2', len(Num_of_Events_2),Num_of_Events_2)
            else:
                Cooking_Time.append(Cooking_Time_sumation)
                Household_FF.append(id_number)
                Num_of_Events.append(Event_Count)
                Num_of_Events_2.append(-1)
                Cooking_Time_2.append(-1)
                print('----this is the HH number 1', len(Household_FF),Household_FF)
                print('----this is cooking time 1', len(Cooking_Time),Cooking_Time)
                print('----this is cooking time 2', len(Cooking_Time_2),Cooking_Time_2)
                print('----this is event number 1', len(Num_of_Events),Num_of_Events)
                print('----this is event number 2', len(Num_of_Events_2),Num_of_Events_2)


Tryoutdata = {'Household': Household_FF, 'Cooking Time first stove': Cooking_Time, 
    'Num_of_Events for first stove': Num_of_Events,'Cooking Time second stove': Cooking_Time_2, 
    'Num_of_Events for second stove': Num_of_Events_2}

DF_tryout = pd.DataFrame(Tryoutdata)
path = USB+":/24_hour_pump/"+Phase+"/Phase_"+Phase+"_Firefinder_both.csv"
DF_tryout.to_csv(path, index=False, mode= 'a')


