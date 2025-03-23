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

plt.plot([380,380],[0,2450],linewidth=3,color='indigo')
plt.fill_betweenx([0, 2450], 0, 380, color='mediumorchid', alpha=0.5)

plt.text(400,1400,'Peatland: 15.5%',fontsize=14,color='indigo',fontweight='demibold')
plt.text(400,1300,'£3.1M or £0.M/1%',fontsize=15,color='black')
plt.arrow(-100,1500,440,0,head_width=25,head_length=25,color='black')
plt.arrow(290,1500,-250,0,head_width=25,head_length=25,color='black')

ticksx=[500,1000,1500,2000,2450]
ticksy=[500,1000,1500,2000,2450]
plt.xticks(ticksx)
plt.yticks(ticksy)

plt.tick_params(labelsize=15)