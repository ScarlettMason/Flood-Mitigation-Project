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

plt.bar(490,2445,width=973,color='lightcoral',label="Higher walls 1m: £17M for approximately 40% of FEV")
plt.bar(1345,2445,width=741,color='lightblue',label="Tree planting: £[0.36-0.65]M for approximately 30% of FEV")
plt.bar(2050,2445,width=668,color='lightgreen',label="Floodplain storage winter: £40M for approximately 26% of FEV")

ticksx=[500,1000,1500,2000,2450]
ticksy=[500,1000,1500,2000,2450]

plt.xticks(ticksx)
plt.yticks(ticksy)

plt.tick_params(labelsize=15)

plt.legend(bbox_to_anchor=(0.015, 0.55), loc=2, borderaxespad=0.,prop={'size': 15})