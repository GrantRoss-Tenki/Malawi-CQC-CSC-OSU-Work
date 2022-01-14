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
Hood_or_no = 'no_hood'   # 'no_hood' or 'hood'
#what household do you want to remove make sure it is in ascending order
# if there is nothing, then put a placeholder of 1045 or higher
Household_removal = [1045]
#Household_removal = Household_removal.sort(reverse=False)
if Hood_or_no == 'hood':
    C_Place_holder = 2001
else:
    C_Place_holder = 1001
    
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


print('---------------Fuel per Day per Adult No-Hood Phase---------------------')
if Hood_or_no == 'no_hood':
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
        if c == (Household_removal[count] - C_Place_holder):
            count = count + 1
            if count == len(Household_removal):
                count = 0
            continue
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
    # percentage Change of Fuel per day between the phases
    Fuel_per_day_per_adult_2N_1N = []
    f_d_a_2N_1N = []
    Fuel_per_day_per_adult_3N_1N = []
    f_d_a_3N_1N = []
    Fuel_per_day_per_adult_4N_1N = []
    f_d_a_4N_1N = []
    
    Fuel_per_day_per_adult_3N_2N = []
    f_d_a_3N_2N = []
    Fuel_per_day_per_adult_4N_3N = []
    f_d_a_4N_3N = []
    Fuel_per_day_per_adult_4N_2N = []
    f_d_a_4N_2N = []
    print('-------- what is out of index 4N------', Fuel_per_day_per_adult_4N[32])
    print('-------- what is out of index 1N------', Fuel_per_day_per_adult_1N[32])
    count = 0
    for c in NO_hood_counter:
        if c == (Household_removal[count] - C_Place_holder):
            count = count + 1
            if count == len(Household_removal):
                count = 0
            continue
        if (len(Fuel_per_day_per_adult_2N)-1) >= c and (len(Fuel_per_day_per_adult_1N)-1) >= c:
            if Day_1N.iloc[c,13] > 0 and Day_2N.iloc[c,13]  > 0 and Day_1N.iloc[c,0] == Day_2N.iloc[c,0]:
                Fuel_per_day_per_adult_2N_1N.append(Fuel_per_day_per_adult_2N[c]/Fuel_per_day_per_adult_1N[c])
                f_d_a_2N_1N.append(Day_1N.iloc[c,0])
        if (len(Fuel_per_day_per_adult_3N)-1) >= c and (len(Fuel_per_day_per_adult_1N)-1) >= c:
            if Day_3N.iloc[c,13] > 0 and Day_1N.iloc[c,13]  > 0 and Day_3N.iloc[c,0] == Day_1N.iloc[c,0]:
                Fuel_per_day_per_adult_3N_1N.append(Fuel_per_day_per_adult_3N[c]/Fuel_per_day_per_adult_1N[c])
                f_d_a_3N_1N.append(Day_1N.iloc[c,0])
        if (len(Fuel_per_day_per_adult_4N)-1) >= c and (len(Fuel_per_day_per_adult_1N)-1) >= c:
            if Day_4N.iloc[c,13] > 0 and Day_1N.iloc[c,13]  > 0 and Day_4N.iloc[c,0] == Day_1N.iloc[c,0]:
                Fuel_per_day_per_adult_4N_1N.append(Fuel_per_day_per_adult_4N[c]/Fuel_per_day_per_adult_1N[c])
                f_d_a_4N_1N.append(Day_1N.iloc[c,0])
        if (len(Fuel_per_day_per_adult_3N)-1) >= c and (len(Fuel_per_day_per_adult_2N)-1) >= c:
            if Day_3N.iloc[c,13] > 0 and Day_2N.iloc[c,13]  > 0 and Day_3N.iloc[c,0] == Day_2N.iloc[c,0]:
                Fuel_per_day_per_adult_3N_2N.append(Fuel_per_day_per_adult_3N[c]/Fuel_per_day_per_adult_2N[c])
                f_d_a_3N_2N.append(Day_2N.iloc[c,0])
        if (len(Fuel_per_day_per_adult_4N)-1) >= c and (len(Fuel_per_day_per_adult_3N)-1) >= c:
            if Day_4N.iloc[c,13] > 0 and Day_3N.iloc[c,13]  > 0 and Day_4N.iloc[c,0] == Day_3N.iloc[c,0]:
                Fuel_per_day_per_adult_4N_3N.append(Fuel_per_day_per_adult_4N[c]/Fuel_per_day_per_adult_3N[c])
                f_d_a_4N_3N.append(Day_3N.iloc[c,0])
        if (len(Fuel_per_day_per_adult_4N)-1) >= c and (len(Fuel_per_day_per_adult_2N)-1) >= c:
            if Day_4N.iloc[c,13] > 0 and Day_2N.iloc[c,13]  > 0 and Day_4N.iloc[c,0] == Day_2N.iloc[c,0]:
                Fuel_per_day_per_adult_4N_2N.append(Fuel_per_day_per_adult_4N[c]/Fuel_per_day_per_adult_2N[c])
                f_d_a_4N_2N.append(Day_4N.iloc[c,0])
    
    
    
    # now for box plotting for Fuel per day beteen Phases
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
    
    
    #Plotting on the same graph
    fig, ax = plt.subplots()
    plt.title('No-Hood Fuel per Day per Adult')
    plt.hold(True)
    #1N
    quant_1_1N = np.percentile(Fuel_per_day_per_adult_1N, [25,50,75])
    Top_lim_1_1N = quant_1_1N[2] + 1.5*(quant_1_1N[2] - quant_1_1N[0])
    Low_lim_1_1N = quant_1_1N[0] - 1.5*(quant_1_1N[2] - quant_1_1N[0])
    
    bp_1 = plt.boxplot(Fuel_per_day_per_adult_1N, positions = [1], widths = 0.6)
    for v,a in enumerate(Fuel_per_day_per_adult_1N):
        if a > Top_lim_1_1N or a < Low_lim_1_1N:
            plt.text(1,a,f_d_a_1N[v])
    plt.text(1,0.1,'1N',color='b')

    #2N    
    quant_1_2N = np.percentile(Fuel_per_day_per_adult_2N, [25,50,75])
    Top_lim_1_2N = quant_1_2N[2] + 1.5*(quant_1_2N[2] - quant_1_2N[0])
    Low_lim_1_2N = quant_1_2N[0] - 1.5*(quant_1_2N[2] - quant_1_2N[0])
    
    bp_1 = plt.boxplot(Fuel_per_day_per_adult_2N,positions = [2], widths = 0.6)
    for v,a in enumerate(Fuel_per_day_per_adult_2N):
        if a > Top_lim_1_2N or a < Low_lim_1_2N:
            plt.text(2,a,f_d_a_2N[v])
    plt.text(2,0.1,'2N', color= 'g')
    #3N
    quant_1_3N = np.percentile(Fuel_per_day_per_adult_3N, [25,50,75])
    Top_lim_1_3N = quant_1_3N[2] + 1.5*(quant_1_3N[2] - quant_1_3N[0])
    Low_lim_1_3N = quant_1_3N[0] - 1.5*(quant_1_3N[2] - quant_1_3N[0])
    
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
    
    #4N
    quant_1_4N = np.percentile(Fuel_per_day_per_adult_4N, [25,50,75])
    Top_lim_1_4N = quant_1_4N[2] + 1.5*(quant_1_4N[2] - quant_1_4N[0])
    Low_lim_1_4N = quant_1_4N[0] - 1.5*(quant_1_4N[2] - quant_1_4N[0])
    
    bp_1 = plt.boxplot(Fuel_per_day_per_adult_4N,positions = [4], widths = 0.6)
    for v,a in enumerate(Fuel_per_day_per_adult_4N):
        if a > Top_lim_1_4N or a < Low_lim_1_4N:
            plt.text(4,a,f_d_a_4N[v])
    plt.text(4,0.1,'4N', color='y')        
            
    plt.xlim(0,5)
    plt.ylim(0,2.3)
    
    plt.show()



    # % change of fuel per day per adult between each phase
    fig_2, ax2 = plt.subplots()
    plt.title('% No_hood Change from Fuel per Day per Adult' )
    #plt.hold(True)
    #2N to 1N
    quant_1_2N_1N = np.percentile(Fuel_per_day_per_adult_2N_1N, [25,50,75])
    Top_lim_1_2N_1N = quant_1_2N_1N[2] + 1.5*(quant_1_2N_1N[2]-quant_1_2N_1N[0])
    Low_lim_1_2N_1N = quant_1_2N_1N[0] - 1.5*(quant_1_2N_1N[2]-quant_1_2N_1N[0])

    bp_1_1 = plt.boxplot(Fuel_per_day_per_adult_2N_1N, positions=[1], widths= 0.6)
    for v,a in enumerate(Fuel_per_day_per_adult_2N_1N):
        if a > Top_lim_1_2N_1N or a < Low_lim_1_2N_1N:
            plt.text(1, a, f_d_a_2N_1N[v])
    plt.text(0.5, 0, '2N / 1N', color= 'g')
    
    #3N to 1N
    quant_1_3N_1N = np.percentile(Fuel_per_day_per_adult_3N_1N, [25,50,75])
    Top_lim_1_3N_1N = quant_1_3N_1N[2] + 1.5*(quant_1_3N_1N[2]-quant_1_3N_1N[0])
    Low_lim_1_3N_1N = quant_1_3N_1N[0] - 1.5*(quant_1_3N_1N[2]-quant_1_3N_1N[0])

    bp_1_1 = plt.boxplot(Fuel_per_day_per_adult_3N_1N, positions=[2], widths= 0.6)
    for v,a in enumerate(Fuel_per_day_per_adult_3N_1N):
        if a > Top_lim_1_3N_1N or a < Low_lim_1_3N_1N:
            plt.text(2, a, f_d_a_3N_1N[v])
    plt.text(1.5, 0, '3N / 1N', color= 'r')
    
    #4N to 1N
    quant_1_4N_1N = np.percentile(Fuel_per_day_per_adult_4N_1N, [25,50,75])
    Top_lim_1_4N_1N = quant_1_4N_1N[2] + 1.5*(quant_1_4N_1N[2]-quant_1_4N_1N[0])
    Low_lim_1_4N_1N = quant_1_4N_1N[0] - 1.5*(quant_1_4N_1N[2]-quant_1_4N_1N[0])

    bp_1_1 = plt.boxplot(Fuel_per_day_per_adult_4N_1N, positions=[3], widths= 0.6)
    for v,a in enumerate(Fuel_per_day_per_adult_4N_1N):
        if a > Top_lim_1_4N_1N or a < Low_lim_1_4N_1N:
            plt.text(3, a, f_d_a_4N_1N[v])
    plt.text(2.5, 0, '4N / 1N', color= 'y')
    
    #3N to 2N
    quant_1_3N_2N = np.percentile(Fuel_per_day_per_adult_3N_2N, [25,50,75])
    Top_lim_1_3N_2N = quant_1_3N_2N[2] + 1.5*(quant_1_3N_2N[2]-quant_1_3N_2N[0])
    Low_lim_1_3N_2N = quant_1_3N_2N[0] - 1.5*(quant_1_3N_2N[2]-quant_1_3N_2N[0])

    bp_1_1 = plt.boxplot(Fuel_per_day_per_adult_3N_2N, positions=[4], widths= 0.6)
    for v,a in enumerate(Fuel_per_day_per_adult_3N_2N):
        if a > Top_lim_1_3N_2N or a < Low_lim_1_3N_2N:
            plt.text(4, a, f_d_a_3N_2N[v])
    plt.text(3.5, 0, '3N / 2N', color= 'm')
    
    #4N to 3N
    quant_1_4N_3N = np.percentile(Fuel_per_day_per_adult_4N_3N, [25,50,75])
    Top_lim_1_4N_3N = quant_1_4N_3N[2] + 1.5*(quant_1_4N_3N[2]-quant_1_4N_3N[0])
    Low_lim_1_4N_3N = quant_1_4N_3N[0] - 1.5*(quant_1_4N_3N[2]-quant_1_4N_3N[0])

    bp_1_1 = plt.boxplot(Fuel_per_day_per_adult_4N_3N, positions=[5], widths= 0.6)
    for v,a in enumerate(Fuel_per_day_per_adult_4N_3N):
        if a > Top_lim_1_4N_3N or a < Low_lim_1_4N_3N:
            plt.text(5, a, f_d_a_4N_3N[v])
    plt.text(4.5, 0, '4N / 3N', color= 'k')
    
    #4N to 2N
    quant_1_4N_2N = np.percentile(Fuel_per_day_per_adult_4N_2N, [25,50,75])
    Top_lim_1_4N_2N = quant_1_4N_2N[2] + 1.5*(quant_1_4N_2N[2]-quant_1_4N_2N[0])
    Low_lim_1_4N_2N = quant_1_4N_2N[0] - 1.5*(quant_1_4N_2N[2]-quant_1_4N_2N[0])

    bp_1_1 = plt.boxplot(Fuel_per_day_per_adult_4N_2N, positions=[6], widths= 0.6)
    for v,a in enumerate(Fuel_per_day_per_adult_4N_2N):
        if a > Top_lim_1_4N_2N or a < Low_lim_1_4N_2N:
            plt.text(6, a, f_d_a_4N_2N[v])
    plt.text(5.5, 0, '4N / 2N', color= 'tab:orange')
    
    
    plt.xlim(0,7)
    plt.ylim(-0.5,4)
    plt.show()
    
    D_50_quant_phase_f_d_a = {'Percentile %': [25,50,75], '1N': quant_1_1N, '2N': quant_1_2N,'3N' : quant_1_3N,'4N': quant_1_4N}
    F_D_A_50_phase_no_hood = pd.DataFrame(data=D_50_quant_phase_f_d_a)
    D_50_quant_percent_f_d_a ={'Percentile %': [25,50,75],'2N / 1N': quant_1_2N_1N,'3N / 1N': quant_1_3N_1N,'4N / 1N': quant_1_4N_1N,
                               '3N / 2N': quant_1_3N_2N,'4N / 3N': quant_1_4N_3N,'4N / 2N': quant_1_4N_2N}
    F_D_A_50_percent_change_no_hood = pd.DataFrame(data=D_50_quant_percent_f_d_a)

# add more
print ('-------------------Fuel per Day per Adult Hood Phse -------------------')

if Hood_or_no == 'hood':
    Fuel_per_day_per_adult_1H = []
    f_d_a_1H = []
    Fuel_per_day_per_adult_2H = []
    f_d_a_2H = []
    Fuel_per_day_per_adult_3H = []
    f_d_a_3H = []
    
    count = 0
    for c in hood_counter:
        if c == (Household_removal[count] - C_Place_holder):
            count = count + 1
            if count == len(Household_removal):
                count = 0
            continue
        if Day_1H.iloc[c,13] != -1.00:
            Fuel_per_day_per_adult_1H.append(Day_1H.iloc[c,13]/Survey_1H.iloc[c,7])
            f_d_a_1H.append(Day_1H.iloc[c,0])
            
        if Day_2H.iloc[c, 13] != -1.00:
            Fuel_per_day_per_adult_2H.append(Day_2H.iloc[c, 13] / Survey_2H.iloc[c, 7])
            f_d_a_2H.append(Day_2H.iloc[c,0])
            
        if Day_3H.iloc[c, 13] != -1.00:
            Fuel_per_day_per_adult_3H.append(Day_3H.iloc[c, 13] / Survey_3H.iloc[c, 7])
            f_d_a_3H.append(Day_3H.iloc[c, 0])
    
    # percentage Change of Fuel per day between the phases
    Fuel_per_day_per_adult_2H_1H = []
    f_d_a_2H_1H = []
    Fuel_per_day_per_adult_3H_1H = []
    f_d_a_3H_1H = []
    Fuel_per_day_per_adult_3H_2H = []
    f_d_a_3H_2H = []
    
    count = 0
    for c in NO_hood_counter:
        if c == (Household_removal[count] - C_Place_holder):
            count = count + 1
            if count == len(Household_removal):
                count = 0
            continue
        if (len(Fuel_per_day_per_adult_2H)-1) >= c and (len(Fuel_per_day_per_adult_1H)-1) >= c:
            if Day_1H.iloc[c,13] > 0 and Day_2H.iloc[c,13]  > 0 and Day_1H.iloc[c,0] == Day_2H.iloc[c,0]:
                Fuel_per_day_per_adult_2H_1H.append(Fuel_per_day_per_adult_2H[c]/Fuel_per_day_per_adult_1H[c])
                f_d_a_2H_1H.append(Day_1H.iloc[c,0])
        if (len(Fuel_per_day_per_adult_3H)-1) >= c and (len(Fuel_per_day_per_adult_1H)-1) >= c:
            if Day_3H.iloc[c,13] > 0 and Day_1H.iloc[c,13]  > 0 and Day_3H.iloc[c,0] == Day_1H.iloc[c,0]:
                Fuel_per_day_per_adult_3H_1H.append(Fuel_per_day_per_adult_3H[c]/Fuel_per_day_per_adult_1H[c])
                f_d_a_3H_1H.append(Day_1H.iloc[c,0]) 
        if (len(Fuel_per_day_per_adult_3H)-1) >= c and (len(Fuel_per_day_per_adult_2H)-1) >= c:
            if Day_3H.iloc[c,13] > 0 and Day_2H.iloc[c,13]  > 0 and Day_3H.iloc[c,0] == Day_2H.iloc[c,0]:
                Fuel_per_day_per_adult_3H_2H.append(Fuel_per_day_per_adult_3H[c]/Fuel_per_day_per_adult_2H[c])
                f_d_a_3H_2H.append(Day_1H.iloc[c,0])
    
    # now for plotting
    #1H
    sns.set(style="ticks")
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)})
    sns.boxplot(Fuel_per_day_per_adult_1H, ax=ax_box, color='b')
    sns.distplot(Fuel_per_day_per_adult_1H, ax=ax_hist, color='b')
    ax_box.set(yticks=[])
    sns.despine(ax=ax_hist)
    sns.despine(ax=ax_box, left=True)
    plt.title('1H Fuel per Day per Adult')
    plt.ylim(top=2)
    plt.ylim(bottom = 0)
    
    #2H
    sns.set(style="ticks")
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)})
    sns.boxplot(Fuel_per_day_per_adult_2H, ax=ax_box, color='g')
    sns.distplot(Fuel_per_day_per_adult_2H, ax=ax_hist, color='g')
    ax_box.set(yticks=[])
    sns.despine(ax=ax_hist)
    sns.despine(ax=ax_box, left=True)
    plt.title('2H Fuel per Day per Adult')
    plt.ylim(top=2)
    plt.ylim(bottom = 0)
    
    #3H
    sns.set(style="ticks")
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)})
    sns.boxplot(Fuel_per_day_per_adult_3H, ax=ax_box, color='r')
    sns.distplot(Fuel_per_day_per_adult_3H, ax=ax_hist, color='r')
    ax_box.set(yticks=[])
    sns.despine(ax=ax_hist)
    sns.despine(ax=ax_box, left=True)
    plt.title('3H Fuel per Day per Adult')
    plt.ylim(top=2)
    plt.ylim(bottom = 0)
    
    fig_2, ax_2 = plt.subplots()
    plt.title('Hood Fuel per Day per Adult')
    #plt.hold(True)
    
    quant_1_1H = np.percentile(Fuel_per_day_per_adult_1H, [25,50,75])
    Top_lim_1_1H = quant_1_1H[2] + 1.5*(quant_1_1H[2] - quant_1_1H[0])
    Low_lim_1_1H = quant_1_1H[0] - 1.5*(quant_1_1H[2] - quant_1_1H[0])
    
    bp_1 = plt.boxplot(Fuel_per_day_per_adult_1H, positions = [1], widths = 0.6)
    for v,a in enumerate(Fuel_per_day_per_adult_1H):
        if a > Top_lim_1_1H or a < Low_lim_1_1H:
            plt.text(1,a,f_d_a_1H[v])
    plt.text(1,0,'1H',color='b')
        
        
    quant_1_2H = np.percentile(Fuel_per_day_per_adult_2H, [25,50,75])
    Top_lim_1_2H = quant_1_2H[2] + 1.5*(quant_1_2H[2] - quant_1_2H[0])
    Low_lim_1_2H = quant_1_2H[0] - 1.5*(quant_1_2H[2] - quant_1_2H[0])
    
    bp_1 = plt.boxplot(Fuel_per_day_per_adult_2H,positions = [2], widths = 0.6)
    count = 0
    for v,a in enumerate(Fuel_per_day_per_adult_2H):
        if a > Top_lim_1_2H or a < Low_lim_1_2H:
            count = count + 1
            if count == 1:
                plt.text(2,a,f_d_a_2H[v],ha='left',va='bottom')
            elif count !=1:
                plt.text(2,a,f_d_a_2H[v],ha='right',va='bottom')
    plt.text(2,0,'2H', color= 'g')
    
    quant_1_3H = np.percentile(Fuel_per_day_per_adult_3H, [25,50,75])
    Top_lim_1_3H = quant_1_3H[2] + 1.5*(quant_1_3H[2] - quant_1_3H[0])
    Low_lim_1_3H = quant_1_3H[0] - 1.5*(quant_1_3H[2] - quant_1_3H[0])
    
    bp_1 = plt.boxplot(Fuel_per_day_per_adult_3H,positions = [3], widths = 0.6)
    count = 0
    for v,a in enumerate(Fuel_per_day_per_adult_3H):
        if a > Top_lim_1_3H or a < Low_lim_1_3H:
            count = count + 1
            if count == 3:
                plt.text(3,a,f_d_a_3H[v],ha='left',va='bottom')
            elif count != 1:
                plt.text(3,a,f_d_a_3H[v],ha='right',va='bottom')
    plt.text(3,0,'3H', color='r')        
    
    
    plt.xlim(-0,4)
    plt.ylim(-0.25,2.5)
    
    plt.show()
    
    
    #% change of fuel perday per adult between each phase 
    fig_2, ax2 = plt.subplots()
    plt.title('% No_hood Change from Fuel per Day per Adult' )
    #plt.hold(True)
    #2H to 1H
    quant_1_2H_1H = np.percentile(Fuel_per_day_per_adult_2H_1H, [25,50,75])
    Top_lim_1_2H_1H = quant_1_2H_1H[2] + 1.5*(quant_1_2H_1H[2]-quant_1_2H_1H[0])
    Low_lim_1_2H_1H = quant_1_2H_1H[0] - 1.5*(quant_1_2H_1H[2]-quant_1_2H_1H[0])

    bp_1_1 = plt.boxplot(Fuel_per_day_per_adult_2H_1H, positions=[1], widths= 0.6)
    for v,a in enumerate(Fuel_per_day_per_adult_2H_1H):
        if a > Top_lim_1_2H_1H or a < Low_lim_1_2H_1H:
            plt.text(1, a, f_d_a_2H_1H[v])
    plt.text(0.75, -0.25, '2H / 1H', color= 'g')
    
    #3H to 1H
    quant_1_3H_1H = np.percentile(Fuel_per_day_per_adult_3H_1H, [25,50,75])
    Top_lim_1_3H_1H = quant_1_3H_1H[2] + 1.5*(quant_1_3H_1H[2]-quant_1_3H_1H[0])
    Low_lim_1_3H_1H = quant_1_3H_1H[0] - 1.5*(quant_1_3H_1H[2]-quant_1_3H_1H[0])

    bp_1_1 = plt.boxplot(Fuel_per_day_per_adult_3H_1H, positions=[2], widths= 0.6)
    for v,a in enumerate(Fuel_per_day_per_adult_3H_1H):
        if a > Top_lim_1_3H_1H or a < Low_lim_1_3H_1H:
            plt.text(2, a, f_d_a_3H_1H[v])
    plt.text(1.75, -0.25, '3H / 1H', color= 'r')
    
    #3H to 2H
    quant_1_3H_2H = np.percentile(Fuel_per_day_per_adult_3H_2H, [25,50,75])
    Top_lim_1_3H_2H = quant_1_3H_2H[2] + 1.5*(quant_1_3H_2H[2]-quant_1_3H_2H[0])
    Low_lim_1_3H_2H = quant_1_3H_2H[0] - 1.5*(quant_1_3H_2H[2]-quant_1_3H_2H[0])

    bp_1_1 = plt.boxplot(Fuel_per_day_per_adult_3H_2H, positions=[3], widths= 0.6)
    for v,a in enumerate(Fuel_per_day_per_adult_3H_2H):
        if a > Top_lim_1_3H_2H or a < Low_lim_1_3H_2H:
            plt.text(3, a, f_d_a_3H_2H[v])
    plt.text(2.75, -0.25, '2H / 1H', color= 'm')
    
    plt.xlim(-0,4)
    plt.ylim(-0.25,6)
    plt.show()
    
    
    D_50_quant_phase_f_d_a_hood = {'Percentile %': [25,50,75], '1H': quant_1_1H, '2H': quant_1_2H,'3H' : quant_1_3H}
    F_D_A_50_phase_hood = pd.DataFrame(data=D_50_quant_phase_f_d_a_hood)
    
    D_50_quant_percent_f_d_a_hood ={'Percentile %': [25,50,75],'2H / 1H': quant_1_2H_1H,'3H / 1H': quant_1_3H_1H,'3H / 2H': quant_1_3H_2H}
    F_D_A_50_percent_change_hood = pd.DataFrame(data=D_50_quant_percent_f_d_a_hood)


print('----------------------- Kitchen PM per Day -----------------------------')
if Hood_or_no == 'no_hood':
    Kit_PM_per_day_1N = []
    K_PM_D_1N = []
    Kit_PM_per_day_2N = []
    K_PM_D_2N = []
    Kit_PM_per_day_3N = []
    K_PM_D_3N = []
    Kit_PM_per_day_4N = []
    K_PM_D_4N = []
    count = 0
    for c in NO_hood_counter:
        if c == (Household_removal[count] - C_Place_holder):
            count = count + 1
            if count == len(Household_removal):
                count = 0
            continue
        if Day_1N.iloc[c,7] != -1.00:
            Kit_PM_per_day_1N.append(Day_1N.iloc[c,7]/Day_1N.iloc[c,1])
            K_PM_D_1N.append(Day_1N.iloc[c,0])
        if Day_2N.iloc[c, 7] != -1.00:
            Kit_PM_per_day_2N.append(Day_2N.iloc[c,7]/Day_2N.iloc[c,1])
            K_PM_D_2N.append(Day_2N.iloc[c,0])
        if Day_3N.iloc[c, 7] != -1.00:
            Kit_PM_per_day_3N.append(Day_3N.iloc[c,7]/Day_3N.iloc[c,1])
            K_PM_D_3N.append(Day_3N.iloc[c, 0])
        if Day_4N.iloc[c, 7] != -1.00:
            Kit_PM_per_day_4N.append(Day_4N.iloc[c,7]/Day_4N.iloc[c,1])
            K_PM_D_4N.append(Day_4N.iloc[c, 0])
            
     
    # percentages Between Phases of kitchen PM per day
    Kit_per_day_2N_1N = []
    K_PM_D_2N_1N = []
    Kit_per_day_3N_1N = []
    K_PM_D_3N_1N = []
    Kit_per_day_4N_1N = []
    K_PM_D_4N_1N = []
    
    Kit_per_day_3N_2N = []
    K_PM_D_3N_2N = []
    Kit_per_day_4N_3N = []
    K_PM_D_4N_3N = []
    Kit_per_day_4N_2N = []
    K_PM_D_4N_2N = []

    count = 0
    for c in NO_hood_counter:
        if c == (Household_removal[count] - C_Place_holder):
            count = count + 1
            if count == len(Household_removal):
                count = 0
            continue
        if (len(Kit_PM_per_day_2N)-1) >= c and (len(Kit_PM_per_day_1N)-1) >= c:
            if Day_1N.iloc[c,7] > 0 and Day_2N.iloc[c,7]  > 0 and Day_1N.iloc[c,0] == Day_2N.iloc[c,0]:
                Kit_per_day_2N_1N.append(Kit_PM_per_day_2N[c]/Kit_PM_per_day_1N[c])
                K_PM_D_2N_1N.append(Day_1N.iloc[c,0])
        if (len(Kit_PM_per_day_3N)-1) >= c and (len(Kit_PM_per_day_1N)-1) >= c:
            if Day_3N.iloc[c,7] > 0 and Day_1N.iloc[c,7]  > 0 and Day_3N.iloc[c,0] == Day_1N.iloc[c,0]:
                Kit_per_day_3N_1N.append(Kit_PM_per_day_3N[c]/Kit_PM_per_day_1N[c])
                K_PM_D_3N_1N.append(Day_1N.iloc[c,0])
        if (len(Kit_PM_per_day_4N)-1) >= c and (len(Kit_PM_per_day_1N)-1) >= c:
            if Day_4N.iloc[c,7] > 0 and Day_1N.iloc[c,7]  > 0 and Day_4N.iloc[c,0] == Day_1N.iloc[c,0]:
                Kit_per_day_4N_1N.append(Kit_PM_per_day_4N[c]/Kit_PM_per_day_1N[c])
                K_PM_D_4N_1N.append(Day_1N.iloc[c,0])
        
        if (len(Kit_PM_per_day_3N)-1) >= c and (len(Kit_PM_per_day_2N)-1) >= c:
            if Day_3N.iloc[c,7] > 0 and Day_2N.iloc[c,7]  > 0 and Day_3N.iloc[c,0] == Day_2N.iloc[c,0]:
                Kit_per_day_3N_2N.append(Kit_PM_per_day_3N[c]/Kit_PM_per_day_2N[c])
                K_PM_D_3N_2N.append(Day_2N.iloc[c,0])
        if (len(Kit_PM_per_day_4N)-1) >= c and (len(Kit_PM_per_day_3N)-1) >= c:
            if Day_4N.iloc[c,7] > 0 and Day_3N.iloc[c,7]  > 0 and Day_4N.iloc[c,0] == Day_3N.iloc[c,0]:
                Kit_per_day_4N_3N.append(Kit_PM_per_day_4N[c]/Kit_PM_per_day_3N[c])
                K_PM_D_4N_3N.append(Day_3N.iloc[c,0])
        if (len(Kit_PM_per_day_4N)-1) >= c and (len(Kit_PM_per_day_2N)-1) >= c:
            if Day_4N.iloc[c,7] > 0 and Day_2N.iloc[c,7]  > 0 and Day_4N.iloc[c,0] == Day_2N.iloc[c,0]:
                Kit_per_day_4N_2N.append(Kit_PM_per_day_4N[c]/Kit_PM_per_day_2N[c])
                K_PM_D_4N_2N.append(Day_4N.iloc[c,0])
      
    # now for box plotting for Kitchen PM per day percent changes
    
    #2N to 1N
    sns.set(style="ticks")
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)})
    sns.boxplot(Kit_per_day_2N_1N, ax=ax_box, color='g')
    sns.distplot(Kit_per_day_2N_1N, ax=ax_hist, color='g')
    ax_box.set(yticks=[])
    sns.despine(ax=ax_hist)
    sns.despine(ax=ax_box, left=True)
    plt.title('% 2N/1N (Kitchen PM per Day)')
    plt.ylim(top=1)
    plt.ylim(bottom = 0)
    
    #3N to 1N  
    sns.set(style="ticks")
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)})
    sns.boxplot(Kit_per_day_3N_1N, ax=ax_box, color='r')
    sns.distplot(Kit_per_day_3N_1N, ax=ax_hist, color='r')
    ax_box.set(yticks=[])
    sns.despine(ax=ax_hist)
    sns.despine(ax=ax_box, left=True)
    plt.title('% 3N/1N (Kitchen PM per Day)')
    plt.ylim(top=1.5)
    plt.ylim(bottom = 0)
    #4N to 1N
    sns.set(style="ticks")
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)})
    sns.boxplot(Kit_per_day_4N_1N, ax=ax_box, color='y')
    sns.distplot(Kit_per_day_4N_1N, ax=ax_hist, color='y')
    ax_box.set(yticks=[])
    sns.despine(ax=ax_hist)
    sns.despine(ax=ax_box, left=True)
    plt.title('% 4N/1N (Kitchen PM per Day)')
    plt.ylim(top=1.5)
    plt.ylim(bottom = 0)
    
    #3N to 2N 
    sns.set(style="ticks")
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)})
    sns.boxplot(Kit_per_day_3N_2N, ax=ax_box, color='m')
    sns.distplot(Kit_per_day_3N_2N, ax=ax_hist, color='m')
    ax_box.set(yticks=[])
    sns.despine(ax=ax_hist)
    sns.despine(ax=ax_box, left=True)
    plt.title('% 3N/2N (Kitchen PM per Day)')
    plt.ylim(top=1)
    plt.ylim(bottom = 0)
    #4N to 3N 
    sns.set(style="ticks")
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)})
    sns.boxplot(Kit_per_day_4N_3N, ax=ax_box, color='k')
    sns.distplot(Kit_per_day_4N_3N, ax=ax_hist, color='k')
    ax_box.set(yticks=[])
    sns.despine(ax=ax_hist)
    sns.despine(ax=ax_box, left=True)
    plt.title('% 4N/3N (Kitchen PM per Day)')
    plt.ylim(top=0.5)
    plt.ylim(bottom = 0)
    #4N to 2N 
    sns.set(style="ticks")
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.15, 0.85)})
    sns.boxplot(Kit_per_day_4N_2N, ax=ax_box, color='tab:orange')
    sns.distplot(Kit_per_day_4N_2N, ax=ax_hist, color='tab:orange')
    ax_box.set(yticks=[])
    sns.despine(ax=ax_hist)
    sns.despine(ax=ax_box, left=True)
    plt.title('% 4N/2N (Kitchen PM per Day)')
    plt.ylim(top=0.75)
    plt.ylim(bottom = 0)
    
    
    #Plotting on the same graph
    fig, ax = plt.subplots()
    plt.title('No-Hood Kitchen PM per day')
    plt.hold(True)
    #1N
    quant_1_1N = np.percentile(Kit_PM_per_day_1N, [25,50,75])
    Top_lim_1_1N = quant_1_1N[2] + 1.5*(quant_1_1N[2] - quant_1_1N[0])
    Low_lim_1_1N = quant_1_1N[0] - 1.5*(quant_1_1N[2] - quant_1_1N[0])
    
    bp_1 = plt.boxplot(Kit_PM_per_day_1N, positions = [1], widths = 0.6)
    for v,a in enumerate(Kit_PM_per_day_1N):
        if a > Top_lim_1_1N or a < Low_lim_1_1N:
            plt.text(1,a,K_PM_D_1N[v])
    plt.text(1,0.1,'1N',color='b')

    #2N    
    quant_1_2N = np.percentile(Kit_PM_per_day_2N, [25,50,75])
    Top_lim_1_2N = quant_1_2N[2] + 1.5*(quant_1_2N[2] - quant_1_2N[0])
    Low_lim_1_2N = quant_1_2N[0] - 1.5*(quant_1_2N[2] - quant_1_2N[0])
    
    bp_1 = plt.boxplot(Kit_PM_per_day_2N,positions = [2], widths = 0.6)
    for v,a in enumerate(Kit_PM_per_day_2N):
        if a > Top_lim_1_2N or a < Low_lim_1_2N:
            plt.text(2,a,K_PM_D_2N[v])
    plt.text(2,0.1,'2N', color= 'g')
    #3N
    quant_1_3N = np.percentile(Kit_PM_per_day_3N, [25,50,75])
    Top_lim_1_3N = quant_1_3N[2] + 1.5*(quant_1_3N[2] - quant_1_3N[0])
    Low_lim_1_3N = quant_1_3N[0] - 1.5*(quant_1_3N[2] - quant_1_3N[0])
    kitchen_3N_outlier = []
    bp_1 = plt.boxplot(Kit_PM_per_day_3N,positions = [3], widths = 0.6)
    count = 0
    for v,a in enumerate(Kit_PM_per_day_3N):
        if a > Top_lim_1_3N or a < Low_lim_1_3N:
            kitchen_3N_outlier.append(K_PM_D_3N[v])
            count = count + 1
            if count == (3):
                plt.text(3,a,K_PM_D_3N[v],ha='left', va='bottom')
            if count == (1):
                plt.text(3,a,K_PM_D_3N[v],ha='left', va='top')
            else:
                plt.text(3,a,K_PM_D_3N[v],ha='right', va='bottom')
    plt.text(3,0.1,'3N---', color='r')        
    
    #4N
    quant_1_4N = np.percentile(Kit_PM_per_day_4N, [25,50,75])
    Top_lim_1_4N = quant_1_4N[2] + 1.5*(quant_1_4N[2] - quant_1_4N[0])
    Low_lim_1_4N = quant_1_4N[0] - 1.5*(quant_1_4N[2] - quant_1_4N[0])
    
    bp_1 = plt.boxplot(Kit_PM_per_day_4N,positions = [4], widths = 0.6)
    for v,a in enumerate(Kit_PM_per_day_4N):
        if a > Top_lim_1_4N or a < Low_lim_1_4N:
            plt.text(4,a,K_PM_D_4N[v])
    plt.text(4,0.1,'4N', color='y')        
            
    plt.xlim(0,5)
    plt.ylim(0,2000000)
    
    plt.show()
    print('3N had these values as outliers   ' , kitchen_3N_outlier)

    # % change of PM per day 

    fig_2, ax2 = plt.subplots()
    plt.title('% No_hood PM per Day Change' )
    #plt.hold(True)
    #2N to 1N
    quant_1_2N_1N = np.percentile(Kit_per_day_2N_1N, [25,50,75])
    Top_lim_1_2N_1N = quant_1_2N_1N[2] + 1.5*(quant_1_2N_1N[2]-quant_1_2N_1N[0])
    Low_lim_1_2N_1N = quant_1_2N_1N[0] - 1.5*(quant_1_2N_1N[2]-quant_1_2N_1N[0])

    bp_1_1 = plt.boxplot(Kit_per_day_2N_1N, positions=[1], widths= 0.6)
    for v,a in enumerate(Kit_per_day_2N_1N):
        if a > Top_lim_1_2N_1N or a < Low_lim_1_2N_1N:
            plt.text(1, a, K_PM_D_2N_1N[v])
    plt.text(0.5, 0, '2N / 1N', color= 'g')
    
    #3N to 1N
    quant_1_3N_1N = np.percentile(Kit_per_day_3N_1N, [25,50,75])
    Top_lim_1_3N_1N = quant_1_3N_1N[2] + 1.5*(quant_1_3N_1N[2]-quant_1_3N_1N[0])
    Low_lim_1_3N_1N = quant_1_3N_1N[0] - 1.5*(quant_1_3N_1N[2]-quant_1_3N_1N[0])

    bp_1_1 = plt.boxplot(Kit_per_day_3N_1N, positions=[2], widths= 0.6)
    for v,a in enumerate(Kit_per_day_3N_1N):
        if a > Top_lim_1_3N_1N or a < Low_lim_1_3N_1N:
            plt.text(2, a, K_PM_D_3N_1N[v])
    plt.text(1.5, 0, '3N / 1N', color= 'r')
    
    #4N to 1N
    quant_1_4N_1N = np.percentile(Kit_per_day_4N_1N, [25,50,75])
    Top_lim_1_4N_1N = quant_1_4N_1N[2] + 1.5*(quant_1_4N_1N[2]-quant_1_4N_1N[0])
    Low_lim_1_4N_1N = quant_1_4N_1N[0] - 1.5*(quant_1_4N_1N[2]-quant_1_4N_1N[0])

    bp_1_1 = plt.boxplot(Kit_per_day_4N_1N, positions=[3], widths= 0.6)
    for v,a in enumerate(Kit_per_day_4N_1N):
        if a > Top_lim_1_4N_1N or a < Low_lim_1_4N_1N:
            plt.text(3, a, K_PM_D_4N_1N[v])
    plt.text(2.5, 0, '4N / 1N', color= 'y')
    
    #3N to 2N
    quant_1_3N_2N = np.percentile(Kit_per_day_3N_2N, [25,50,75])
    Top_lim_1_3N_2N = quant_1_3N_2N[2] + 1.5*(quant_1_3N_2N[2]-quant_1_3N_2N[0])
    Low_lim_1_3N_2N = quant_1_3N_2N[0] - 1.5*(quant_1_3N_2N[2]-quant_1_3N_2N[0])

    bp_1_1 = plt.boxplot(Kit_per_day_3N_2N, positions=[4], widths= 0.6)
    for v,a in enumerate(Kit_per_day_3N_2N):
        if a > Top_lim_1_3N_2N or a < Low_lim_1_3N_2N:
            plt.text(4, a, K_PM_D_3N_2N[v])
    plt.text(3.5, 0, '3N / 2N', color= 'm')
    
    #4N to 3N
    quant_1_4N_3N = np.percentile(Kit_per_day_4N_3N, [25,50,75])
    Top_lim_1_4N_3N = quant_1_4N_3N[2] + 1.5*(quant_1_4N_3N[2]-quant_1_4N_3N[0])
    Low_lim_1_4N_3N = quant_1_4N_3N[0] - 1.5*(quant_1_4N_3N[2]-quant_1_4N_3N[0])

    bp_1_1 = plt.boxplot(Kit_per_day_4N_3N, positions=[5], widths= 0.6)
    for v,a in enumerate(Kit_per_day_4N_3N):
        if a > Top_lim_1_4N_3N or a < Low_lim_1_4N_3N:
            plt.text(5, a, K_PM_D_4N_3N[v])
    plt.text(4.5, 0, '4N / 3N', color= 'k')
    
    #4N to 2N
    quant_1_4N_2N = np.percentile(Kit_per_day_4N_2N, [25,50,75])
    Top_lim_1_4N_2N = quant_1_4N_2N[2] + 1.5*(quant_1_4N_2N[2]-quant_1_4N_2N[0])
    Low_lim_1_4N_2N = quant_1_4N_2N[0] - 1.5*(quant_1_4N_2N[2]-quant_1_4N_2N[0])

    bp_1_1 = plt.boxplot(Kit_per_day_4N_2N, positions=[6], widths= 0.6)
    for v,a in enumerate(Kit_per_day_4N_2N):
        if a > Top_lim_1_4N_2N or a < Low_lim_1_4N_2N:
            plt.text(6, a, K_PM_D_4N_2N[v])
    plt.text(5.5, 0, '4N / 2N', color= 'tab:orange')
    
    
    plt.xlim(0,7)
    plt.ylim(-0.5,4)
    plt.show()
#    
#    D_50_quant_phase_f_d_a = {'Percentile %': [25,50,75], '1N': quant_1_1N, '2N': quant_1_2N,'3N' : quant_1_3N,'4N': quant_1_4N}
#    F_D_A_50_phase_no_hood = pd.DataFrame(data=D_50_quant_phase_f_d_a)
#    D_50_quant_percent_f_d_a ={'Percentile %': [25,50,75],'2N / 1N': quant_1_2N_1N,'3N / 1N': quant_1_3N_1N,'4N / 1N': quant_1_4N_1N,
#                               '3N / 2N': quant_1_3N_2N,'4N / 3N': quant_1_4N_3N,'4N / 2N': quant_1_4N_2N}
#    F_D_A_50_percent_change_no_hood = pd.DataFrame(data=D_50_quant_percent_f_d_a)

    
    
#if Hood_or_no == 'hood':
































