import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [10,10]
plt.rcParams['axes.edgecolor']='white'


plt.xlim(0,1000)
plt.ylim(0,1000)

plt.xlabel('x (m)', size=17)
plt.ylabel('y (m)',size=17)

plt.plot([0,2450],[0,0],linewidth=5,color='black')
plt.plot([0,0],[0,9450],linewidth=5,color='black')
plt.plot([2450,2450],[2450,0],linewidth=3,color='black')
plt.plot([0,2450],[2450,2450],linewidth=3,color='black')


plt.bar(1230,2445,width=2450,color='Gold',label="Reservoir: £583.65 for approximately 100% of FEV")

ticksx=[500,1000,1500,2000,2450]
ticksy=[500,1000,1500,2000,2450]

plt.xticks(ticksx)
plt.yticks(ticksy)

plt.tick_params(labelsize=15)

plt.legend(bbox_to_anchor=(0.015, 0.55), loc=2, borderaxespad=0.,prop={'size': 15})
