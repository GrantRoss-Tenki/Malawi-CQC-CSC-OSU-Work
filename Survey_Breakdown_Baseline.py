import itertools
import os
import pandas as pd
import numpy as np
import csv
import glob
from decimal import *
from itertools import chain
import statistics as stat
import datetime
from io import StringIO
import matplotlib.pyplot as plt
import scipy as scipy
import math


Phase_number = '4N'

datafile_path = 'C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/4N/Survey_4N.xlsx'
Survey_1H_1N = pd.read_excel(datafile_path)
Household_array = Survey_1H_1N.iloc[:,0]
# Information and arrays that i want to remove and look at
House_hold = []
#feeding attributes
Feed_Child_14_avg =[]
Feed_Female_avg = []
Feed_male_15_59_avg = []
Feed_male_60_avg = []
Pots_used_avg = []
Standard_Adult = []
#hapex locaiton
HAPEx_hypot = []
HAPEX_wall = []
#Moisture
Moisture_avg = []
Moisture_std = []
#kitchen
Kit_avg_height = []
Kit_roof_slope = []
Kit_volume = []
Kit_square_foot = []
Kit_Number_windows = []
Pump_flow = []
#fuel atrributes
FUEL_scale = []
#ventilation
Kitchen_upper_ventilation = []
#self reported symptoms
EYE_symptoms = []
#self reported symptoms
Breathing_symptoms = []
#is the HAPEx being worn
COOK_HAPEx_worn = []

for n,hhh in enumerate(Household_array):
    House_hold.append(Survey_1H_1N.iloc[n,0])
    #Standard Adult Equivalence for four days
    Feed_Child_14_avg.append((Survey_1H_1N.iloc[n,6] + Survey_1H_1N.iloc[n,29] +Survey_1H_1N.iloc[n,76] +Survey_1H_1N.iloc[n,110])/ 4)
    Feed_Female_avg.append((Survey_1H_1N.iloc[n,7] + Survey_1H_1N.iloc[n,30] +Survey_1H_1N.iloc[n,77] +Survey_1H_1N.iloc[n,111])/ 4)
    Feed_male_15_59_avg.append((Survey_1H_1N.iloc[n,8] + Survey_1H_1N.iloc[n,31] +Survey_1H_1N.iloc[n,78] +Survey_1H_1N.iloc[n,112])/ 4)
    Feed_male_60_avg.append((Survey_1H_1N.iloc[n,9] + Survey_1H_1N.iloc[n,32] +Survey_1H_1N.iloc[n,79] +Survey_1H_1N.iloc[n,113])/ 4)
    Pots_used_avg.append((Survey_1H_1N.iloc[n,10] + Survey_1H_1N.iloc[n,33] +Survey_1H_1N.iloc[n,80] +Survey_1H_1N.iloc[n,114])/ 4)
    Standard_Adult.append(((Survey_1H_1N.iloc[n,6] + Survey_1H_1N.iloc[n,29] +Survey_1H_1N.iloc[n,76] +Survey_1H_1N.iloc[n,110])*(0.5/4)) +
                          ((Survey_1H_1N.iloc[n,7] + Survey_1H_1N.iloc[n,30] +Survey_1H_1N.iloc[n,77] +Survey_1H_1N.iloc[n,111])*(0.8/4)) +
                          ((Survey_1H_1N.iloc[n,8] + Survey_1H_1N.iloc[n,31] +Survey_1H_1N.iloc[n,78] +Survey_1H_1N.iloc[n,112])/ 4) +
                          (Survey_1H_1N.iloc[n,9] + Survey_1H_1N.iloc[n,32] +Survey_1H_1N.iloc[n,79] +Survey_1H_1N.iloc[n,113])*(0.8/ 4))
    #HAPEx hypotenuse
    HAPEx_hypot.append((int(math.sqrt(((Survey_1H_1N.iloc[n,11])**2)+((Survey_1H_1N.iloc[n,12])**2)) * 100)/100))
    HAPEX_wall.append((Survey_1H_1N.iloc[n,13]))
    #moisure readings
    Moisture_avg.append(((int((sum(Survey_1H_1N.iloc[n,16:25]))*100)/100) + (int((sum(Survey_1H_1N.iloc[n,115:124]))*100)/100))/18)
    # this average can be changed to np.average if needed
    Moisture_std_1 = (Survey_1H_1N.iloc[n,16:25])
    Moisture_std_2 = (Survey_1H_1N.iloc[n,115:124])
    Moisture_compiler_1 = [water for water in Moisture_std_1]
    Moisture_compiler_2 = [water for water in Moisture_std_2]
    Moisture_std.append((int((stat.stdev((Moisture_compiler_1+Moisture_compiler_2))) * 100)) / 100)
    ## Kitchen Characheristics
    #kitchen size
    Kit_avg_height.append(((int((Survey_1H_1N.iloc[n,35])*100)/100)+(int((Survey_1H_1N.iloc[n,36])*100)/100))/2)
    Kit_roof_slope.append((int((Survey_1H_1N.iloc[n,36])/(Survey_1H_1N.iloc[n,35])*100))/100)
    kit_vol_equ = (int((Kit_avg_height[-1] * (Survey_1H_1N.iloc[n,37]) * (Survey_1H_1N.iloc[n,38]))*100))/100
    Kit_volume.append(kit_vol_equ)
    Kit_square_foot.append((int(((Survey_1H_1N.iloc[n,37])* (Survey_1H_1N.iloc[n,38]))*100))/100)
    Kit_Number_windows.append(Survey_1H_1N.iloc[n,39])
    # pump flow
    Pump_flow.append(Survey_1H_1N.iloc[n,70])


    #multiple answers and averaging all similar information
    ##type of fuel used and observed
    # This is calculating a scale for Firewood and Agricultural Residue
    # 0 is all firewood
    # 1 is all Agricultural residue
    # first is enumerators observation

    Fuel_check_1 = Survey_1H_1N.iloc[n,15]
    if Fuel_check_1 == 'Only Wood':
        Score_fuel_1 = 0
    if Fuel_check_1 == 'Mostly wood and a little bit of agricultural residues':
        Score_fuel_1 = 0.25
    if Fuel_check_1 == 'About half wood and half agricultural residues':
        Score_fuel_1 = 0.5
    if Fuel_check_1 == 'Mostly agricultural residues and a little bit of wood':
        Score_fuel_1 = 0.75
    if Fuel_check_1 == 'Only agricultural residues':
        Score_fuel_1 = 1

    Fuel_check_2 = Survey_1H_1N.iloc[n,66]
    if Fuel_check_2 == 'Only Wood':
        Score_fuel_2 = 0
    if Fuel_check_2 == 'Mostly wood and a little bit of agricultural residues':
        Score_fuel_2 = 0.25
    if Fuel_check_2 == 'About half wood and half agricultural residues':
        Score_fuel_2 = 0.5
    if Fuel_check_2 == 'Mostly agricultural residues and a little bit of wood':
        Score_fuel_2 = 0.75
    if Fuel_check_2 == 'Only agricultural residues':
        Score_fuel_2 = 1

    Fuel_check_3 = Survey_1H_1N.iloc[n,87]
    if Fuel_check_3 == 'Only Wood':
        Score_fuel_3 = 0
    if Fuel_check_3 == 'Mostly wood and a little bit of agricultural residues':
        Score_fuel_3 = 0.25
    if Fuel_check_3 == 'About half wood and half agricultural residues':
        Score_fuel_3 = 0.5
    if Fuel_check_3 == 'Mostly agricultural residues and a little bit of wood':
        Score_fuel_3 = 0.75
    if Fuel_check_3 == 'Only agricultural residues':
        Score_fuel_3 = 1

    Fuel_check_4 = Survey_1H_1N.iloc[n,124]
    if Fuel_check_4 == 'Only Wood':
        Score_fuel_4 = 0
    if Fuel_check_4 == 'Mostly wood and a little bit of agricultural residues':
        Score_fuel_4 = 0.25
    if Fuel_check_4 == 'About half wood and half agricultural residues':
        Score_fuel_4 = 0.5
    if Fuel_check_4 == 'Mostly agricultural residues and a little bit of wood':
        Score_fuel_4 = 0.75
    if Fuel_check_4 == 'Only agricultural residues':
        Score_fuel_4 = 1

    #second is the Firewood and agricultural residue details survey
    # the math for these values are detemined by a separating three, twice, and once a day
    #with once a week and less than a week evenly between 0-0.5 for wood and 0.5 and 1 for agriculture
    Firewood_quest = Survey_1H_1N.iloc[n,45]
    if Firewood_quest == 'Three times a day or more':
        Score_Fuel_Firewood = 0
    if Firewood_quest == 'Twice a day':
        Score_Fuel_Firewood = 0.0357
    if Firewood_quest == 'Once a day':
        Score_Fuel_Firewood = 0.0714
    if Firewood_quest == 'At least once a week':
        Score_Fuel_Firewood = 0.214
    if Firewood_quest == 'Less than once a week':
        Score_Fuel_Firewood = 0.357
    if Firewood_quest == 'Never': # this is now assumed that they are using all Agricultural
        Score_Fuel_Firewood = 1

    Agri_quest = Survey_1H_1N.iloc[n,54]
    if Agri_quest == 'Three times a day or more':
        Score_Fuel_Agri = 1
    if Agri_quest == 'Twice a day':
        Score_Fuel_Agri = 0.928
    if Agri_quest == 'Once a day':
        Score_Fuel_Agri = 0.857
    if Agri_quest == 'At least once a week':
        Score_Fuel_Agri = 0.785
    if Agri_quest == 'Less than once a week':
        Score_Fuel_Agri = 0.642
    if Agri_quest == 'Never': # this is now assumed they are using all Firewood
        Score_Fuel_Agri = 0

    FUEL_sum = (int(((Score_Fuel_Agri+Score_Fuel_Firewood+Score_fuel_4+Score_fuel_3+Score_fuel_2+Score_fuel_1)/6)*100))/100
    FUEL_scale.append(FUEL_sum)
    #kitchen ventilation
    Kit_up_v = Survey_1H_1N.iloc[n,42]
    if Kit_up_v == 'No openings':
        Score_vent = 0
    if Kit_up_v == 'between 0 and 5 cm (included)':
        Score_vent = 0.33
    if Kit_up_v == 'more than 5cm but less than 10 cm':
        Score_vent = 0.66
    if Kit_up_v == 'more than 10 cm':
        Score_vent = 1

    Kitchen_upper_ventilation.append(Score_vent)


    #Self reported issues
    #eye symptoms are first
    Is_eye_none = Survey_1H_1N.iloc[n,89]
    if Is_eye_none == 'None':
        Score_EYE = 0
    if Is_eye_none != 'None':
        EYE = (Survey_1H_1N.iloc[n,90:97])
        EYE_Sum = [e for e in EYE]
        Score_EYE = sum(EYE_Sum)
    EYE_symptoms.append(Score_EYE)
    #breathing symptoms
    Is_breath_none = Survey_1H_1N.iloc[n,97]
    if Is_breath_none == 'None':
        Score_Breath = 0
    if Is_breath_none != 'None':
        Breath = (Survey_1H_1N.iloc[n,98:105])
        Breath_Sum = [b for b in Breath]
        Score_Breath = sum(Breath_Sum)

    Breathing_symptoms.append(Score_Breath)

    #Amount the hapex was worn
    Hapex_wear_1 = Survey_1H_1N.iloc[n,60]
    if Hapex_wear_1 == 'Never':
        Score_1_hapex = 0
    if Hapex_wear_1 == 'Some of the time':
        Score_1_hapex = 0.33
    if Hapex_wear_1 == 'Only when i cooked':
        Score_1_hapex = 0.66
    if Hapex_wear_1 == 'All of the time':
        Score_1_hapex = 1

    Hapex_wear_2 = Survey_1H_1N.iloc[n,81]
    if Hapex_wear_2 == 'Never':
        Score_2_hapex = 0
    if Hapex_wear_2 == 'Some of the time':
        Score_2_hapex = 0.33
    if Hapex_wear_2 == 'Only when i cooked':
        Score_2_hapex = 0.66
    if Hapex_wear_2 == 'All of the time':
        Score_2_hapex = 1

    Hapex_wear_3 = Survey_1H_1N.iloc[n,128]
    if Hapex_wear_3 == 'Never':
        Score_3_hapex = 0
    if Hapex_wear_3 == 'Some of the time':
        Score_3_hapex = 0.33
    if Hapex_wear_3 == 'Only when i cooked':
        Score_3_hapex = 0.66
    if Hapex_wear_3 == 'All of the time':
        Score_3_hapex = 1

    HAPEx_worn = (Score_1_hapex+Score_2_hapex+Score_3_hapex)/3
    COOK_HAPEx_worn.append(HAPEx_worn)


Survey_data = {'Household' : House_hold, 'Child 14 or Under Feed (avg)' : Feed_Child_14_avg,
               'Female Feed (avg)': Feed_Female_avg, 'Male 15-59 Feed (avg)': Feed_male_15_59_avg ,
               'Male 60+ Feed (avg)': Feed_male_60_avg, 'Pots that were used (avg)': Pots_used_avg, 'Standard Adult Equivalence': Standard_Adult,
               'Hypotenuse of HAPEx from Stove (meters)': HAPEx_hypot,
               'HAPEx Distance from Wall (meters)': HAPEX_wall, 'Amount the Cook HAPEx Worn':COOK_HAPEx_worn,
               'Moisture of all Fuel (avg)': Moisture_avg, 'Moisture of all Fuel (std)': Moisture_std,
               'Height of Kitchen (avg)(meters)': Kit_avg_height, ' Kitchen Roof Slope (meters)': Kit_roof_slope,
               'Kitchen Volume (meters^3)': Kit_volume, 'Kitchen Square Footage (meters^2)': Kit_square_foot,
               'Numbers of Windows in Kitchen (#)': Kit_Number_windows, 'Flow of Pump (L/m)': Pump_flow,
               'Scale of Fuel (0 = wood) (1 = residue)': FUEL_scale, 'Kitchen Upper Ventilation (cm)': Kitchen_upper_ventilation,
               'Reported Eye Symptoms': EYE_symptoms, 'Breathing Symptoms':Breathing_symptoms}

df_Survey_data = pd.DataFrame(Survey_data)

Path_Survey= "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase_number
File_phase_1_survey = str(Path_Survey) + "/"+Phase_number+"_Survey_summary_"+".csv"
df_Survey_data.to_csv(File_phase_1_survey)

