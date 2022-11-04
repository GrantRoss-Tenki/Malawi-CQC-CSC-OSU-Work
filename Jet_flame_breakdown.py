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


Source = 'work' #input("laptop or Work: ")  # 'work' or 'laptop'
Household = 'HH1' #input("HH1 or HH2... etc:  ")
log_rate_per_min = 15
Running_Average_length = 12 #int(input(" Enter Number for running length (8 would be ~ half a minute):  "))
if Source == 'laptop':
    USB = 'D'
else:
    USB = 'F'
# getting the metrics and times
Specific_JFK_breakdown_METRICS = (USB+":/Malawi 1.1/"+Household+"/Raw Event")

E_files = os.listdir(Specific_JFK_breakdown_METRICS)

Stage_1_Kitchen_PM = []; Stage_2_Kitchen_PM = []; Stage_3_Kitchen_PM = []
Stage_1_Cook_PM = []; Stage_2_Cook_PM = []; Stage_3_Cook_PM = []
Stage_1_Cook_Comp = []; Stage_2_Cook_Comp = []; Stage_3_Cook_Comp = []
Event = []

for file in E_files:
    file_path = f'{Specific_JFK_breakdown_METRICS}\\{file}'
    print('----', Specific_JFK_breakdown_METRICS+"/"+str(file))
    JFK_event_compiler = pd.read_csv(Specific_JFK_breakdown_METRICS+"/"+str(file))
    event = JFK_event_compiler.iloc[0,0]
    JFK_start = JFK_event_compiler.iloc[0,1]
    JFK_end = JFK_event_compiler.iloc[0,2]
    JFK_current = [float(a) for a in JFK_event_compiler.iloc[2:,0]]
    JFK_voltage = [float(a) for a in JFK_event_compiler.iloc[2:,1]]
    Kitchen_PM = [float(a) for a in JFK_event_compiler.iloc[2:,2]]
    Cook_PM = [float(a) for a in JFK_event_compiler.iloc[2:,3]]
    Cook_comp =  [float(a) for a in JFK_event_compiler.iloc[2:,4]]
    #JFK_voltage = list(JFK_voltage)
    print(event, type(JFK_voltage), type(JFK_voltage[10]),'this is bulllshit  ',JFK_voltage[126], float(JFK_voltage[126])*2 )
    # finding the start of Jet Flame
    Start_jfk = 0
    End_jfk = len(JFK_voltage) -1
    for tv, on in enumerate(JFK_voltage):
        #print('i am done', on, tv)
        if tv +1 != len(JFK_voltage):
            next = JFK_voltage[tv+1]
        else:
            break
        
        
        if on == 0.0 and next != 0.0:
            Start_jfk = tv +1
        elif on != 0.0 and next == 0.0:
            End_jfk = tv -1
            break
    
    print('start jfk',Start_jfk, 'end jfk',  End_jfk)
    Event.append(event)
    Stage_1_Kitchen_PM.append(np.median(Kitchen_PM[0:Start_jfk+1]))
    Stage_2_Kitchen_PM.append(np.median(Kitchen_PM[Start_jfk:End_jfk+1]))
    Stage_3_Kitchen_PM.append(np.median(Kitchen_PM[End_jfk:]))

    Stage_1_Cook_PM.append(np.median(Cook_PM[0:Start_jfk+1]))
    Stage_2_Cook_PM.append(np.median(Cook_PM[Start_jfk:End_jfk+1]))
    Stage_3_Cook_PM.append(np.median(Cook_PM[End_jfk:]))

    Stage_1_Cook_Comp.append(int(((sum(Cook_comp[0:Start_jfk+1]))/len(Cook_comp[0:Start_jfk+1]))*10)/10)
    Stage_2_Cook_Comp.append(int(((sum(Cook_comp[Start_jfk:End_jfk+1]))/(End_jfk-Start_jfk))*10)/10)
    Stage_3_Cook_Comp.append(int((sum(Cook_comp[End_jfk:]))/(len(Cook_comp)-End_jfk)*10)/10)


    
    # where_max_array = np.array(np.where(Kitchen_PM == max(Kitchen_PM)))
    # where_max = where_max_array[0][0]
    # print('here is max: ', max(Kitchen_PM), where_max)
    # Hapex_from_end = [int(a) for a in (Kitchen_PM[int(where_max): -2])]
    # Kitchen_PM = [int(a) for a in (Kitchen_PM)]
    # x = np.arange(0, len(Kitchen_PM), 1)
    # x_j = np.arange(0, len(Hapex_from_end), 1)
    # print('------Types ------',type(Hapex_from_end), len(Hapex_from_end), type(x_j), len(x_j))



    # print('------',Hapex_from_end[0:30],x_j[0:30] )
    # Hapex_from_end = list(map(float, Hapex_from_end))

    # COEFf =  (np.polyfit(x,Kitchen_PM,5))
    # #print('~~~~~~~ COEF ~~~~~~~ ', COEFf)
    # x_new = np.linspace(x[0], x[-1], num=len(x))
    # fffit = poly.polyval(x_new, COEFf)
    # fig, ax = plt.subplots()
    # ax2 = ax.twinx()
    # ax.scatter(x, Kitchen_PM, label = "Raw", color = 'r')
    # ax2.scatter(x_new, fffit, label = "line 1", color ='g')
    # #ax5.plot(x_new, fffit)
    # plt.show()

#post export

df_Jetflame_breakdown = pd.DataFrame({'Event ': Event, 'Median Kit Pm S1':Stage_1_Kitchen_PM, 'Median Kit Pm S2':Stage_2_Kitchen_PM,
'Median Kit Pm S3':Stage_3_Kitchen_PM, 'Median Cook Pm S1':Stage_1_Cook_PM, 'Median Cook Pm S2':Stage_2_Cook_PM,'Median Cook Pm S3':Stage_3_Cook_PM,
'% Cook comp S1':Stage_1_Cook_Comp, '% Cook comp S2':Stage_2_Cook_Comp,'% Cook comp S3':Stage_3_Cook_Comp})

print(df_Jetflame_breakdown)

path_export = USB+":/Malawi 1.1/"+Household+"_JFK_breakdown.csv"

df_Jetflame_breakdown.to_csv(path_export,index=False, mode='a')