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
from itertools import zip_longest
import plotly.express as px
import plotly.graph_objects as go


Path = "C:/Users/gvros/Desktop/4N - Copy and Code Worksheet.csv"

gimie = pd.read_csv(Path, skiprows = 0)

print(gimie.iloc[0,0])
hh = gimie.iloc[:,0]
JFK_SUM_Time = []
JFK_SUM_Time = []
#for row, col in eumerate(hh):


#with open(Path, 'r') as data:
#    for line in csv.DictReader(data):
#        print(line)

# first round is for 1N and 10071007


Phase = "2N"
Houshold = 1007

Path_CE_MErge = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_1_exact/Raw_D_metrics/"+Phase+"_HH_raw_Day_metrics_"+str(Houshold)+"_1_exact_3.55555.csv"
Range = np.arange( 20, 60,1)

EXACT_tester = pd.read_csv(Path_CE_MErge,skiprows = 2 )
TEMp = EXACT_tester.iloc[:,4]
Usage = EXACT_tester.iloc[:,3]

print('hafskfhkjeahfisekjfahsiufwa',EXACT_tester.iloc[2,0])

if Phase  == ("2N") or Phase == "3N" or Phase == "3N" or Phase == "4N":
    cooking_threshold = 5
    length_decrease = 40
    start_threshold = 1
    end_threshold = -5
    min_CE_length = 5
    window_slope = 8
else:
    cooking_threshold = 1
    length_decrease = 10
    start_threshold = 1
    end_threshold = -5
    min_CE_length = 8
    window_slope = 12

SUM_cooking_sense = []

for a in Range:
    Usage, Fire_start, Fire_end = Functions_malawi.FireFinder(TEMp, Usage, cooking_threshold, length_decrease, start_threshold, end_threshold, a, min_CE_length, window_slope)
    SUM_cooking_sense.append(sum(Usage))


fig = go.Figure()
fig.add_trace(go.Scatter(x=Range, y=SUM_cooking_sense, mode='lines+markers'))
fig.show()