import pandas as pd
import matplotlib.pyplot as plt

# Set basic plot style preferences
plt.rcParams['axes.grid'] = False                   # Turn off grid lines
plt.rcParams["figure.figsize"] = [8, 6]             # Set figure size
plt.rcParams['axes.edgecolor'] = 'black'           # Set axis edge color to black
fig, ax1 = plt.subplots()                           # Create the first axis object

# Load data from CSV file (contains h_T values, FEV, and side lengths)
data = pd.read_csv('FEV h_T Side length graph.csv')
hT = data['h_T']                                    # Threshold height (m)
FEV = data['FEV Mm^3']                              # Flood Excess Volume (in Mm³)
Side = data['Side length']                          # Side length of equivalent square lake (2m deep)

# Configure primary y-axis (left) for FEV vs h_T
ax1.set_xlabel('$h_T$ [m]', size=15)                # x-axis label
ax1.set_ylabel('$FEV$ [Mm$^3$]', size=15, color='red')  # y-axis label (left)
ax1.plot(hT, FEV, color='red', marker='x', markeredgecolor='k')  # Red line with x markers
ax1.tick_params(axis='y', labelcolor='red')         # Match tick label color to plot color
ax1.set_ybound(0, 20)                               # Set lower and upper bounds of y-axis
ax1.set_ylim(0, 20)                                 # Explicit y-axis limits (redundant but safe)
ax1.set_xlim(2.6, 4.2)                              # x-axis range for h_T

# Create a second y-axis (right) sharing the same x-axis
ax2 = ax1.twinx()

# Configure secondary y-axis for Side Length vs h_T
ax2.set_ylabel('2m deep square lake side length [m]', size=15, color='blue')  # Right y-axis label
ax2.plot(hT, Side, color='blue', marker='o', markeredgecolor='k')            # Blue line with circle markers
ax2.tick_params(axis='y', labelcolor='blue')         # Match tick label color to line
ax2.set_ybound(0, 3050)                              # Set upper bound for lake side length (in metres)

# Adjust layout to prevent overlap of axis labels
fig.tight_layout()

# Display the final graph
plt.show()