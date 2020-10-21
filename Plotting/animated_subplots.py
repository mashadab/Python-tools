# clear all 
from IPython import get_ipython
get_ipython().magic('reset -sf') #for clearing everything
get_ipython().run_line_magic('matplotlib', 'qt') #for plotting in separate window

from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 22})

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 4)
ax1.set_xlim(0, 2)
ax1.set_ylim(-2, 2)
ax1.set_ylabel(r'$sin(x)*cosine(x)$')
ax1.set_xlabel(r'$x$')

ax2.set_xlim(0, 2)
ax2.set_ylim(-2, 2)
ax2.set_ylabel(r'$cosine(x)$')

ax3.set_xlim(0, 2)
ax3.set_ylim(-2, 2)
ax3.set_ylabel(r'$sin(x)$')
ax3.set_xlabel(r'$x$')

manager = plt.get_current_fig_manager()
manager.window.showMaximized()

x = np.linspace(0, 2, 1000)
y = np.zeros_like(x)
z = np.zeros_like(x)
a = np.zeros_like(x)

line1, = ax1.plot(x, y, lw=2, color= 'r')
line2, = ax2.plot(x, z, lw=2, color= 'b')
line3, = ax3.plot(x, a, lw=2, color= 'k')
line   = [line1, line2, line3]

# initialization function: plot the background of each frame
def init():
    line[0].set_data([], [])
    line[1].set_data([], [])
    line[2].set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    y = np.cos(2 * np.pi * (x - 0.01 * i)) + np.sin(2 * np.pi * (x - 0.01 * i))
    z = np.cos(2 * np.pi * (x - 0.01 * i))
    a = np.sin(2 * np.pi * (x - 0.01 * i))
    line[0].set_data(x, y)
    line[1].set_data(x, z)
    line[2].set_data(x, a)
    ax1.set_title("Step: %0.2f" %i,loc = 'center', fontsize=18)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The codec argument ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30, codec='libx264')