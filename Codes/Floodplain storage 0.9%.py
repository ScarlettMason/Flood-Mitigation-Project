import matplotlib.pyplot as plt

# Set figure size and axis style
plt.rcParams["figure.figsize"] = [10,10]
plt.rcParams['axes.edgecolor']='white'

# Set axis limits (defines a 2450m x 2450m square)
plt.xlim(0,2450)
plt.ylim(0,2450)

# Add axis labels
plt.xlabel('x (m)', size=17)
plt.ylabel('y (m)',size=17)

# Draw a rightward arrow from (0, 1250) to represent a horizontal line
plt.arrow(0,1250,22,0,head_width=20,head_length=20,color='black')
# Arrow may indicate floodplain depth or border

# Draw the boundary of the full flood-lake box
plt.plot([0,2450],[0,0],linewidth=5,color='black')        # Bottom border
plt.plot([0,0],[0,2450],linewidth=5,color='black')        # Left border
plt.plot([2450,2450],[2450,0],linewidth=3,color='black')  # Right border (slightly thinner)
plt.plot([0,2450],[2450,2450],linewidth=3,color='black')  # Top border (slightly thinner)

# Draw a vertical line at x=22m to represent floodplain volume equivalent
plt.plot([22,22],[0,2450],linewidth=3,color='darkgreen')
plt.plot([13,13],[10,2435],linewidth=3,color='lightgreen')

# Add annotation text for the mitigation impact and cost
plt.text(60,1350,'Floodplain storage in Summer: 0.9%',fontsize=15,color='darkgreen',fontweight='demibold')
plt.text(60,1230,'£398,610 or £0.44M/1%',fontsize=15,color='black')

# Custom tick values for both axes
ticksx=[500,1000,1500,2000,2450]
ticksy=[500,1000,1500,2000,2450]
plt.xticks(ticksx)
plt.yticks(ticksy)
# Set tick label font size
plt.tick_params(labelsize=15)