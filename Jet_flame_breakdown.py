import os
import pandas as pd
import numpy as np
import csv
import glob
from datetime import datetime
from csv import reader
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import Functions_malawi
import numpy.polynomial.polynomial as poly


Source = 'Work' #input("laptop or Work: ")  # 'work' or 'laptop'
Household = 'HH2' #input("HH1 or HH2... etc:  ")

Running_Average_length = 12 #int(input(" Enter Number for running length (8 would be ~ half a minute):  "))
if Source == 'laptop':
    USB = 'D'
else:
    USB = 'F'
# getting the metrics and times
Specific_JFK_breakdown_METRICS = (USB+":/Malawi 1.1/"+Household+"/Raw Event")

E_files = os.listdir(Specific_JFK_breakdown_METRICS)



for file in E_files:
    file_path = f'{Specific_JFK_breakdown_METRICS}\\{file}'
    print('----', Specific_JFK_breakdown_METRICS+"/"+str(file))
    JFK_event_compiler = pd.read_csv(Specific_JFK_breakdown_METRICS+"/"+str(file))
    event = JFK_event_compiler.iloc[1,0]
    JFK_start = JFK_event_compiler.iloc[1,1]
    JFK_end = JFK_event_compiler.iloc[1,2]
    JFK_current = JFK_event_compiler.iloc[3:,0]
    JFK_voltage = JFK_event_compiler.iloc[3:,1]
    Kitchen_PM = JFK_event_compiler.iloc[3:,2]
    Cook_PM = JFK_event_compiler.iloc[3:,3]
    Cook_comp =  JFK_event_compiler.iloc[3:,4]

    
    
    where_max_array = np.array(np.where(Kitchen_PM == max(Kitchen_PM)))
    where_max = where_max_array[0][0]
    print('here is max: ', max(Kitchen_PM), where_max)
    Hapex_from_end = [int(a) for a in (Kitchen_PM[int(where_max): -2])]
    Kitchen_PM = [int(a) for a in (Kitchen_PM)]
    x = np.arange(0, len(Kitchen_PM), 1)
    x_j = np.arange(0, len(Hapex_from_end), 1)
    print('------Types ------',type(Hapex_from_end), len(Hapex_from_end), type(x_j), len(x_j))



    print('------',Hapex_from_end[0:30],x_j[0:30] )
    Hapex_from_end = list(map(float, Hapex_from_end))

    COEFf =  (np.polyfit(x,Kitchen_PM,5))
    #print('~~~~~~~ COEF ~~~~~~~ ', COEFf)
    x_new = np.linspace(x[0], x[-1], num=len(x))
    fffit = poly.polyval(x_new, COEFf)
    fig, ax = plt.subplots()
    ax2 = ax.twinx()
    ax.scatter(x, Kitchen_PM, label = "Raw", color = 'r')
    ax2.scatter(x_new, fffit, label = "line 1", color ='g')
    #ax5.plot(x_new, fffit)
    plt.show()



