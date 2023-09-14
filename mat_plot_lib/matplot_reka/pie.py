# Use a pie chart to represent parts of a categorical dataset.
# Suitable for showing percentages, such as market share for different product categories.
# Best used when you have a small number of categories (3-7) 

import matplotlib.pyplot as plt

slices = [5,3,5,5]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','g']

plt.pie(
    slices,
    labels=activities,
    colors=cols,
    startangle=90,
    shadow=True,
    explode=(0,0.1,0,0),
    autopct='%1.1f%%'
)

plt.title('Pie Plot')
plt.show()