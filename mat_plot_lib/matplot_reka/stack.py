import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [5,8,4,2,6]
eating = [7,1,0,2,5]
plying = [6,9,2,3,4]
working = [1,0,9,5,7]

plt.plot([],[],color='m',label = 'sleeping', linewidth=1)
plt.plot([],[],color='c',label = 'Eating', linewidth=1)
plt.plot([],[],color='r',label = 'Working', linewidth=1)
plt.plot([],[],color='k',label = 'Playing', linewidth=1)

plt.stackplot(days,sleeping,eating,working,plying, colors=['m','c','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Stack Plot')

plt.legend()
plt.show()