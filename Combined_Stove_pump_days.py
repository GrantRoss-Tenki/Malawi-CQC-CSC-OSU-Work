import os
import pandas as pd
import numpy as np
import csv
import glob
import statistics as stat
from datetime import datetime
from csv import reader
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path, PureWindowsPath
import Functions_malawi


Phase = "4N"

if Phase== "2N":
   exact_2_hh = [1007]
elif Phase== "3N":
   exact_2_hh = [1001]
elif Phase== "4N":
   exact_2_hh = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1011, 1013, 1014, 1016, 1017, 1018, 1019, 1021, 1022, 1023, 1024, 1025, 1026, 1028, 1029, 1030, 1031, 1032, 1033, 1035, 1036, 1037, 1038, 1039]
elif Phase== "2H":
   exact_2_hh = [2006]
elif Phase== "3H":
   exact_2_hh = [2001, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
else:
   exact_2_hh = [0]


if Phase  == ("2N") or Phase == "3N" or Phase == "3N" or Phase == "4N":
    cooking_threshold = 5
    length_decrease = 40
    start_threshold = 1
    end_threshold = -5
    merge_CE_threshold = 60
    min_CE_length = 5
    window_slope = 8
else:
    cooking_threshold = 1
    length_decrease = 10
    start_threshold = 1
    end_threshold = -5
    merge_CE_threshold = 40
    min_CE_length = 8
    window_slope = 12


os.chdir("E:/24_hour_pump/"+Phase+"/Raw_pump_Time")
Day_met_path = os.getcwd()
csv_R_m = glob.glob(os.path.join(Day_met_path, "*.csv"))

for file in csv_R_m:
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        hh = []
        for letter_num, letter in enumerate(file):
            if letter_num == 39: # 39 is the exact number
                Number_stove = letter
            elif letter_num == 41 or letter_num == 42 or letter_num == 43 or letter_num == 44:
                hh.extend(list(letter))
    home= []
    for h in hh:
        home.append((int(h)))

    household = Functions_malawi.flatten_list(home)
    print('this is the household', household)
    for second in exact_2_hh:
        if second == household:
            second_exact = 0
            break

        else:
            second_exact = 1


    print(second_exact)


    

    if second_exact != 1:
        path_exact_1 = "E:/24_hour_pump/"+Phase+"/Raw_pump_Time/Exact_1_"+str(household)+"_"+Phase+"_.csv"
        path_exact_2 = "E:/24_hour_pump/"+Phase+"/Raw_pump_Time/Second_stove/Exact_2_"+str(household)+"_"+Phase+"_.csv"
        Stove_1 = pd.read_csv(path_exact_1, skiprows = 2)
        Stove_2 = pd.read_csv(path_exact_2, skiprows = 2)
        Temp_1 = Stove_1.iloc[:,0]
        Temp_2 = Stove_2.iloc[:,0]
        Usage_1 = Stove_1.iloc[:,1]
        Stove_1_ff, S_1_start, S_1_end = Functions_malawi.FireFinder(Temp_1, Usage_1, cooking_threshold, length_decrease, start_threshold,
                                                                     end_threshold, merge_CE_threshold, min_CE_length, window_slope)
        Usage_2 = Stove_2.iloc[:,1]
        Stove_2_ff, S_2_start, S_2_end = Functions_malawi.FireFinder(Temp_2, Usage_2, cooking_threshold, length_decrease, start_threshold,
                                                                     end_threshold, merge_CE_threshold, min_CE_length, window_slope)
    else:
        path_exact_1 = "E:/24_hour_pump/"+Phase+"/Raw_pump_Time/Exact_1_"+str(household)+"_"+Phase+"_.csv"
        Stove_1 = pd.read_csv(path_exact_1, skiprows = 2)
        Temp_1 = Stove_1.iloc[:,0]
        Usage_1 = Stove_1.iloc[:,1]
        Stove_1_ff, S_1_start, S_1_end = Functions_malawi.FireFinder(Temp_1, Usage_1, cooking_threshold, length_decrease, start_threshold,
                                                                     end_threshold, merge_CE_threshold, min_CE_length, window_slope)
        Stove_2_ff = []
        for length in (np.arange(0,len(Stove_1_ff),1)):
            Stove_2_ff.append(-1)

    Merge_stoves = Functions_malawi.Squish_usage(Phase,household,Stove_1_ff, Stove_2_ff)

print(sum(Stove_1_ff), sum(Merge_stoves) )
        