import itertools
import os
import pandas as pd
import numpy as np
import csv
from decimal import *
from itertools import chain
import statistics as stat
import datetime
from io import StringIO
import matplotlib.pyplot as plt
import itertools
import os
import pandas as pd
import numpy as np
import csv
import glob


Fuel_Total = []
os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/1N/Villages/MALILI")
Day_met_path = os.getcwd()
csv_R_m = glob.glob(os.path.join(Day_met_path, "*.csv"))

for file in csv_R_m:
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        for idx, row in enumerate(csv_reader):
            if '0' in row:
                id_number_m = (row[1])
                #Fuel_type_m = (row[2])
                #Exact_stove_m = (row[3])
                #Kitchen_Hapex_m = (row[4])
                #Cook_hapex_m = (row[5])
            elif 'Timestamp'  in row:
                data_start = idx
                break


        sensor_data = pd.read_csv(file, skiprows=data_start)
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
        print('next household')
        ## below is counting down the minutes between each fuel removal


        Fuel_Total.extend(KG_burned)

print((int((sum(list(set(Fuel_Total))))*100))/100)