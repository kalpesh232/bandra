import matplotlib.pyplot as plt

plt.bar([2,8,4,5],[9,5,4,3], label = 'Example one')
plt.bar([8,1,5,9],[1,4,5,8], label = 'Example two', color='r')

plt.title('Bar Graph')
plt.xlabel('x axis')
plt.ylabel('y label')

plt.legend()

plt.show()