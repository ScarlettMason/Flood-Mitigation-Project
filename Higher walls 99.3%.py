import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [10,10]
plt.rcParams['axes.edgecolor']='white'


plt.xlim(0,2450)
plt.ylim(0,2450)

plt.xlabel('x (m)', size=17)
plt.ylabel('y (m)',size=17)




plt.plot([0,2450],[0,0],linewidth=5,color='black')
plt.plot([0,0],[0,2450],linewidth=5,color='black')
plt.plot([2450,2450],[2450,0],linewidth=3,color='black')
plt.plot([0,2450],[2450,2450],linewidth=3,color='black')

plt.plot([2432,2432],[0,2450],linewidth=3,color='brown')
plt.fill_betweenx([0, 2450], 0, 2432, color='lightcoral', alpha=0.5)

plt.text(30,1400,'Higher walls 1m: 99.3%',fontsize=14,color='brown',fontweight='demibold')
plt.text(30,1300,'£85.14M or 0.86M/1%',fontsize=15,color='black')
plt.arrow(1000,1500,1400,0,head_width=25,head_length=25,color='black')
plt.arrow(1300,1500,-1250,0,head_width=25,head_length=25,color='black')

ticksx=[500,1000,1500,2000,2450]
ticksy=[500,1000,1500,2000,2450]
plt.xticks(ticksx)
plt.yticks(ticksy)

plt.tick_params(labelsize=15)
