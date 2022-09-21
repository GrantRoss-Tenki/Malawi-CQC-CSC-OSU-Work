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

HH_Number_array = ['HH1', 'HH2', 'HH3', 'HH4', 'HH5','HH6']
Stove_array = ['1','2','3']
CCT_array = ['1','2','3', '4']

Source = 'laptop' #input("laptop or Work: ")  # 'work' or 'laptop'
Household = 'HH4' #input("HH1 or HH2... etc:  ")
Stove = '1'#input("1 = TSF, 2 = CQC, 3 = JFK:  ")
CCT_Num = '1'#input("CCT Number - 1, 2, or 3: ")
Running_Average_length = 12 #int(input(" Enter Number for running length (8 would be ~ half a minute):  "))
if Source == 'laptop':
    USB = 'D'
else:
    USB = 'E'
# getting the metrics and times
CCT_TIMES_METRICS = pd.read_csv(USB+":/Malawi 1.1 CCT Fire Start Times.csv")
identifyer = Household+' - CCT-'+ CCT_Num
if Stove == '1':
    for rows, name in enumerate(CCT_TIMES_METRICS.iloc[:,0]):
        if name == identifyer:
            Fire_Start = CCT_TIMES_METRICS.iloc[rows,1]
            Fuel_change = CCT_TIMES_METRICS.iloc[rows,2]
            Fuel_MJ = CCT_TIMES_METRICS.iloc[rows, 3]
            Boil_time = CCT_TIMES_METRICS.iloc[rows, 4]
            Coking_Length = CCT_TIMES_METRICS.iloc[rows, 5]
if Stove == '2':
    for rows, name in enumerate(CCT_TIMES_METRICS.iloc[:,6]):
        if name == identifyer:
            Fire_Start = CCT_TIMES_METRICS.iloc[rows,7]
            Fuel_change = CCT_TIMES_METRICS.iloc[rows,8]
            Fuel_MJ = CCT_TIMES_METRICS.iloc[rows, 9]
            Boil_time = CCT_TIMES_METRICS.iloc[rows, 10]
            Coking_Length = CCT_TIMES_METRICS.iloc[rows, 11]
if Stove == '3':
    for rows, name in enumerate(CCT_TIMES_METRICS.iloc[:,12]):
        if name == identifyer:
            Fire_Start = CCT_TIMES_METRICS.iloc[rows,13]
            Fuel_change = CCT_TIMES_METRICS.iloc[rows,14]
            Fuel_MJ = CCT_TIMES_METRICS.iloc[rows, 15]
            Boil_time = CCT_TIMES_METRICS.iloc[rows, 16]
            Coking_Length = CCT_TIMES_METRICS.iloc[rows, 17]


CCT_Stove_Path = USB+":/Malawi 1.1/"+Household+"/S- "+Stove+"; CCT-"+CCT_Num
l_files = os.listdir(CCT_Stove_Path)

for file in l_files:

    file_path = f'{CCT_Stove_Path}\\{file}'
    if file[0] == "H":
        if (file[6:10] == '1577') or (file[6:10] == '1558') or (file[6:10] == '3275'):
            Inline_hapex_name = 'HAPEx '+ file[6:10]
            I_H_File = os.getcwd()
            I_H_open = glob.glob((file_path))
            for files in I_H_open:
                with open(files, 'r') as f:
                    csv_reader = csv.reader(f)
                    for idx, row in enumerate(csv_reader):
                        if 'Timestamp' in row:
                            print('inline')
                            Inline_hapex_csv = pd.read_csv(file_path, skiprows= (idx))
                            I_Hap_Time = (Inline_hapex_csv.iloc[:,0])
                            Day_date = Inline_hapex_csv.iloc[0,0][0:10]
                            Inline_Hap_Comp = Inline_hapex_csv.iloc[:,1]
                            Inline_Hap_PM = Inline_hapex_csv.iloc[:,2]
                            for tv, f in enumerate(I_Hap_Time):
                                if f[11:16] == Fire_Start[9:] or str(f[10:16]) == Fire_Start[10:]:
                                    Inline_Hapex_FIRE_START_TV = tv
                                    break
        elif file[1] == "H":
            print('Household')
        else:
            Cook_hapex_name = 'HAPEx '+ file[6:10]
            C_H_File = os.getcwd()
            C_H_open = glob.glob((file_path))
            for files in C_H_open:
                with open(files, 'r') as f:
                    csv_reader = csv.reader(f)
                    for idx, row in enumerate(csv_reader):
                        if 'Timestamp' in row:
                            Cook_hapex_csv = pd.read_csv(file_path, skiprows= (idx))
                            C_Hap_Time = Cook_hapex_csv.iloc[:,0]
                            Cook_Hap_Comp = Cook_hapex_csv.iloc[:,1]
                            Cook_Hap_PM = Cook_hapex_csv.iloc[:,2]
                            #print('TEEESTER', str(C_Hap_Time[0][11:16]),Fire_Start[9:] )
                            for tv, f in enumerate(C_Hap_Time):
                                if f[9:16] == Fire_Start[9:] or str(f[11:16]) == Fire_Start[10:] or str(f[11:16]) == Fire_Start[9:]:
                                    Cook_hapex_FIRE_START_TV = tv
                                    break

    elif file[0] == "B":
        Cook_Beacon_name = 'Beacon ' + file[7:11]
        C_Beacon_File = os.getcwd()
        C_Beacon_open = glob.glob((file_path))
        for files in C_Beacon_open:
            with open(files, 'r') as f:
                csv_reader = csv.reader(f)
                for idx, row in enumerate(csv_reader):
                    if 'Timestamp' in row:
                        Beacon_Failure = False
                        Cook_Beacon_csv = pd.read_csv(file_path, skiprows=(idx))
                        Cook_Beacon_Time = Cook_Beacon_csv.iloc[:, 0]
                        Cook_Beacon_Move= Cook_Beacon_csv.iloc[:, 1]
                        Cook_Beacon_Accel = Cook_Beacon_csv.iloc[:, 2]
                        #print('TEEESTER' ,str(Cook_Beacon_Time))#,Fire_Start[9:], str(Cook_Beacon_Time[0][10:16]), Fire_Start[10:])
                        for tv, f in enumerate(Cook_Beacon_Time):
                            if f[11:16] == Fire_Start[9:] or str(f[10:16]) == Fire_Start[10:]:
                                Beacon_FIRE_START_TV = tv
                                break
    elif file[0] == 'U':
        USB_name = 'USBLog ' + file[7:11]
        USB_File = os.getcwd()
        USB_open = glob.glob((file_path))
        for files in USB_open:
            with open(files, 'r') as f:
                csv_reader = csv.reader(f)
                for idx, row in enumerate(csv_reader):
                    if 'Timestamp' in row:
                        USB_Failure = False
                        USB_CSV = pd.read_csv(file_path, skiprows=(idx))
                        USB_Time = USB_CSV.iloc[:, 0]
                        USB_Battery = USB_CSV.iloc[:, 1]
                        USB_Current = USB_CSV.iloc[:, 2]
                        USB_Voltage = USB_CSV.iloc[:, 3]
                        USB_Power = USB_CSV.iloc[:, 4]
                        USB_Energy  = USB_CSV.iloc[:, 5]
                        USB_Usage = USB_CSV.iloc[:, 6]
                        USB_Proximity_DF = pd.DataFrame(USB_CSV.iloc[:, 6:])
                        for tv, f in enumerate(USB_Time):
                            if f[11:16] == Fire_Start[9:] or str(f[10:16]) == Fire_Start[10:]:
                                USB_FIRE_START_TV = tv
                                break
    elif file[0] == 'G':
        Gas_name = 'GasSense ' + file[9:13]
        Gas_File = os.getcwd()
        Gas_open = glob.glob((file_path))
        for files in Gas_open:
            with open(files, 'r') as f:
                csv_reader = csv.reader(f)
                for idx, row in enumerate(csv_reader):
                    if 'Timestamp' in row:
                        GasSense_Failure = False
                        Gas_csv = pd.read_csv(file_path, skiprows=(idx))
                        Gas_Time = Gas_csv.iloc[:, 0]
                        Gas_Battery = Gas_csv.iloc[:, 1]
                        Gas_CO2 = Gas_csv.iloc[:, 2]
                        Gas_CO = Gas_csv.iloc[:, 3]
                        Gas_Termal = Gas_csv.iloc[:, 4]
                        Gas_T_Bosh = Gas_csv.iloc[:, 5]
                        Gas_T_Sen = Gas_csv.iloc[:, 6]
                        Gas_Pressure = Gas_csv.iloc[:, 7]
                        Gas_RH = Gas_csv.iloc[:, 8]
                        #finding fire start time value
                        print('~~~~~', Gas_Time[0][9:16], Fire_Start[10:])
                        for tv, f in enumerate(Gas_Time):
                            if f[11:16] == Fire_Start[9:] or str(f[10:16]) == Fire_Start[10:] or str(f[9:16]) == Fire_Start[10:]:
                                GAS_FIRE_START_TV = tv
                                break
    elif file[0] != 'B':
        Beacon_Failure = True
        print('There is no Beacon data')
    elif file[0] != 'U':
        USB_Failure = True
        print('There is no USB data')
    elif file[0] != 'G':
        GasSense_Failure = True
        print('There is no GasSense data')

co2_filter = Functions_malawi.Running_Average(Gas_CO2, Running_Average_length)
co_filter = Functions_malawi.Running_Average(Gas_CO, Running_Average_length)

# Finding the fire start and starting with gas

print('----Plotting Gas Sense----')
x = np.linspace(0.0, len(co2_filter), int(len(co2_filter)/(15*5)))
xval = []
for tt in x:
    xval.append(int(tt/15))

fig, ax = plt.subplots()
plt.title('CO2 Filter')

plt.plot(Gas_CO2, label='Orginal CO2', color='green')
plt.plot(co2_filter, label='CO2 Filter', color='r')

ax2 = ax.twinx()
labels = [x]

ax2.plot(Inline_Hap_PM,label='Inline HAPEx', color = 'blue')
ax2.plot(Cook_Hap_PM,label='Cook HAPEx',  color = 'm')

#getting start up before fire start
plt.axvline(GAS_FIRE_START_TV, color='k',linestyle = '--')#label='Fire Start',

Avg_Fire_CO2_Setup = np.average(co2_filter[0:GAS_FIRE_START_TV])
Median_Fire_CO2_Setup = np.median(co2_filter[0:GAS_FIRE_START_TV])
print('Average CO2 PPM to Start:  ', int(Avg_Fire_CO2_Setup))
print('Median CO2 PPM to Start:  ', int(Median_Fire_CO2_Setup))
Slope_CO2_to_Start = (co2_filter[GAS_FIRE_START_TV] - co2_filter[0]) / ((GAS_FIRE_START_TV + 1 - 0) / 15)
print('CO2 Before Fire Slope:  ', int(Slope_CO2_to_Start))



ax.set_ylabel('CO2 - PPM')
ax.set_xlabel("Minutes")
plt.ylabel('Hapex PM ')
if Boil_time != '-1':
    Gas_boil = (GAS_FIRE_START_TV) + (15*int(Boil_time))
    plt.axvline(Gas_boil, color='k', linestyle=':')# label='Boil Time',
    if GasSense_Failure == False:
        Avg_Fire_CO2_Start_to_boil = np.average(co2_filter[GAS_FIRE_START_TV:Gas_boil +1])
        Median_Fire_CO2_Start_to_boil = np.median(co2_filter[GAS_FIRE_START_TV:Gas_boil +1])
        print('Average CO2 PPM from Start - Boil:  ', int(Avg_Fire_CO2_Start_to_boil))
        print('Median CO2 PPM from Start - Boil:  ', int(Median_Fire_CO2_Start_to_boil))
        Slope_CO2_Boil = (co2_filter[Gas_boil+1] - co2_filter[GAS_FIRE_START_TV])/((Gas_boil+1 -GAS_FIRE_START_TV)/15)
        print('CO2 Start - Boil Slope:  ', int(Slope_CO2_Boil))
if Coking_Length != '-1':
    Gas_CE = (GAS_FIRE_START_TV) + (15 * int(Coking_Length))
    plt.axvline(Gas_CE, color='k')# label='Cooking End',
    if GasSense_Failure == False:
        Avg_CO2_Cooking_length = np.average(co2_filter[GAS_FIRE_START_TV:Gas_CE+1])
        Median_CO2_Boil_to_Cooking_end = np.median(co2_filter[GAS_FIRE_START_TV:Gas_CE +1])
        print('Average CO2 PPM for Cooking Length:  ', int(Avg_CO2_Cooking_length))
        print('Median CO2 PPM for Cooking Length:  ',int(Median_CO2_Boil_to_Cooking_end) )
        Slope_CO2_CE = (co2_filter[Gas_CE + 1] - co2_filter[GAS_FIRE_START_TV]) / ((Gas_CE + 1 - GAS_FIRE_START_TV) / 15)
        print('CO2 Cooking length Slope:  ', int(Slope_CO2_CE))
if Coking_Length != '-1' and Boil_time != '-1':
    if GasSense_Failure == False:
        Avg_CO2_Boil_to_Cooking_end = np.average(co2_filter[Gas_boil: Gas_CE+1])
        Median_CO2_Boil_to_Cooking_end = np.median(co2_filter[Gas_boil: Gas_CE+1])
        print('Average CO2 PPM from Boil - Cooking End:  ', int(Avg_CO2_Boil_to_Cooking_end))
        print('Median CO2 PPM from Boil - Cooking End:  ', int(Median_CO2_Boil_to_Cooking_end))
        Slope_CO2_boil_CE = (co2_filter[Gas_CE + 1] - co2_filter[Gas_boil]) / ((Gas_CE + 1 - Gas_boil) / 15)
        print('CO2 boil - Cooking end Slope:  ', int(Slope_CO2_boil_CE))
        Slope_CO2_Cooldown = (co2_filter[-1] - co2_filter[Gas_CE]) / ((len(co2_filter) - 1 - Gas_CE) / 15)
        print('CO2 Cooldown Slope:  ', int(Slope_CO2_Cooldown), 'Cooldown Length (minutes):  ', int(((len(co2_filter) - 1 - Gas_CE) / 15)))



plt.xticks(x, xval)
plt.legend()
#plt.show()


fig2, ax1 = plt.subplots()

labels2 = [x]
plt.title('CO Filter')
#plt.ylabel("CO - PPM")





# getitng the slope before the fire starr
plt.axvline(GAS_FIRE_START_TV, color='k',linestyle = '--') #label='Fire Start',
Avg_Fire_CO_Setup = np.average(co_filter[0:GAS_FIRE_START_TV])
Median_Fire_CO_Setup = np.median(co_filter[0:GAS_FIRE_START_TV])
print('Average CO PPM to Start:  ', int(Avg_Fire_CO_Setup))
print('Median CO PPM to Start:  ', int(Median_Fire_CO_Setup))
Slope_CO_to_Start = (co_filter[GAS_FIRE_START_TV] - co_filter[0]) / ((GAS_FIRE_START_TV + 1 - 0) / 15)
print('CO Before Fire Slope:  ', int(Slope_CO_to_Start))

ax1.set_ylabel('CO - PPM')
ax1.set_xlabel("Minutes")
plt.ylabel('Hapex PM ')
if Boil_time != '-1':
    Gas_boil = (GAS_FIRE_START_TV) + (15*int(Boil_time))
    plt.axvline(Gas_boil, color='k', linestyle=':') # label='Boil Time',
    if GasSense_Failure == False:
        Avg_Fire_CO_Start_to_boil = np.average(co_filter[GAS_FIRE_START_TV:Gas_boil +1])
        Median_Fire_CO_Start_to_boil = np.median(co_filter[GAS_FIRE_START_TV:Gas_boil +1])
        print('Average CO PPM from Start - Boil:  ', int(Avg_Fire_CO_Start_to_boil))
        print('Median CO PPM from Start - Boil:  ', int(Median_Fire_CO_Start_to_boil))
if Coking_Length != '-1':
    Gas_CE = (GAS_FIRE_START_TV) + (15 * int(Coking_Length))
    plt.axvline(Gas_CE,  color='k')#label='Cooking End',
    if GasSense_Failure == False:
        Avg_CO_Cooking_length = np.average(co_filter[GAS_FIRE_START_TV:Gas_CE+1])
        Median_CO_Boil_to_Cooking_end = np.median(co_filter[GAS_FIRE_START_TV:Gas_CE +1])
        print('Average CO PPM for Cooking Length:  ', int(Avg_CO_Cooking_length))
        print('Median CO PPM for Cooking Length:  ',int(Median_CO_Boil_to_Cooking_end) )
        # Gradient for the array section
        Gradient_Fire_CO_Cooking = np.gradient(co_filter[GAS_FIRE_START_TV:Gas_CE+1])

        grad_count = 0
        Local_maxima_Cooking = []
        Local_minima_Cooking = []
        CO_Gradient, CO_Gradient_TV =  Functions_malawi.Remove_Repeated_Values(Gradient_Fire_CO_Cooking)
        for gg in CO_Gradient:
            if grad_count + 1 == len(CO_Gradient)-1:
                break
            elif CO_Gradient[grad_count+1] < 0 and gg > 0:
                Local_maxima_Cooking.append(CO_Gradient_TV[grad_count]+GAS_FIRE_START_TV)
            elif CO_Gradient[grad_count+1] > 0 and gg < 0:
                Local_minima_Cooking.append(CO_Gradient_TV[grad_count] + GAS_FIRE_START_TV)
            grad_count = grad_count + 1
        maxima_CO_Cooking = []
        for place,B in enumerate(Local_maxima_Cooking):
            maxima_CO_Cooking.append(co_filter[B])

        Y_Max_CO_Cooking = max(maxima_CO_Cooking)
        Where_Y_Max_CO_Cooking = np.where(maxima_CO_Cooking == (Y_Max_CO_Cooking))
        X_Max_CO_Cooking = Local_maxima_Cooking[int(Where_Y_Max_CO_Cooking[0])]
        print('The toal max CO (minutes):   ', X_Max_CO_Cooking/15 )
if Coking_Length != '-1' and Boil_time != '-1':
    if GasSense_Failure == False:
        Avg_CO_Boil_to_Cooking_end = np.average(co_filter[Gas_boil: Gas_CE+1])
        Median_CO_Boil_to_Cooking_end = np.median(co_filter[Gas_boil: Gas_CE+1])
        print('Average CO PPM from Boil - Cooking End:  ', int(Avg_CO_Boil_to_Cooking_end))
        print('Median CO PPM from Boil - Cooking End:  ', int(Median_CO_Boil_to_Cooking_end))


plt.xticks(x, xval)
ax1.plot(X_Max_CO_Cooking, Y_Max_CO_Cooking, label='Local Max ',color = 'k', marker=".", markersize=30)

ax22 = ax1.twinx()

ax1.plot(Gas_CO, label='Orginal CO', color='green')
ax1.plot(co_filter, color='r', label='CO Filter')
ax22.plot(Inline_Hap_PM, color = 'blue',) #label='Inline HAPEx',
ax22.plot(Cook_Hap_PM,  color = 'm',label='Cook HAPEx') #label='Cook HAPEx',


#going to solve for CO cooldown usingx previous steady state work
# First USe Local Max


#print('CO min count', Local_minima_Cooking)
# For maximum, I am going to use the total maximum for the test and coking event
Co_MIN_tv, Co_MAX_tv ,Co_MIN_Count, Co_MAX_Count = Functions_malawi.Local_Max_min(Gas_CO[Gas_CE:], Gas_CE,0)
#print('CO from local min max', Co_MIN_tv, Co_MAX_tv ,Co_MIN_Count, Co_MAX_Count)

#Steady_start_Time_value = Functions_malawi.SteadyState_Finder(Gas_CO, 25, Co_MIN_Count,Gas_CO[Gas_CE],Co_MAX_Count ,10)
#print(Steady_start_Time_value, type(Gas_CO), type(Gas_CO[Gas_CE:]))

#Hap_MIN_tv, Hap_MAX_tv ,Hap_MIN_Count, Hap_MAX_Count = Functions_malawi.Local_Max_min(Inline_Hap_PM[Gas_CE:], Gas_CE,0)
#HAPEX_Steady_start_Time_value = Functions_malawi.SteadyState_Finder(Inline_Hap_PM, 25, Hap_MIN_Count,Inline_Hap_PM[Gas_CE],Hap_MAX_Count ,10)
#print(HAPEX_Steady_start_Time_value)
#ax1.plot(Steady_start_Time_value, Gas_CO[Steady_start_Time_value], label='Local Max ',color = 'k', marker=".", markersize=30)
plt.legend()
plt.show()


