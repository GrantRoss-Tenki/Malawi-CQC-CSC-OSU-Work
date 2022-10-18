import itertools
import os
from turtle import shape
import pandas as pd
import numpy as np
import csv
from decimal import *
from itertools import chain
import statistics as stat
import datetime
from datetime import datetime
from itertools import islice, cycle
from io import StringIO
import matplotlib.pyplot as plt
import Functions_malawi


Source = 'work' #input("laptop or Work: ")  # 'work' or 'laptop'

if Source == 'laptop':
    USB_D = 'D'
elif Source != 'laptop':
    USB_D = 'F'


Beacon_tester_array = USB_D+":/Malawi 1.1/Proximity_tester_array.csv"
Array = pd.read_csv(Beacon_tester_array)
Array = Array.iloc[:,0]
print(type(Array), Array[0:20])
At_stove,Jet_flame_adjust ,Time_away_from_stove,zero_to_one, zero_to_one_tv,  Reaching_to_stove_tv, Going_away_from_stove, Going_away_from_stove_tv = Functions_malawi.Beacon_Movement_change(1, Array)

print('at the stove for this long: ', At_stove, Jet_flame_adjust)
print('done with script')