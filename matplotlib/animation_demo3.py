import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 500)
x = np.exp(-0.5 * t) * np.sin(2 * np.pi * t)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
line, = plt.plot(t, x)

def update_line(frame, line, t, x):
    line.set_data(t[:frame], x[:frame])

anim = FuncAnimation(fig, update_line, fargs=(line, t, x), interval=50, 
                     frames=t.size)
plt.show()