import numpy as np
import matplotlib.pyplot as plt
import csv

rs = np.linspace(1,4,100000)
N = 500
x = 0.1 + np.zeros(N)
endcap = np.arange(int(N*0.9),N)

rates = []
uniques = []

# Compute the Fixed Values for each Growth Rate (r)
for ri in range(len(rs)):
    for n in range(N-1):
        x[n+1] = rs[ri]*x[n]*(1-x[n])
    u = np.unique(x[endcap])
    r = rs[ri]*np.ones(len(u))
    for i in u:
        rates.append(rs[ri])
        uniques.append(i)

# Generate CSV File
with open('logistic_map.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(["Growth Rate","Fixed Value"])
    for i in range(len(uniques)):
        writer.writerow([rates[i],uniques[i]])

# Plot the values
plt.style.use('dark_background')
plt.figure(figsize=(16, 9))
plt.axis('off')
plt.plot(rates,uniques,'.',color='white',markersize=0.03)
plt.savefig("Logistic Map.png",dpi=1200) # Save the diagram as a .png file
plt.show() # Show the diagram using matplotlib
