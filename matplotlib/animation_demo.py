""" Demo of a timer and an animation using matplotlib: crashes on WX but work 
with the QT backend. 
""" 

from matplotlib import pyplot as plt

from datetime import datetime
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

def updateTime(axes):
    axes.set_title(datetime.now())
    axes.figure.canvas.draw()

# Specifying interval=100 is enough except for QT backend
timer = fig.canvas.new_timer(interval=100) 
# Add a call back to the function above. The callback can also be give a class 
# with a __call__ method. See animation_demo2.
timer.add_callback(updateTime, ax)
timer.interval = 100 # Work around bug in QT timer

timer.start()
plt.show()