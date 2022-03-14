
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import plotly.express as px
#import plotly.graph_objects as go
#from plotly.subplots import make_subplots
import seaborn as sns


computer = input("personal or work computer - ")

Household_removal = [1045]
Household_Removal_PUMP_1N = [1045]
Household_Removal_PUMP_1H = [2016]
Household_Removal_PUMP_2N = [1045]
Household_Removal_PUMP_2H = [1045]
Household_Removal_PUMP_3N = [1045]
Household_Removal_PUMP_3H = [2016]
Household_Removal_PUMP_4N = [1045]


if computer == "work":
    USB = "D"
else:
    USB = "E"

path_1N = USB+":/PUMP FILES/Pump_and_HAP_1N.csv"
path_1H = USB+":/PUMP FILES/Pump_and_HAP_1H.csv"
path_2N = USB+":/PUMP FILES/Pump_and_HAP_2N.csv"
path_2H = USB+":/PUMP FILES/Pump_and_HAP_2H.csv"
path_3N = USB+":/PUMP FILES/Pump_and_HAP_3N.csv"
path_3H = USB+":/PUMP FILES/Pump_and_HAP_3H.csv"
path_4N = USB+":/PUMP FILES/Pump_and_HAP_4N.csv"

Frame_1N = pd.read_csv(path_1N, delimiter=',')
Frame_1H = pd.read_csv(path_1H, delimiter=',')
Frame_2N = pd.read_csv(path_2N, delimiter=',')
Frame_2H = pd.read_csv(path_2H, delimiter=',')
Frame_3N = pd.read_csv(path_3N, delimiter=',')
Frame_3H = pd.read_csv(path_3H, delimiter=',')
Frame_4N = pd.read_csv(path_4N, delimiter=',')

HH_1N = []
Pump_1N = []
Hapex_1N = []
Cook_1N = []
for val, hh in enumerate(Frame_1N.iloc[:,0]):
    count = 0
    for HH_total_remove in Household_removal:
        if (int(hh) == HH_total_remove):
            break
        for HH_1N_remove in Household_Removal_PUMP_1N:
            if (int(hh) == HH_total_remove) or (int(hh) == HH_1N_remove):
                print('----- Removed from 1N--------------------', hh)
                break
            if count != 1:
                if (int(hh) != HH_total_remove) or (int(hh) != HH_1N_remove) :
                    HH_1N.append((Frame_1N.iloc[val,0]))
                    Pump_1N.append((Frame_1N.iloc[val,1]))
                    Hapex_1N.append((Frame_1N.iloc[val,2]))
                    Cook_1N.append((Frame_1N.iloc[val,3]))
                    count = 1
print(HH_1N)
HH_1H = []
Pump_1H = []
Hapex_1H = []
Cook_1H = []
for val, hh in enumerate(Frame_1H.iloc[:,0]):
    count = 0
    for HH_total_remove in Household_removal:
        if (int(hh) == HH_total_remove):
            break
        for HH_1H_remove in Household_Removal_PUMP_1H:
            if (int(hh) == HH_total_remove) or (int(hh) == HH_1H_remove):
                print('----- Removed from 1H--------------------', hh)
                break
            if count != 1:
                if (int(hh) != HH_total_remove) or (int(hh) != HH_1H_remove) :
                    HH_1H.append((Frame_1H.iloc[val,0]))
                    Pump_1H.append((Frame_1H.iloc[val,1]))
                    Hapex_1H.append((Frame_1H.iloc[val,2]))
                    Cook_1H.append((Frame_1H.iloc[val,3]))
                    count = 1
HH_2N = []
Pump_2N = []
Hapex_2N = []
Cook_2N = []
for val, hh in enumerate(Frame_2N.iloc[:,0]):
    count = 0
    for HH_total_remove in Household_removal:
        if (int(hh) == HH_total_remove):
            break
        for HH_2N_remove in Household_Removal_PUMP_2N:
            if (int(hh) == HH_total_remove) or (int(hh) == HH_2N_remove):
                print('----- Removed from 2N--------------------', hh)
                break
            if count != 1:
                if (int(hh) != HH_total_remove) or (int(hh) != HH_2N_remove) :
                    HH_2N.append((Frame_2N.iloc[val,0]))
                    Pump_2N.append((Frame_2N.iloc[val,1]))
                    Hapex_2N.append((Frame_2N.iloc[val,2]))
                    Cook_2N.append((Frame_2N.iloc[val,3]))
                    count = 1
print('2n array', HH_2N)
HH_2H = []
Pump_2H = []
Hapex_2H = []
Cook_2H = []
for val, hh in enumerate(Frame_2H.iloc[:,0]):
    count = 0
    for HH_total_remove in Household_removal:
        if (int(hh) == HH_total_remove):
            break
        for HH_2H_remove in Household_Removal_PUMP_2H:
            if (int(hh) == HH_total_remove) or (int(hh) == HH_2H_remove):
                print('----- Removed from 2H--------------------', hh)
                break
            if count != 1:
                if (int(hh) != HH_total_remove) or (int(hh) != HH_2H_remove) :
                    HH_2H.append((Frame_2H.iloc[val,0]))
                    Pump_2H.append((Frame_2H.iloc[val,1]))
                    Hapex_2H.append((Frame_2H.iloc[val,2]))
                    Cook_2H.append((Frame_2H.iloc[val,3]))
                    count = 1
HH_3N = []
Pump_3N = []
Hapex_3N = []
Cook_3N = []
for val, hh in enumerate(Frame_3N.iloc[:,0]):
    count = 0
    for HH_total_remove in Household_removal:
        if (int(hh) == HH_total_remove):
            break
        for HH_3N_remove in Household_Removal_PUMP_3N:
            if (int(hh) == HH_total_remove) or (int(hh) == HH_3N_remove):
                print('----- Removed from 3N--------------------', hh)
                break
            if count != 1:
                if (int(hh) != HH_total_remove) or (int(hh) != HH_3N_remove) :
                    HH_3N.append((Frame_3N.iloc[val,0]))
                    Pump_3N.append((Frame_3N.iloc[val,1]))
                    Hapex_3N.append((Frame_3N.iloc[val,2]))
                    Cook_3N.append((Frame_3N.iloc[val,3]))
                    count = 1
HH_3H = []
Pump_3H = []
Hapex_3H = []
Cook_3H = []
for val, hh in enumerate(Frame_3H.iloc[:,0]):
    count = 0
    for HH_total_remove in Household_removal:
        if (int(hh) == HH_total_remove):
            break
        for HH_3H_remove in Household_Removal_PUMP_3H:
            if (int(hh) == HH_total_remove) or (int(hh) == HH_3H_remove):
                print('----- Removed from 3H--------------------', hh)
                break
            if count != 1:
                if (int(hh) != HH_total_remove) or (int(hh) != HH_3H_remove) :
                    HH_3H.append((Frame_3H.iloc[val,0]))
                    Pump_3H.append((Frame_3H.iloc[val,1]))
                    Hapex_3H.append((Frame_3H.iloc[val,2]))
                    Cook_3H.append((Frame_3H.iloc[val,3]))
                    count = 1
HH_4N = []
Pump_4N = []
Hapex_4N = []
Cook_4N = []
for val, hh in enumerate(Frame_4N.iloc[:,0]):
    count = 0
    for HH_total_remove in Household_removal:
        if (int(hh) == HH_total_remove):
            break
        for HH_4N_remove in Household_Removal_PUMP_4N:
            if (int(hh) == HH_total_remove) or (int(hh) == HH_4N_remove):
                print('----- Removed from 4N--------------------', hh)
                break
            if count != 1:
                if (int(hh) != HH_total_remove) or (int(hh) != HH_4N_remove) :
                    HH_4N.append((Frame_4N.iloc[val,0]))
                    Pump_4N.append((Frame_4N.iloc[val,1]))
                    Hapex_4N.append((Frame_4N.iloc[val,2]))
                    Cook_4N.append((Frame_4N.iloc[val,3]))
                    count = 1
#df = px.data.tips()

#fig = px.box(df, x="day", y="total_bill", color="smoker")
#fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
#fig.show()


fig, ax = plt.subplots()
plt.title('No-Hood Pump Box Plots')

#1N
quant_1_1N = np.percentile(Pump_1N, [25,50,75])
Top_lim_1_1N = quant_1_1N[2] + 1.5*(quant_1_1N[2] - quant_1_1N[0])
Low_lim_1_1N = quant_1_1N[0] - 1.5*(quant_1_1N[2] - quant_1_1N[0])
    
bp_1 = plt.boxplot(Pump_1N, positions = [1], widths = 0.6)
pump_1N_outlier = []
for v,a in enumerate(Pump_1N):
    if a > Top_lim_1_1N or a < Low_lim_1_1N:
        pump_1N_outlier.append(HH_1N[v])
        plt.text(1,a,HH_1N[v])
plt.text(1,0.1,'1N',color='b')

#2N    
quant_1_2N = np.percentile(Pump_2N, [25,50,75])
Top_lim_1_2N = quant_1_2N[2] + 1.5*(quant_1_2N[2] - quant_1_2N[0])
Low_lim_1_2N = quant_1_2N[0] - 1.5*(quant_1_2N[2] - quant_1_2N[0])
    
bp_1 = plt.boxplot(Pump_2N,positions = [2], widths = 0.6)
pump_2N_outlier = []
for v,a in enumerate(Pump_1N):
    if a > Top_lim_1_2N or a < Low_lim_1_2N:
        pump_2N_outlier.append(HH_2N[v])
        plt.text(2,a,HH_2N[v])
plt.text(2,0.1,'2N', color= 'g')
#3N
quant_1_3N = np.percentile(Pump_3N, [25,50,75])
Top_lim_1_3N = quant_1_3N[2] + 1.5*(quant_1_3N[2] - quant_1_3N[0])
Low_lim_1_3N = quant_1_3N[0] - 1.5*(quant_1_3N[2] - quant_1_3N[0])
    
bp_1 = plt.boxplot(Pump_2N,positions = [3], widths = 0.6)
count = 0
pump_3N_outlier = []
for v,a in enumerate(Pump_2N):
    if a > Top_lim_1_3N or a < Low_lim_1_3N:
        pump_3N_outlier.append(HH_3N[v])
        plt.text(3,a,HH_3N[v])

plt.text(3,0.1,'3N', color='r')        
    
#4N
quant_1_4N = np.percentile(Pump_4N, [25,50,75])
Top_lim_1_4N = quant_1_4N[2] + 1.5*(quant_1_4N[2] - quant_1_4N[0])
Low_lim_1_4N = quant_1_4N[0] - 1.5*(quant_1_4N[2] - quant_1_4N[0])
    
bp_1 = plt.boxplot(Pump_3N,positions = [4], widths = 0.6)
pump_4N_outlier = []
for v,a in enumerate(Pump_3N):
    if a > Top_lim_1_4N or a < Low_lim_1_4N:
        pump_4N_outlier.append(HH_4N[v])
        plt.text(4,a,HH_4N[v])
plt.text(4,0.1,'4N', color='y')        
            
plt.xlim(0,5)
plt.ylim(0,1000)
print('1N had these values as outliers   ', pump_1N_outlier)
print('2N had these values as outliers   ', pump_2N_outlier)
print('3N had these values as outliers   ', pump_3N_outlier)
print('4N had these values as outliers   ', pump_4N_outlier)
plt.show()

#no hood compare
Pump_2N_1N = []
hh_2N_1N = []
Pump_3N_1N = []
hh_3N_1N = []
Pump_4N_1N = []
hh_4N_1N = []
Pump_3N_2N = []
hh_3N_2N = []
Pump_4N_3N = []
hh_4N_3N = []
Pump_4N_2N = []
hh_4N_2N = []
#2N to 1N
for v, h in enumerate(HH_1N):
    for vv, hh in enumerate(HH_2N):
        if hh == h:
            hh_2N_1N.append(hh)
            divisi = Pump_2N[vv]/ Pump_1N[v]
            Pump_2N_1N.append(divisi)

fig_2, ax2 = plt.subplots()
plt.title('% No_hood Change from Pump PM 2.5' )

quant_1_2N_1N = np.percentile(Pump_2N_1N, [25,50,75])
Top_lim_1_2N_1N = quant_1_2N_1N[2] + 1.5*(quant_1_2N_1N[2]-quant_1_2N_1N[0])
Low_lim_1_2N_1N = quant_1_2N_1N[0] - 1.5*(quant_1_2N_1N[2]-quant_1_2N_1N[0])
bp_1_1 = plt.boxplot(Pump_2N_1N, positions=[1], widths= 0.6)
pump_2N_1N_outlier = []
for v,a in enumerate(Pump_2N_1N):
    if a > Top_lim_1_2N_1N or a < Low_lim_1_2N_1N:
        pump_2N_1N_outlier.append(hh_2N_1N[v])
        plt.text(1, a, hh_2N_1N[v])
plt.text(0.5, -0.5, '2N / 1N', color= 'g')

#3N to 1N
for v, h in enumerate(HH_1N):
    for vv, hh in enumerate(HH_3N):
        if hh == h:
            hh_3N_1N.append(hh)
            divisi = Pump_3N[vv]/ Pump_1N[v]
            Pump_3N_1N.append(divisi)

quant_1_3N_1N = np.percentile(Pump_3N_1N, [25,50,75])
Top_lim_1_3N_1N = quant_1_3N_1N[2] + 1.5*(quant_1_3N_1N[2]-quant_1_3N_1N[0])
Low_lim_1_3N_1N = quant_1_3N_1N[0] - 1.5*(quant_1_3N_1N[2]-quant_1_3N_1N[0])

bp_1_1 = plt.boxplot(Pump_3N_1N, positions=[2], widths= 0.6)
pump_3N_1N_outlier = []
for v,a in enumerate(Pump_3N_1N):
    if a > Top_lim_1_3N_1N or a < Low_lim_1_3N_1N:
        pump_3N_1N_outlier.append(hh_3N_1N[v])
        plt.text(2, a, hh_3N_1N[v])
plt.text(1.5, -0.5, '3N / 1N', color= 'r')
    
#4N to 1N
for v, h in enumerate(HH_1N):
    for vv, hh in enumerate(HH_4N):
        if hh == h:
            hh_4N_1N.append(hh)
            divisi = Pump_4N[vv]/ Pump_1N[v]
            Pump_4N_1N.append(divisi)

quant_1_4N_1N = np.percentile(Pump_4N_1N, [25,50,75])
Top_lim_1_4N_1N = quant_1_4N_1N[2] + 1.5*(quant_1_4N_1N[2]-quant_1_4N_1N[0])
Low_lim_1_4N_1N = quant_1_4N_1N[0] - 1.5*(quant_1_4N_1N[2]-quant_1_4N_1N[0])
bp_1_1 = plt.boxplot(Pump_4N_1N, positions=[3], widths= 0.6)
pump_4N_1N_outlier = []
for v,a in enumerate(Pump_4N_1N):
    if a > Top_lim_1_4N_1N or a < Low_lim_1_4N_1N:
        pump_4N_1N_outlier.append(hh_4N_1N[v])
        plt.text(3, a, hh_4N_1N[v])
plt.text(2.5, -0.5, '4N / 1N', color= 'y')
    
#3N to 2N
for v, h in enumerate(HH_2N):
    for vv, hh in enumerate(HH_3N):
        if hh == h:
            hh_3N_2N.append(hh)
            divisi = Pump_3N[vv]/ Pump_2N[v]
            Pump_3N_2N.append(divisi)

quant_1_3N_2N = np.percentile(Pump_3N_2N, [25,50,75])
Top_lim_1_3N_2N = quant_1_3N_2N[2] + 1.5*(quant_1_3N_2N[2]-quant_1_3N_2N[0])
Low_lim_1_3N_2N = quant_1_3N_2N[0] - 1.5*(quant_1_3N_2N[2]-quant_1_3N_2N[0])
bp_1_1 = plt.boxplot(Pump_3N_2N, positions=[4], widths= 0.6)
pump_3N_2N_outlier = []
for v,a in enumerate(Pump_3N_2N):
    if a > Top_lim_1_3N_2N or a < Low_lim_1_3N_2N:
        pump_3N_2N_outlier.append(hh_3N_2N[v])
        plt.text(4, a, hh_3N_2N[v])
plt.text(3.5, -0.5, '3N / 2N', color= 'm')
    
#4N to 3N
for v, h in enumerate(HH_4N):
    for vv, hh in enumerate(HH_3N):
        if hh == h:
            hh_4N_3N.append(hh)
            divisi = Pump_4N[v]/ Pump_3N[vv]
            Pump_4N_3N.append(divisi)

quant_1_4N_3N = np.percentile(Pump_4N_3N, [25,50,75])
Top_lim_1_4N_3N = quant_1_4N_3N[2] + 1.5*(quant_1_4N_3N[2]-quant_1_4N_3N[0])
Low_lim_1_4N_3N = quant_1_4N_3N[0] - 1.5*(quant_1_4N_3N[2]-quant_1_4N_3N[0])
bp_1_1 = plt.boxplot(Pump_4N_3N, positions=[5], widths= 0.6)
pump_4N_3N_outlier = []
for v,a in enumerate(Pump_4N_3N):
    if a > Top_lim_1_4N_3N or a < Low_lim_1_4N_3N:
        pump_4N_3N_outlier.append(hh_4N_3N[v])
        plt.text(5, a, hh_4N_3N[v])
plt.text(4.5, -0.5, '4N / 3N', color= 'k')
    
#4N to 2N
for v, h in enumerate(HH_4N):
    for vv, hh in enumerate(HH_2N):
        if hh == h:
            hh_4N_2N.append(hh)
            divisi = Pump_4N[v]/ Pump_2N[vv]
            Pump_4N_2N.append(divisi)

quant_1_4N_2N = np.percentile(Pump_4N_2N, [25,50,75])
Top_lim_1_4N_2N = quant_1_4N_2N[2] + 1.5*(quant_1_4N_2N[2]-quant_1_4N_2N[0])
Low_lim_1_4N_2N = quant_1_4N_2N[0] - 1.5*(quant_1_4N_2N[2]-quant_1_4N_2N[0])
bp_1_1 = plt.boxplot(Pump_4N_2N, positions=[6], widths= 0.6)
pump_4N_2N_outlier = []
for v,a in enumerate(Pump_4N_2N):
    if a > Top_lim_1_4N_2N or a < Low_lim_1_4N_2N:
       pump_4N_2N_outlier.append(hh_4N_2N[v])
       plt.text(6, a, hh_4N_2N[v])
plt.text(5.5, -0.5, '4N / 2N', color= 'tab:orange')
    
    
plt.xlim(0,7)
plt.ylim(-0.5,8)
print('2N/1N had these values as outliers   ', pump_2N_1N_outlier,)
print('3N/1N had these values as outliers   ', pump_3N_1N_outlier)
print('4N/1N had these values as outliers   ', pump_4N_1N_outlier)
print('3N/2N had these values as outliers   ', pump_3N_2N_outlier)
print('4N/3N had these values as outliers   ', pump_4N_3N_outlier)
print('4N/2N had these values as outliers   ', pump_4N_2N_outlier)
plt.show()

#no hood tables
quant_1_1N = np.append(quant_1_1N, np.average(Pump_1N))
quant_1_2N = np.append(quant_1_2N, np.average(Pump_2N))
quant_1_3N = np.append(quant_1_3N, np.average(Pump_3N))
quant_1_4N = np.append(quant_1_4N, np.average(Pump_4N))
  
D_50_quant_phase_phase = {'Percentile %': ['25','50','75', 'Avg'], '1N': quant_1_1N, '2N': quant_1_2N,'3N' : quant_1_3N,'4N': quant_1_4N}
Pump_50_phase_no_hood = pd.DataFrame(data=D_50_quant_phase_phase, columns=['Percentile %','1N', '2N', '3N','4N'])
    
quant_1_2N_1N = np.append(quant_1_2N_1N , np.average(Pump_2N_1N))
quant_1_3N_1N = np.append(quant_1_3N_1N , np.average(Pump_3N_1N))
quant_1_4N_1N = np.append(quant_1_4N_1N , np.average(Pump_4N_1N))
quant_1_3N_2N = np.append(quant_1_3N_2N , np.average(Pump_3N_2N))
quant_1_4N_3N = np.append(quant_1_4N_3N , np.average(Pump_4N_3N))
quant_1_4N_2N = np.append(quant_1_4N_2N , np.average(Pump_4N_2N))

        
D_50_quant_percent ={'Percentile %': ['25','50','75', 'Avg'],'2N / 1N': quant_1_2N_1N,'3N / 1N': quant_1_3N_1N,'4N / 1N': quant_1_4N_1N,
                               '3N / 2N': quant_1_3N_2N,'4N / 3N': quant_1_4N_3N,'4N / 2N': quant_1_4N_2N}
pump_50_percent_change_no_hood = pd.DataFrame(data=D_50_quant_percent, columns=['Percentile %','2N / 1N','3N / 1N', '4N / 1N'
                                                                                           ,'3N / 2N','4N / 3N','4N / 2N'])
print('Numbers of Values (1N)', len(Pump_1N))
print('Numbers of Values (2N)', len(Pump_2N))
print('Numbers of Values (3N)', len(Pump_3N))
print('Numbers of Values (4N)', len(Pump_4N))
print(Pump_50_phase_no_hood)
print('Numbers of Values (2N/1N)', len(Pump_2N_1N))
print('Numbers of Values (3N/1N)', len(Pump_3N_1N))
print('Numbers of Values (4N/1N)', len(Pump_4N_1N))
print('Numbers of Values (3N/2N)', len(Pump_3N_2N))
print('Numbers of Values (4N/3N)', len(Pump_4N_3N))
print('Numbers of Values (4N/2N)', len(Pump_4N_2N))
print(pump_50_percent_change_no_hood)





# hood portion

fig, ax = plt.subplots()
plt.title('Hood Pump Box Plots')


    
quant_1_1H = np.percentile(Pump_1H, [25,50,75])
Top_lim_1_1H = quant_1_1H[2] + 1.5*(quant_1_1H[2] - quant_1_1H[0])
Low_lim_1_1H = quant_1_1H[0] - 1.5*(quant_1_1H[2] - quant_1_1H[0])
    
bp_1 = plt.boxplot(Pump_1H, positions = [1], widths = 0.6)
pump_1H_outlier = []
for v,a in enumerate(Pump_1H):
    if a > Top_lim_1_1H or a < Low_lim_1_1H:
        pump_1H_outlier.append(HH_1H[v])
        plt.text(1,HH_1H[v])
plt.text(1,0,'1H',color='b')
        
        
quant_1_2H = np.percentile(Pump_2H, [25,50,75])
Top_lim_1_2H = quant_1_2H[2] + 1.5*(quant_1_2H[2] - quant_1_2H[0])
Low_lim_1_2H = quant_1_2H[0] - 1.5*(quant_1_2H[2] - quant_1_2H[0])
    
bp_1 = plt.boxplot(Pump_2H,positions = [2], widths = 0.6)
count = 0
pump_2H_outlier = []
for v,a in enumerate(Pump_2H):
    if a > Top_lim_1_2H or a < Low_lim_1_2H:
        pump_2H_outlier.append(HH_2H[v])
        plt.text(2,a,HH_2H[v])
plt.text(2,0,'2H', color= 'g')
   
quant_1_3H = np.percentile(Pump_3H, [25,50,75])
Top_lim_1_3H = quant_1_3H[2] + 1.5*(quant_1_3H[2] - quant_1_3H[0])
Low_lim_1_3H = quant_1_3H[0] - 1.5*(quant_1_3H[2] - quant_1_3H[0])
    
bp_1 = plt.boxplot(Pump_3H,positions = [3], widths = 0.6)
pump_3H_outlier = []
for v,a in enumerate(Pump_3H):
    if a > Top_lim_1_3H or a < Low_lim_1_3H:
        pump_3H_outlier.append(HH_3H[v])
        count = count + 1
        plt.text(3,a,HH_a_3H[v])
    plt.text(3,0,'3H', color='r')        
    
    
plt.xlim(-0,4)
plt.ylim(0,1000)
print('1H had these values as outliers   ', pump_1H_outlier)
print('2H had these values as outliers   ', pump_2H_outlier)
print('3H had these values as outliers   ', pump_3H_outlier)
plt.show()

Pump_2H_1H= []
hh_2H_1H = []
Pump_3H_1H = []
hh_3H_1H = []
Pump_3H_2H = []
hh_3H_2H = []

    #% change of fuel perday per adult between each phase 
fig_2, ax2 = plt.subplots()
plt.title('% hood Change from Pump pm 2.5' )
#2H to 1H
for v, h in enumerate(HH_2H):
    for vv, hh in enumerate(HH_1H):
        if hh == h:
            hh_2H_1H.append(hh)
            divisi = Pump_2H[v]/ Pump_1H[vv]
            Pump_2H_1H.append(divisi)

quant_1_2H_1H = np.percentile(Pump_2H_1H, [25,50,75])
Top_lim_1_2H_1H = quant_1_2H_1H[2] + 1.5*(quant_1_2H_1H[2]-quant_1_2H_1H[0])
Low_lim_1_2H_1H = quant_1_2H_1H[0] - 1.5*(quant_1_2H_1H[2]-quant_1_2H_1H[0])
bp_1_1 = plt.boxplot(Pump_2H_1H, positions=[1], widths= 0.6)
pump_2H_1H_outlier = []
for v,a in enumerate(Pump_2H_1H):
    if a > Top_lim_1_2H_1H or a < Low_lim_1_2H_1H:
        pump_2H_1H_outlier.append(hh_2H_1H[v])
        plt.text(1, a, hh_2H_1H[v])
plt.text(0.75, -0.25, '2H / 1H', color= 'g')
    
#3H to 1H
for v, h in enumerate(HH_3H):
    for vv, hh in enumerate(HH_1H):
        if hh == h:
            hh_3H_1H.append(hh)
            divisi = Pump_3H[v]/ Pump_1H[vv]
            Pump_3H_1H.append(divisi)

quant_1_3H_1H = np.percentile(Pump_3H_1H, [25,50,75])
Top_lim_1_3H_1H = quant_1_3H_1H[2] + 1.5*(quant_1_3H_1H[2]-quant_1_3H_1H[0])
Low_lim_1_3H_1H = quant_1_3H_1H[0] - 1.5*(quant_1_3H_1H[2]-quant_1_3H_1H[0])
bp_1_1 = plt.boxplot(Pump_3H_1H, positions=[2], widths= 0.6)
pump_3H_1H_outlier = []
count = 0
for v,a in enumerate(Pump_3H_1H):
    if a > Top_lim_1_3H_1H or a < Low_lim_1_3H_1H:
        pump_3H_1H_outlier.append(hh_3H_1H[v])
        count = count + 1
        if count == 1:
            plt.text(2, a, hh_3H_1H[v], ha='left',va='bottom')
        elif count != 1:
            plt.text(2, a, hh_3H_1H[v], ha='right',va='bottom')
plt.text(1.75, -0.25, '3H / 1H', color= 'r')
    
#3H to 2H
for v, h in enumerate(HH_3H):
    for vv, hh in enumerate(HH_2H):
        if hh == h:
            hh_3H_2H.append(hh)
            divisi = Pump_3H[v]/ Pump_2H[vv]
            Pump_3H_2H.append(divisi)

quant_1_3H_2H = np.percentile(Pump_3H_2H, [25,50,75])
Top_lim_1_3H_2H = quant_1_3H_2H[2] + 1.5*(quant_1_3H_2H[2]-quant_1_3H_2H[0])
Low_lim_1_3H_2H = quant_1_3H_2H[0] - 1.5*(quant_1_3H_2H[2]-quant_1_3H_2H[0])
bp_1_1 = plt.boxplot(Pump_3H_2H, positions=[3], widths= 0.6)
pump_3H_2H_outlier = []
for v,a in enumerate(Pump_3H_2H):
    if a > Top_lim_1_3H_2H or a < Low_lim_1_3H_2H:
        pump_3H_2H_outlier.append(hh_3H_2H[v])
        plt.text(3, a, hh_3H_2H[v])
plt.text(2.75, -0.25, '2H / 1H', color= 'm')
    
plt.xlim(-0,4)
plt.ylim(-0.25,2)
print('2H/1H had these values as outliers   ', pump_2H_1H_outlier)
print('3H/1H had these values as outliers   ', pump_3H_1H_outlier)
print('3H/2H had these values as outliers   ', pump_3H_2H_outlier)
plt.show()
    
quant_1_1H = np.append(quant_1_1H, np.average(Pump_1H))
quant_1_2H = np.append(quant_1_2H, np.average(Pump_2H))
quant_1_3H = np.append(quant_1_3H, np.average(Pump_3H))
    
D_50_quant_phase_hood = {'Percentile %': ['25','50','75', 'Avg'], '1H': quant_1_1H, '2H': quant_1_2H,'3H' : quant_1_3H}
Pump_50_phase_hood = pd.DataFrame(data=D_50_quant_phase_hood, columns=['Percentile %','1H', '2H','3H'] )
    
quant_1_2H_1H = np.append(quant_1_2H_1H , np.average(Pump_2H_1H))
quant_1_3H_1H = np.append(quant_1_3H_1H , np.average(Pump_3H_1H))
quant_1_3H_2H = np.append(quant_1_3H_2H , np.average(Pump_3H_2H))
    
D_50_quant_percent_pump_hood ={'Percentile %': ['25','50','75', 'Avg'],'2H / 1H': quant_1_2H_1H,'3H / 1H': quant_1_3H_1H,'3H / 2H': quant_1_3H_2H}
Pump_50_percent_change_hood = pd.DataFrame(data=D_50_quant_percent_pump_hood, columns=['Percentile %','2H / 1H','3H / 1H','3H / 2H'])
print('Numbers of Values (1H)', len(Pump_1H))
print('Numbers of Values (2H)', len(Pump_2H))
print('Numbers of Values (3H)', len(Pump_3H))
print(Pump_50_phase_hood)
print('Numbers of Values (2H/1H)', len(Pump_2H_1H))
print('Numbers of Values (3H/1H)', len(Pump_3H_1H))
print('Numbers of Values (3H/2H)', len(Pump_3H_2H))
print(Pump_50_percent_change_hood)



# plotly graph of hapex and pump

Hapex_1H_filter_1 = []
Names_1H_filter_1 = []
Pump_1H_filter_1 = []
for c, a in enumerate(Hapex_1H):
    if (a <= 0 ):
        Hapex_1H_filter_1.append(Hapex_1H[c])
        Names_1H_filter_1.append(HH_1H[c])
        Pump_1H_filter_1.append(Pump_1H[c])

Names_1H = ['2007', '2010', '2011', '2013', '2015']
fig = go.Figure(data=[ 
                go.Bar(name='Pump (ug/m^3)', x=Names_1H, y=Pump_1H_filter_1),
                go.Bar(name='Hapex (24 hour PM Average/ min)', x=Names_1H, y=Hapex_1H_filter_1)])

fig.update_layout(barmode='group')
fig.update_layout(title_text='1H Pump and Hapex')
#fig.show()

Names_2H = ['2001', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2013', '2015']
fig = go.Figure(data=[ 
                go.Bar(name='Pump (ug/m^3)', x=Names_2H, y=Pump_2H),
                go.Bar(name='Hapex (24 hour PM Average/ min)', x=Names_2H, y=Hapex_2H)])

fig.update_layout(barmode='group')
fig.update_layout(title_text='2H Pump and Hapex')
#fig.show()


Names_3H = ['2001', '2003','2006', '2007', '2009', '2010', '2011', '2013', '2014', '2015']
fig = go.Figure(data=[ 
                go.Bar(name='Pump (ug/m^3)', x=Names_3H, y=Pump_3H),
                go.Bar(name='Hapex (24 hour PM Average/ min)', x=Names_3H, y=Hapex_3H)])

fig.update_layout(barmode='group')
fig.update_layout(title_text='3H Pump and Hapex')
#fig.show()

# bar graph plotting no hood


Names_1N = ['1001', '1005', '1007', '1008', '1009', '1010', '1011', '1012', '1013', '1014', '1015', '1017', '1018', '1022', '1023', '1027', '1028', '1029', '1030', '1033', '1035', '1036', '1037', '1039', '1040']
fig = go.Figure(data=[ 
                go.Bar(name='Pump (ug/m^3)', x=Names_1N, y=Pump_1N),
                go.Bar(name='Hapex (24 hour PM Average/ min)', x=Names_1N, y=Hapex_1N)])

fig.update_layout(barmode='group')
fig.update_layout(title_text='1N Pump and Hapex')
#fig.show()

Names_2N = ['1001', '1002', '1003', '1005', '1008', '1009', '1011', '1012', '1013', '1014', '1015', '1017', '1019', '1020', '1021', '1023', '1024', '1026', '1027', '1028', '1029', '1030', '1031', '1032', '1033', '1035', '1036', '1037', '1038', '1039', '1040']
fig = go.Figure(data=[ 
                go.Bar(name='Pump (ug/m^3)', x=Names_2N, y=Pump_2N),
                go.Bar(name='Hapex (24 hour PM Average/ min)', x=Names_2N, y=Hapex_2N)])

fig.update_layout(barmode='group')
fig.update_layout(title_text='2N Pump and Hapex')
#fig.show()

Names_3N = ['1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009', '1010', '1011', '1012','1013', '1014', '1015', '1017', '1018', '1019', '1020', '1021', '1022', '1023', '1024', '1025', '1026', '1027', '1028', '1030', '1031', '1032', '1035', '1036', '1037', '1038', '1039', '1040']
                                                                   
fig = go.Figure(data=[ 
                go.Bar(name='Pump (ug/m^3)', x=Names_3N, y=Pump_3N),
                go.Bar(name='Hapex (24 hour PM Average/ min)', x=Names_3N, y=Hapex_3N)])

fig.update_layout(barmode='group')
fig.update_layout(title_text='3N Pump and Hapex')
#fig.show()

Names_4N = ['1001', '1002', '1004', '1005', '1006', '1007', '1008', '1009', '1011', '1012', '1013', '1014', '1015', '1017', '1018', '1019', '1020', '1021', '1022', '1023', '1024', '1025', '1026', '1027', '1028', '1030', '1031', '1032', '1033', '1035', '1036', '1037', '1038', '1039', '1040']
                                                                   
fig = go.Figure(data=[ 
                go.Bar(name='Pump (ug/m^3)', x=Names_4N, y=Pump_4N),
                go.Bar(name='Hapex (24 hour PM Average/ min)', x=Names_4N, y=Hapex_4N)])

fig.update_layout(barmode='group')
fig.update_layout(title_text='4N Pump and Hapex')
#fig.show()