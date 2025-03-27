import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Set up a plain white plot style with a square figure.
plt.rcParams["figure.figsize"] = [10,10]
plt.rcParams['axes.edgecolor']='white'
fig, ax = plt.subplots()

#Import the data (CSV with Time, Flow, Stage columns)
derwent=pd.read_csv('River Derwent 2009 data.csv')
day = derwent['Time']
flow = derwent['Flow']
height = derwent['Stage']

#Coefficients for the rating curve equation
a = [0.0567,0.3099,1.0879,0]
b = [2.4519,1.160,0.9194,2.4460]
c = [38.2262,37.4022,77.9101,11.5420]
lowlims = [0.235,0.235,0.235,0.235] #Lower limits for rating stages
uplims = [4.32,4.32,4.32,4.32] #Upper limits for rating stages
          
#Define threshold height h_T
ht = 3.0

#Manual min/max values for normalising height and flow
minh=0
maxh=4.5
minF=0
maxF=450

#Scale function to normalise values between 0 and 1
def scaleheightflow(x,minx,maxx):
    return ((x-minx)/(maxx-minx))

error=0.055
errorheightup = [i*(1+error) for i in height]
errorheightdown = [i*(1-error) for i in height]
hup= ht*(1+error)
print(hup)

#Scale time, height and flow data
scaledday = scaleheightflow(day, 0, 7)
scaledheightnew = scaleheightflow(height,minh,maxh)
scaledflownew = scaleheightflow(flow,minF,maxF)
negdaynew = -(scaledday)
negheightnew = -(scaledheightnew)

scaledflownewup = [i*(1+error) for i in scaledflownew]
scaledflownewdown = [i*(1-error) for i in scaledflownew]

#Find mean height (h_m) above threshold (h_T)
HM = []
for i in height:
    if i>=ht:
        HM.append(i)
hm=sum(HM)/len(HM)

#Manually defined values of Q_T and Q_m
qtnew=174.438
qmnew=294.44526

#Reconstructing rating curve using equation
Flow = []
for i in height:
    if i<=uplims[0] and i>=lowlims[0]:
        Flow.append(c[0]*((i-a[0])**b[0]))
    elif i<=uplims[1] and i>lowlims[1]:
        Flow.append(c[1]*((i-a[1])**b[1]))
    elif i<=uplims[2] and i>lowlims[2]:
        Flow.append(c[2]*((i-a[2])**b[2]))
    elif i<=max(height) and i>lowlims[3]:
        Flow.append(c[3]*((i-a[3])**b[3]))

#Scale the computed flow values
scaledFlow = []
for i in Flow:
    scaledFlow.append((i-min(Flow))/(max(Flow)-min(Flow)))

#Plot rating curve, flow over time, and height vs time.
ax.plot(negheightnew,scaledflownew,'black',linewidth=2) #Q(h)
ax.plot([-1,-1/9],[1,0],'white',linestyle='--', marker='', linewidth=2, alpha=0)

#Plot hydrograph (flow vs time) and reverse height vs time
ax.plot(scaledday, scaledflownew, 'black', linewidth=2)
ax.plot(negheightnew, negdaynew, 'black', linewidth=2)

#Scale h_T, h_m, Q_T and Q_m for plotting dashed lines.
scaledhtnew = scaleheightflow(ht,minh,maxh)
print('scaledhtnew',scaledhtnew)
scaledhmnew = scaleheightflow(hm,minh,maxh)
print('scaledhmnew', scaledhmnew)
scaledqtnew = scaleheightflow(qtnew,minF,maxF)
print('scaledqtnew', scaledqtnew)
scaledqmnew = scaleheightflow(qmnew,minF,maxF)
print('scaledqmnew', scaledqmnew)

# Plot dashed reference lines showing h_T, h_m, Q_T, Q_m on the graph
ax.plot([-scaledhtnew,-scaledhtnew],[-1,scaledqtnew], 'black', linestyle='--', linewidth=1)
ax.plot([-scaledhmnew,-scaledhmnew],[-1,scaledqmnew], 'black', linestyle='--', linewidth=1)
ax.plot([-scaledhtnew,1],[scaledqtnew,scaledqtnew], 'black', linestyle='--', linewidth=1)
ax.plot([-scaledhmnew,1],[scaledqmnew,scaledqmnew], 'black', linestyle='--', linewidth=1)
ax.plot([3.45/7,3.45/7,3.45/7],[scaledqtnew,scaledqmnew,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([270/400,270/400,270/400],[scaledqtnew,scaledqmnew,-1/5], 'black', linestyle='--', linewidth=1)

# Draw rectangle bounding the FEV area on the plot
ax.plot([3.45/7,3.45/7],[scaledqmnew,scaledqtnew], 'black',linewidth=1.5)
ax.plot([3.45/7,270/400],[scaledqmnew,scaledqmnew], 'black',linewidth=1.5)
ax.plot([3.45/7,270/400],[scaledqtnew,scaledqtnew], 'black',linewidth=1.5)
ax.plot([270/400,270/400],[scaledqmnew,scaledqtnew], 'black',linewidth=1.5)

# Define custom axis ticks and labels (for visual clarity)
ticks_x = [-1,-8/9,-7/9,-6/9,-5/9,-4/9,-3/9,-2/9,-1/9,0,1/7,2/7,3/7,4/7,5/7,6/7,1]
ticks_y = [-1,-6/7,-5/7,-4/7,-3/7,-2/7,-1/7,0,1/9,2/9,3/9,4/9,5/9,6/9,7/9,8/9,9/9]
ax.set_xticks(ticks_x)
ax.set_yticks(ticks_y)

# Custom axis labels (real values corresponding to scaled positions)
Ticks_x = [4.5,4,3.5,3,2.5,2,1.5,1,0.5,0,1,2,3,4,5,6,7]
Ticks_y = [7,6,5,4,3,2,1,0,50,100,150,200,250,300,350,400,450]
ax.set_xticklabels(Ticks_x)
ax.set_yticklabels(Ticks_y)

# Format axes and tick marks
ax.spines['left'].set_position(('center'))
ax.spines['bottom'].set_position(('center'))
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.tick_params(axis='x', colors='black', direction='out', length=10, width=1)
ax.tick_params(axis='y', colors='black', direction='out', length=10, width=1)

#Plot Title.
plt.title('2009 River Derwent data')

# Add text labels
plt.text(-0.65, -1,'$h_T$')
plt.text(-0.81, -1,'$h_m$')
plt.text(1, scaledqmnew,'$Q_m$')
plt.text(1, scaledqtnew,'$Q_T$')
plt.text(0.3,0.7,'FEV', size=15)
plt.text(scaledday[370],-0.3,'$T_f$',size=13)
plt.annotate('', xy=(scaledday[325],-0.22), xytext=(scaledday[460],-0.22), arrowprops=dict(arrowstyle='<->'))

#Axis labels.
plt.text(0.02, 1.05,'Q $[m^3/s]$', size=10)
plt.text(0.95, -0.2,'t [day]', size=10)
plt.text(-0.18, -1.11,'t [day]', size=10)
plt.text(-1.1, 0.05,r'$\bar{h}$  $[m]$', size=10)

#Arrowheads on axis lines.
plt.text(-0.015,1.075,'^')
plt.text(-0.012,-1.11,'v')
plt.text(1.08,-0.01,'>')
plt.text(-1.105,-0.01,'<')

#Text box with FEV values and calculates parameters.
plt.text(0.4,-0.5,'$FEV≈13.2Mm^3$', size=15)
plt.text(0.4,-0.6,'$T_f=30.5hrs$', size=15)
plt.text(0.4,-0.7,'$h_T=3.0m$', size=15)
plt.text(0.4,-0.8,'$h_m=3.73m$', size=15)
plt.text(0.4,-0.9,'$Q_T=174.4m^3/s$', size=15)
plt.text(0.4,-1,'$Q_m=294.45m^3/s$', size=15)

#Fill the area between Q(t) and Q_T to represent FEV (pink region)
QT=[]
for i in scaledflownew:
    i = scaledqtnew
    QT.append(i)
a=np.array(scaledflownew)
b=np.array(QT)
ax.fill_between(scaledday,a,b,where=a>=b,facecolor='pink')

#Find T_f (flood duration) from intersection points
idx = np.argwhere(np.diff(np.sign(b - a))).flatten()
print(scaledday[idx])

lists1 = sorted(zip(*[negheightnew, scaledflownewdown]))
negheight1, scaledflownewdown1 = list(zip(*lists1))
lists2 = sorted(zip(*[negheightnew, scaledflownewup]))
negheight1, scaledflownewup1 = list(zip(*lists2))
ax.fill_between(negheight1,scaledflownewdown1,scaledflownewup1,color="grey", alpha = 0.3)
ax.fill_between(scaledday,scaledflownewup,scaledflownewdown,color="grey", alpha = 0.3)
QtU = scaledqtnew*(1+error)
QtD = scaledqtnew*(1-error)
ax.fill_between([scaledday[idx[0]], scaledday[idx[-1]]], QtU, QtD, color = "grey", alpha = 0.3)
ax.tick_params(axis='x',colors='black',direction='out',length=9,width=1)
ax.tick_params(axis='y',colors='black',direction='out',length=10,width=1)

#Convert scaled time to unscaled time (in days)
def unscaleday(x):
    return (((max(day)-min(day))*x)+min(day))

#T_f boundaries from manual inspection
c=3.447916667
d=4.71875
Tf=(d-c)*24 #in hours
Tfs=Tf*(60**2) #in seconds

# Compute FEV using mean and threshold discharges
FEV=(qmnew-qtnew)*Tfs
print('FEV', FEV/1000000) # Convert to million cubic metres

# Output key parameters to console for record-keeping
print('ht', ht)
print('qt', qtnew)
print('qm', qmnew)
print('Tf', Tf)
print('hm', hm)
print('maxheight',max(height))
print('minheight',min(height))
print('maxflow', max(flow))
print('minflow', min(flow))

#Show the final plot
plt.show()