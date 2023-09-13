# distribution of continuous or numerical data.
# distribution of data within a specific range or bin.

import matplotlib.pyplot as plt

population_ages = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,21,21,21,21,21,21,21,21,21,21,21,21,21,21,100]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)

plt.legend()

plt.xlabel('X')
plt.xlabel('Y')
plt.title('histrogram')

plt.show()