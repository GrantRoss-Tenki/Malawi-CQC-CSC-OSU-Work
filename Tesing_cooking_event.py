import itertools
import os
import pandas as pd
import numpy as np
import csv
from decimal import *
from itertools import chain
import statistics as stat
import datetime
from datetime import datetime
from itertools import islice, cycle
from io import StringIO
import matplotlib.pyplot as plt

Phase = "1N"
print('Phase Number', Phase)

datafile_path ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/1N/Collection/Clean_HH_1001_2021-10-01_12-36-06.csv"
#datafile_path ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/3H/Collection/Clean_HH_2002_2021-11-29_10-17-02.csv"

Second_Exact = 0

with open(datafile_path, 'r') as f:
    csv_reader = csv.reader(f)
    for idx, row in enumerate(csv_reader):
        if 'Household ID:' in row:
            id_number = (row[1])
        elif 'Timestamp' in row:
            Fueltype = row[1]
            Exact = row[3]
            Usage = row[2]
            K_hapex = row[5]
            C_hapex = row[7]
            data_start = idx

            if len(row) < 9:
                print('There is no second exact')
                break
            elif row[8] == 'Second EXACT Usage':
                Exact_2 = row[9]
                Usage_2 = row[8]
                Second_Exact = 1
                print('--------------Two EXACT-------------')
            break

# this is so far from heather and her "Data Processing Instructions" Using fire Finder algorithm

sensor_data = pd.read_csv(datafile_path, skiprows=data_start)
print('Type of fuel used:  ',Fueltype)
print('Type of exact used:  ',Exact)
print('Type of Kitchen Hapex:  ',(K_hapex))
print('Type of Cook Hapex:  ',(C_hapex))
print('The household ID number is:  ',  (id_number))
print('this is the exact row ', Exact)
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


count = 1
Two_exact = [1]
if No_exact == 0:
    if Second_Exact == 1:
        Two_exact.append(2)

    for q in Two_exact:
        print('this is q =', q)
        if q == 1:
            Usage = sensor_data.iloc[:,2]
            temp = sensor_data.iloc[:,3]
            Testing_end_thresh = np.arange(0, 1, 1)
            Is_thresh_good = []
        elif q == 2:
            Usage = sensor_data.iloc[:,8]
            temp = sensor_data.iloc[:,9]
            Testing_end_thresh = np.arange(0, 1, 1)
            Is_thresh_good = []

        for tet in Testing_end_thresh:
            cooking_threshold = 7
            length_decrease = 20
            start_threshold = 7
            end_threshold = -1
            merge_CE_threshold = 10
            min_CE_length = 5
            window_slope = 5

            n = len(Usage)
            Temp_slope = []

            count = 1
            for t, us in enumerate(Usage):
                if count == len(temp):
                    Temp_slope.append(0)
                    break
                else:
                    slope = count - us
                long_slope = temp[slope + us] - temp[t]
                Temp_slope.append((long_slope/slope))
                count = count + 1

            ## this is to get out the singe times in midst of burning event

            neg_slope = 0
            for t,s in enumerate(Temp_slope):
                if s <= 0:
                    if temp[t] < 127:
                        neg_slope = neg_slope +1

                    neg_slope = 0


                elif neg_slope > length_decrease:
                    Usage[t - length_decrease] = 0
            print('negative slope', neg_slope)
            print('this is temp slope', Temp_slope[220])

            for t,s in enumerate(Temp_slope):
                if s <= end_threshold and temp[t] <= cooking_threshold:
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
                    if (ISCOOKING == False) and (time_since_no_cooking < merge_CE_threshold) and (CE_time>1):
                        #print('is time no cooking working', time_since_no_cooking)
                        tsnc = np.arange(1, time_since_no_cooking+1, 1)
                        for c,g in enumerate(tsnc):
                            Usage[v-g] = 1
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
                        for te in ce_tme_span:
                            Usage[t-te] = 0
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
            #
            # print('FireFinder start', ff_start)
            # print('Firefinder end' , ff_end)
            # remove_f_start = []
            # remove_f_end = []
            # for num, burn in enumerate(ff_start):
            #     if num == len(ff_start):
            #         break
            #     elif abs(burn - ff_end[num-1]) <= 5:
            #         #remove_f_start.append(burn)
            #         #remove_f_start.append(ff_end[num-1])
            #         count = 0
            #         while abs(ff_start[num + count] - ff_end[num+count-1]) <= 5:
            #             remove_f_start.append(ff_start[num + count])
            #             remove_f_end.append(ff_end[num+count-1])
            #             count = count +1

            # remove_f_start = list(set(remove_f_start))
            # remove_f_end = list(set(remove_f_end))
            # for start in remove_f_start:
            #     ff_start.remove(start)
            #
            # for end in remove_f_end:
            #     ff_end.remove(end)

            Fire_start = ff_start
            Fire_end = ff_end
            Is_thresh_good.append(len(Fire_start))
            #if statment counting for the second stove and exact sensor
            if Second_Exact == 1 and q == 2:
                Fire_start_2 = Fire_start
                Fire_end_2 = Fire_end
                print('two Exact, fire start_2', Fire_start_2)
                print('two Exact, fire end_2', Fire_end_2)
                break
            elif Second_Exact == 0 or q == 1:
                Fire_start_1 = Fire_start
                Fire_end_1 = Fire_end
            else:
                count = count + 1

    print('Fire start',Fire_start_1)
    print('Fire end', Fire_end_1)

# plt.plot(Testing_end_thresh, Is_thresh_good)
# plt.xscale('linear')
# plt.yscale('linear')
# xlab = 'Variations'
# ylab = 'Number of Events'
#
# plt.xlabel(xlab)
# plt.ylabel(ylab)
# plt.show()




#Start of my own filtering techniques to further find cooking event
#fire finder did not work in final determination
# F_start = []
# F_end = []
# for t,fil in enumerate(Usage):
#     if t +1 == len(Usage):
#         break
#     elif t == 0 and fil == 1:
#         pass
# #filtering out start and end to the fire looking at one before and one after from the usage
#     elif fil == 1 and (Usage[t-1] == 0) and (Usage[t+1] == 1):
#         if (Usage[t-1] != 1) and (Usage[t+1] != 0):
#             F_start.append(t)
#     elif fil == 1 and (Usage[t-1] == 1) and (Usage[t+1] == 0):
#         if (Usage[t-1] != 0) and (Usage[t+1] != 1):
#             F_end.append(t)
#
# to_five = np.arange(1,6,1)
# filter_start = []
# for z in F_start:
#     memory_l = []
#     memory_h = []
#     for five in to_five:
#         memory_h.append(Usage[z+five])
#         memory_l.append(Usage[z - five])
# #looking at five minute difference between events
#     if sum(memory_h) == len(to_five):
# #memory L is for values for before fire start. Sum has to be less than 3 meaning there should not
# # be too many usages before fire is started and temperature is increased
#
#         if sum(memory_l) <= 3:
#             filter_start.append(z)
# print('Filter Start', filter_start)
# filter_end = []
# for z in F_end:
#     memory_l = []
#     memory_h =[]
#     for five in to_five:
#         memory_l.append(Usage[z-five])
#         memory_h.append(Usage[z+five])
#     if sum(memory_l) == len(to_five):
#         if sum(memory_h) <= 3:
#             filter_end.append(z)
# print('Filter End', filter_end)
# close_times_end = []
# close_times_start = []
#
# for val,n in enumerate(filter_start):
#     if val == len(filter_start):
#         break
#     elif (filter_end[val] - n) < 6:
#         filter_end.remove(filter_end[val])
#         filter_start.remove(n)
#
#
# if len(filter_start) != len(filter_end):
#     print("This program is trying another way")
# #can maybe try an while loop to fix my algorithm
# Fire_start = filter_start
# Fire_end = filter_end

### next going to solve for the fuel change, this method was delivered by Heather Miller and her thesis
print('Fuel removal Algorithm')
if No_fuel == 0:
    Fuel_KG_nf = sensor_data.iloc[:,1]

    n  = 0
    Fuel_KG = []
    Thres_fuel = 0.14
    insert = []
    remove = []
    previous = 0
    for kg in Fuel_KG_nf:
        n = n + 1
        if n+1 == (len(Fuel_KG_nf)):
            Fuel_KG.append(Fuel_KG_nf.iloc[(n)])
            break
        elif (Fuel_KG_nf.iloc[(n)] - Fuel_KG_nf.iloc[(n+1)]) > Thres_fuel:
            Fuel_KG.append(Fuel_KG_nf.iloc[n])
            insert.append(n)
        elif (Fuel_KG_nf.iloc[(n+1)] - Fuel_KG_nf.iloc[(n)]) > Thres_fuel:
            Fuel_KG.append(Fuel_KG_nf.iloc[n])
            remove.append(n)
        elif previous < Fuel_KG_nf.iloc[n] and Fuel_KG_nf.iloc[(n)] > Fuel_KG_nf.iloc[(n+1)]:
            Fuel_KG.append(previous)
        elif previous < Fuel_KG_nf.iloc[n] and Fuel_KG_nf.iloc[(n)] > Fuel_KG_nf.iloc[(n+1)] and previous < Fuel_KG_nf.iloc[(n+1)]:
            Fuel_KG.append(Fuel_KG_nf.iloc[(n+1)])
        else:
            Fuel_KG.append(Fuel_KG_nf.iloc[(n)])
        previous = Fuel_KG[-1]

    Fuel_KG.insert(0, Fuel_KG_nf.iloc[0])

    remove = []
    remove_kg = []
    insert = []
    insert_kg = []
    v = 0
    for weight in Fuel_KG:
        v = v + 1
        #print(weight)
        if v+1 == (len(Fuel_KG_nf)):
            break
        elif Fuel_KG[v] <= 0 or weight <= 0:
            if (abs(weight - Fuel_KG[v]) > Thres_fuel) or (abs(weight + Fuel_KG[v]) > Thres_fuel):
                if weight - Fuel_KG[v] > Thres_fuel:
                    remove.append(v)
                    kg_amount = weight - Fuel_KG[v]
                    remove_kg.append((int(kg_amount*1000))/1000)
                elif (weight + Fuel_KG[v] > Thres_fuel):
                    insert.append(v)
                    kg_amount = weight + Fuel_KG[v]
                    insert_kg.append((int(kg_amount*1000))/1000)
            else:
                pass
        elif (weight - Fuel_KG[v]) > Thres_fuel:
            remove.append(v)
            remove_kg.append((int((abs(Fuel_KG[v] - weight))*1000)/1000))

        elif (Fuel_KG[v] - weight) > Thres_fuel:
            insert.append(v)
            insert_kg.append(Fuel_KG[v] - weight)
    v = 0

    print('Removing the fuel at this timestamp value' , remove)
    print('Removing the fuel for this many kgs at remove timevalue' , remove_kg)
    print('inserting the fuel at this timestamp value' , insert)

    kg = np.arange(0, len(Fuel_KG_nf),1)
    count = 0
    KG_burned = []
    for wei in kg:
        if (wei) == (len(Fuel_KG_nf)-1):
            KG_burned.append(KG_burned[-1])
            break
        elif remove[-1] == len(KG_burned)-2:
            KG_burned.append(KG_burned[-1])
            pass
        elif wei == remove[count]:
            KG_burned.append(remove_kg[count])
            if remove[-1] == wei:
                end_bit = np.arange(wei, len(Fuel_KG_nf),1)
                for a in end_bit:
                    KG_burned.append(KG_burned[-1])
                break
            count = count + 1
        elif wei == 0 and remove_kg[wei] != 0:
            KG_burned.append(0)
        else:
            KG_burned.append(KG_burned[-1])
    #print('at each timevalue of kgs burned', KG_burned)
    ## below is counting down the minutes between each fuel removal

    time = np.arange(0,len(Fuel_KG_nf),1)
    Fuel_removal_countdown = []
    count = 0
    start = 0
    for t in time:
        if t < remove[0]:
            Fuel_removal_countdown.append(-1)
        elif start + 1 == len(remove)+1:
            g = np.arange (len(Fuel_KG_nf)- len(Fuel_removal_countdown), len(Fuel_KG_nf)-1, 1)
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
    print(len(Fuel_removal_countdown))
    print(len(Fuel_KG_nf))
    Fuel_insert_countdown = []
    count = insert[0]
    start = 0
    for t in time:
        if t < insert[0]:
            Fuel_insert_countdown.append(-1)
        elif start + 1 == len(insert):
            val = np.arange(start,insert[-1],1)
            for v in val:
                Fuel_insert_countdown.append(0)
            break
        elif t == insert[start]:
            start = start + 1
            Fuel_insert_countdown.append(insert[start])
            count = 0
        else:
            Fuel_insert_countdown.append(insert[start]- insert[start-1] - count)
        count = count + 1

print('Timestamp')
# #finaly start to get metrics
# # gathering hapex informaion (was previously filtered through Climate solutions website)
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
        elif q == 2:
            Fire_start = Fire_start_2
            Fire_end = Fire_end_2
    else:
        Fire_start = [-1, -1]
        Fire_end = [-1, -1]
    ## starting with event metrics
    ## Event time
    print('Gathering metrics to be anylized')
    E_Time_Start = []
    E_Time_End = []
    E_Event_length = []
    E_AVG_Temp = []
    E_STD_Temp = []
    ##Event Fuel
    E_Fuel_Used = []
    E_Time_Fuel_Remove = [] #how much time was fuel removed until fire started
    E_Time_Fuel_Insert = [] #how much time was fuel interted from fire end
    ##Event Cook PM
    E_Avg_Cook_PM = []
    E_Med_Cook_PM = []
    E_STD_Cook_PM = []
    E_PC_Cook_Move =[]
    E_Spread_Cook_PM =[] #in order to get the average you need to extend to 5 and RAW
    E_Spread_AVG_Cook_PM = []
    ##Event Kitchen PM
    E_Avg_Kit_PM = []
    E_Med_Kit_PM = []
    E_STD_Kit_PM = []
    E_PC_Kit_PM = []
    E_Spread_Kit_PM = [] #in order to get the average you need to extend to 5 and RAW
    E_Spread_AVG_Kit_PM = []
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
    filler_spread_values = np.full(shape=11,fill_value=-1)

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
            else:
                E_Time_Start.append(event_T[st])
                E_Time_End.append(event_T[Fire_end[tv]])
                E_Event_length.append((Fire_end[tv]-st))
                E_AVG_Temp.append((int((np.average([a for a in temp[st:Fire_end[tv]]]))*10))/10)
                E_STD_Temp.append((int((stat.stdev(temp[st:Fire_end[tv]]))*100))/100)
                Raw_E_Temp.extend([a for a in temp[st:Fire_end[tv]]])
                ##Starting Fuel Useage
            if No_fuel == 0 and No_exact == 0:
                fuel_bounds = list(set(KG_burned[st:Fire_end[tv]]))
                E_Fuel_Used.append((int((sum(fuel_bounds))*1000)/1000))
                E_Time_Fuel_Remove.append(Fuel_removal_countdown[st])
                E_Time_Fuel_Insert.append(Fuel_insert_countdown[Fire_end[tv]])
                #raw metrics
                Raw_E_Fuel.extend([a for a in Fuel_KG_nf[st:Fire_end[tv]]])
                Raw_E_Fuel_removed.extend(KG_burned[st:Fire_end[tv]])

            else:
                E_Fuel_Used.append(-1)
                E_Time_Fuel_Remove.append(-1)
                E_Time_Fuel_Insert.append(-1)
                Raw_E_Fuel.extend(filler_value)
                Raw_E_Fuel_removed.extend(filler_value)
            ### Cook HAPEx
            if No_cook == 0 and No_exact == 0:
                E_Avg_Cook_PM.append((int((np.average([a for a in Cook_PM[st:Fire_end[tv]]]))*100))/100)
                E_Med_Cook_PM.append((int((np.median([a for a in Cook_PM[st:Fire_end[tv]]])) * 100)) / 100)
                E_STD_Cook_PM.append((int((stat.stdev(Cook_PM[st:Fire_end[tv]])) * 100)) / 100)
                E_PC_Cook_Move.append((int(((sum(Cook_comp[st:Fire_end[tv]]))/(Fire_end[tv]-st))*100)))
                E_Cook_S_before = (list([a for a in Cook_PM[(st - 5):st]]))
                E_Cook_S_after = (list([a for a in Cook_PM[st:(st + 6)]]))
                E_cook_spread_combo = E_Cook_S_before + E_Cook_S_after + Cook_PM[st]
                E_Spread_Cook_PM.extend(E_cook_spread_combo)
                E_Spread_AVG_Cook_PM.append(np.average(E_Spread_Cook_PM))
                #raw values for total compare
                Raw_E_Cook_PM.extend([a for a in Cook_PM[st:Fire_end[tv]]])
                Raw_E_Cook_Comp.extend([a for a in Cook_comp[st:Fire_end[tv]]])
                Raw_Spread_Cook = E_Spread_Cook_PM
            else:
                E_Avg_Cook_PM.append(-1)
                E_Med_Cook_PM.append(-1)
                E_STD_Cook_PM.append(-1)
                E_PC_Cook_Move.append(-1)
                E_Spread_AVG_Cook_PM.append(-1)
                Raw_E_Cook_PM.extend(filler_value)
                Raw_E_Cook_Comp.extend(filler_value)
                Raw_Spread_Cook.extend(filler_spread_values)

            # Kitchen HAPEx
            if No_kitchen == 0 and No_exact == 0:
                E_Avg_Kit_PM.append((int((np.average([a for a in Kitcen_PM[st:Fire_end[tv]]]))*100))/100)
                E_Med_Kit_PM.append((int((np.median([a for a in Kitcen_PM[st:Fire_end[tv]]])) * 100)) / 100)
                E_STD_Kit_PM.append((int((stat.stdev(Kitcen_PM[st:Fire_end[tv]])) * 100)) / 100)
                E_PC_Kit_PM.append((int((sum(Kitchen_Comp[st:Fire_end[tv]]))/(len(Kitchen_Comp[st:Fire_end[tv]]))*100)))

                E_Kit_S_before = (list([a for a in Kitcen_PM[(st - 5):st]]))
                E_Kit_S_after = (list([a for a in Kitcen_PM[st:(st + 6)]]))
                E_Kit_spread_combo = E_Kit_S_before + E_Kit_S_after + Kitcen_PM[st]
                E_Spread_Kit_PM.extend(E_Kit_spread_combo)
                E_Spread_AVG_Kit_PM.append(np.average(E_Spread_Kit_PM))
                # raw values for total compare
                Raw_E_Kit_PM.extend([a for a in Kitcen_PM[st:Fire_end[tv]]])
                Raw_E_Kit_Comp.extend([a for a in Kitchen_Comp[st:Fire_end[tv]]])
                Raw_Spread_Kit = E_Spread_Kit_PM
            else:
                E_Avg_Kit_PM.append(-1)
                E_Med_Kit_PM.append(-1)
                E_STD_Kit_PM.append(-1)
                E_PC_Kit_PM.append(-1)
                E_Spread_AVG_Kit_PM.append(-1)
                Raw_E_Kit_PM.extend(filler_value)
                Raw_E_Kit_Comp.extend(filler_value)
                Raw_Spread_Kit.extend(filler_spread_values)





        # else:
        #     print('There is no EXACT DATA, No Event data, Only Day metrics are available')
        #     break

    #if No_exact == 0:
    Event_num = np.arange(1,len(E_Event_length)+1,1)
    print('data frame length test__________', len(E_Avg_Cook_PM))

    Data_event = {'| Event Number |' : Event_num,
                      '| Event Start |' : E_Time_Start,
                       '| Event Stop |' : E_Time_End,
                      '| Removed Fuel Before Start (min) |' : E_Time_Fuel_Remove,
                      '| Inserted Fuel After Stop (min) |' : E_Time_Fuel_Insert,
                       '| Length of Event (min)|': E_Event_length,
                       '| Fuel Used (FUEL) |' : E_Fuel_Used,
                       '| Average Temperature for Event (EXACT) |' : E_AVG_Temp,
                       '| Std of Event Temperature |' : E_AVG_Temp,
                       '| Average PM for Cook in Event (HAPEx) |' : E_Avg_Cook_PM,
                       '| Median PM for Cook in Event (HAPEx) |': E_Med_Cook_PM,
                       '| Std of Cook PM |' : E_STD_Cook_PM,
                      '| 10 minutes spread Cook Exposure|' : E_Spread_AVG_Cook_PM,
                       '| Percentage Cook Compliance for Event (HAPEx) |': E_PC_Cook_Move,
                       '| Average PM in Kitchen for Event (HAPEx) |' : E_Avg_Kit_PM,
                       '| Median PM in Kitchen for Event (HAPEx) |' : E_Med_Kit_PM,
                       '| Std of Kitchen PM |' : E_STD_Kit_PM,
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

    print('raw_spread cook', len(Raw_Spread_Cook))
    print('raw_spread Kitchen', len(Raw_Spread_Kit))
    print('is there no Kitchen Hapex', No_kitchen)
    RAW_Spread_PM = {'10 minutes spread (Cook PM)': Raw_Spread_Cook,'10 minutes spread (Kitchen PM)': Raw_Spread_Kit}

    Df_raw_event = pd.DataFrame(RAW_event)
    Df_first_five = pd.DataFrame(RAW_Spread_PM)
        # Taking some metrics that need to be compared to each other, will be in own CSV file
        # these metrics are to be compared to other households, there are no averages inside here
        # these are repeated, but want to have a separate file to easily gather

    Summary_event = {'Length of Event':E_Event_length,'Fuel Used (FUEL)' : E_Fuel_Used,
                         'Removed Fuel Before Start (min)': E_Time_Fuel_Remove,
                         'Inserted Fuel After Stop (min)' : E_Time_Fuel_Insert,
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
    print(Df_sensor)

    ### iterate over the day

    Day_start = []
    Day_end = []
    Date_day = []
    count = 0
    print(day[-1])
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
    print('Day_start',Day_start[-1])
    print('Day_end',Day_end[-1])
    print('Date_day',Date_day[-1])
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
        else:
            D_Fuel_Used.append(-1)
            Raw_D_Fuel.extend(filler_value)
            Raw_D_Fuel_removed.extend(filler_value)
        #temperature and exact characteristics
        if No_exact == 0:
            DAY_TEMP = [a for a in temp[ds:Day_end[tv]]]
            D_AVG_Temp.append((int((np.average(DAY_TEMP)*10))/10))
            D_STD_Temp.append((int((stat.stdev(DAY_TEMP)) * 100)) / 100)
            Raw_D_Temp.extend(temp[ds:Day_end[tv]])
        else:
            D_AVG_Temp.append(-1)
            D_STD_Temp.append(-1)
            Raw_D_Temp.extend(filler_value)
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

    # raw for day
    RAW_day = {'Fuel Raw Data': Raw_D_Fuel, 'Fuel Removed (kg change)': Raw_D_Fuel_removed,
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

    print('Exporting to csv format...')
    ### making all different CSV files for all metrics (This spit out 6 different files)
    ####first is the Specific summary metrics for Household
    Path_HH_Sum_event = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_"+str(q)+"_exact/HH_summary_Event"
    File_name_HH_sum_Event = str(Path_HH_Sum_event) + "/"+ Phase +"_HH_Summary_Event_"+str(id_number)+"_"+str(q)+"_exact"+".csv"
    Df_sensor.to_csv(File_name_HH_sum_Event)
    df_event.to_csv(File_name_HH_sum_Event,index=False,mode='a')

    Path_HH_Sum_day = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_"+str(q)+"_exact/HH_summary_Day"
    File_name_HH_sum_Day = str(Path_HH_Sum_day) + "/"+ Phase+"_HH_Summary_Day_"+str(id_number)+"_"+str(q)+"_exact"+".csv"
    Df_sensor.to_csv(File_name_HH_sum_Day)
    Df_day.to_csv(File_name_HH_sum_Day,index=False, mode= 'a')

    Path_Raw_Event = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_"+str(q)+"_exact/Raw_Event"
    File_event_Raw_metrics = str(Path_Raw_Event) + "/Raw_E_metrics/"+Phase+"_HH_raw_Event_metrics_"+str(id_number)+"_"+str(q)+"_exact"+".csv"
    Df_sensor.to_csv(File_event_Raw_metrics)
    Df_raw_event.to_csv(File_event_Raw_metrics,index=False,mode='a')

    File_event_Raw_summary = str(Path_Raw_Event) + "/Raw_E_summary/"+Phase+"_HH_raw_Event_summary_"+str(id_number)+"_"+str(q)+"_exact"+".csv"
    Df_sensor.to_csv(File_event_Raw_summary)
    Df_Summary_Event.to_csv(File_event_Raw_summary,index=False,mode='a')

    File_event_Raw_first_five = str(Path_Raw_Event) + "/Raw_E_first_five/"+ Phase+"_HH_Event_first_five_"+str(id_number)+"_"+str(q)+"_exact"+".csv"
    Df_sensor.to_csv(File_event_Raw_first_five)
    Df_first_five.to_csv(File_event_Raw_first_five,index=False,mode='a')

    Path_Raw_Day = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_"+str(q)+"_exact/Raw_Day"
    File_Day_Raw_metrics = str(Path_Raw_Day) + "/Raw_D_metrics/"+Phase+"_HH_raw_Day_metrics_"+str(id_number)+"_"+str(q)+"_exact"+".csv"
    Df_sensor.to_csv(File_Day_Raw_metrics)
    Df_raw_day.to_csv(File_Day_Raw_metrics, index=False,mode='a')

    File_Day_Raw_summary = str(Path_Raw_Day) + "/Raw_D_summary/"+ Phase+ "_HH_raw_Day_summary_"+str(id_number)+"_"+str(q)+"_exact"+".csv"
    Df_sensor.to_csv(File_Day_Raw_summary)
    Df_Summary_day.to_csv(File_Day_Raw_summary, index=False,mode='a')

