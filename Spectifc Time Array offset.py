# -*- coding: utf-8 -*-
"""
Created on Thu May 12 20:52:41 2022

@author: rossgra
"""

# this is pure arrat time array


import pandas as pd

path = "//depot.engr.oregonstate.edu/users/rossgra/Windows.Documents/Desktop/Time array.csv"

CSV = pd.read_csv(path, skiprows=0)
print(CSV)
#hour_1 = []
#hour_2 = []
#minute_1 = []
#minute_2 = []
minutes = []
for tume in CSV.iloc[:,0]:
    next_tume = 0
    #print(tume, type(tume))
    for space, letter in enumerate(tume):
        if tume == '0':
            minutes.append(0)
        elif next_tume == 0 and len(tume) != 0:
            if space == 0:
                hour_1 = (letter)
                #print(letter)
            elif space == 1:
                hour_2 = (letter)
                #print(letter)
            elif space == 3:
                minute_1 =(letter)
                #print(letter)
            elif space == 4:
                minute_2 = (letter)
                #print(letter)
            elif space == 5:
                next_tume = 1
                hour_conv = (int(hour_1) *600)+(int(hour_2)*60)
                min_conv = (int(minute_1) * 10) + int(minute_2)
                minutes.append(hour_conv+min_conv)
                


print(minutes)
pd_minutes = pd.DataFrame(minutes)
output_path = "//depot.engr.oregonstate.edu/users/rossgra/Windows.Documents/Desktop/ouotput_time.csv"
pd_minutes.to_csv(output_path)