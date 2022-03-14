# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:28:31 2022

@author: rossgra
"""
import itertools
import os
import pandas as pd
import numpy as np
import csv
import glob
from decimal import *
from itertools import chain

Phase = "1H"
Exact = "1"
computer = "personal"

HH_list_no_hood = ['1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011','1012','1013','1014','1015','1016','1017',
           '1018','1019','1020','1021','1022','1023','1024','1025','1026','1027','1028','1029','1030','1031','1032','1033','1034',
           '1035','1036','1037','1038','1039','1040']
HH_list_hood = ['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
if Phase == ("1H") or Phase == "2H" or Phase == "3H":
    HH_list = HH_list_hood
else:
    HH_list =HH_list_no_hood
    
if computer == "work":
    USB = "D"
    os.chdir(USB+":/24_hour_pump/"+Phase+"/Raw_pump_Time")  
if computer == "personal":
    USB = "E"
    os.chdir(USB+":/24_hour_pump/"+Phase+"/Raw_pump_Time")
#Gathering pump metric information
PUmp_mertics_path = (USB+":/24_hour_pump/"+Phase+"/pump metrics_"+Phase+"_.csv")
Pump_Metrics = pd.read_csv(PUmp_mertics_path, delimiter=',')
HouseHold_pump = Pump_Metrics.iloc[:,0]
Pump_start_time_value = Pump_Metrics.iloc[:,1]
#print('pump star time value and type',Pump_start_time_value[5], type(Pump_start_time_value[5]))
Pump_pumped_time = Pump_Metrics.iloc[:,4]
#print('pump star time',Pump_pumped_time, type(Pump_pumped_time))
#metrics that i want to gather for the output and compare 
Household_looked_at = []
Number_of_pumped_events = []
Pump_cooking_time = []
is_thresh_good = []
Day_met_path = os.getcwd()
csv_R_m = glob.glob(os.path.join(Day_met_path, "*.csv"))
files = []
for file in csv_R_m:
    files.append(file)

for exact, jj in enumerate(files):
    for num, l in enumerate(HH_list):
        if (int(jj[39]) == int(Exact)) and (int(HH_list[num]) == int(jj[41] +jj[42]+jj[43]+jj[44])):
            for hh_line,hhh in enumerate(HouseHold_pump):
                read_file = pd.read_csv(jj)
                Household = HH_list[num]
                #print('this is the hh', Household, hhh)
                if (hhh == int(HH_list[num])) and ((Pump_start_time_value[hh_line] != -1)):
                    Household_looked_at.append(Household)
                    print('they are the same',Household)
                    FF_go = 1
                elif (len(read_file.iloc[:,0]) < 6):# or (Pump_start_time_value[hh_line] == -1):
                    print('ther is no exact for this house',Household)
                    Household_looked_at.append(Household)
                    Pump_cooking_time.append(-1)
                    Number_of_pumped_events.append(-1)
                    FF_go = 0
                    break
                else:
                    FF_go = 0

                if FF_go == 1:
                    temp = []
                    spread = int(Pump_start_time_value[hh_line])+int(Pump_pumped_time[hh_line])+1
                    
                    for t in read_file.iloc[:,0]: #read_file.iloc[int(Pump_start_time_value[hh_line]):spread,0]
                        if int(float(t)) == 'Exact 1 Temp':
                            print('this ')
                        temp.append(int(float(t)))
                    #print('len temp', len(temp))
                    usage =  read_file.iloc[:,1] #read_file.iloc[int(Pump_start_time_value[hh_line]):spread,1]
                    testing_end_thresh = np.arange(0, 1, 1)

                    for tet in testing_end_thresh:
                            if Phase  == ("2N") or Phase == "3N" or Phase == "3H" or Phase == "4N":
                                print('-00-------- phase change- ------------')
                                cooking_threshold = 5
                                length_decrease = 40
                                start_threshold = 1
                                end_threshold = -5
                                merge_ce_threshold = 60
                                min_ce_length = 5
                                window_slope = 8
                            else:
                                cooking_threshold = 1
                                length_decrease = 10
                                start_threshold = 1
                                end_threshold = -5
                                merge_ce_threshold = 40
                                min_ce_length = 8
                                window_slope = 12

                            n = len(usage) - 1
                            temp_slope = []
                            print('n length', n)
                            count = 1
                            for t, us in enumerate(usage):
                                if window_slope < (n+1) - t:
                                    actual_slope = window_slope
                                #elif n == t: 
                                #    temp_slope.append(0)
                                #    actual_slope = n - 2
                                #    break
                                else:
                                    actual_slope = (n+1) - t
                                if t < window_slope - 1:
                                    temp_slope.append(0)
                                elif n > t + actual_slope:
                                    f1 = temp[actual_slope + t] - temp[t]
                                    temp_slope.append((f1/actual_slope))
                                elif n <= t + actual_slope:
                                    temp_slope.append(0)
                        
                            print('length of usage', len(usage))
                            print('length of temp slope', len(temp_slope))


                            ## this is to get out the singe times in midst of burning event

                            neg_slope = 0
                            for t,s in enumerate(temp_slope):
                                if s <= 1:
                                    #print('temp at t', temp[t])
                                    if temp[t] < 127:# and temp[t] > cooking_threshold:
                                        neg_slope = neg_slope +1

                                    else:
                                        neg_slope = 0
                                else:
                                    neg_slope = 0
                                if neg_slope > length_decrease:   
                                    usage[t - length_decrease: t+1] = 0


                            for t,s in enumerate(temp_slope):
                                if s <= end_threshold and temp[t] != 127:
                                    usage[t] = 0
                                elif s > start_threshold:
                                    usage[t] = 1
                
                        
                            ce_time = 0
                            time_since_no_cooking = 0
                            iscooking = False

                            for v,f in enumerate(usage):
                                if f == 0:
                                    time_since_no_cooking = time_since_no_cooking + 1
                                    iscooking = False
                                elif f == 1:
                                    if (iscooking == False) and (time_since_no_cooking < merge_ce_threshold) and (ce_time > 0):
                                        tsnc = np.arange(0, time_since_no_cooking+1, 1)
                                        for c,g in enumerate(tsnc):
                                            usage[v-c] = 1
                                    iscooking = True
                                    time_since_no_cooking  = 0
                                    ce_time = ce_time +1


                            ce_time = 0
                            iscooking = False
                            nb_cooking_ev = 0
                            nb_minute_cook = 0
                            nb_minute_inter = 0
                            ff_start = []
                            ff_end = []
                            start_cooking = []
                            for t,c in enumerate(usage):
                                nb_minute_inter = nb_minute_inter + 1
                                if c  == 1:
                                    ce_time = ce_time + 1
                                    iscooking = True
                                    start_cooking.append(t)
                                elif c == 0:
                                    if (iscooking == True) and (ce_time < min_ce_length):
                                        ce_tme_span = np.arange(0,ce_time,1)
                                        for i, te in enumerate(ce_tme_span):
                                            usage[t-i-1] = 0
                                        start_cooking = []

                                    elif (iscooking == True) and ce_time > min_ce_length:
                                        nb_cooking_ev = nb_cooking_ev +1
                                        nb_minute_cook = nb_minute_cook + ce_time
                                        nb_minute_inter = 0
                                        split_dif_sum = sum([a for a in usage[start_cooking[0]:t]])
                                        split_diff = t - start_cooking[0]
                                        if (split_dif_sum/split_diff) > 0.75:
                                            ff_start.append(start_cooking[0])
                                            ff_end.append(t)

                                        start_cooking = []
                                    iscooking = False
                                    ce_time = 0
                            cooking_time_sumation = np.sum(usage)
                            fire_start = ff_start
                            fire_end = ff_end
                            is_thresh_good.append(len(fire_start))
                            #if statment counting for the second stove and exact sensor

                            print(fire_start)
                            print(fire_end)
                            print('pump pump time',Pump_pumped_time[hh_line], int(Pump_pumped_time[hh_line]))
                            #Temp_counter = np.arange(0, float(Pump_pumped_time[hh_line],1))
                            fire_finder_cooking = []
                            event_count = 0
                            for val in temp:
                                if event_count > len(fire_start)-1: # or event_count > 20:
                                    fire_finder_cooking.append(0)
                                    cut_off = val + 1

                                elif val == fire_start[event_count]:
                                    fire_finder_cooking.append(cooking_threshold)
                                elif val <= fire_end[event_count] and val > fire_start[event_count]:
                                    fire_finder_cooking.append(cooking_threshold)
                                    if val == fire_end[event_count]:
                                        event_count = event_count +1
                                else: 
                                    fire_finder_cooking.append(0)
                            Cooking_duration = []
                            for event,fire in enumerate(fire_start):
                                time = fire_end[event] -fire
                                Cooking_duration.append(time)
                            
                            print('Sumation of cooking duration', sum(Cooking_duration))
                            Pump_cooking_time.append(sum(Cooking_duration))
                            Number_of_pumped_events.append(len(fire_start))
#
Pump_ff_count = {'Household': Household_looked_at, 'Cooking Time for pump': Pump_cooking_time, 'Num of Events': Number_of_pumped_events}
#,'Cooking Time second stove': Cooking_Time_2, 
#    'Num_of_Events for second stove': Num_of_Events_2}
#
DF_pump_fft = pd.DataFrame(Pump_ff_count, columns=['Household','Cooking Time for pump','Num of Events'])
path = USB+":/24_hour_pump/"+Phase+"/Pump_"+Phase+"_Firefinder_pump_times_exact_"+Exact+"_#events.csv"
DF_pump_fft.to_csv(path, index=False, mode= 'a')

        