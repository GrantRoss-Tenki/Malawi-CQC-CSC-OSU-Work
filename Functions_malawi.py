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
# Fire Finder Algorithm
def FireFinder(temp, Usage, cooking_threshold, length_decrease, start_threshold, end_threshold, merge_CE_threshold, min_CE_length, window_slope):
        n = len(Usage) - 1
        if temp[0] == 'NO EXACT':
            No_exact = 0
        else:
            No_exact = 1
        Temp_slope = []
        #print('minutes sensed-', n)
        count = 1
        for t, us in enumerate(Usage):
            if window_slope < (n+1) - t:
                actual_slope = window_slope
            else:
                actual_slope = (n+1) - t
            if t < window_slope - 1:
                Temp_slope.append(0)
            elif n > t + actual_slope:
                f1 = temp[actual_slope + t] - temp[t]
                Temp_slope.append((f1/actual_slope))
            elif n <= t + actual_slope:
                Temp_slope.append(0)
                        
                ## this is to get out the singe times in midst of burning event

        neg_slope = 0
        for t,s in enumerate(Temp_slope):
            if s <= 1:
                if temp[t] < 127 and temp[t] >= cooking_threshold:
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
       
        return Usage, Fire_start, Fire_end

# Fuel Algorithm 
def FUEL_REMOVAL(Fuel_KG_nf, Thresold, min_average_spread,No_fuel):
        
        if No_fuel != 1:

            count = 0
            n = 0
            Fuel_KG = []

            insert = []
            remove = []

            # this is for running average
            Mean_Count_min = []
            one_to_five = np.arange(0,6,1)
            for one in one_to_five:
                fiveee = abs(Fuel_KG_nf[one])
                Mean_Count_min.append(fiveee)

            count = 0
            not_first_value = 0
            inside_spread = [0]
            for kg in (Fuel_KG_nf):
                if count == min_average_spread:
                    median = stat.median(inside_spread)
                    Mean_Count_min.append(median)
                    inside_spread = []
                    count = -1
                elif not_first_value == 0:
                    Mean_Count_min.append(Mean_Count_min[-1])
                    inside_spread.append(abs(kg))
                    not_first_value = 1
                else:
                    Mean_Count_min.append(Mean_Count_min[-1])
                    inside_spread.append(abs(kg))

                count = count + 1
            
            Mean_Count_min.remove(Mean_Count_min[0])
            
            # two in one algorithm taking in the threshold and running average 
            KG_burned = [0]
            insert = []
            for vv, kg in enumerate(Fuel_KG_nf):
                if ((vv % 2) == 0) or (vv == 0):
                    KG_burned.append(KG_burned[-1])
                    if vv + 3 == len(Fuel_KG_nf):
                        KG_burned.append(KG_burned[-1])
                        KG_burned.append(KG_burned[-1])
                        KG_burned.remove(KG_burned[0])  
                        break
                    if (vv == 0):
                        previous = Fuel_KG_nf.iloc[(0)]
                        delta_up = 0
                        delta_down = 0
                    else:
                        previous = Fuel_KG_nf.iloc[vv -1]
                        delta_up =  abs(Fuel_KG_nf.iloc[vv +2] -kg)
                        delta_down = abs(kg - Fuel_KG_nf.iloc[vv +2])
                    pass
                elif vv + 3 == len(Fuel_KG_nf):
                        KG_burned.append(KG_burned[-1])
                        KG_burned.append(KG_burned[-1])
                        
                        break
                elif  delta_up > Thresold and Fuel_KG_nf[vv +3] > Mean_Count_min[vv]:
                    if previous < kg:
                        insert.append(vv)
                        KG_burned.append(KG_burned[-1])
                    else:
                        KG_burned.append(KG_burned[-1])
                elif delta_down > Thresold and Fuel_KG_nf.loc[vv +3] < Mean_Count_min[vv]:
                    if (kg  < previous) or (kg < Mean_Count_min[vv]) or (Fuel_KG_nf.loc[vv +1] < previous):
                        
                        KG_burned.append(delta_down)
                    else:
                        KG_burned.append(KG_burned[-1])
                else:
                    KG_burned.append(KG_burned[-1])
        else:
            KG_burned =-1
            Mean_Count_min = -1

        return KG_burned, Mean_Count_min
#removal algorithm

def FuelRemovalTime(KG_burned, No_fuel):
        if No_fuel != 1:
            time = np.arange(0,len(KG_burned),1)
            remove = []
            count_rr = 1
            for rr in KG_burned:
                if count_rr +1 == len(time):
                    remove.append(remove[-1])
                    break
                elif rr != KG_burned[count_rr]:
                    remove.append(count_rr -1)
                    count_rr = count_rr +1
                else:
                    count_rr = count_rr +1
            Fuel_removal_countdown = []
            count = 0
            start = 0
            for t in time:
                if t < remove[0]:
                    Fuel_removal_countdown.append(-1)
                elif start + 1 == len(remove)+1:
                    g = np.arange (len(KG_burned)- len(Fuel_removal_countdown), len(KG_burned)-1, 1)
                    for h in g:
                        Fuel_removal_countdown.append(h)
                        break
                elif t == remove[start]:
                    Fuel_removal_countdown.append(0)
                    start = start +1
                    count = 0
                else:
                    Fuel_removal_countdown.append(count)
                count = count + 1
        else:
            Fuel_removal_countdown = -1
        return Fuel_removal_countdown
    
    
def Olivier_Fuel_Algo(Fuel_KG_nf, Thresold, min_average_spread,No_fuel):
        if No_fuel != 1:
            Mean_Count_min = []
            one_to_five = np.arange(0,6,1)
            for one in one_to_five:
                fiveee = abs(Fuel_KG_nf[one])
                Mean_Count_min.append(fiveee)

            count = 0
            not_first_value = 0
            inside_spread = [0]
            for kg in (Fuel_KG_nf):
                if count == min_average_spread:
                    median = stat.median(inside_spread)
                    Mean_Count_min.append(median)
                    inside_spread = []
                    count = -1
                elif not_first_value == 0:
                    Mean_Count_min.append(Mean_Count_min[-1])
                    inside_spread.append(abs(kg))
                    not_first_value = 1
                else:
                    Mean_Count_min.append(Mean_Count_min[-1])
                    inside_spread.append(abs(kg))

                count = count + 1
            
            Mean_Count_min.remove(Mean_Count_min[0])
            
            Olivier_filter = []
            for tv, change in enumerate(Mean_Count_min):
                if len(Mean_Count_min) == tv +1:
                    Olivier_filter.append(Olivier_filter[-1])
                    break
                elif change != Mean_Count_min[tv+1]:
                    if abs(change - Mean_Count_min[tv+1]) > Thresold:
                        fuel_change = change - Mean_Count_min[tv+1]
                        Olivier_filter.append(fuel_change)
                else:
                    Olivier_filter.append(0)
        else:
            Olivier_filter = -1
            
        return Olivier_filter


def flatten_list(_2d_list):
    s = [str(i) for i in _2d_list]

    flat_list = int(''.join(s))

    return flat_list

def Local_Max_min(arrayyyy, start, Start_Spread):
    # the array needs be a whole spread meaning the startup (10 min before ) Fire finder and cool down (30 after) 
    # *** the array is not just firefinder*****
    array = (arrayyyy)
    gradienttt = list(np.gradient(array))
    Mini_value = min(gradienttt)
    Max_value = max(gradienttt)
    Time_Vaue_min = (np.where(gradienttt == Mini_value))
    Time_Vaue_max = (np.where(gradienttt == Max_value))

    local_min_count = []
    local_maxima_count = []
    # the for loop is for determining the number of local minmums and maximums 
    # local max and mins are determined by the gradient
    for tv, a in enumerate(gradienttt):
        if gradienttt[tv-1] < 0 and a > 0:

            local_min_count.append(tv + (start -Start_Spread))
        elif gradienttt[tv-1] > 0 and a < 0:
            local_maxima_count.append(tv + (start -Start_Spread))

    return (Time_Vaue_min[0]+(start-Start_Spread)), (Time_Vaue_max[0]+(start -Start_Spread)), local_min_count, local_maxima_count


def StartUp_max_Next_min(Hapex,start, start_spread):
    # only for Hapex needs be a whole spread meaning the startup (10 min before ) Fire finder and cool down (30 after)
    # *** the array is not just firefinder*****
    # NOTE---- this function has the same input as the "Local_Max_min" with differnt names
    Hap = list(np.gradient(Hapex))
    StartUp_max = max(Hap[0:(2*start_spread)])
    StartUp_max_TV = (np.where(Hap == StartUp_max))
    #print('---------=--=-=-=---==-------',StartUp_max_TV)
    found_min = 0
    for tt, grad in enumerate(Hap):
        if tt == StartUp_max_TV[0]:
            
            for s_tv, s_grad in enumerate(Hap[tt:]):
                next_tt = tt + s_tv
                if Hap[next_tt -1] < 0 and s_grad > 0:
                    Next_min_TV = tt + s_tv
                    found_min = 1
                    break

        if found_min == 0:
            Next_min_TV = -1000
    
    return (StartUp_max_TV[0] +(start - start_spread)), (Next_min_TV + (start -start_spread))




def SteadyState_Finder(Combined_event_Hapex, window, Local_min_array,startup, Loca_Max_array, start):

    max_array_scale = []
    for g in Loca_Max_array:
        max_array_scale.append(g- (start-10))
    min_array_scale = [] 
    for h in Local_min_array:
        min_array_scale.append(h-(start - 10))

    Max_reverse = list(reversed(Loca_Max_array))
    Min_reverse = list(reversed(Local_min_array))
    Minn_reverse_first = min_array_scale[-1]
    Maxx_reverse_first = max_array_scale[-1]
    Min_reverse_count = 0
    stop = [0]

    Gradient_Hapex = (np.gradient(Combined_event_Hapex))
 
    max_grad = max(list(Gradient_Hapex))
    max_grad_where = np.where(Gradient_Hapex == max_grad)
    max_PM = np.where(Combined_event_Hapex == max(Combined_event_Hapex))
    
    Medain_of_Max_Hapex = np.median(Combined_event_Hapex[int(max_grad_where[0]):])

    #print(startup,'max hapex',max_PM[0],max_grad_where, Combined_event_Hapex[0],'median',Medain_of_Max_Hapex, startup)
    #print('from function, type of min and max', type(Minn_reverse_first),  type(Maxx_reverse_first), Minn_reverse_first>Maxx_reverse_first)

    if Minn_reverse_first > Maxx_reverse_first:
        where_grad = Gradient_Hapex[Maxx_reverse_first:Minn_reverse_first]
    elif Minn_reverse_first < Maxx_reverse_first:
        where_grad = Gradient_Hapex[Minn_reverse_first:Maxx_reverse_first]

    print('from function, this is the array i am looking at' ,Minn_reverse_first>Maxx_reverse_first,where_grad)
    where = min(where_grad)
    for tv_1, hapex_vauue in enumerate(where_grad):
        if hapex_vauue == where: 
            where_is_the_MinSlope = tv_1 + Max_reverse[0]
        else:
            where_is_the_MinSlope = Min_reverse[0]
    how_many_steady_state = []
    min_reverse_array_count = []
    max_reverse_array_count = []
    for tv_rev, rev_hapex in enumerate(reversed(Combined_event_Hapex)):
        if (len(Combined_event_Hapex) - tv_rev) < max_grad_where[0]:
            break

        elif (len(Combined_event_Hapex)-1- tv_rev) == Min_reverse[Min_reverse_count]:
            for tv_max, rev_max in enumerate(Max_reverse):
                if  (Min_reverse[Min_reverse_count] - window) <= rev_max <= (Min_reverse[Min_reverse_count] + window):
                    #print('is this the good max', Combined_event_Hapex[rev_max], rev_max, Combined_event_Hapex[Min_reverse[Min_reverse_count-1]], Min_reverse[Min_reverse_count-1])
                    if rev_max > Min_reverse[Min_reverse_count] and Min_reverse_count > len(Min_reverse):
                        Final_last_slope = [t for t in Gradient_Hapex[Min_reverse[Min_reverse_count]:]]
                        min_last_slope = min(Final_last_slope)
                        where_last_slope = np.where(Final_last_slope == min_last_slope)
                        where_is_the_MinSlope = rev_max + where_last_slope[0]
                        stop = where_is_the_MinSlope

                    elif Combined_event_Hapex[rev_max] > Medain_of_Max_Hapex and Combined_event_Hapex[Min_reverse[Min_reverse_count]] < Medain_of_Max_Hapex:
                        if rev_max < Min_reverse[Min_reverse_count]:
                            two = Min_reverse[Min_reverse_count]
                            one = rev_max
                            
                        else:
                            continue
                        print('------------- it made it here-------------', (len(Combined_event_Hapex) - tv_rev), one, two)
                        Steady_window_gradient = np.array([a for a in Gradient_Hapex[one:two]])
                        #mini_window_gradient_array = [(min(Steady_window_gradient))]
                        mini_window_gradient_array, idx = min([(abs(val), idx) for (idx, val) in enumerate(Steady_window_gradient)])
                        #print('------------- it made it here-------values----', idx, Combined_event_Hapex[one], Combined_event_Hapex[two])
                       
                        for tv_steady, steady_grad in enumerate(Steady_window_gradient):
                            if idx == tv_steady and rev_max > max_grad_where[0] and stop != tv_steady + rev_max:
                                
                                where_is_the_MinSlope = tv_steady + rev_max
                                how_many_steady_state.append(where_is_the_MinSlope)
                                min_reverse_array_count.append(Combined_event_Hapex[two])
                                max_reverse_array_count.append(Combined_event_Hapex[one])
                                clossest_min_median = np.where((min_reverse_array_count) == min((min_reverse_array_count)))
                                clossest_max_median = np.where((max_reverse_array_count) == max((max_reverse_array_count)))
                                stop = how_many_steady_state[-1]
                                #break
                else:
                    continue
                
            Min_reverse_count = Min_reverse_count +1
            
    
    #print('here are the steady states', how_many_steady_state,min_reverse_array_count,max_reverse_array_count,clossest_min_median[0], clossest_max_median[0])
    last_filter = []
    if len(how_many_steady_state) > 1:
        for nec in how_many_steady_state:
            filtering = 0
            for hapex_pm in Combined_event_Hapex[nec:]:
                if hapex_pm > Medain_of_Max_Hapex:
                    #where_is_the_MinSlope = 
                    filtering = 1
                    break
            if filtering == 0:
                last_filter.append(nec)
        print('last_filter ',list(set(last_filter)),how_many_steady_state  )
        if len(last_filter) > 1:
            where_is_the_MinSlope = min((set(last_filter)))
        else:
            where_is_the_MinSlope = Min_reverse[0]
            print('it di not work-----:()')

    return (where_is_the_MinSlope)

def Squish_usage(Phase, Houseold, First_usage, Second_usage, min_CE_length):
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
    
    for hh in exact_2_hh:
        if int(Houseold) == int(hh):
            Second_exact = 0
            break
        else:
            Second_exact = 1

    if Second_exact != 1:
        if len(First_usage) > len(Second_usage):
           Greatest_stove = First_usage
           least_stove = Second_usage
        else:
           Greatest_stove = First_usage
           least_stove = Second_usage

        Collection_length = np.arange(0, len(Greatest_stove)-1, 1)
        Squish_array = []
        Two_stove_once =[]
        print('length of least and collection legnth', len(least_stove), len(Collection_length))
        for tv in Collection_length:
            if tv == len(least_stove):
                Squish_array.append(Greatest_stove[tv:])
                break
            elif (Greatest_stove[tv] == 1) or (least_stove[tv] == 1):
                Squish_array.append(1)
                if (Greatest_stove[tv] == 1) and (least_stove[tv] == 1):
                    Two_stove_once.append(1)
            else:
                Squish_array.append(0)
    elif Second_exact == 1:
        if First_usage[2] == -1:
            Squish_array = -1
            Two_stove_once = [-1, -1]
        else:
            Squish_array = First_usage
            Two_stove_once = [-1, -1]
    event = 0 
    for tvv, one in enumerate(Squish_array):
        if tvv +1 == len(Squish_array):
            break
        elif one == 0 and Squish_array[tvv +1] == 1:
            if Squish_array[tvv + min_CE_length-1] == 1:
                event = event +1
        elif tvv == 0 and Squish_array[tvv + min_CE_length - 1] == 1:
            event = event +1
        
    return Squish_array, event, Two_stove_once

def Running_Average(array, Running_Average_length):
    Array_filter = [array[0]]
    Array_length = len(array)
    running_average_co = []
    count_four = 0
    for tv, place in enumerate(array):
        count_four = count_four + 1
        running_average_co.append(place)
        if count_four == Running_Average_length:
            Array_filter.append(np.average(running_average_co))
            count_four = 0
            running_average_co = []
        elif tv + 1 == Array_length:
            break
        else:
            Array_filter.append(Array_filter[-1])

    return Array_filter

def Remove_Repeated_Values(array):
    Removed_excess = []
    Removes_at_time = []
    for RV, Value in enumerate(array):
        if RV + 1 == len(array):
            break
        elif array[RV+1] != Value and Value != 0:
            Removed_excess.append(Value)
            Removes_at_time.append(RV)
    return Removed_excess, Removes_at_time