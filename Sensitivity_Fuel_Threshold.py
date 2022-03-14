import itertools
import os
from types import prepare_class
import pandas as pd
import numpy as np
import csv
import glob
from decimal import *
from itertools import chain
#import statistics as stat
import datetime
from datetime import datetime
from itertools import islice, cycle
from io import StringIO
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

Phase = "1N"
Computer = "Personal"

if Computer == "work":
    USB = "D"
    os.chdir("D:/Sensitivity Fuel Threshold/"+Phase)
else:
    USB = "E"
    os.chdir("E:/Sensitivity Fuel Threshold/"+Phase)

if  Phase  == ("2N") or Phase == "3N" or Phase == "1N" or Phase == "4N":
    HH_1_fuel_sense = []
    HH_2_fuel_sense = []
    HH_3_fuel_sense = []
    HH_4_fuel_sense = []
    HH_5_fuel_sense = []
    HH_6_fuel_sense = []
    HH_7_fuel_sense = []

else:
    HH_11_fuel_sense = []
    HH_22_fuel_sense = []
    HH_33_fuel_sense = []

Day_met_path = os.getcwd()
csv_R_m = glob.glob(os.path.join(Day_met_path, "*.csv"))
#Thresh_step = np.arange(0,0.22, 0.005)
houshold_count = 1
for file in csv_R_m:
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        for idx, row in enumerate(csv_reader):
            if 'Household Number' in row:
                id_number = (row[1])
                print('------- ID Number------', id_number)
                print('houshold_count      ------',houshold_count)
                #print('thressh', Thresh_step)
            elif  'Fuel Raw Data':
               Start_data = idx
               #print('row where everything starts', Start_data)
               break

    sensor_data = pd.read_csv(file, skiprows=Start_data)

    Thresh_step = np.arange(0,0.22, 0.005)
    #Thresh_step = 0,0.02 
    Fuel_KG_nf = sensor_data.iloc[:,0]
    #print('length of Fuel_KG_nf',Fuel_KG_nf)
    Fuel_consumed = []
    for thres_fuel in Thresh_step:
        n  = 0
        fuel_kg = []
        insert = []
        remove = []
        for v, kg in enumerate(Fuel_KG_nf):
            
            if v+1 == len(Fuel_KG_nf):
                fuel_kg.append(fuel_kg[-1])
                break
            else:
                change = Fuel_KG_nf.iloc[v+1] - (kg)
                next_weight = Fuel_KG_nf[v+1]
                
                if v == 0:
                    previous = Fuel_KG_nf.iloc[0]
                    up_thresh = previous + thres_fuel
                    low_thresh = previous - thres_fuel
                else:
                    previous = fuel_kg[-1]
                    up_thresh = previous + thres_fuel
                    low_thresh = previous - thres_fuel

            if abs(change) < thres_fuel:
                fuel_kg.append(previous)
                
            elif abs(change) > thres_fuel:
                
                if (next_weight <= previous) or (low_thresh <= next_weight <= up_thresh):
                    fuel_kg.append(next_weight)
                elif (next_weight<kg) and (previous< next_weight):
                    fuel_kg.append(next_weight)
                else:
                    fuel_kg.append(next_weight)
            else:
                if (next_weight > previous) or (low_thresh <= next_weight <= up_thresh):
                    fuel_kg.append(previous)
                elif (next_weight>kg) and (previous>next_weight):
                    fuel_kg.append(next_weight)
                else:
                    fuel_kg.append(kg)
        #previous = Fuel_KG_nf.iloc[(0)]
        #for kg in Fuel_KG_nf:
        #    n = n + 1
        #    if n+2 == (len(Fuel_KG_nf)):
        #        fuel_kg.append(Fuel_KG_nf.iloc[(n)])
        #        fuel_kg.append(Fuel_KG_nf.iloc[(n+1)])
        #        break

        #    elif (previous < Fuel_KG_nf.iloc[n+2]) and  (Fuel_KG_nf.iloc[(n+2)] < Fuel_KG_nf.iloc[(n)]):
        #        fuel_kg.append(Fuel_KG_nf.iloc[n+2])

        #    elif Fuel_KG_nf.iloc[n+2] >= previous:
        #         fuel_kg.append(previous)

        #    elif (previous > Fuel_KG_nf.iloc[n+2]) and (Fuel_KG_nf.iloc[(n)] < Fuel_KG_nf.iloc[(n+2)]):
        #        fuel_kg.append(Fuel_KG_nf.iloc[n+2])

        #    else:
        #        fuel_kg.append(Fuel_KG_nf.iloc[(n)])

        #    previous = fuel_kg[-1]
        fuel_kg.insert(0, Fuel_KG_nf.iloc[0])
        #count = count + 1
        #fuel_kg.insert(0, Fuel_KG_nf.iloc[0])

        remove = []
        remove_kg = []
        insert = []
        insert_kg = []
        v = 0
        for tv, weight in enumerate(fuel_kg):
            if tv + 1 == len(fuel_kg):
                break 
            elif weight > fuel_kg[tv+1]:
                remove.append(tv+1)
                remove_kg.append((int((abs(fuel_kg[tv +1 ] - weight))*1000)/1000))
            elif fuel_kg[tv +1] > weight:
                insert.append(tv)
                insert_kg.append(fuel_kg[tv+1] - weight)
        v = 0


        kg = np.arange(0, len(Fuel_KG_nf),1)
        count = 0
        kg_burned = []
        for wei in kg:
            if (wei) == (len(Fuel_KG_nf)-1):
                kg_burned.append(kg_burned[-1])
                break
            elif remove[-1] == len(kg_burned)-2:
                kg_burned.append(kg_burned[-1])
                pass
            elif wei == remove[count]:
                kg_burned.append(remove_kg[count])
                if remove[-1] == wei:
                    end_bit = np.arange(wei, len(Fuel_KG_nf),1)
                    for a in end_bit:
                        kg_burned.append(kg_burned[-1])
                    break
                count = count + 1
            elif wei == 0 and remove_kg[wei] != 0:
                kg_burned.append(0)
            else:
                kg_burned.append(kg_burned[-1])
#seting the kg burned out of array time values to sum and set
        set_kg_burned = []
        for fiber, wood in enumerate(kg_burned):
            if len(kg_burned) == fiber +1:
                if wood != set_kg_burned[-1]:
                    set_kg_burned.append(wood)
                break
            elif kg_burned[fiber+1] != wood:
                set_kg_burned.append(wood)
            #    count = count + 1
        #print('here is the fuel used', sum(set_kg_burned))
        Fuel_consumed.append((int(sum(set_kg_burned)*100))/100)

        if  Phase  == ("1N") or Phase  == ("2N") or Phase == "3N" or Phase == "4N":
            if houshold_count == 1:
                HH_1_fuel_sense.append((int(sum(set_kg_burned)*100))/100)
                HH_1 = id_number
                min_1 = kg
                HH_1_raw = Fuel_KG_nf
                HH_1_filter = fuel_kg
            elif houshold_count == 2:
                HH_2_fuel_sense.append((int(sum(set_kg_burned)*100))/100)
                HH_2 = id_number
                min_2 = kg
                HH_2_raw = Fuel_KG_nf
                HH_2_filter = fuel_kg
            elif houshold_count == 3:
                HH_3_fuel_sense.append((int(sum(set_kg_burned)*100))/100)
                HH_3 = id_number
                min_3 = kg
                HH_3_raw = Fuel_KG_nf
                HH_3_filter = fuel_kg
            elif houshold_count == 4:
                HH_4_fuel_sense.append((int(sum(set_kg_burned)*100))/100)
                HH_4 = id_number
                min_4 = kg
                HH_4_raw = Fuel_KG_nf
                HH_4_filter = fuel_kg
            elif houshold_count == 5:
                HH_5_fuel_sense.append((int(sum(set_kg_burned)*100))/100)
                HH_5 = id_number
            elif houshold_count == 6:
                HH_6_fuel_sense.append((int(sum(set_kg_burned)*100))/100)
                HH_6 = id_number
            elif houshold_count == 7:
                HH_7_fuel_sense.append((int(sum(set_kg_burned)*100))/100)
                HH_7 = id_number
        else:
            if houshold_count == 1:
                HH_11_fuel_sense.append((int(sum(set_kg_burned)*100))/100)
                HH_11 = id_number
            elif houshold_count == 2:
                HH_22_fuel_sense.append((int(sum(set_kg_burned)*100))/100)
                HH_22 = id_number
            elif houshold_count == 3:
                HH_33_fuel_sense.append((int(sum(set_kg_burned)*100))/100)
                HH_33 = id_number
    houshold_count = houshold_count +1
#print('----------------------------------',Thresh_step, HH_1_fuel_sense, type(Thresh_step), type(HH_1_fuel_sense))

#if  Phase  == ("2N") or Phase == "3N" or Phase == "1N" or Phase == "4N":
    #fig = go.Figure()
    #fig.add_trace(go.Scatter(x=Thresh_step, y=HH_1_fuel_sense,
    #                mode='lines+markers',
    #                name=HH_1))
    #fig.add_trace(go.Scatter(x=Thresh_step, y=HH_2_fuel_sense,
    #                mode='lines+markers',
    #                name=HH_2))
    #fig.add_trace(go.Scatter(x=Thresh_step, y=HH_3_fuel_sense,
    #                mode='lines+markers', name=HH_3))
    #fig.add_trace(go.Scatter(x=Thresh_step, y=HH_4_fuel_sense,
    #                mode='lines+markers',
    #                name=HH_4))
    #fig.add_trace(go.Scatter(x=Thresh_step, y=HH_5_fuel_sense,
    #                mode='lines+markers',
    #                name=HH_5))
  
    #fig.add_trace(go.Scatter(x=Thresh_step, y=HH_6_fuel_sense,
    #                mode='lines+markers', name=HH_6))
    #if houshold_count > 6:
    #    fig.add_trace(go.Scatter(x=Thresh_step, y=HH_7_fuel_sense,
    #                mode='lines+markers', name=HH_7))
    #fig.update_layout(title=Phase+" Sensitivity for Fuel Threshold",
    #               xaxis_title='Threshold',
    #               yaxis_title='Fuel Removed')
    #fig.show()

#else:
#    fig = go.Figure()
#    fig.add_trace(go.Scatter(x=Thresh_step, y=HH_11_fuel_sense,
#                    mode='lines+markers',
#                    name=HH_11))
#    fig.add_trace(go.Scatter(x=Thresh_step, y=HH_22_fuel_sense,
#                    mode='lines+markers',
#                    name=HH_22))
#    fig.add_trace(go.Scatter(x=Thresh_step, y=HH_33_fuel_sense,
#                    mode='lines+markers', name=HH_33))
#    fig.update_layout(title=Phase+" Sensitivity for Fuel Threshold",
#                   xaxis_title='Threshold',
#                   yaxis_title='Fuel Removed')
#    fig.show()

fig = go.Figure()
fig.add_trace(go.Scatter(x=min_1, y=HH_1_filter,
                mode='lines+markers',
                    name=HH_1))
#fig.add_trace(go.Scatter(x=min_2, y=HH_2_filter,
#                    mode='lines+markers',
#                    name=HH_2))
#fig.add_trace(go.Scatter(x=min_3, y=HH_3_filter,
#                    mode='lines+markers', name=HH_3))
fig.add_trace(go.Scatter(x=min_4, y=HH_4_filter,
                    mode='lines+markers',
                    name=HH_4))
fig.add_trace(go.Scatter(x=min_1, y=HH_1_raw,
                mode='lines+markers',
                    name=HH_1+'raw'))
#fig.add_trace(go.Scatter(x=min_2, y=HH_2_raw,
#                    mode='lines+markers',
#                    name=HH_2+'raw'))
#fig.add_trace(go.Scatter(x=min_3, y=HH_3_raw,
#                    mode='lines+markers', name=HH_3+'raw'))
fig.add_trace(go.Scatter(x=min_4, y=HH_4_raw,
                    mode='lines+markers',
                    name=HH_4+'raw'))
fig.update_layout(title=Phase+" Sensitivity for Fuel Threshold",
                   xaxis_title='Threshold',
                   yaxis_title='Fuel Removed')
fig.show()
