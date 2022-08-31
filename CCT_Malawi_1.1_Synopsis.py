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

Source = 'laptop'  # 'work' or 'laptop'

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
Name_TSF = TSF['Household and Test']
Wood_TSF = TSF['Wood Used'];Cooked_TSF = TSF['Cooked Food'];Charcoal_TSF = TSF['Hot Charcoal'];Flour_In_TSF = TSF['Start to Flour in']
Stir_TSF = TSF['Start to Stir'];Boil_TSF = TSF['Start to Boil'];CE_Time_TSF = TSF['Cooking Time']

for TSF_Row, TSF in enumerate(TSF['Flour Used']):
    if TSF == 1300:
        TSF_Filter.append(TSF_Row)
    else:
        TSF_Non_Filter.append(TSF_Row)
        
CQC_Filter = []
CQC_Non_Filter = []
Name_CQC = CQC['Household and Test']
Wood_CQC = CQC['Wood Used'];Cooked_CQC = CQC['Cooked Food'];Charcoal_CQC = CQC['Hot Charcoal'];Flour_In_CQC = CQC['Start to Flour in']
Stir_CQC = CQC['Start to Stir'];Boil_CQC = CQC['Start to Boil'];CE_Time_CQC = CQC['Cooking Time']

for CQC_Row, CQC in enumerate(CQC['Flour Used']):
    if CQC == 1300:
        CQC_Filter.append(CQC_Row)
    else:
        CQC_Non_Filter.append(CQC_Row)
        
CQC_JFK_Filter = []
CQC_JFK_Non_Filter = []
Name_CQC_JFK = CQC_JFK['Household and Test'];
Wood_CQC_JFK = CQC_JFK['Wood Used'];Cooked_CQC_JFK = CQC_JFK['Cooked Food'];Charcoal_CQC_JFK = CQC_JFK['Hot Charcoal']
Flour_In_CQC_JFK = CQC_JFK['Start to Flour in'];Stir_CQC_JFK = CQC_JFK['Start to Stir'];Boil_CQC_JFK = CQC_JFK['Start to Boil']
CE_Time_CQC_JFK = CQC_JFK['Cooking Time']

for CQC_JFK_Row, CQC_JFK in enumerate(CQC_JFK['Flour Used']):
    if CQC_JFK == 1300:
        CQC_JFK_Filter.append(CQC_JFK_Row)
    else:
        CQC_JFK_Non_Filter.append(CQC_JFK_Row)



# Three stone Fire Baseline Matrix Partition

for TSF_val in TSF_Non_Filter:
    #print('is the first loop for tstf working?  ', TSF_val, TSF_Filter)
    
    Name_TSF.pop(TSF_val)
    Wood_TSF.pop(TSF_val)
    Cooked_TSF.pop(TSF_val)
    Charcoal_TSF.pop(TSF_val)
    Flour_In_TSF.pop(TSF_val)
    Stir_TSF.pop(TSF_val)
    Boil_TSF.pop(TSF_val)
    CE_Time_TSF.pop(TSF_val)

# CQC Stove Matrix Partition


for CQC_val in CQC_Non_Filter:
    Name_CQC.pop(CQC_val)
    Wood_CQC.pop(CQC_val)
    Cooked_CQC.pop(CQC_val)
    Charcoal_CQC.pop(CQC_val)
    Flour_In_CQC.pop(CQC_val)
    Stir_CQC.pop(CQC_val)
    Boil_CQC.pop(CQC_val)
    CE_Time_CQC.pop(CQC_val)
    
# CQC with Jet Flame Matrix Partition


for JFK_val in CQC_JFK_Non_Filter:
    Name_CQC_JFK.pop(JFK_val)
    Wood_CQC_JFK.pop(JFK_val)
    Cooked_CQC_JFK.pop(JFK_val)
    Charcoal_CQC_JFK.pop(JFK_val)
    Flour_In_CQC_JFK.pop(JFK_val)
    Stir_CQC_JFK.pop(JFK_val)
    Boil_CQC_JFK.pop(JFK_val)
    CE_Time_CQC_JFK.pop(JFK_val)


## Wood Savings 
#wood_tsf.remove(-1)
Wood_CQC = list(Wood_CQC)
Wood_CQC.remove(-1)
#wood_cqc_jfk.remove(-1)

ax1 = plt.subplot()
plt.title('Wood Consumption')
plt.ylabel("Grams of wood") 
# TSF
plot_tsf_wood = plt.boxplot(Wood_TSF, positions=[1], widths = 0.6)
plt.text(1,0.1,'TSF',color='b')

Box_TSF_Wood = np.percentile(Wood_TSF, [25,50,75])
Box_TSF_Wood= np.append(Box_TSF_Wood, np.average(Wood_TSF))
# CQC
plot_cqc_wood = plt.boxplot(Wood_CQC, positions=[2], widths = 0.6)
plt.text(2,0.1,'CQC', color= 'g')

Box_CQC_Wood = np.percentile(Wood_CQC, [25,50,75])
Box_CQC_Wood = np.append(Box_CQC_Wood, np.average(Wood_CQC))
#JET Flame
plot_cqc_jfk_wood = plt.boxplot(Wood_CQC_JFK, positions = [3], widths = 0.6)
plt.text(3,0.1,'Jet Flame', color='r')  

Box_JFK_Wood = np.percentile(Wood_CQC_JFK, [25,50,75])
Box_JFK_Wood = np.append(Box_JFK_Wood, np.average(Wood_CQC_JFK))

plt.show()

print('thre are so many issues with Python right now and it does not make any sense------', type(Box_JFK_Wood),'Box for CQC',type(Box_CQC_Wood))
DF_Box_Wood_Consumtion = {'Percentile %': ['25','50','75', 'Avg'], 'TSF': Box_TSF_Wood, 'CQC': Box_CQC_Wood,'JFK' : Box_JFK_Wood}
Wood_CCT_Consumption = pd.DataFrame(data=DF_Box_Wood_Consumtion, columns=['Percentile %','TSF', 'CQC','JET Flame'] )

print(Wood_CCT_Consumption)

## Cooked Food
ax2 = plt.subplot()
plt.title('COOKED FOOD')
plt.ylabel("Grams of Sema") 

PLOT_TSF_COOKED = plt.boxplot(Cooked_TSF, positions=[1], widths = 0.6)
plt.text(1,0.1,'TSF',color='b')

PLOT_CQC_COOKED = plt.boxplot(Cooked_CQC, positions=[2], widths = 0.6)
plt.text(2,0.1,'CQC', color= 'g')

PLOT_CQC_JFK_COOKED = plt.boxplot(Cooked_CQC_JFK, positions = [3], widths = 0.6)
plt.text(3,0.1,'JET FLAME', color='r')   

plt.show()


## Charcaol
ax3 = plt.subplot()
plt.title('Hot Charcoal')
plt.ylabel("Grams of Charcaol") 

PLOT_TSF_CHAR = plt.boxplot(Charcoal_TSF, positions=[1], widths = 0.6)
plt.text(1,0.1,'TSF',color='b')

PLOT_CQC_CHAR = plt.boxplot(Charcoal_CQC, positions=[2], widths = 0.6)
plt.text(2,0.1,'CQC', color= 'g')

PLOT_CQC_JFK_CHAR = plt.boxplot(Charcoal_CQC_JFK, positions = [3], widths = 0.6)
plt.text(3,0.1,'JET FLAME', color='r')   

plt.show()


## BOIL
Boil_TSF = list(Boil_TSF)
Boil_TSF.remove(-1)

#print('CQC Stove ',Boil_CQC)
Boil_CQC = list(Boil_CQC)
Boil_CQC.remove(-1)
#print('CQC Stove Fter -1 filter',Boil_CQC)

# There is a wierd bug in this spectific section. No idea wha thte bug is, no clue. 
# But in order to solve, Needed to manually solve and remove

Boil_CQC_JFK = list(Boil_CQC_JFK)
count = 0
for val, bb in enumerate(Boil_CQC_JFK):
    if bb < 0:
        count = count + 1 
        Boil_CQC_JFK.pop(val)

Boil_CQC_JFK.remove(-5)
Boil_CQC_JFK.pop(8)

ax4 = plt.subplot()
plt.title('Time to Boil')
plt.ylabel("Minutes from Fire Start to Boil") 

PLOT_TSF_BOIL = plt.boxplot(Boil_TSF, positions=[1], widths = 0.6)
plt.text(1,0.1,'TSF',color='b')

PLOT_CQC_BOIL = plt.boxplot(Boil_CQC, positions=[2], widths = 0.6)
plt.text(2,0.1,'CQC', color= 'g')

PLOT_CQC_JFK_BOIL = plt.boxplot(Boil_CQC_JFK, positions = [3], widths = 0.6)
plt.text(3,0.1,'JET FLAME', color='r')   

plt.show()

### Total cooking time

ax5 = plt.subplot()
plt.title('Total Cooking Time')
plt.ylabel("Minutes from Fire Start to End") 

PLOT_TSF_CE_LENGTH = plt.boxplot(CE_Time_TSF, positions=[1], widths = 0.6)
plt.text(1,0.1,'TSF',color='b')

PLOT_CQC_CE_LENGTH = plt.boxplot(CE_Time_CQC, positions=[2], widths = 0.6)
plt.text(2,0.1,'CQC', color= 'g')

PLOT_CQC_JFK_CE_LENGTH = plt.boxplot(CE_Time_CQC_JFK, positions = [3], widths = 0.6)
plt.text(3,0.1,'JET FLAME', color='r')   

plt.show()


