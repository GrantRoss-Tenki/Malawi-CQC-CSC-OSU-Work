# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:51:45 2022

@author: rossgra
"""

import pandas as pd
import numpy as np
import csv
import os
import glob

Phase = "1N"
Computer = "work"
# THis file is for gathering 24 hour averages 
#Work computer
#colecting metrics for each household comparison
HH_NUMBER = []
DAYS_O = []
TIME_START = []
TIME_END = []
PHASE_24_HR_AVG = []
HIGHEST_PM_PER_DAY = []
DAY_OF_HIGHEST_PM = []
day_1 = []
day_2 = []
day_3 = []
day_4 = []
day_5 = []
day_6 = []
day_7 = []
day_8 = []
day_9 = []
day_10 = []
day_11 = []
day_12 = []
day_13 = []
day_14 = []
if Computer == 'work':
    os.chdir("C:/Users/rossgra/Box/OSU, CSC, CQC Project files/"+Phase +"/Compiler_1_exact/Raw_Day/Raw_D_metrics")

else:
    os.chdir("C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/"+ Phase +"/Collection")