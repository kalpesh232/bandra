import matplotlib.pyplot as plt

x = [2,4,6,8]
y = [10,9,8,7]

plt.scatter(x,y,label='skitscat',color='g',s=10,marker="o")

plt.xlabel('x')
plt.ylabel('y')
plt.title('sactter')

plt.legend()
plt.show()