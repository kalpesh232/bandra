# Use a scatter plot to visualize the relationship between two continuous variables.
# Suitable for identifying patterns(linear, quadratic, or nonlinear) , trends, or correlations between two variables.

import matplotlib.pyplot as plt

x = [2,4,6,8]
y = [10,9,8,7]

plt.scatter(x,y,label='skitscat',color='g',s=10,marker="o")

plt.xlabel('x')
plt.ylabel('y')
plt.title('sactter')

plt.legend()
plt.show()