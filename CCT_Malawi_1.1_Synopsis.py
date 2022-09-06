# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 13:18:47 2022

@author: rossgra
"""

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


Source = 'work'   # 'work' or 'laptop'

if Source == 'laptop':
    USB = 'E'
else:
    USB = 'D'
    
Path_Stove_1 = USB+":/CCT-Stove-1-Matrix.csv"
Path_Stove_2 = USB+":/CCT-Stove-2-Matrix.csv"
Path_Stove_3 = USB+":/CCT-Stove-3-Matrix.csv"

COl_namnes = ['Household and Test','Wood Used','Flour Used','Water used','Cooked Food',
              'Hot Charcoal','Start to Flour in','Start to Stir','Start to Boil','Cooking Time']

TSF = pd.DataFrame(pd.read_csv(Path_Stove_1, names=COl_namnes, header =0))
CQC = pd.DataFrame(pd.read_csv(Path_Stove_2, names=COl_namnes, header =0))
CQC_JFK = pd.DataFrame(pd.read_csv(Path_Stove_3, names=COl_namnes, header =0))


# Filtering out the non Standardized Water and Flour
TSF_Filter = []
TSF_Non_Filter = []
Name_TSF = (TSF['Household and Test'])
Wood_TSF = list(TSF['Wood Used']);Cooked_TSF = list(TSF['Cooked Food']);Charcoal_TSF = list(TSF['Hot Charcoal']);Flour_In_TSF = list(TSF['Start to Flour in'])
Stir_TSF = list(TSF['Start to Stir']);Boil_TSF = list(TSF['Start to Boil']);CE_Time_TSF = list(TSF['Cooking Time'])

for TSF_Row, TSF in enumerate(TSF['Flour Used']):
    if TSF == 1300:
        TSF_Filter.append(TSF_Row)
    else:
        TSF_Non_Filter.append(TSF_Row)
        
CQC_Filter = []
CQC_Non_Filter = []
Name_CQC = (CQC['Household and Test'])
Wood_CQC = list(CQC['Wood Used']);Cooked_CQC = list(CQC['Cooked Food']);Charcoal_CQC = list(CQC['Hot Charcoal']);Flour_In_CQC = list(CQC['Start to Flour in'])
Stir_CQC = list(CQC['Start to Stir']);Boil_CQC = list(CQC['Start to Boil']);CE_Time_CQC = list(CQC['Cooking Time'])

for CQC_Row, CQC in enumerate(CQC['Flour Used']):
    if CQC == 1300:
        CQC_Filter.append(CQC_Row)
    else:
        CQC_Non_Filter.append(CQC_Row)
        
CQC_JFK_Filter = []
CQC_JFK_Non_Filter = []
Name_CQC_JFK = (CQC_JFK['Household and Test']);
Wood_CQC_JFK = list(CQC_JFK['Wood Used']);Cooked_CQC_JFK = list(CQC_JFK['Cooked Food']);Charcoal_CQC_JFK = list(CQC_JFK['Hot Charcoal'])
Flour_In_CQC_JFK = list(CQC_JFK['Start to Flour in']);Stir_CQC_JFK = list(CQC_JFK['Start to Stir']);Boil_CQC_JFK = list(CQC_JFK['Start to Boil'])
CE_Time_CQC_JFK = list(CQC_JFK['Cooking Time'])

for CQC_JFK_Row, CQC_JFK in enumerate(CQC_JFK['Flour Used']):
    if CQC_JFK == 1300:
        CQC_JFK_Filter.append(CQC_JFK_Row)
    else:
        CQC_JFK_Non_Filter.append(CQC_JFK_Row)



# Three stone Fire Baseline Matrix Partition

def delete_multiple_element(list_object, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)
            


delete_multiple_element(Name_TSF, TSF_Non_Filter)
delete_multiple_element(Wood_TSF, TSF_Non_Filter)
delete_multiple_element(Cooked_TSF, TSF_Non_Filter)
delete_multiple_element(Charcoal_TSF, TSF_Non_Filter)
delete_multiple_element(Flour_In_TSF, TSF_Non_Filter)
delete_multiple_element(Stir_TSF, TSF_Non_Filter)
delete_multiple_element(Boil_TSF, TSF_Non_Filter)
delete_multiple_element(CE_Time_TSF, TSF_Non_Filter)

#for TSF_val in TSF_Non_Filter:
#    print('is the first loop for tstf working?  ', TSF_val, TSF_Filter)
    
#    Name_TSF.pop(TSF_val)
#    Wood_TSF.pop(TSF_val)
#    Cooked_TSF.pop(TSF_val)
#    Charcoal_TSF.pop(TSF_val)
#    Flour_In_TSF.pop(TSF_val)
#    Stir_TSF.pop(TSF_val)
#    Boil_TSF.pop(TSF_val)
#    CE_Time_TSF.pop(TSF_val)

# CQC Stove Matrix Partition
delete_multiple_element(Name_CQC, CQC_Non_Filter)
delete_multiple_element(Wood_CQC, CQC_Non_Filter)
delete_multiple_element(Cooked_CQC, CQC_Non_Filter)
delete_multiple_element(Charcoal_CQC, CQC_Non_Filter)
delete_multiple_element(Flour_In_CQC, CQC_Non_Filter)
delete_multiple_element(Stir_CQC, CQC_Non_Filter)
delete_multiple_element(Boil_CQC, CQC_Non_Filter)
delete_multiple_element(CE_Time_CQC, CQC_Non_Filter)

#for CQC_val in CQC_Non_Filter:
#    Name_CQC.pop(CQC_val)
#    Wood_CQC.pop(CQC_val)
#    Cooked_CQC.pop(CQC_val)
#    Charcoal_CQC.pop(CQC_val)
#    Flour_In_CQC.pop(CQC_val)
#    Stir_CQC.pop(CQC_val)
#    Boil_CQC.pop(CQC_val)
#    CE_Time_CQC.pop(CQC_val)
#    
# CQC with Jet Flame Matrix Partition
delete_multiple_element(Name_CQC_JFK, CQC_JFK_Non_Filter)
delete_multiple_element(Wood_CQC_JFK, CQC_JFK_Non_Filter)
delete_multiple_element(Cooked_CQC_JFK, CQC_JFK_Non_Filter)
delete_multiple_element(Charcoal_CQC_JFK, CQC_JFK_Non_Filter)
delete_multiple_element(Flour_In_CQC_JFK, CQC_JFK_Non_Filter)
delete_multiple_element(Stir_CQC_JFK, CQC_JFK_Non_Filter)
delete_multiple_element(Boil_CQC_JFK, CQC_JFK_Non_Filter)
delete_multiple_element(CE_Time_CQC_JFK, CQC_JFK_Non_Filter)


#for JFK_val in CQC_JFK_Non_Filter:
#    Name_CQC_JFK.pop(JFK_val)
#    Wood_CQC_JFK.pop(JFK_val)
#    Cooked_CQC_JFK.pop(JFK_val)
#    Charcoal_CQC_JFK.pop(JFK_val)
#    Flour_In_CQC_JFK.pop(JFK_val)
#    Stir_CQC_JFK.pop(JFK_val)
#    Boil_CQC_JFK.pop(JFK_val)
#    CE_Time_CQC_JFK.pop(JFK_val)


## Wood Savings

Wood_CQC = list(Wood_CQC)
Wood_CQC.remove(-1)


ax1 = plt.subplot()
plt.title('Wood Consumption')
plt.ylabel("Grams of wood") 
# TSF
plot_tsf_wood = plt.boxplot(Wood_TSF, positions=[1], widths = 0.6)
plt.text(1,0.1,'TSF',color='b')

Box_TSF_Wood = list(np.percentile(Wood_TSF, [25,50,75]))
Box_TSF_Wood.extend([np.average(Wood_TSF), len(Wood_TSF)])

# CQC
plot_cqc_wood = plt.boxplot(Wood_CQC, positions=[2], widths = 0.6)
plt.text(2,0.1,'CQC', color= 'g')

Box_CQC_Wood = list(np.percentile(Wood_CQC, [25,50,75]))
Box_CQC_Wood.extend([np.average(Wood_CQC), len(Wood_CQC)])
#JET Flame
plot_cqc_jfk_wood = plt.boxplot(Wood_CQC_JFK, positions = [3], widths = 0.6)
plt.text(3,0.1,'Jet Flame', color='r')  

Box_JFK_Wood = list(np.percentile(Wood_CQC_JFK, [25,50,75]))
Box_JFK_Wood.extend([np.average(Wood_CQC_JFK), len(Wood_CQC_JFK)])

plt.show()

# Tables for Wood Consumption
DF_Box_Wood_Consumtion = {'Percentile %': ['25','50','75', 'Avg', 'n'], 'TSF': Box_TSF_Wood, 'CQC': Box_CQC_Wood,'JFK' : Box_JFK_Wood}
Wood_CCT_Consumption = pd.DataFrame(data=DF_Box_Wood_Consumtion, columns=['Percentile %','TSF', 'CQC','JFK'] )
print('--------Wood Consumed-----------')
print(Wood_CCT_Consumption)
# Wood % Difference Between Stoves
Wood_percent_TSF_CQC = []
Wood_percent_TSF_JFK = []
Wood_percent_CQC_JFK = []
Box_TSF_Wood.pop(-1)
for vv, w in enumerate(Box_TSF_Wood):
    Wood_percent_TSF_CQC.append(int(((Box_CQC_Wood[vv])/w)*100))
    Wood_percent_TSF_JFK.append(int(((Box_JFK_Wood[vv])/w)*100))
    Wood_percent_CQC_JFK.append(int(((Box_JFK_Wood[vv])/(Box_CQC_Wood[vv]))*100))

DF_Percent_Box_Wood_Consumtion = {'Percentile %': ['25','50','75', 'Avg'], 'CQC/TSF %': Wood_percent_TSF_CQC, 'JFK/TSF %': Wood_percent_TSF_JFK,'JFK/CQC %' : Wood_percent_CQC_JFK}
Wood_Percent_CCT_Consumption = pd.DataFrame(data=DF_Percent_Box_Wood_Consumtion, columns=['Percentile %','CQC/TSF %', 'JFK/TSF %','JFK/CQC %'] )
print('% Difference Wood Consumed')
print(Wood_Percent_CCT_Consumption)

## Cooked Food
ax2 = plt.subplot()
plt.title('COOKED FOOD')
plt.ylabel("Grams of Sema") 
# TSF
PLOT_TSF_COOKED = plt.boxplot(Cooked_TSF, positions=[1], widths = 0.6)
plt.text(1,0.1,'TSF',color='b')

Box_TSF_Food = list(np.percentile(Cooked_TSF, [25,50,75]))
Box_TSF_Food.extend([np.average(Cooked_TSF), len(Cooked_TSF)])

#CQC
PLOT_CQC_COOKED = plt.boxplot(Cooked_CQC, positions=[2], widths = 0.6)
plt.text(2,0.1,'CQC', color= 'g')

Box_CQC_Food = list(np.percentile(Cooked_CQC, [25,50,75]))
Box_CQC_Food.extend([np.average(Cooked_CQC), len(Cooked_CQC)])

# JET Flame
PLOT_CQC_JFK_COOKED = plt.boxplot(Cooked_CQC_JFK, positions = [3], widths = 0.6)
plt.text(3,0.1,'JET FLAME', color='r')   

Box_JFK_Food = list(np.percentile(Cooked_CQC_JFK, [25,50,75]))
Box_JFK_Food.extend([np.average(Cooked_CQC_JFK), len(Cooked_CQC_JFK)])

plt.show()

#Tables for Food Consumption
DF_Box_Food_Consumtion = {'Percentile %': ['25','50','75', 'Avg', 'n'], 'TSF': Box_TSF_Food, 'CQC': Box_CQC_Food,'JFK' : Box_JFK_Food}
Food_CCT_Consumption = pd.DataFrame(data=DF_Box_Food_Consumtion, columns=['Percentile %','TSF', 'CQC','JFK'] )
print('-------Food Consumed--------')
print(Food_CCT_Consumption)
# Food % Difference Between Stoves
Food_TSF_CQC = []
Food_TSF_JFK = []
Food_CQC_JFK = []
Box_TSF_Food.pop(-1) # This is to remove the sample size from the box plots

for vv, f in enumerate(Box_TSF_Food):
    Food_TSF_CQC.append(int(((Box_CQC_Food[vv])/f)*100))
    Food_TSF_JFK.append(int(((Box_JFK_Food[vv])/f)*100))
    Food_CQC_JFK.append(int(((Box_JFK_Food[vv])/(Box_CQC_Food[vv]))*100))

DF_Percent_Box_Food_Consumtion = {'Percentile %': ['25','50','75', 'Avg'], 'CQC/TSF %': Food_TSF_CQC, 'JFK/TSF %': Food_TSF_JFK,'JFK/CQC %' : Food_CQC_JFK}
Food_Percent_CCT_Consumption = pd.DataFrame(data=DF_Percent_Box_Food_Consumtion, columns=['Percentile %','CQC/TSF %', 'JFK/TSF %','JFK/CQC %'] )
print('% Difference Food Consumed')
print(Food_Percent_CCT_Consumption)

## Charcaol
ax3 = plt.subplot()
plt.title('Hot Charcoal')
plt.ylabel("Grams of Charcaol") 
# TSF
PLOT_TSF_CHAR = plt.boxplot(Charcoal_TSF, positions=[1], widths = 0.6)
plt.text(1,0.1,'TSF',color='b')

Box_TSF_CHAR = list(np.percentile(Charcoal_TSF, [25,50,75]))
Box_TSF_CHAR.extend([np.average(Charcoal_TSF), len(Charcoal_TSF)])

# CQC
PLOT_CQC_CHAR = plt.boxplot(Charcoal_CQC, positions=[2], widths = 0.6)
plt.text(2,0.1,'CQC', color= 'g')

Box_CQC_CHAR = list(np.percentile(Charcoal_CQC, [25,50,75]))
Box_CQC_CHAR.extend([np.average(Charcoal_CQC), len(Charcoal_CQC)])

#Jet Flame
PLOT_CQC_JFK_CHAR = plt.boxplot(Charcoal_CQC_JFK, positions = [3], widths = 0.6)
plt.text(3,0.1,'JET FLAME', color='r')   

Box_JFK_CHAR = list(np.percentile(Charcoal_CQC_JFK, [25,50,75]))
Box_JFK_CHAR.extend([np.average(Charcoal_CQC_JFK), len(Charcoal_CQC_JFK)])

plt.show()

#Tables for Charcoal Consumption
DF_Box_CHAR_Consumtion = {'Percentile %': ['25','50','75', 'Avg', 'n'], 'TSF': Box_TSF_CHAR, 'CQC': Box_CQC_CHAR,'JFK' : Box_JFK_CHAR}
CHAR_CCT_Consumption = pd.DataFrame(data=DF_Box_CHAR_Consumtion, columns=['Percentile %','TSF', 'CQC','JFK'] )
print('-------Charcaol Consumed--------')
print(CHAR_CCT_Consumption)
# CHARCOAL % Difference Between Stoves
CHAR_TSF_CQC = []
CHAR_TSF_JFK = []
CHAR_CQC_JFK = []
Box_TSF_CHAR.pop(-1) # This is to remove the sample size from the box plots

for vv, C in enumerate(Box_TSF_CHAR):
    CHAR_TSF_CQC.append(int(((Box_CQC_CHAR[vv])/C)*100))
    CHAR_TSF_JFK.append(int(((Box_JFK_CHAR[vv])/C)*100))
    CHAR_CQC_JFK.append(int(((Box_JFK_CHAR[vv])/(Box_CQC_CHAR[vv]))*100))

DF_Percent_Box_CHAR_Consumtion = {'Percentile %': ['25','50','75', 'Avg'], 'CQC/TSF %': CHAR_TSF_CQC, 'JFK/TSF %': CHAR_TSF_JFK,'JFK/CQC %' : CHAR_CQC_JFK}
CHAR_Percent_CCT_Consumption = pd.DataFrame(data=DF_Percent_Box_CHAR_Consumtion, columns=['Percentile %','CQC/TSF %', 'JFK/TSF %','JFK/CQC %'] )
print('% Difference Charcaol Consumed')
print(CHAR_Percent_CCT_Consumption)


## BOIL
Boil_TSF = list(Boil_TSF)
Boil_TSF.remove(-1)

#print('CQC Stove ',Boil_CQC)
Boil_CQC = list(Boil_CQC)
Boil_CQC.remove(-1)
#print('CQC Stove Fter -1 filter',Boil_CQC)

# There is a wierd bug in this spectific section. No idea wha the bug is, no clue. 
# But in order to solve, Needed to manually solve and remove

Boil_CQC_JFK = list(Boil_CQC_JFK)
count = 0
for val, bb in enumerate(Boil_CQC_JFK):
    if bb < 0:
        count = count + 1 
        Boil_CQC_JFK.pop(val)
# had to change the values to -5 for Jet flame in order to track the wierd changes and bug
Boil_CQC_JFK.remove(-5) 
Boil_CQC_JFK.pop(8)

ax4 = plt.subplot()
plt.title('Time to Boil')
plt.ylabel("Minutes from Fire Start to Boil") 
# TSF
PLOT_TSF_BOIL = plt.boxplot(Boil_TSF, positions=[1], widths = 0.6)
plt.text(1,0.1,'TSF',color='b')

Box_TSF_BOIL = list(np.percentile(Boil_TSF, [25,50,75]))
Box_TSF_BOIL.extend([np.average(Boil_TSF), len(Boil_TSF)])

#CQC
PLOT_CQC_BOIL = plt.boxplot(Boil_CQC, positions=[2], widths = 0.6)
plt.text(2,0.1,'CQC', color= 'g')

Box_CQC_BOIL = list(np.percentile(Boil_CQC, [25,50,75]))
Box_CQC_BOIL.extend([np.average(Boil_CQC), len(Boil_CQC)])

#JET Flame
PLOT_CQC_JFK_BOIL = plt.boxplot(Boil_CQC_JFK, positions = [3], widths = 0.6)
plt.text(3,0.1,'JET FLAME', color='r')   

Box_JFK_BOIL = list(np.percentile(Boil_CQC_JFK, [25,50,75]))
Box_JFK_BOIL.extend([np.average(Boil_CQC_JFK), len(Boil_CQC_JFK)])

plt.show()

#Tables for Boil time
DF_Box_BOIL_Consumtion = {'Percentile %': ['25','50','75', 'Avg', 'n'], 'TSF': Box_TSF_BOIL, 'CQC': Box_CQC_BOIL,'JFK' : Box_JFK_BOIL}
BOIL_CCT_Consumption = pd.DataFrame(data=DF_Box_BOIL_Consumtion, columns=['Percentile %','TSF', 'CQC','JFK'] )
print('-------BOILING TIME--------')
print(BOIL_CCT_Consumption)
# CHARCOAL % Difference Between Stoves
BOIL_TSF_CQC = []
BOIL_TSF_JFK = []
BOIL_CQC_JFK = []
Box_TSF_BOIL.pop(-1) # This is to remove the sample size from the box plots

for vv, B in enumerate(Box_TSF_BOIL):
    BOIL_TSF_CQC.append(int(((Box_CQC_BOIL[vv])/B)*100))
    BOIL_TSF_JFK.append(int(((Box_JFK_BOIL[vv])/B)*100))
    BOIL_CQC_JFK.append(int(((Box_JFK_BOIL[vv])/(Box_CQC_BOIL[vv]))*100))

DF_Percent_Box_BOIL_Consumtion = {'Percentile %': ['25','50','75', 'Avg'], 'CQC/TSF %': BOIL_TSF_CQC, 'JFK/TSF %': BOIL_TSF_JFK,'JFK/CQC %' : BOIL_CQC_JFK}
BOIL_Percent_CCT_Consumption = pd.DataFrame(data=DF_Percent_Box_BOIL_Consumtion, columns=['Percentile %','CQC/TSF %', 'JFK/TSF %','JFK/CQC %'] )
print('% Difference BOILING TIME')
print(BOIL_Percent_CCT_Consumption)


### Total cooking time

ax5 = plt.subplot()
plt.title('Total Cooking Time')
plt.ylabel("Minutes from Fire Start to End") 
#JFK
PLOT_TSF_CE_LENGTH = plt.boxplot(CE_Time_TSF, positions=[1], widths = 0.6)
plt.text(1,0.1,'TSF',color='b')

Box_TSF_CE_TIME = list(np.percentile(CE_Time_TSF, [25,50,75]))
Box_TSF_CE_TIME.extend([np.average(CE_Time_TSF), len(CE_Time_TSF)])

#CQC
PLOT_CQC_CE_LENGTH = plt.boxplot(CE_Time_CQC, positions=[2], widths = 0.6)
plt.text(2,0.1,'CQC', color= 'g')

Box_CQC_CE_TIME = list(np.percentile(CE_Time_CQC, [25,50,75]))
Box_CQC_CE_TIME.extend([np.average(CE_Time_CQC), len(CE_Time_CQC)])

#JET FLAME
PLOT_CQC_JFK_CE_LENGTH = plt.boxplot(CE_Time_CQC_JFK, positions = [3], widths = 0.6)
plt.text(3,0.1,'JET FLAME', color='r')   

Box_JFK_CE_TIME = list(np.percentile(CE_Time_CQC_JFK, [25,50,75]))
Box_JFK_CE_TIME.extend([np.average(CE_Time_CQC_JFK), len(CE_Time_CQC_JFK)])

plt.show()


#Tables for total cooking time
DF_Box_CE_LENGTH_Consumtion = {'Percentile %': ['25','50','75', 'Avg', 'n'], 'TSF': Box_TSF_CE_TIME, 'CQC': Box_CQC_CE_TIME,'JFK' : Box_JFK_CE_TIME}
CE_TIME_CCT_Consumption = pd.DataFrame(data=DF_Box_CE_LENGTH_Consumtion, columns=['Percentile %','TSF', 'CQC','JFK'] )
print('-------COOKING TIME-------')
print(CE_TIME_CCT_Consumption)
# CHARCOAL % Difference Between Stoves
CE_TIME_TSF_CQC = []
CE_TIME_TSF_JFK = []
CE_TIME_CQC_JFK = []
Box_TSF_CE_TIME.pop(-1) # This is to remove the sample size from the box plots

for vv, T in enumerate(Box_TSF_CE_TIME):
    CE_TIME_TSF_CQC.append(int(((Box_CQC_CE_TIME[vv])/T)*100))
    CE_TIME_TSF_JFK.append(int(((Box_JFK_CE_TIME[vv])/T)*100))
    CE_TIME_CQC_JFK.append(int(((Box_JFK_CE_TIME[vv])/(Box_CQC_CE_TIME[vv]))*100))

DF_Percent_Box_CE_TIME_Consumtion = {'Percentile %': ['25','50','75', 'Avg'], 'CQC/TSF %': CE_TIME_TSF_CQC, 'JFK/TSF %': CE_TIME_TSF_JFK,'JFK/CQC %' : CE_TIME_CQC_JFK}
CE_TIME_Percent_CCT_Consumption = pd.DataFrame(data=DF_Percent_Box_CE_TIME_Consumtion, columns=['Percentile %','CQC/TSF %', 'JFK/TSF %','JFK/CQC %'] )
print('% Difference COOKING TIME')
print(CE_TIME_Percent_CCT_Consumption)

###Stirr in Flour


Flour_In_CQC_JFK.remove(-1)

ax6 = plt.subplot()
plt.title('Time for First Flour')
plt.ylabel("Minutes from Fire Start to Sema in") 
#JFK
PLOT_TSF_Flour_LENGTH = plt.boxplot(Flour_In_TSF, positions=[1], widths = 0.6)
plt.text(1,0.1,'TSF',color='b')

Box_TSF_flour= list(np.percentile(Flour_In_TSF, [25,50,75]))
Box_TSF_flour.extend([np.average(Flour_In_TSF), len(Flour_In_TSF)])

#CQC
PLOT_CQC_Flour = plt.boxplot(Flour_In_CQC, positions=[2], widths = 0.6)
plt.text(2,0.1,'CQC', color= 'g')

Box_CQC_Flour = list(np.percentile(Flour_In_CQC, [25,50,75]))
Box_CQC_Flour.extend([np.average(Flour_In_CQC), len(Flour_In_CQC)])

#JET FLAME
PLOT_CQC_JFK_CE_LENGTH = plt.boxplot(Flour_In_CQC_JFK, positions = [3], widths = 0.6)
plt.text(3,0.1,'JET FLAME', color='r')   

Box_JFK_Flour = list(np.percentile(Flour_In_CQC_JFK, [25,50,75]))
Box_JFK_Flour.extend([np.average(Flour_In_CQC_JFK), len(Flour_In_CQC_JFK)])

plt.show()


#Tables for flour in 
DF_Box_Flour_Consumtion = {'Percentile %': ['25','50','75', 'Avg', 'n'], 'TSF': Box_TSF_flour, 'CQC': Box_CQC_Flour,'JFK' : Box_JFK_Flour}
Flour_CCT_Consumption = pd.DataFrame(data=DF_Box_Flour_Consumtion, columns=['Percentile %','TSF', 'CQC','JFK'] )
print('-------Time Until Flour in -------')
print(Flour_CCT_Consumption)
# CHARCOAL % Difference Between Stoves
Flour_TSF_CQC = []
Flour_TSF_JFK = []
Flour_CQC_JFK = []
Box_TSF_flour.pop(-1) # This is to remove the sample size from the box plots

for vv, F in enumerate(Box_TSF_flour):
    Flour_TSF_CQC.append(int(((Box_CQC_Flour[vv])/F)*100))
    Flour_TSF_JFK.append(int(((Box_JFK_Flour[vv])/F)*100))
    Flour_CQC_JFK.append(int(((Box_JFK_Flour[vv])/(Box_CQC_Flour[vv]))*100))

DF_Percent_Box_Flour_Consumtion = {'Percentile %': ['25','50','75', 'Avg'], 'CQC/TSF %': Flour_TSF_CQC, 'JFK/TSF %': Flour_TSF_JFK,'JFK/CQC %' : Flour_CQC_JFK}
Flour_Percent_CCT_Consumption = pd.DataFrame(data=DF_Percent_Box_Flour_Consumtion, columns=['Percentile %','CQC/TSF %', 'JFK/TSF %','JFK/CQC %'] )
print('% Difference for Putting in FLour')
print(Flour_Percent_CCT_Consumption)


# Next section is to compare each household summary and instead of averages and medians
# TSF Household breakdown
TSF_Filter_HH = []
HH_1_TSF_Wood = []; HH_1_TSF_Char = []; HH_1_TSF_Cooked = []; HH_1_TSF_Boil = []; HH_1_TSF_CE_Time = []; HH_1_TSF_Flour= []
HH_2_TSF_Wood = []; HH_2_TSF_Char = []; HH_2_TSF_Cooked = []; HH_2_TSF_Boil = []; HH_2_TSF_CE_Time = []; HH_2_TSF_Flour= []
HH_3_TSF_Wood = []; HH_3_TSF_Char = []; HH_3_TSF_Cooked = []; HH_3_TSF_Boil = []; HH_3_TSF_CE_Time = []; HH_3_TSF_Flour= []
HH_4_TSF_Wood = []; HH_4_TSF_Char = []; HH_4_TSF_Cooked = []; HH_4_TSF_Boil = []; HH_4_TSF_CE_Time = []; HH_4_TSF_Flour= []
HH_5_TSF_Wood = []; HH_5_TSF_Char = []; HH_5_TSF_Cooked = []; HH_5_TSF_Boil = []; HH_5_TSF_CE_Time = []; HH_5_TSF_Flour= []
HH_6_TSF_Wood = []; HH_6_TSF_Char = []; HH_6_TSF_Cooked = []; HH_6_TSF_Boil = []; HH_6_TSF_CE_Time = []; HH_6_TSF_Flour= []


for tl, hh_TSF in enumerate(Name_TSF):
    HH_count = 0
    for letter in hh_TSF:
        if HH_count == 2 and tl <= len(Boil_TSF)-1 and tl <= len(CE_Time_TSF)-1:
            TSF_Filter_HH.append(letter)
            if letter == '1':
                HH_1_TSF_Wood.append(Wood_TSF[tl])
                HH_1_TSF_Char.append(Charcoal_TSF[tl])
                HH_1_TSF_Cooked.append(Cooked_TSF[tl])
                HH_1_TSF_Boil.append(Boil_TSF[tl])
                HH_1_TSF_CE_Time.append(CE_Time_TSF[tl])
                HH_1_TSF_Flour.append(Flour_In_TSF[tl])
            elif letter == '2':
                HH_2_TSF_Wood.append(Wood_TSF[tl])
                HH_2_TSF_Char.append(Charcoal_TSF[tl])
                HH_2_TSF_Cooked.append(Cooked_TSF[tl])
                HH_2_TSF_Boil.append(Boil_TSF[tl])
                HH_2_TSF_CE_Time.append(CE_Time_TSF[tl])
                HH_2_TSF_Flour.append(Flour_In_TSF[tl])
            elif letter == '3':
                HH_3_TSF_Wood.append(Wood_TSF[tl])
                HH_3_TSF_Char.append(Charcoal_TSF[tl])
                HH_3_TSF_Cooked.append(Cooked_TSF[tl])
                HH_3_TSF_Boil.append(Boil_TSF[tl])
                HH_3_TSF_CE_Time.append(CE_Time_TSF[tl])
                HH_3_TSF_Flour.append(Flour_In_TSF[tl])
            elif letter == '4':
                HH_4_TSF_Wood.append(Wood_TSF[tl])
                HH_4_TSF_Char.append(Charcoal_TSF[tl])
                HH_4_TSF_Cooked.append(Cooked_TSF[tl])
                HH_4_TSF_Boil.append(Boil_TSF[tl])
                HH_4_TSF_CE_Time.append(CE_Time_TSF[tl])
                HH_4_TSF_Flour.append(Flour_In_TSF[tl])
            elif letter == '5':
                HH_5_TSF_Wood.append(Wood_TSF[tl])
                HH_5_TSF_Char.append(Charcoal_TSF[tl])
                HH_5_TSF_Cooked.append(Cooked_TSF[tl])
                HH_5_TSF_Boil.append(Boil_TSF[tl])
                HH_5_TSF_CE_Time.append(CE_Time_TSF[tl])
                HH_5_TSF_Flour.append(Flour_In_TSF[tl])
            elif letter == '6':
                HH_6_TSF_Wood.append(Wood_TSF[tl])
                HH_6_TSF_Char.append(Charcoal_TSF[tl])
                HH_6_TSF_Cooked.append(Cooked_TSF[tl])
                HH_6_TSF_Boil.append(Boil_TSF[tl])
                HH_6_TSF_CE_Time.append(CE_Time_TSF[tl])
                HH_6_TSF_Flour.append(Flour_In_TSF[tl])
                
        HH_count = HH_count + 1


# CQC Household breakdown
CQC_Filter_HH = []
HH_1_CQC_Wood = []; HH_1_CQC_Char = []; HH_1_CQC_Cooked = []; HH_1_CQC_Boil = []; HH_1_CQC_CE_Time = []; HH_1_CQC_Flour= []
HH_2_CQC_Wood = []; HH_2_CQC_Char = []; HH_2_CQC_Cooked = []; HH_2_CQC_Boil = []; HH_2_CQC_CE_Time = []; HH_2_CQC_Flour= []
HH_3_CQC_Wood = []; HH_3_CQC_Char = []; HH_3_CQC_Cooked = []; HH_3_CQC_Boil = []; HH_3_CQC_CE_Time = []; HH_3_CQC_Flour= []
HH_4_CQC_Wood = []; HH_4_CQC_Char = []; HH_4_CQC_Cooked = []; HH_4_CQC_Boil = []; HH_4_CQC_CE_Time = []; HH_4_CQC_Flour= []
HH_5_CQC_Wood = []; HH_5_CQC_Char = []; HH_5_CQC_Cooked = []; HH_5_CQC_Boil = []; HH_5_CQC_CE_Time = []; HH_5_CQC_Flour= []
HH_6_CQC_Wood = []; HH_6_CQC_Char = []; HH_6_CQC_Cooked = []; HH_6_CQC_Boil = []; HH_6_CQC_CE_Time = []; HH_6_CQC_Flour= []


for tl, hh_CQC in enumerate(Name_CQC):
    HH_count = 0
    for letter in hh_CQC:
        if HH_count == 2 and tl <= len(Boil_CQC)-1 and tl <= len(CE_Time_CQC)-1:
            CQC_Filter_HH.append(letter)
            if letter == '1':
                HH_1_CQC_Wood.append(Wood_CQC[tl])
                HH_1_CQC_Char.append(Charcoal_CQC[tl])
                HH_1_CQC_Cooked.append(Cooked_CQC[tl])
                HH_1_CQC_Boil.append(Boil_CQC[tl])
                HH_1_CQC_CE_Time.append(CE_Time_CQC[tl])
                HH_1_CQC_Flour.append(Flour_In_CQC[tl])
            elif letter == '2':
                HH_2_CQC_Wood.append(Wood_CQC[tl])
                HH_2_CQC_Char.append(Charcoal_CQC[tl])
                HH_2_CQC_Cooked.append(Cooked_CQC[tl])
                HH_2_CQC_Boil.append(Boil_CQC[tl])
                HH_2_CQC_CE_Time.append(CE_Time_CQC[tl])
                HH_2_CQC_Flour.append(Flour_In_CQC[tl])
            elif letter == '3':
                HH_3_CQC_Wood.append(Wood_CQC[tl])
                HH_3_CQC_Char.append(Charcoal_CQC[tl])
                HH_3_CQC_Cooked.append(Cooked_CQC[tl])
                HH_3_CQC_Boil.append(Boil_CQC[tl])
                HH_3_CQC_CE_Time.append(CE_Time_CQC[tl])
                HH_3_CQC_Flour.append(Flour_In_CQC[tl])
            elif letter == '4':
                HH_4_CQC_Wood.append(Wood_CQC[tl])
                HH_4_CQC_Char.append(Charcoal_CQC[tl])
                HH_4_CQC_Cooked.append(Cooked_CQC[tl])
                HH_4_CQC_Boil.append(Boil_CQC[tl])
                HH_4_CQC_CE_Time.append(CE_Time_CQC[tl])
                HH_4_CQC_Flour.append(Flour_In_CQC[tl])
            elif letter == '5':
                HH_5_CQC_Wood.append(Wood_CQC[tl])
                HH_5_CQC_Char.append(Charcoal_CQC[tl])
                HH_5_CQC_Cooked.append(Cooked_CQC[tl])
                HH_5_CQC_Boil.append(Boil_CQC[tl])
                HH_5_CQC_CE_Time.append(CE_Time_CQC[tl])
                HH_5_CQC_Flour.append(Flour_In_CQC[tl])
            elif letter == '6':
                HH_6_CQC_Wood.append(Wood_CQC[tl])
                HH_6_CQC_Char.append(Charcoal_CQC[tl])
                HH_6_CQC_Cooked.append(Cooked_CQC[tl])
                HH_6_CQC_Boil.append(Boil_CQC[tl])
                HH_6_CQC_CE_Time.append(CE_Time_CQC[tl])
                HH_6_CQC_Flour.append(Flour_In_CQC[tl])
                
        HH_count = HH_count + 1


# JFK Household breakdown
JFK_Filter_HH = []
HH_1_JFK_Wood = []; HH_1_JFK_Char = []; HH_1_JFK_Cooked = []; HH_1_JFK_Boil = []; HH_1_JFK_CE_Time = []; HH_1_JFK_Flour= []
HH_2_JFK_Wood = []; HH_2_JFK_Char = []; HH_2_JFK_Cooked = []; HH_2_JFK_Boil = []; HH_2_JFK_CE_Time = []; HH_2_JFK_Flour= []
HH_3_JFK_Wood = []; HH_3_JFK_Char = []; HH_3_JFK_Cooked = []; HH_3_JFK_Boil = []; HH_3_JFK_CE_Time = []; HH_3_JFK_Flour= []
HH_4_JFK_Wood = []; HH_4_JFK_Char = []; HH_4_JFK_Cooked = []; HH_4_JFK_Boil = []; HH_4_JFK_CE_Time = []; HH_4_JFK_Flour= []
HH_5_JFK_Wood = []; HH_5_JFK_Char = []; HH_5_JFK_Cooked = []; HH_5_JFK_Boil = []; HH_5_JFK_CE_Time = []; HH_5_JFK_Flour= []
HH_6_JFK_Wood = []; HH_6_JFK_Char = []; HH_6_JFK_Cooked = []; HH_6_JFK_Boil = []; HH_6_JFK_CE_Time = []; HH_6_JFK_Flour= []

print('name for Jet flame' ,Name_CQC_JFK,  CE_Time_CQC_JFK)
for tl, hh_JFK in enumerate(Name_CQC_JFK):
    HH_count = 0
    for letter in hh_JFK:
        if HH_count == 2 and tl <= len(Boil_CQC_JFK)-1 :#and tl <= len(CE_Time_CQC_JFK)-1 and tl <= len(Flour_In_CQC_JFK)-1 and tl <= len(Wood_CQC_JFK)-1:
            JFK_Filter_HH.append(letter)
            print('at 6?????',letter)
            if letter == '1':
                HH_1_JFK_Wood.append(Wood_CQC_JFK[tl])
                HH_1_JFK_Char.append(Charcoal_CQC_JFK[tl])
                HH_1_JFK_Cooked.append(Cooked_CQC_JFK[tl])
                HH_1_JFK_Boil.append(Boil_CQC_JFK[tl])
                HH_1_JFK_CE_Time.append(CE_Time_CQC_JFK[tl])
                HH_1_JFK_Flour.append(Flour_In_CQC_JFK[tl])
            elif letter == '2':
                HH_2_JFK_Wood.append(Wood_CQC_JFK[tl])
                HH_2_JFK_Char.append(Charcoal_CQC_JFK[tl])
                HH_2_JFK_Cooked.append(Cooked_CQC_JFK[tl])
                HH_2_JFK_Boil.append(Boil_CQC_JFK[tl])
                HH_2_JFK_CE_Time.append(CE_Time_CQC_JFK[tl])
                HH_2_JFK_Flour.append(Flour_In_CQC_JFK[tl])
            elif letter == '3':
                HH_3_JFK_Wood.append(Wood_CQC_JFK[tl])
                HH_3_JFK_Char.append(Charcoal_CQC_JFK[tl])
                HH_3_JFK_Cooked.append(Cooked_CQC_JFK[tl])
                HH_3_JFK_Boil.append(Boil_CQC_JFK[tl])
                HH_3_JFK_CE_Time.append(CE_Time_CQC_JFK[tl])
                HH_3_JFK_Flour.append(Flour_In_CQC_JFK[tl])
            elif letter == '4':
                HH_4_JFK_Wood.append(Wood_CQC_JFK[tl])
                HH_4_JFK_Char.append(Charcoal_CQC_JFK[tl])
                HH_4_JFK_Cooked.append(Cooked_CQC_JFK[tl])
                HH_4_JFK_Boil.append(Boil_CQC_JFK[tl])
                HH_4_JFK_CE_Time.append(CE_Time_CQC_JFK[tl])
                HH_4_JFK_Flour.append(Flour_In_CQC_JFK[tl])
            elif letter == '5':
                HH_5_JFK_Wood.append(Wood_CQC_JFK[tl])
                HH_5_JFK_Char.append(Charcoal_CQC_JFK[tl])
                HH_5_JFK_Cooked.append(Cooked_CQC_JFK[tl])
                HH_5_JFK_Boil.append(Boil_CQC_JFK[tl])
                HH_5_JFK_CE_Time.append(CE_Time_CQC_JFK[tl])
                HH_5_JFK_Flour.append(Flour_In_CQC_JFK[tl])
            elif letter == '6':
                HH_6_JFK_Wood.append(Wood_CQC_JFK[tl])
                HH_6_JFK_Char.append(Charcoal_CQC_JFK[tl])
                HH_6_JFK_Cooked.append(Cooked_CQC_JFK[tl])
                HH_6_JFK_Boil.append(Boil_CQC_JFK[tl])
                HH_6_JFK_CE_Time.append(CE_Time_CQC_JFK[tl])
                HH_6_JFK_Flour.append(Flour_In_CQC_JFK[tl])
                
        HH_count = HH_count + 1

print('cooking time array for JFK',CE_Time_CQC_JFK,'boil time fopr tsf', Boil_CQC_JFK)
# Three stone Fire HH== Breakdown
print(HH_6_JFK_CE_Time)
DF_Household_Compiler_TSF = {'Household-TSF':['HH1', 'HH2','HH3', 'HH4', 'HH5','HH6'], 'Average Wood Used': [np.average(HH_1_JFK_Wood), np.average(HH_2_JFK_Wood),
                         np.average(HH_3_JFK_Wood),np.average(HH_4_JFK_Wood),np.average(HH_5_JFK_Wood), np.average(HH_6_JFK_Wood)],
                            'STEV.P Wood Used':[np.std(HH_1_JFK_Wood),np.std(HH_2_JFK_Wood), np.std(HH_3_JFK_Wood),np.std(HH_4_JFK_Wood),np.std(HH_5_JFK_Wood), np.std(HH_6_JFK_Wood)],
                            'Average Char Used': [np.average(HH_1_TSF_Char),np.average(HH_2_TSF_Char), np.average(HH_3_TSF_Char),np.average(HH_4_TSF_Char),np.average(HH_5_TSF_Char), np.average(HH_6_TSF_Char)],
                            'STEV.P Char Used':[np.std(HH_1_TSF_Char), np.std(HH_2_TSF_Char), np.std(HH_3_TSF_Char),np.std(HH_4_TSF_Char),np.std(HH_5_TSF_Char), np.std(HH_6_TSF_Char)],
                            'Average Food Cooked': [np.average(HH_1_TSF_Cooked),np.average(HH_2_TSF_Cooked), np.average(HH_3_TSF_Cooked),np.average(HH_4_TSF_Cooked),np.average(HH_5_TSF_Cooked), np.average(HH_6_TSF_Cooked)],
                            'STEV.P Food Cooked':[np.std(HH_1_TSF_Cooked), np.std(HH_2_TSF_Cooked), np.std(HH_3_TSF_Cooked),np.std(HH_4_TSF_Cooked),np.std(HH_5_TSF_Cooked), np.std(HH_6_TSF_Cooked)],
                            'Average Time for Flour in (min)': [np.average(HH_1_TSF_Flour),np.average(HH_2_TSF_Flour), np.average(HH_3_TSF_Flour),np.average(HH_4_TSF_Flour),np.average(HH_5_TSF_Flour), np.average(HH_6_TSF_Flour)],
                            'STEV.P Time for Flour in (min)':[np.std(HH_1_TSF_Flour), np.std(HH_2_TSF_Flour), np.std(HH_3_TSF_Flour),np.std(HH_4_TSF_Flour),np.std(HH_5_TSF_Flour), np.std(HH_6_TSF_Flour)],
                            'Average Time until boiling (min)': [np.average(HH_1_TSF_Boil),np.average(HH_2_TSF_Boil), np.average(HH_3_TSF_Boil),np.average(HH_4_TSF_Boil),np.average(HH_5_TSF_Boil), np.average(HH_6_TSF_Boil)],
                            'STEV.P Time until boiling (min)':[np.std(HH_1_TSF_Boil), np.std(HH_2_TSF_Boil), np.std(HH_3_TSF_Boil),np.std(HH_4_TSF_Boil),np.std(HH_5_TSF_Boil), np.std(HH_6_TSF_Boil)],
                            'Average Time Cooking (min)': [np.average(HH_1_TSF_CE_Time),np.average(HH_2_TSF_CE_Time), np.average(HH_3_TSF_CE_Time),np.average(HH_4_TSF_CE_Time),np.average(HH_5_TSF_CE_Time), np.average(HH_6_TSF_CE_Time)],
                            'STEV.P Time Cooking (min)':[np.std(HH_1_TSF_CE_Time), np.std(HH_2_TSF_CE_Time), np.std(HH_3_TSF_CE_Time),np.std(HH_4_TSF_CE_Time),np.std(HH_5_TSF_CE_Time), np.std(HH_6_TSF_CE_Time)]}
Household_TSF_CCT_Consumption = pd.DataFrame(data=DF_Household_Compiler_TSF, columns=['Household-TSF','Average Wood Used', 'STEV.P Wood Used','Average Char Used', 'STEV.P Char Used', 'Average Food Cooked','STEV.P Food Cooked',
                                                                                      'Average Time for Flour in (min)', 'STEV.P Time for Flour in (min)','Average Time until boiling (min)', 'STEV.P Time until boiling (min)',
                                                                                      'Average Time Cooking (min)','STEV.P Time Cooking (min)'] )
print(Household_TSF_CCT_Consumption)


# CQC HH== Breakdown
print(np.std(HH_1_CQC_Wood),HH_1_CQC_Wood)
DF_Household_Compiler_CQC = {'Household-CQC':['HH1', 'HH2','HH3', 'HH4', 'HH5','HH6'], 'Average Wood Used': [np.average(HH_1_CQC_Wood), np.average(HH_2_CQC_Wood),
                         np.average(HH_3_CQC_Wood),np.average(HH_4_CQC_Wood),np.average(HH_5_CQC_Wood), np.average(HH_6_CQC_Wood)],
                            'STEV.P Wood Used':[np.std(HH_1_CQC_Wood),np.std(HH_2_CQC_Wood), np.std(HH_3_CQC_Wood),np.std(HH_4_CQC_Wood),np.std(HH_5_CQC_Wood), np.std(HH_6_CQC_Wood)],
                            'Average Char Used': [np.average(HH_1_CQC_Char),np.average(HH_2_CQC_Char), np.average(HH_3_CQC_Char),np.average(HH_4_CQC_Char),np.average(HH_5_CQC_Char), np.average(HH_6_CQC_Char)],
                            'STEV.P Char Used':[np.std(HH_1_CQC_Char), np.std(HH_2_CQC_Char), np.std(HH_3_CQC_Char),np.std(HH_4_CQC_Char),np.std(HH_5_CQC_Char), np.std(HH_6_CQC_Char)],
                            'Average Food Cooked': [np.average(HH_1_CQC_Cooked),np.average(HH_2_CQC_Cooked), np.average(HH_3_CQC_Cooked),np.average(HH_4_CQC_Cooked),np.average(HH_5_CQC_Cooked), np.average(HH_6_CQC_Cooked)],
                            'STEV.P Food Cooked':[np.std(HH_1_CQC_Cooked), np.std(HH_2_CQC_Cooked), np.std(HH_3_CQC_Cooked),np.std(HH_4_CQC_Cooked),np.std(HH_5_CQC_Cooked), np.std(HH_6_CQC_Cooked)],
                            'Average Time for Flour in (min)': [np.average(HH_1_CQC_Flour),np.average(HH_2_CQC_Flour), np.average(HH_3_CQC_Flour),np.average(HH_4_CQC_Flour),np.average(HH_5_CQC_Flour), np.average(HH_6_CQC_Flour)],
                            'STEV.P Time for Flour in (min)':[np.std(HH_1_CQC_Flour), np.std(HH_2_CQC_Flour), np.std(HH_3_CQC_Flour),np.std(HH_4_CQC_Flour),np.std(HH_5_CQC_Flour), np.std(HH_6_CQC_Flour)],
                            'Average Time until boiling (min)': [np.average(HH_1_CQC_Boil),np.average(HH_2_CQC_Boil), np.average(HH_3_CQC_Boil),np.average(HH_4_CQC_Boil),np.average(HH_5_CQC_Boil), np.average(HH_6_CQC_Boil)],
                            'STEV.P Time until boiling (min)':[np.std(HH_1_CQC_Boil), np.std(HH_2_CQC_Boil), np.std(HH_3_CQC_Boil),np.std(HH_4_CQC_Boil),np.std(HH_5_CQC_Boil), np.std(HH_6_CQC_Boil)],
                            'Average Time Cooking (min)': [np.average(HH_1_CQC_CE_Time),np.average(HH_2_CQC_CE_Time), np.average(HH_3_CQC_CE_Time),np.average(HH_4_CQC_CE_Time),np.average(HH_5_CQC_CE_Time), np.average(HH_6_CQC_CE_Time)],
                            'STEV.P Time Cooking (min)':[np.std(HH_1_CQC_CE_Time), np.std(HH_2_CQC_CE_Time), np.std(HH_3_CQC_CE_Time),np.std(HH_4_CQC_CE_Time),np.std(HH_5_CQC_CE_Time), np.std(HH_6_CQC_CE_Time)]}
Household_CQC_CCT_Consumption = pd.DataFrame(data=DF_Household_Compiler_CQC, columns=['Household-CQC','Average Wood Used', 'STEV.P Wood Used','Average Char Used', 'STEV.P Char Used', 'Average Food Cooked','STEV.P Food Cooked',
                                                                                      'Average Time for Flour in (min)', 'STEV.P Time for Flour in (min)','Average Time until boiling (min)', 'STEV.P Time until boiling (min)',
                                                                                      'Average Time Cooking (min)','STEV.P Time Cooking (min)'] )
print(Household_CQC_CCT_Consumption)

#JKF HH== Breakdown
print(np.std(HH_1_JFK_Wood),HH_1_JFK_Wood)
DF_Household_Compiler_JFK = {'Household-JFK':['HH1', 'HH2','HH3', 'HH4', 'HH5','HH6'], 'Average Wood Used': [np.average(HH_1_JFK_Wood), np.average(HH_2_JFK_Wood),
                         np.average(HH_3_JFK_Wood),np.average(HH_4_JFK_Wood),np.average(HH_5_JFK_Wood), np.average(HH_6_JFK_Wood)],
                            'STEV.P Wood Used':[np.std(HH_1_JFK_Wood),np.std(HH_2_JFK_Wood), np.std(HH_3_JFK_Wood),np.std(HH_4_JFK_Wood),np.std(HH_5_JFK_Wood), np.std(HH_6_JFK_Wood)],
                            'Average Char Used': [np.average(HH_1_JFK_Char),np.average(HH_2_JFK_Char), np.average(HH_3_JFK_Char),np.average(HH_4_JFK_Char),np.average(HH_5_JFK_Char), np.average(HH_6_JFK_Char)],
                            'STEV.P Char Used':[np.std(HH_1_JFK_Char), np.std(HH_2_JFK_Char), np.std(HH_3_JFK_Char),np.std(HH_4_JFK_Char),np.std(HH_5_JFK_Char), np.std(HH_6_JFK_Char)],
                            'Average Food Cooked': [np.average(HH_1_JFK_Cooked),np.average(HH_2_JFK_Cooked), np.average(HH_3_JFK_Cooked),np.average(HH_4_JFK_Cooked),np.average(HH_5_JFK_Cooked), np.average(HH_6_JFK_Cooked)],
                            'STEV.P Food Cooked':[np.std(HH_1_JFK_Cooked), np.std(HH_2_JFK_Cooked), np.std(HH_3_JFK_Cooked),np.std(HH_4_JFK_Cooked),np.std(HH_5_JFK_Cooked), np.std(HH_6_JFK_Cooked)],
                            'Average Time for Flour in (min)': [np.average(HH_1_JFK_Flour),np.average(HH_2_JFK_Flour), np.average(HH_3_JFK_Flour),np.average(HH_4_JFK_Flour),np.average(HH_5_JFK_Flour), np.average(HH_6_JFK_Flour)],
                            'STEV.P Time for Flour in (min)':[np.std(HH_1_JFK_Flour), np.std(HH_2_JFK_Flour), np.std(HH_3_JFK_Flour),np.std(HH_4_JFK_Flour),np.std(HH_5_JFK_Flour), np.std(HH_6_JFK_Flour)],
                            'Average Time until boiling (min)': [np.average(HH_1_JFK_Boil),np.average(HH_2_JFK_Boil), np.average(HH_3_JFK_Boil),np.average(HH_4_JFK_Boil),np.average(HH_5_JFK_Boil), np.average(HH_6_JFK_Boil)],
                            'STEV.P Time until boiling (min)':[np.std(HH_1_JFK_Boil), np.std(HH_2_JFK_Boil), np.std(HH_3_JFK_Boil),np.std(HH_4_JFK_Boil),np.std(HH_5_JFK_Boil), np.std(HH_6_JFK_Boil)],
                            'Average Time Cooking (min)': [np.average(HH_1_JFK_CE_Time),np.average(HH_2_JFK_CE_Time), np.average(HH_3_JFK_CE_Time),np.average(HH_4_JFK_CE_Time),np.average(HH_5_JFK_CE_Time), np.average(HH_6_JFK_CE_Time)],
                            'STEV.P Time Cooking (min)':[np.std(HH_1_JFK_CE_Time), np.std(HH_2_JFK_CE_Time), np.std(HH_3_JFK_CE_Time),np.std(HH_4_JFK_CE_Time),np.std(HH_5_JFK_CE_Time), np.std(HH_6_JFK_CE_Time)]}
Household_JFK_CCT_Consumption = pd.DataFrame(data=DF_Household_Compiler_JFK, columns=['Household-JFK','Average Wood Used', 'STEV.P Wood Used','Average Char Used', 'STEV.P Char Used', 'Average Food Cooked','STEV.P Food Cooked',
                                                                                      'Average Time for Flour in (min)', 'STEV.P Time for Flour in (min)','Average Time until boiling (min)', 'STEV.P Time until boiling (min)',
                                                                                      'Average Time Cooking (min)','STEV.P Time Cooking (min)'] )
print(Household_JFK_CCT_Consumption)

print('cooking time array',CE_Time_CQC_JFK )

Path_export = USB+":/HOUSEHOLD_CCT_COMPILER.csv"

CE_TIME_CCT_Consumption.to_csv(Path_export, index=False, mode='a')
CE_TIME_Percent_CCT_Consumption.to_csv(Path_export, index=False, mode='a')
#Household_JFK_CCT_Consumption.to_csv(Path_export, index=False, mode='a')







