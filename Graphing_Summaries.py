import matplotlib as plt
import numpy as np
import pandas as pd
import os
import glob
import itertools
import csv

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
#1st starting with 


        

    
    
    
    
    