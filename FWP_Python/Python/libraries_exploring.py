import matplotlib.animation as animation
import numpy as np
from IPython.display import Image

fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)
(line,) = ax.plot(x, np.sin(x))
ax.set_ylim(-1.5, 1.5)
sx.set_title("Animated Sine Wave")

def animate(frame):
    line.set_ydata(np.sin(x+fram/10.0))
    return(line,)

ani = animation.FuncAnimation(fig, animate, frames=10, interval=50, blit=True)
ani.save("sine_wave_animation.gif", writer="pillow", fps=30)
Image("sine_wave_animation.gif")
