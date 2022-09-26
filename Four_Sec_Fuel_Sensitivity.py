
import itertools
import os
from types import prepare_class
import pandas as pd
import numpy as np
import csv
import glob
from decimal import *
from itertools import chain
#import statistics as stat
import datetime
from datetime import datetime
from itertools import islice, cycle
from io import StringIO
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import Functions_malawi

#read = (pd.read_csv("//depot.engr.oregonstate.edu/users/rossgra/Windows.Documents/My Documents/CSV_Tester/Fuel_sens_1.csv"))
read = (pd.read_csv("C:/Users/gvros/Documents/CSV_FUEL_tester.csv"))
Fueel = read.iloc[:,0]
print('-------', Fueel[1])
Threshold_array = np.arange(.0001, 0.06,0.0001)
#Threshold_array = np.arange(1, 30,0.1)

KG_Removed = []
for thresh in Threshold_array:
    KG_burned_1, KG_1_mean = Functions_malawi.FUEL_REMOVAL(Fueel, thresh, 15, True, 30)
    
    #eliminate_repeat = Functions_malawi.Remove_Repeated_Values(KG_burned_1)
    KG_Removed.append(sum(list(set(KG_burned_1))))


fig = go.Figure()
fig.add_trace(go.Scatter(x=Threshold_array, y=KG_Removed,
                mode='lines+markers'))
                    
fig.update_layout(title=" Sensitivity for Fuel Threshold",
                   xaxis_title='Threshold',
                   yaxis_title='Fuel Removed')

fig.show()