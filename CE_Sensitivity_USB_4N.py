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

# first round is for 1N and 1007

Path_CE_MErge = "E:/24_hour_pump/1N/Raw_pump_Time/Exact_1_1007_1N_.csv"

Range = np.arange( 20, 90,1)

EXACT_tester = pd.read_csv(Path_CE_MErge)
TEMp = EXACT_tester.iloc[:,0]
Usage = EXACT_tester.iloc[:,1]

cooking_threshold = 1
length_decrease = 10
start_threshold = 1
end_threshold = -5

#merge_CE_threshold = 40

min_CE_length = 8
window_slope = 12

SUM_cooking_sense = []

for a in Range:
    Usage, Fire_start, Fire_end = Functions_malawi.FireFinder(TEMp, Usage, cooking_threshold, length_decrease, start_threshold, end_threshold, a, min_CE_length, window_slope)
    SUM_cooking_sense.append(sum(Usage))


fig = go.Figure()
fig.add_trace(go.Scatter(x=Range, y=SUM_cooking_sense, mode='lines+markers'))
fig.show()