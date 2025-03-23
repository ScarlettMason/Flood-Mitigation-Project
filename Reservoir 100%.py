import numpy as np
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

plt.plot([1959, 2673], [0, 2450], linewidth=3, color='saddlebrown')

y_values = np.linspace(0, 2450, 100)
x_values = (y_values / 3.43) + 1959
plt.fill_betweenx(y_values, 0, x_values, color='gold', alpha=0.5)


plt.text(750,1900,'Reservoir: 100%',fontsize=14,color='saddlebrown',fontweight='demibold')
plt.text(750,1800,'£583.65M or 5.84M/1%',fontsize=15,color='black')
plt.arrow(-80,2000,2500,0,head_width=25,head_length=25,color='black')
plt.arrow(500,2000,-450,0,head_width=25,head_length=25,color='black')

plt.text(500,200,'Reservoir: 80%',fontsize=14,color='saddlebrown',fontweight='demibold')
plt.text(500,100,'£583.65M or 7.3M/1%',fontsize=15,color='black')
plt.arrow(-80,40,2000,0,head_width=25,head_length=25,color='black')
plt.arrow(500,40,-450,0,head_width=25,head_length=25,color='black')

ticksx=[500,1000,1500,2000,2450]
ticksy=[500,1000,1500,2000,2450]
plt.xticks(ticksx)
plt.yticks(ticksy)

plt.tick_params(labelsize=15)
