import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 10)
y = np.linspace(0, 10, 11)
fig = plt.figure()
axes = fig.add_axes([0, 0, 1, 1])
axes.plot(x, y)
