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
from datetime import datetime
from itertools import islice, cycle
from io import StringIO
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

Phase = "4N"
exact = "2"

os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase +"/Compiler_"+exact+"_exact/Raw_D_metrics")

ff_path = os.getcwd()
csv_R_m = glob.glob(os.path.join(ff_path, "*.csv"))
if exact == "2":
    HH_second_exact = []
for file in csv_R_m:
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        for idx, row in enumerate(csv_reader):
            #HH_gimmie = pd.read_csv(csv_reader)
            #hh = HH_gimmie.iloc[0,1]
            if '0' in row: 
                hh= row[1]
                print(hh, type(hh))
                if exact == "2":
                    HH_second_exact.append(int(hh))
                    
            elif 'Fuel Raw Data' in row:
                data_sart = idx
                break
    start_ff = pd.read_csv(file, skiprows=data_sart)

    USage= start_ff.iloc[:,4]

    Max_event_num = np.arange(0,50,1)
    Event_num = []
    event_count = 0
    for meat,mom in enumerate(USage):
        if meat == len(USage)-1:
            Event_num.append(event_count)
            break
        elif USage[meat+1] == 1 and mom == 0:
            event_count = event_count + 1
            Event_num.append(event_count)
        else:
            Event_num.append(event_count)
    dataframe = pd.DataFrame({"eventnum": Event_num})
    path = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase +"/FIREFINDER/"+exact+" exact/"+hh+"_FF_"+exact+".csv"
    dataframe.to_csv(path,index=False,mode='a')
#print(HH_second_exact)