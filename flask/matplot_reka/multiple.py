import numpy as np
import matplotlib.pyplot as plt

def f(t):
    print(np.exp(-t) * np.cos(2*np.pi*t))
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0,6.0,0.1)
t2 = np.arange(0.0,6.0,0.02)

plt.subplot(211)
plt.plot(t1,f(t1), 'go', t2, f(t2))

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2))

plt.show()