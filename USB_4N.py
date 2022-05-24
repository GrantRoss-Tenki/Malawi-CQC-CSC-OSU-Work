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


Path = "C:/Users/gvros/Desktop/4N - Copy and Code Worksheet.csv"

gimie = pd.read_csv(Path, skiprows = 0)

print(gimie.iloc[0,0])
hh = gimie.iloc[:,0]
JFK_SUM_Time = []
JFK_SUM_Time = []
for row, col in eumerate(hh):


#with open(Path, 'r') as data:
#    for line in csv.DictReader(data):
#        print(line)