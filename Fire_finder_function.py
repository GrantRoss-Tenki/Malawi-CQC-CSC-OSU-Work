import itertools
import os
#from typing_extensions import clear_overloads
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

def FireFinder(temp, Usage, False_or_true,cooking_threshold, length_decrease, start_threshold, end_threshold, merge_CE_threshold, min_CE_length, window_slope):
        # Temp = temperature array that you want to read
        # Usage = array next to the temeprature array. From the raw file, this is only determined by a threshold
        # False or true = True is the file is not corrupted, false is corrupted
        # Cooking threshold (1)= Temperature wof stead fire, depends on the stove, for open fire was set to 7C
        # Length decrease min(10)= looks at the negative slope for temperature and is set for a maximum
        # start_threshold (1)= startign of an event and the gradient
        # end_threshold (5)= Temperature at end when stoped cooking (take into account embers at the end)
        # merge_CE_threshold (30)= how close are two cooking events
        # min_CE_length (8)= Minimum cooking event length
        # window_slope (12)= running avverage fro the window and slope that is gathered

        n = len(Usage) - 1
        if False_or_true == False:
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
        # Retuns a 1 or 0 for cooking on or off. 
        # Fire start is array indexes for when a fire is started
        # Fire end is the array indexes for when a fire ended
        # these array indexes are compared to all other sensors, since they are all started and eneded at the same time
        
        return Usage, Fire_start, Fire_end