import decimal
import itertools
import os
import pandas as pd
import numpy as np
import csv
import glob
from decimal import *
from itertools import chain
import datetime
from datetime import datetime
from itertools import islice, cycle
from io import StringIO
import matplotlib.pyplot as plt

Phase = "1N"
computer = "personal"
USB = "D"
print('Phase Number', Phase)

if Phase == "1N":
    ambient = 11
if Phase == "1H":
    ambient = 12
if Phase == "2N":
    ambient = 21
if Phase == "2H":
    ambient = 22
if Phase == "3N":
    ambient = 31
if Phase == "3H":
    ambient = 32
if Phase == "4N":
    ambient = 41

os.chdir(USB+":/PUMP FILES/"+ Phase +"/UPump")
Pump_information_path  = USB+":/PUMP FILES/Gravimetric_Analysis_MALAWI_2_16_2022.csv"
Pump_Household_information = USB+":/PUMP FILES/Phase_HH_SN.csv"
Weights_path = USB+":/PUMP FILES/"+ Phase +"_Compress_SN.csv"

Filter_information = pd.read_csv(Pump_information_path, delimiter= ',')
Household_information = pd.read_csv(Pump_Household_information, delimiter= ',')
Weights_divider = pd.read_csv(Weights_path, delimiter= ',')
Weigh_list = (Weights_divider.iloc[:,2])
time = []
if Phase == ("1N" or "1H" or "2N"):
    g = (Weights_divider.iloc[:,3])
    for c in g:
        x = float(c)
        time.append(x)

Weights = []
for a in Weigh_list:
    x = float(a)
    Weights.append((x))

HH_weights = Weights_divider.iloc[:,0]

Day_met_path = os.getcwd()
csv_R_m = glob.glob(os.path.join(Day_met_path, "*.csv"))

ID_numbers = []
Volume = []

Second_Exact = 0
for file in csv_R_m:
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        for idx, row in enumerate(csv_reader):
            if 'Household ID:' in row:
                id_number = (row[1])

            elif 'Total L pumped:' in row:
                liters =  (row[1])


    #print(id_number, liters)
    ID_numbers.append(id_number)
    Volume.append(float(liters))

Ratio = []
Household_ratio = []
MinCollected_ratio = []

Negated_housholds_weights = []
Negated_weights = []
Negated_housholds_Volume = []
Negated_Volume = []
for place_v, vol in enumerate(Volume):
    if float(vol) == 1080.7:
        for place_w, hh in enumerate(HH_weights):
            if (hh) == int(ID_numbers[place_v]):
                if (Weights[place_w]) != -1 or (Weights[place_w]) > 1:
                    if Phase == ("1N" or "1H" or "2N"):
                        MinCollected_ratio.append(time[place_w])
                        Household_ratio.append(hh)
                        equ_1 = ((int(((Weights[place_w])/((time[place_w]*1.5*0.5)*0.001))*100))/100)
                        print('this is equ', equ_1)
                        Ratio.append(equ_1)
                    else:
                        Household_ratio.append(hh)
                        equ_1 = ((int(((Weights[place_w])/(vol*0.001))*100))/100)
                        Ratio.append(equ_1)
                    
                else: 
                    Negated_housholds_weights.append(hh)
                    Negated_weights.append((Weights[place_w]))
            elif hh == ambient:
                Phase_ambient_weight =  Weights[place_w]
    else:
        Negated_housholds_Volume.append(int(ID_numbers[place_v]))
        Negated_Volume.append(float(vol))

print('household and ratios',  Ratio)
#print('household and negated weights',(Negated_housholds_weights), Negated_weights)
#print('household and negated volume',(Negated_housholds_Volume), Negated_Volume)
print('Household total looked at', len(Household_ratio)+len(Negated_housholds_weights)+len(Negated_housholds_Volume))

Micro_gram_per_m_3_per_min_ratio = []
#if Phase == ("1N" or "1H" or "2N"):
for val,r in enumerate(Ratio):
    Micro_gram_per_m_3_per_min_ratio.append(r)


print(Micro_gram_per_m_3_per_min_ratio)
print(len(Micro_gram_per_m_3_per_min_ratio))
print(len(Household_ratio))

#i have now recieved the information for the households that have fine pump information
#now i need to ge the day of correct visit
path_pump_install = USB+":/SAE_Moisture_Split/Moisture_SAE_split_"+Phase+"_.csv"
Pump_day  = pd.read_csv(path_pump_install, delimiter=',')

PM_per_day = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+ Phase +"/"+Phase+"_Household_Kitchen_breakdown_PM.csv"

PM_pump_day = pd.read_csv(PM_per_day, delimiter=',')

HH_pump_day = Pump_day.iloc[:,0] 
Pump_day_1 = Pump_day.iloc[:,5] 
Pump_day_2 = Pump_day.iloc[:,7]

PUMP = []
HomeNumber = []
for val, hh in enumerate(HH_pump_day):
    for ratios, home in enumerate(Household_ratio):
        if hh == home:
            day_count = int(Pump_day_1[val] + Pump_day_2[val]) +1
            #print(hh)
            #print(val)
            #print(day_count)
            #print(PM_pump_day.iloc[val,day_count])
            if PM_pump_day.iloc[val,day_count] != 0 and (Phase != "1H"):
                if PM_pump_day.iloc[val,day_count] == hh:

                    PUMP.append(Micro_gram_per_m_3_per_min_ratio[ratios])
                    HomeNumber.append(hh)
                else:

                    PUMP.append(Micro_gram_per_m_3_per_min_ratio[ratios])
                    HomeNumber.append(hh)
            elif Phase == "1H":
                if day_count < 1:

                    HomeNumber.append(hh)
                    PUMP.append(Micro_gram_per_m_3_per_min_ratio[ratios])
                elif PM_pump_day.iloc[val,day_count] != 0:

                    PUMP.append(Micro_gram_per_m_3_per_min_ratio[ratios])
                    HomeNumber.append(hh)


print(len(PUMP), len(Volume))
print(HomeNumber)
#print("ambient Pump weight",Phase_ambient_weight)
phase_emiision_compare = {'Household': HomeNumber,'Liters pumped': Volume,'Pump PM 2.5 (ug/m^3)*(min collected/ min in day)' : PUMP}
DF_emmisions = pd.DataFrame(phase_emiision_compare, columns= ['Household','Pump PM 2.5 (ug/m^3)*(min collected/ min in day)','Liters pumped'])
path_over = USB +":/PUMP FILES/Pump_pm_2.5_"+Phase+".csv"
DF_emmisions.to_csv(path_over, index=False, mode= 'a')