import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import ult2
fig, ax = plt.subplots()

x = np.arange(0, 3000, 0.01)
y= np.arange(0, 3000, 0.01)
line, = ax.plot(x, y)


def animate(i):
    line.set_ydata(ult2.read())
    # update the data.
    return line,


g=ult2.read()
print(g)

ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()