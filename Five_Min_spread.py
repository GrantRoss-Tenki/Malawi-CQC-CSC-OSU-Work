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



Phase  = "1N"
House_hold = [1006, 1007, 1009, 1019, 1023, 1025, 1029, 1035]

for HH in House_hold:
    print('Household- ', HH)
    path_HH1 = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+Phase+"/Compiler_1_exact/HH_summary_Event/"+Phase+"_HH_Summary_Event_"+str(HH)+"_1_exact_1.11.csv"
    HH_1 = pd.read_csv(path_HH1, skiprows = 2)
    Event_length = HH_1.iloc[:,6]
    print(Event_length[0])