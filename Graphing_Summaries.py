import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#from pylab import plot, show, xlim,figure,hold, ylim,legend, boxplot, setup, axes
import os
import glob
import itertools
import csv
import seaborn as sns

# Is this a personal or work computer
# Are you graphing for hood or no hood

Computer = 'work' #or 'personal' or 'work'
Hood_or_no = 'no_hood' # 'no_hood' or 'hood'

if Computer == 'personal' and Hood_or_no == 'no_hood':
    # 1N
    datafile_path_day_1N ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/1N/1N_Summary_Day_1_exact.csv"
    Day_1N = pd.read_csv(datafile_path_day_1N, skiprows=2)
    datafile_path_event_1N = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/1N/1N_Summary_Event_1_exact.csv"
    Event_1N = pd.read_csv(datafile_path_event_1N, skiprows=2)
    # there is no second exact in phase 1N
    #1N Survey
    datafile_path_survey_1N = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/1N/1N_1H_Survey_summary_.csv"
    Filter_1n_survey = pd.read_csv(datafile_path_survey_1N, skiprows=0)
    #print(Filter_1n_survey.iloc[0:40, :])
    Survey_1N = Filter_1n_survey.iloc[0:40,:]
    
    #2N
    datafile_path_day_2N ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/2N/2N_Summary_Day_1_exact.csv"
    Day_2N = pd.read_csv(datafile_path_day_2N, skiprows=2)
    datafile_path_event_2N_1 ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/2N/2N_Summary_Event_1_exact.csv"
    Event_2N_1 = pd.read_csv(datafile_path_event_2N_1, skiprows=2)
    #2N second Exact
    datafile_path_event_2N_2 ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/2N/2N_Summary_Event_2_exact.csv"
    Event_2N_2 = pd.read_csv(datafile_path_event_2N_2, skiprows=2)
    #2N Survey
    datafile_path_survey_2N = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/2N/2N_Survey_summary_.csv"
    Survey_2N = pd.read_csv(datafile_path_survey_2N, skiprows=0)
    
    #3N
    datafile_path_day_3N ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/3N/3N_Summary_Day_1_exact.csv"
    Day_3N = pd.read_csv(datafile_path_day_3N, skiprows=2)
    datafile_path_event_3N_1 ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/3N/3N_Summary_Event_1_exact.csv"
    Event_3N_1 = pd.read_csv(datafile_path_event_3N_1, skiprows=2)
    #3N second Exact
    datafile_path_event_3N_2 ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/3N/3N_Summary_Event_2_exact.csv"
    Event_3N_2 = pd.read_csv(datafile_path_event_3N_2, skiprows=2)
    #3N Survey 
    datafile_path_survey_3N = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/3N/3N_Survey_summary_.csv"
    Survey_3N = pd.read_csv(datafile_path_survey_3N, skiprows=0)
    
    #4N
    datafile_path_day_4N ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/4N/4N_Summary_Day_1_exact.csv"
    Day_4N = pd.read_csv(datafile_path_day_4N, skiprows=2)
    datafile_path_event_4N_1 ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/4N/4N_Summary_Event_1_exact.csv"
    Event_4N_1 = pd.read_csv(datafile_path_event_4N_1, skiprows=2)
    #4N second Exact
    datafile_path_event_4N_2 ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/4N/4N_Summary_Event_2_exact.csv"
    Event_4N_2 = pd.read_csv(datafile_path_event_4N_2, skiprows=2)
    #4N Survey 
    datafile_path_survey_4N = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/4N/4N_Survey_summary_.csv"
    Survey_4N = pd.read_csv(datafile_path_survey_4N, skiprows=0)
    
elif Computer == 'personal' and Hood_or_no == 'hood':
    #1H
    datafile_path_day_1H ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/1H/1H_Summary_Day_1_exact.csv"
    Day_1H = pd.read_csv(datafile_path_day_1H, skiprows=2)
    datafile_path_event_1H ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/1H/1H_Summary_Event_1_exact.csv"
    Event_1H = pd.read_csv(datafile_path_event_1H, skiprows=2)
    #there is no second exact in phase 1H
    #1H Survey (row 40 or so afterward is Hood portion column 1 is houshold number)
    datafile_path_survey_1H = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/1N/1N_1H_Survey_summary_.csv"
    Survey_1H = pd.read_csv(datafile_path_survey_1H, skiprows=40)
    
    #2H
    datafile_path_day_2H ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/2H/2H_Summary_Day_1_exact.csv"
    Day_2H = pd.read_csv(datafile_path_day_2H, skiprows=2)
    datafile_path_event_2H_1 ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/2H/2H_Summary_Event_1_exact.csv"
    Event_2H_1 = pd.read_csv(datafile_path_event_2H_1, skiprows=2)
    #2H second Exact
    datafile_path_event_2H_2 ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/2H/2H_Summary_Event_2_exact.csv"
    Event_2H_2 = pd.read_csv(datafile_path_event_2H_2, skiprows=2)
    #2H survey 
    datafile_path_survey_2H = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/2H/2H_Survey_summary_.csv"
    Survey_2H = pd.read_csv(datafile_path_survey_2H, skiprows=0)
    
    #3H
    datafile_path_day_3H ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/3H/3H_Summary_Day_1_exact.csv"
    Day_3H = pd.read_csv(datafile_path_day_3H, skiprows=2)
    datafile_path_event_3N_1 ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/3H/3H_Summary_Event_1_exact.csv"
    Event_3H_1 = pd.read_csv(datafile_path_event_3N_1, skiprows=2)
    #3H second Exact
    datafile_path_event_3H_2 ="C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/3H/3H_Summary_Event_2_exact.csv"
    Event_3H_2 = pd.read_csv(datafile_path_event_3H_2, skiprows=2)
    #3H survey 
    datafile_path_survey_3H = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/3H/3H_Survey_summary_.csv"
    Survey_3H = pd.read_csv(datafile_path_survey_3H, skiprows=0)
    
    #work uses box information and not local data
elif Computer == 'work' and Hood_or_no == 'no_hood':
    # 1N for box file system
    datafile_path_day_1N = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/1N/1N_Summary_Day_1_exact.csv"
    Day_1N = pd.read_csv(datafile_path_day_1N, skiprows=2)
    datafile_path_event_1N ="C:/Users/rossgra/Box/OSU, CSC, CQC Project files/1N/1N_Summary_Event_1_exact.csv"
    Event_1N = pd.read_csv(datafile_path_event_1N, skiprows=2)
    # there is no second exact in phase 1N
    #1N Survey 
    datafile_path_survey_1N = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/1N/1N_1H_Survey_summary_.csv"
    Filter_1n_survey = pd.read_csv(datafile_path_survey_1N, skiprows=0)
    #print(Filter_1n_survey.iloc[0:40, :])
    Survey_1N = Filter_1n_survey.iloc[0:40,:]
    
    #2N
    datafile_path_day_2N ="C:/Users/rossgra/Box/OSU, CSC, CQC Project files/2N/2N_Summary_Day_1_exact.csv"
    Day_2N = pd.read_csv(datafile_path_day_2N, skiprows=2)
    datafile_path_event_2N_1 ="C:/Users/rossgra/Box/OSU, CSC, CQC Project files/2N/2N_Summary_Event_1_exact.csv"
    Event_2N_1 = pd.read_csv(datafile_path_event_2N_1, skiprows=2)
    #2N second Exact
    datafile_path_event_2N_2 ="C:/Users/rossgra/Box/OSU, CSC, CQC Project files/2N/2N_Summary_Event_2_exact.csv"
    Event_2N_2 = pd.read_csv(datafile_path_event_2N_2, skiprows=2)
    #2N Survey
    datafile_path_survey_2N = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/2N/2N_Survey_summary_.csv"
    Survey_2N = pd.read_csv(datafile_path_survey_2N, skiprows=0)
    
    #3N
    datafile_path_day_3N ="C:/Users/rossgra/Box/OSU, CSC, CQC Project files/3N/3N_Summary_Day_1_exact.csv"
    Day_3N = pd.read_csv(datafile_path_day_3N, skiprows=2)
    datafile_path_event_3N_1 ="C:/Users/rossgra/Box/OSU, CSC, CQC Project files/3N/3N_Summary_Event_1_exact.csv"
    Event_3N_1 = pd.read_csv(datafile_path_event_3N_1, skiprows=2)
    #3N second Exact
    datafile_path_event_3N_2 ="C:/Users/rossgra/Box/OSU, CSC, CQC Project files/3N/3N_Summary_Event_2_exact.csv"
    Event_3N_2 = pd.read_csv(datafile_path_event_3N_2, skiprows=2)
    #3N survey
    datafile_path_survey_3N = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/3N/3N_Survey_summary_.csv"
    Survey_3N = pd.read_csv(datafile_path_survey_3N, skiprows=0)
    
    #4N
    datafile_path_day_4N ="C:/Users/rossgra/Box/OSU, CSC, CQC Project files/4N/4N_Summary_Day_1_exact.csv"
    Day_4N = pd.read_csv(datafile_path_day_4N, skiprows=2)
    datafile_path_event_4N_1 ="C:/Users/rossgra/Box/OSU, CSC, CQC Project files/4N/4N_Summary_Event_1_exact.csv"
    Event_4N_1 = pd.read_csv(datafile_path_event_4N_1, skiprows=2)
    #4N second Exact
    datafile_path_event_4N_2 ="C:/Users/rossgra/Box/OSU, CSC, CQC Project files/4N/4N_Summary_Event_2_exact.csv"
    Event_4N_2 = pd.read_csv(datafile_path_event_4N_2, skiprows=2)
    #4N Survey 
    datafile_path_survey_4N = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/4N/4N_Survey_summary_.csv"
    Survey_4N = pd.read_csv(datafile_path_survey_4N, skiprows=0)
else:
    #1H
    datafile_path_day_1H ="C:/Users/rossgra/Box/OSU, CSC, CQC Project files/1H/1H_Summary_Day_1_exact.csv"
    Day_1H = pd.read_csv(datafile_path_day_1H, skiprows=2)
    datafile_path_event_1H ="C:/Users/rossgra/Box/OSU, CSC, CQC Project files/1H/1H_Summary_Event_1_exact.csv"
    Event_1H = pd.read_csv(datafile_path_event_1H, skiprows=2)
    #there is no second exact in phase 1H
    #1H Survey (row 40 or so afterward is Hood portion column 1 is houshold number)
    datafile_path_survey_1H = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/1N/1N_1H_Survey_summary_.csv"
    Survey_1H = pd.read_csv(datafile_path_survey_1H, skiprows=40)
    
    #2H
    datafile_path_day_2H = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/2H/2H_Summary_Day_1_exact.csv"
    Day_2H = pd.read_csv(datafile_path_day_2H, skiprows=2)
    datafile_path_event_2H_1 ="C:/Users/rossgra/Box/OSU, CSC, CQC Project files/2H/2H_Summary_Event_1_exact.csv"
    Event_2H_1 = pd.read_csv(datafile_path_event_2H_1, skiprows=2)
    #2H second Exact
    datafile_path_event_2H_2 ="C:/Users/rossgra/Box/OSU, CSC, CQC Project files/2H/2H_Summary_Event_2_exact.csv"
    Event_2H_2 = pd.read_csv(datafile_path_event_2H_2, skiprows=2)
    #2H survey 
    datafile_path_survey_2H = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/2H/2H_Survey_summary_.csv"
    Survey_2H = pd.read_csv(datafile_path_survey_2H, skiprows=0)
    
    #3H
    datafile_path_day_3H = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/3H/3H_Summary_Day_1_exact.csv"
    Day_3H = pd.read_csv(datafile_path_day_3H, skiprows=2)
    datafile_path_event_3N_1 ="C:/Users/rossgra/Box/OSU, CSC, CQC Project files/3H/3H_Summary_Event_1_exact.csv"
    Event_3H_1 = pd.read_csv(datafile_path_event_3N_1, skiprows=2)
    #3H second Exact
    datafile_path_event_3H_2 ="C:/Users/rossgra/Box/OSU, CSC, CQC Project files/3H/3H_Summary_Event_2_exact.csv"
    Event_3H_2 = pd.read_csv(datafile_path_event_3H_2, skiprows=2)
    #3H survey 
    datafile_path_survey_3H = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/3H/3H_Survey_summary_.csv"
    Survey_3H = pd.read_csv(datafile_path_survey_3H, skiprows=0)
    
#time to start ploting fun things 
#1st starting with the fuel per day per adult histogram and box plot
NO_hood_counter = np.arange(0,39)
hood_counter = np.arange(0,14)
#what household do you want to remove from the graphs (1046 is a dummy spacer)
Household_removal = [1046]

print('---------------Fuel per Day per Adult No-Hood Phase---------------------')
Fuel_per_day_per_adult_1N = []
f_d_a_1N = []
Fuel_per_day_per_adult_2N = []
f_d_a_2N = []
Fuel_per_day_per_adult_3N = []
f_d_a_3N = []
Fuel_per_day_per_adult_4N = []
f_d_a_4N =[]
count = 0
for c in NO_hood_counter:
    if c == (Household_removal[count] - 1001):
        count = count + 1
        pass
    if Day_1N.iloc[c,13] != -1.00:
        Fuel_per_day_per_adult_1N.append(Day_1N.iloc[c,13]/Survey_1N.iloc[c,7])
        f_d_a_1N.append(Day_1N.iloc[c,0])
    if Day_2N.iloc[c, 13] != -1.00:
        Fuel_per_day_per_adult_2N.append(Day_2N.iloc[c, 13] / Survey_2N.iloc[c, 7])
        f_d_a_2N.append(Day_2N.iloc[c,0])
    if Day_3N.iloc[c, 13] != -1.00:
        Fuel_per_day_per_adult_3N.append(Day_3N.iloc[c, 13] / Survey_3N.iloc[c, 7])
        f_d_a_3N.append(Day_3N.iloc[c, 0])
    if Day_4N.iloc[c, 13] != -1.00:
        Fuel_per_day_per_adult_4N.append(Day_4N.iloc[c, 13] / Survey_4N.iloc[c, 7])
        f_d_a_4N.append(Day_3N.iloc[c, 0])

# now for plotting
#1N
sns.set(style="ticks")
f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)})
sns.boxplot(Fuel_per_day_per_adult_1N, ax=ax_box, color='b')
sns.distplot(Fuel_per_day_per_adult_1N, ax=ax_hist, color='b')
ax_box.set(yticks=[])
sns.despine(ax=ax_hist)
sns.despine(ax=ax_box, left=True)
plt.title('1N Fuel per Day per Adult')
plt.ylim(top=2)
plt.ylim(bottom = 0)

#2N
sns.set(style="ticks")
f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)})
sns.boxplot(Fuel_per_day_per_adult_2N, ax=ax_box, color='g')
sns.distplot(Fuel_per_day_per_adult_2N, ax=ax_hist, color='g')
ax_box.set(yticks=[])
sns.despine(ax=ax_hist)
sns.despine(ax=ax_box, left=True)
plt.title('2N Fuel per Day per Adult')
plt.ylim(top=2)
plt.ylim(bottom = 0)
#3N
sns.set(style="ticks")
f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)})
sns.boxplot(Fuel_per_day_per_adult_3N, ax=ax_box, color='r')
sns.distplot(Fuel_per_day_per_adult_3N, ax=ax_hist, color='r')
ax_box.set(yticks=[])
sns.despine(ax=ax_hist)
sns.despine(ax=ax_box, left=True)
plt.title('3N Fuel per Day per Adult')
plt.ylim(top=2)
plt.ylim(bottom = 0)
#4N
sns.set(style="ticks")
f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)})
sns.boxplot(Fuel_per_day_per_adult_4N, ax=ax_box, color='y')
sns.distplot(Fuel_per_day_per_adult_4N, ax=ax_hist, color='y')
ax_box.set(yticks=[])
sns.despine(ax=ax_hist)
sns.despine(ax=ax_box, left=True)
plt.title('4N Fuel per Day per Adult')
plt.ylim(top=2)
plt.ylim(bottom = 0)

fig, ax = plt.subplots()
plt.title('No-Hood Fuel per Day per Adult')
plt.hold(True)

quant_1_1N = np.percentile(Fuel_per_day_per_adult_1N, [25,75])
Top_lim_1_1N = quant_1_1N[1] + 1.5*(quant_1_1N[1] - quant_1_1N[0])
Low_lim_1_1N = quant_1_1N[0] - 1.5*(quant_1_1N[1] - quant_1_1N[0])

bp_1 = plt.boxplot(Fuel_per_day_per_adult_1N, positions = [1], widths = 0.6)
for v,a in enumerate(Fuel_per_day_per_adult_1N):
    if a > Top_lim_1_1N or a < Low_lim_1_1N:
        plt.text(1,a,f_d_a_1N[v])
plt.text(1,0.1,'1N',color='b')
    
    
quant_1_2N = np.percentile(Fuel_per_day_per_adult_2N, [25,75])
Top_lim_1_2N = quant_1_2N[1] + 1.5*(quant_1_2N[1] - quant_1_2N[0])
Low_lim_1_2N = quant_1_2N[0] - 1.5*(quant_1_2N[1] - quant_1_2N[0])

bp_1 = plt.boxplot(Fuel_per_day_per_adult_2N,positions = [2], widths = 0.6)
for v,a in enumerate(Fuel_per_day_per_adult_2N):
    if a > Top_lim_1_2N or a < Low_lim_1_2N:
        plt.text(2,a,f_d_a_2N[v])
plt.text(2,0.1,'2N', color= 'g')

quant_1_3N = np.percentile(Fuel_per_day_per_adult_3N, [25,75])
Top_lim_1_3N = quant_1_3N[1] + 1.5*(quant_1_3N[1] - quant_1_3N[0])
Low_lim_1_3N = quant_1_3N[0] - 1.5*(quant_1_3N[1] - quant_1_3N[0])

bp_1 = plt.boxplot(Fuel_per_day_per_adult_3N,positions = [3], widths = 0.6)
count = 0
for v,a in enumerate(Fuel_per_day_per_adult_3N):
    
    if a > Top_lim_1_3N or a < Low_lim_1_3N:
        count = count + 1
        if count == 2:
            plt.text(3,a,f_d_a_3N[v],ha='left',va='bottom')
        elif count != 2:
            plt.text(3,a,f_d_a_3N[v],ha='right',va='bottom')
plt.text(3,0.1,'3N', color='r')        


quant_1_4N = np.percentile(Fuel_per_day_per_adult_4N, [25,75])
Top_lim_1_4N = quant_1_4N[1] + 1.5*(quant_1_4N[1] - quant_1_4N[0])
Low_lim_1_4N = quant_1_4N[0] - 1.5*(quant_1_4N[1] - quant_1_4N[0])

bp_1 = plt.boxplot(Fuel_per_day_per_adult_4N,positions = [4], widths = 0.6)
for v,a in enumerate(Fuel_per_day_per_adult_4N):
    if a > Top_lim_1_4N or a < Low_lim_1_4N:
        plt.text(4,a,f_d_a_4N[v])
plt.text(4,0.1,'4N', color='y')        
        
plt.xlim(0,5)
plt.ylim(0,2.3)

phase = ['1N' ,'2N', '3N', '4N']
Colors = ['blue', 'green', 'red', 'yellow']
for patch, colo  in (bp_1, Colors):
    patch.set_facecolor(colo)


plt.show()

print ('-------------------Fuel per Day per Adult Hood Phse -------------------')


Fuel_per_day_per_adult_1H = []
f_d_a_1N = []
Fuel_per_day_per_adult_2N = []
f_d_a_2N = []
Fuel_per_day_per_adult_3N = []
f_d_a_3N = []
Fuel_per_day_per_adult_4N = []
f_d_a_4N =[]
count = 0
for c in NO_hood_counter:
    if c == (Household_removal[count] - 1001):
        count = count + 1
        pass
    if Day_1N.iloc[c,13] != -1.00:
        Fuel_per_day_per_adult_1N.append(Day_1N.iloc[c,13]/Survey_1N.iloc[c,7])
        f_d_a_1N.append(Day_1N.iloc[c,0])
    if Day_2N.iloc[c, 13] != -1.00:
        Fuel_per_day_per_adult_2N.append(Day_2N.iloc[c, 13] / Survey_2N.iloc[c, 7])
        f_d_a_2N.append(Day_2N.iloc[c,0])
    if Day_3N.iloc[c, 13] != -1.00:
        Fuel_per_day_per_adult_3N.append(Day_3N.iloc[c, 13] / Survey_3N.iloc[c, 7])
        f_d_a_3N.append(Day_3N.iloc[c, 0])
    if Day_4N.iloc[c, 13] != -1.00:
        Fuel_per_day_per_adult_4N.append(Day_4N.iloc[c, 13] / Survey_4N.iloc[c, 7])
        f_d_a_4N.append(Day_3N.iloc[c, 0])

# now for plotting
#1N
sns.set(style="ticks")
f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)})
sns.boxplot(Fuel_per_day_per_adult_1N, ax=ax_box, color='b')
sns.distplot(Fuel_per_day_per_adult_1N, ax=ax_hist, color='b')
ax_box.set(yticks=[])
sns.despine(ax=ax_hist)
sns.despine(ax=ax_box, left=True)
plt.title('1N Fuel per Day per Adult')
plt.ylim(top=2)
plt.ylim(bottom = 0)

#2N
sns.set(style="ticks")
f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)})
sns.boxplot(Fuel_per_day_per_adult_2N, ax=ax_box, color='g')
sns.distplot(Fuel_per_day_per_adult_2N, ax=ax_hist, color='g')
ax_box.set(yticks=[])
sns.despine(ax=ax_hist)
sns.despine(ax=ax_box, left=True)
plt.title('2N Fuel per Day per Adult')
plt.ylim(top=2)
plt.ylim(bottom = 0)
#3N
sns.set(style="ticks")
f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)})
sns.boxplot(Fuel_per_day_per_adult_3N, ax=ax_box, color='r')
sns.distplot(Fuel_per_day_per_adult_3N, ax=ax_hist, color='r')
ax_box.set(yticks=[])
sns.despine(ax=ax_hist)
sns.despine(ax=ax_box, left=True)
plt.title('3N Fuel per Day per Adult')
plt.ylim(top=2)
plt.ylim(bottom = 0)
#4N
sns.set(style="ticks")
f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)})
sns.boxplot(Fuel_per_day_per_adult_4N, ax=ax_box, color='y')
sns.distplot(Fuel_per_day_per_adult_4N, ax=ax_hist, color='y')
ax_box.set(yticks=[])
sns.despine(ax=ax_hist)
sns.despine(ax=ax_box, left=True)
plt.title('4N Fuel per Day per Adult')
plt.ylim(top=2)
plt.ylim(bottom = 0)

fig, ax = plt.subplots()
plt.title('No-Hood Fuel per Day per Adult')
plt.hold(True)

quant_1_1N = np.percentile(Fuel_per_day_per_adult_1N, [25,75])
Top_lim_1_1N = quant_1_1N[1] + 1.5*(quant_1_1N[1] - quant_1_1N[0])
Low_lim_1_1N = quant_1_1N[0] - 1.5*(quant_1_1N[1] - quant_1_1N[0])

bp_1 = plt.boxplot(Fuel_per_day_per_adult_1N, positions = [1], widths = 0.6)
for v,a in enumerate(Fuel_per_day_per_adult_1N):
    if a > Top_lim_1_1N or a < Low_lim_1_1N:
        plt.text(1,a,f_d_a_1N[v])
plt.text(1,0.1,'1N',color='b')
    
    
quant_1_2N = np.percentile(Fuel_per_day_per_adult_2N, [25,75])
Top_lim_1_2N = quant_1_2N[1] + 1.5*(quant_1_2N[1] - quant_1_2N[0])
Low_lim_1_2N = quant_1_2N[0] - 1.5*(quant_1_2N[1] - quant_1_2N[0])

bp_1 = plt.boxplot(Fuel_per_day_per_adult_2N,positions = [2], widths = 0.6)
for v,a in enumerate(Fuel_per_day_per_adult_2N):
    if a > Top_lim_1_2N or a < Low_lim_1_2N:
        plt.text(2,a,f_d_a_2N[v])
plt.text(2,0.1,'2N', color= 'g')

quant_1_3N = np.percentile(Fuel_per_day_per_adult_3N, [25,75])
Top_lim_1_3N = quant_1_3N[1] + 1.5*(quant_1_3N[1] - quant_1_3N[0])
Low_lim_1_3N = quant_1_3N[0] - 1.5*(quant_1_3N[1] - quant_1_3N[0])

bp_1 = plt.boxplot(Fuel_per_day_per_adult_3N,positions = [3], widths = 0.6)
count = 0
for v,a in enumerate(Fuel_per_day_per_adult_3N):
    
    if a > Top_lim_1_3N or a < Low_lim_1_3N:
        count = count + 1
        if count == 2:
            plt.text(3,a,f_d_a_3N[v],ha='left',va='bottom')
        elif count != 2:
            plt.text(3,a,f_d_a_3N[v],ha='right',va='bottom')
plt.text(3,0.1,'3N', color='r')        


quant_1_4N = np.percentile(Fuel_per_day_per_adult_4N, [25,75])
Top_lim_1_4N = quant_1_4N[1] + 1.5*(quant_1_4N[1] - quant_1_4N[0])
Low_lim_1_4N = quant_1_4N[0] - 1.5*(quant_1_4N[1] - quant_1_4N[0])

bp_1 = plt.boxplot(Fuel_per_day_per_adult_4N,positions = [4], widths = 0.6)
for v,a in enumerate(Fuel_per_day_per_adult_4N):
    if a > Top_lim_1_4N or a < Low_lim_1_4N:
        plt.text(4,a,f_d_a_4N[v])
plt.text(4,0.1,'4N', color='y')        
        
plt.xlim(0,5)
plt.ylim(0,2.3)

phase = ['1N' ,'2N', '3N', '4N']
Colors = ['blue', 'green', 'red', 'yellow']
for patch, colo  in (bp_1, Colors):
    patch.set_facecolor(colo)


plt.show()

# fuction for 