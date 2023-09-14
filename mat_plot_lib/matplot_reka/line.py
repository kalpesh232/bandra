# changes over continuous  data points.
# time series data, such as stock prices over time or temperature fluctuations.
# single variable changes with respect to another.

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [1,2,3]
y = [3,3,1]

x1 = [2,3,4]
y1 = [9,8,7]

plt.plot(x,y,'r',label='1st line',linewidth=5)
plt.plot(x1,y1,'b',label='2nd line',linewidth=5)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('x asis')

plt.legend()
plt.grid(True,color='k')

plt.show()