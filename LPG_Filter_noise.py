## This is to filter out the noise in the LPG Data Set
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#File = pd.read_csv("C:/Users/gvros/Desktop/Oregon State Masters/Work/Data_Dumps/LPG_filter_1_aussie.csv", delimiter=',')

#print(File.iloc[0,1])
#print(File.iloc[:,0])
# This first for loop is to get out the large spikes caused by the trailer
#n= 0
#lpg_time = []
#lpg_we= []
#for time in File.iloc[:,0]:
#    we = File.iloc[n,1]
#    if we < 0:
#        lpg_we.append(we)
#        lpg_time.append(time)
#        n= n+1
#    else:
#        n= n +1
# next i am trying to filter out the noise
# first there is need to find threshold for filtering
#https://glampingorcamping.com/home/how-long-does-msr-fuel-last/  Says that a maximum bottle of 0.45kg bottle
# will burn in 3 to 6 hours
# finding the slope of 3 hours compared to 0.45 kg

#F_thresh = 0.45/180

#v = 0
#l_time = []
#l_we = []
#for t in lpg_time:
#    if (len(lpg_we)-1) == v:
#        break
#    elif abs(lpg_we[v+1] - lpg_we[v])  < F_thresh:

#        l_we.append(lpg_we[v])
#        l_time.append(t)
#        v = v + 1
#    else:
#        v = v+1


#plt.figure()
#axo= plt.subplot(221)
#plt.plot(lpg_time,lpg_we)

#ax1= plt.subplot(222)
#plt.plot(l_time,l_we)
#plt.grid(True)
#plt.show()
## this is to compare to nepal
File = pd.read_csv("C:/Users/gvros/Desktop/Oregon State Masters/Work/Data_Dumps/LPG_filter_1_nepal.csv", delimiter=',')

#print(File.iloc[0,1])
#print(File.iloc[:,0])
## This first for loop is to get out the large spikes caused by the trailer
n= 0
lpg_time = []
lpg_we= []
lpg_use = []
for time in File.iloc[:,0]:
    we = File.iloc[n,1]
    use = File.iloc[n,2]
    if we < 0:
       lpg_time.append(time)
       lpg_we.append(we)
       lpg_use.append(use)
       n= n+1
    else:
        n= n +1
# next i am trying to filter out the noise
## first there is need to find threshold for filtering
##https://glampingorcamping.com/home/how-long-does-msr-fuel-last/  Says that a maximum bottle of 0.45kg bottle
## will burn in 3 to 6 hours
## finding the slope of 3 hours compared to 0.45 kg

#F_thresh = 0.45/180

v = 0
l_time = []
l_we = []
for t in lpg_time:
    if (len(lpg_we)-1) == v:
        break
    elif 0 == v:
        pass
    elif (abs(lpg_we[v+1] - lpg_we[v]) < F_thresh):# and (abs(lpg_we[v-1] - lpg_we[v]) < F_thresh):

        l_we.append(lpg_we[v])
        l_time.append(t)
        v = v + 1
    else:
        v = v+1

## this is to ge the slope and averge of 4
four = len(lpg_time)/4
#print(four)
four_ = np.linspace(0, four,int(four), endpoint=False)
print(four_)
print(lpg_we[0])
g = 0
avg_ne_time = []
avg_ne_we = []
avg_ne_use = []
#inte = np.linspace(1,15,15)
#print(inte)
for t in four_:
    inte = np.linspace(1,4,4)
    val_we = []
    val_use =[]
    e = 0
    for i in inte:
        val_we.append(lpg_we[(g+e)])
        val_use.append(lpg_use[(g+e)])
        e = e+1
    avg_ne_we.append((sum(val_we)+lpg_we[g])/4)
    if ((sum(val_use)+lpg_use[g])) > 3:
        avg_ne_use.append(lpg_use[g])
    else:
        avg_ne_use.append(0)
    avg_ne_time.append(lpg_time[g])
#    avg_ne_use.append(lpg_use[g])
    g = g + 4

print(len(avg_ne_we))
print(len(avg_ne_use))
print(len(avg_ne_time))

times = ['6/3','6/4','6/5','6/6','6/7']
t_time = list(range(len(times)))
plt.figure()
axo= plt.subplot(221)
plt.plot(lpg_time,lpg_we)
plt.xticks(t_time, times)

xlabels = ["2/20" , "2/21" ,"2/22", "2/23", "2/24", "2/25", "2/26", "2/27", "2/28", "3/1", "3/2", "3/3", "3/4"]

fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('Time')
ax1.set_ylabel('LPG KG', color=color)
##ax1.set_xticks(xlabels)
ax1.plot(avg_ne_time,avg_ne_we, color=color)
#ax1.set_xticklabels(xlabels)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Usage', color=color)  # we already handled the x-label with ax1
ax2.plot(avg_ne_time,avg_ne_use, color=color)
ax2.set_xticks(xlabels)
ax2.tick_params(axis='y', labelcolor=color)
plt.grid(True)
fig.tight_layout()
plt.show()
