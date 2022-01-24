import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# from pylab import plot, show, xlim,figure,hold, ylim,legend, boxplot, setup, axes

import seaborn as sns

# Is this a personal or work computer
# Are you graphing for hood or no hood

Computer = 'personal'  # or 'personal' or 'work'
Hood_or_no = 'hood'  # 'no_hood' or 'hood'
# what household do you want to remove make sure it is in ascending order
# if there is nothing, then put a placeholder of 1045 or higher
Household_removal = [1045]
# Household_removal = Household_removal.sort(reverse=False)
Household_removal_NO_Hood_fuel_day_adult = [1045]
Household_removal_Hood_fuel_day_adult = [2020]

Household_removal_NO_Hood_PM = [1045]
Household_removal_Hood_PM = [2020]

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

if Hood_or_no == 'hood':
    C_Place_holder = 2001
else:
    C_Place_holder = 1001

if Computer == 'personal' and Hood_or_no == 'no_hood':
    # 1N
    # 1N Survey
    datafile_path_survey_1N = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/1N/1N_1H_Survey_summary_.csv"
    Filter_1n_survey = pd.read_csv(datafile_path_survey_1N, skiprows=0)
    # print(Filter_1n_survey.iloc[0:40, :])
    Survey_1N = Filter_1n_survey.iloc[0:40, :]
    # 2N
    # 2N Survey
    datafile_path_survey_2N = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/2N/2N_Survey_summary_.csv"
    Survey_2N = pd.read_csv(datafile_path_survey_2N, skiprows=0)
    # 3N
    # 3N Survey
    datafile_path_survey_3N = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/3N/3N_Survey_summary_.csv"
    Survey_3N = pd.read_csv(datafile_path_survey_3N, skiprows=0)
    # 4N
    # 4N Survey
    datafile_path_survey_4N = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/4N/4N_Survey_summary_.csv"
    Survey_4N = pd.read_csv(datafile_path_survey_4N, skiprows=0)

elif Computer == 'personal' and Hood_or_no == 'hood':
    # 1H
    # 1H Survey (row 40 or so afterward is Hood portion column 1 is houshold number)
    datafile_path_survey_1H = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/1N/1N_1H_Survey_summary_.csv"
    Survey_1H = pd.read_csv(datafile_path_survey_1H, skiprows=40)
    # 2H
    # 2H survey
    datafile_path_survey_2H = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/2H/2H_Survey_summary_.csv"
    Survey_2H = pd.read_csv(datafile_path_survey_2H, skiprows=0)
    # 3H
    # 3H survey
    datafile_path_survey_3H = "C:/Users/gvros/Desktop/Oregon State Masters/Work/OSU, CSC, CQC Project files/3H/3H_Survey_summary_.csv"
    Survey_3H = pd.read_csv(datafile_path_survey_3H, skiprows=0)

    # work uses box information and not local data
elif Computer == 'work' and Hood_or_no == 'no_hood':
    # 1N for box file system
    # 1N Survey
    datafile_path_survey_1N = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/1N/1N_1H_Survey_summary_.csv"
    Filter_1n_survey = pd.read_csv(datafile_path_survey_1N, skiprows=0)
    # print(Filter_1n_survey.iloc[0:40, :])
    Survey_1N = Filter_1n_survey.iloc[0:40, :]
    # 2N
    # 2N Survey
    datafile_path_survey_2N = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/2N/2N_Survey_summary_.csv"
    Survey_2N = pd.read_csv(datafile_path_survey_2N, skiprows=0)
    # 3N
    # 3N survey
    datafile_path_survey_3N = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/3N/3N_Survey_summary_.csv"
    Survey_3N = pd.read_csv(datafile_path_survey_3N, skiprows=0)
    # 4N
    # 4N Survey
    datafile_path_survey_4N = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/4N/4N_Survey_summary_.csv"
    Survey_4N = pd.read_csv(datafile_path_survey_4N, skiprows=0)
else:
    # 1H
    # 1H Survey (row 40 or so afterward is Hood portion column 1 is houshold number)
    datafile_path_survey_1H = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/1N/1N_1H_Survey_summary_.csv"
    Survey_1H = pd.read_csv(datafile_path_survey_1H, skiprows=40)
    # 2H
    # 2H survey
    datafile_path_survey_2H = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/2H/2H_Survey_summary_.csv"
    Survey_2H = pd.read_csv(datafile_path_survey_2H, skiprows=0)
    # 3H
    # 3H survey
    datafile_path_survey_3H = "C:/Users/rossgra/Box/OSU, CSC, CQC Project files/3H/3H_Survey_summary_.csv"
    Survey_3H = pd.read_csv(datafile_path_survey_3H, skiprows=0)

if Hood_or_no == 'no_hood':
    plt.title('Histogram of Moisture - NO_Hood' )
    plt.hist([Survey_1N.iloc[:, 11]],
            color=['b'], alpha=0.5, label='1N')
    plt.hist([Survey_2N.iloc[:, 11]],
             color=['g'], alpha=0.5, label='2N')
    plt.hist([Survey_3N.iloc[:, 11]],
             color=['r'], alpha=0.5, label='3N')
    plt.hist([Survey_4N.iloc[:, 11]],
             color=['y'], alpha=0.5, label='4N')
    plt.legend(loc='upper right')
    plt.show()

    plt.title('Histogram of Fuel Scale - NO_Hood' )
    plt.hist([Survey_1N.iloc[:, 19]],
            color=['b'], alpha=0.5, label='1N')
    plt.hist([Survey_2N.iloc[:, 19]],
             color=['g'], alpha=0.5, label='2N')
    plt.hist([Survey_3N.iloc[:, 19]],
             color=['r'], alpha=0.5, label='3N')
    plt.hist([Survey_4N.iloc[:, 19]],
             color=['y'], alpha=0.5, label='4N')
    plt.legend(loc='upper right')
    plt.show()


if Hood_or_no == 'hood':
    plt.title('Histogram of Moisture - Hood')
    plt.hist(Survey_1H.iloc[:,11],
             color=['b'], alpha=0.5, label='1H')
    plt.hist(Survey_2H.iloc[:,11],
             color=['g'], alpha=0.5, label='2H')
    plt.hist(Survey_3H.iloc[:,11],
             color=['r'], alpha=0.5, label='3H')
    plt.legend(loc='upper right')
    plt.show()

    plt.title('Histogram of Fuel Scale - Hood')
    plt.hist(Survey_1H.iloc[:,19],
             color=['b'], alpha=0.5, label='1H')
    plt.hist(Survey_2H.iloc[:,19],
             color=['g'], alpha=0.5, label='2H')
    plt.hist(Survey_3H.iloc[:,19],
             color=['r'], alpha=0.5, label='3H')
    plt.legend(loc='upper right')
    plt.show()