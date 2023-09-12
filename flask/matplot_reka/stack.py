import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [6,4,7,8,5]
eating = [9,5,4,1,0]
plying = [9,5,7,3,2]
working = [8,5,3,9,4]

plt.plot([],[],color='m',label = 'sleeping', linewidth=5)
plt.plot([],[],color='c',label = 'Eating', linewidth=5)
plt.plot([],[],color='r',label = 'Working', linewidth=5)
plt.plot([],[],color='k',label = 'Playing', linewidth=5)

plt.stackplot(days,sleeping,eating,working,plying,working, colors=['m','c','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Stack Plot')

plt.legend()
plt.show()