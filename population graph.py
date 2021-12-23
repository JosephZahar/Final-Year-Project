import matplotlib.pyplot as plt
from matplotlib import animation

# Set your constant values
alpha = 3
beta = .1
gamma = .8
delta = .03
# These will be the lists we pass to the graphing function
# Including the xs as a list even though they're just a range to keep the plotting function looking neat
x1, y1 = [0], [50]
x2, y2 = [0], [20]

# simulate out for 100 steps
for n in range(100):
    new_y1 = y1[-1] + ((alpha - beta * y2[-1]) * y1[-1]) * .1
    new_y2 = y2[-1] + ((delta * y1[-1] - gamma) * y2[-1]) * .1
    x1.append(n)
    y1.append(new_y1)
    x2.append(n)
    y2.append(new_y2)

# Now the graph related stuff, first off, set the x limits to make sure they're consistent
fig = plt.figure()
ax1 = plt.axes(xlim=(0, 50), ylim=(0, 100))

# create the line objects we'll reference later on
line, = ax1.plot([], [], lw=2)
labels = ['Prey', 'Predator']
lines = []
for index in range(2):
    lobj = ax1.plot([], [], lw=2)[0]
    lines.append(lobj)


# Here's an init function that the animation function will use to initialize the plot
def init():
    for index in range(2):
        line = lines[index]
        line.set_data([], [])
        line.set_label(labels[index])
    legend = plt.legend(loc='upper left')

    return lines


# Here's the animating function that will be called for each frame
def animate(i):
    # We're just looking for the relevant slice of the x and y lists
    xlist = [x1[:i + 1], x2[:i + 1]]
    ylist = [y1[:i + 1], y2[:i + 1]]
    # And setting the data in the lines
    for lnum, line in enumerate(lines):
        line.set_data(xlist[lnum], ylist[lnum])  # set data for each line separately.
        line.set_label(labels[lnum])
    legend = plt.legend(loc='upper left')
    return lines + [legend]


# call the animator. 'Frames' tells the function how many times to call the animation function
# Interval says how long to wait between frames and blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init, repeat=False,
                               frames=50, interval=50, blit=False)
plt.show()
# Matplotlib doesn't come with any of the writers to save down the animations
# Imagemagick is a good one for creating gifs
anim.save('lotka_volterra_test.gif', writer='imagemagick')