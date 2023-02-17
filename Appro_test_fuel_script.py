import os
from turtle import shape
import pandas as pd
import numpy as np
import csv
import glob
import statistics as stat
from datetime import datetime
from csv import reader
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import Functions_malawi
import itertools  

Fuel_Path = "F:/FUEL_TEST"
#place the path to your Fuel CSV. Put this in its own folder to read the file, for right now it only works for a single file
Day_met_path = os.getcwd()
csv_R_m = glob.glob(os.path.join(Fuel_Path, "*.csv"))

for file in csv_R_m:
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        for idx, row in enumerate(csv_reader):
            if 'Timestamp' in row:
                print('You have found the data')
                WHOLE_CSV = pd.read_csv(Fuel_Path, skiprows=(idx), encoding='unicode_escape')
                
                for Column, Metric in enumerate(row):
                    if Column == 0:
                        time = WHOLE_CSV.iloc[:,Column]
                    elif Metric[0:8] =='firewood':
                        Fuel = WHOLE_CSV.iloc[:,Column]
                break

print(Fuel[0:3])