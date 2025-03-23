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

plt.plot([741,741],[0,2450],linewidth=3,color='royalblue')
plt.fill_betweenx([0, 2450], 0, 741, color='lightblue', alpha=0.5)

plt.text(750,1400,'Tree planting: 30.2%',fontsize=14,color='royalblue',fontweight='demibold')
plt.text(750,1300,'£[360,000-648,000] or £[0.01-0.021]M/1%',fontsize=15,color='black')
plt.arrow(-80,1500,780,0,head_width=25,head_length=25,color='black')
plt.arrow(500,1500,-450,0,head_width=25,head_length=25,color='black')

ticksx=[500,1000,1500,2000,2450]
ticksy=[500,1000,1500,2000,2450]
plt.xticks(ticksx)
plt.yticks(ticksy)

plt.tick_params(labelsize=15)
