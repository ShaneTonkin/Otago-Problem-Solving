#!/user/bin/env python
import matplotlib.pyplot as plt
import random
import sys


def recursive_circles(current_gen, max_gen, x_center, y_center, radius, prev_radius):
    # Drawing a circle that is too small to see
    if current_gen == 7:
        return
    # Base Case
    if current_gen == 0:
        base_Circle = plt.Circle((x_center, y_center), radius, color=colours[0])
        ax.add_artist(base_Circle)
        return recursive_circles(current_gen+1, max_gen, x_center, y_center, radius/ratios[1], radius)
    # Exit Case
    if current_gen == max_gen:
        circle = plt.Circle((x_center + radius, y_center + 1.725 * radius), radius, color=colours[current_gen])
        ax.add_artist(circle)
        circle = plt.Circle((x_center - radius, y_center + 1.725 * radius), radius, color=colours[current_gen])
        ax.add_artist(circle)
        # Middle Three
        circle = plt.Circle((x_center, y_center), radius, color=colours[current_gen])
        ax.add_artist(circle)
        circle = plt.Circle((x_center - 2 * radius, y_center), radius, color=colours[current_gen])
        ax.add_artist(circle)
        circle = plt.Circle((x_center + 2 * radius, y_center), radius, color=colours[current_gen])
        ax.add_artist(circle)
        # Bottom Two
        circle = plt.Circle((x_center + radius, y_center - 1.725 * radius), radius, color=colours[current_gen])
        ax.add_artist(circle)
        circle = plt.Circle((x_center - radius, y_center - 1.725 * radius), radius, color=colours[current_gen])
        ax.add_artist(circle)
        return
    # Middle Gens
    else:
        # Top Two
        circle = plt.Circle((x_center + prev_radius/2.97, y_center + prev_radius/1.725), radius, color=colours[current_gen])
        ax.add_artist(circle)
        circle = plt.Circle((x_center - prev_radius/2.97, y_center + prev_radius/1.725), radius, color=colours[current_gen])
        ax.add_artist(circle)
        # Middle Three
        circle = plt.Circle((x_center, y_center), radius, color=colours[current_gen])
        ax.add_artist(circle)
        circle = plt.Circle((x_center - prev_radius/1.5, y_center), radius, color=colours[current_gen])
        ax.add_artist(circle)
        circle = plt.Circle((x_center + prev_radius/1.5, y_center), radius, color=colours[current_gen])
        ax.add_artist(circle)
        # Bottom Two
        circle = plt.Circle((x_center + prev_radius/2.97, y_center - prev_radius/1.725), radius, color=colours[current_gen])
        ax.add_artist(circle)
        circle = plt.Circle((x_center - prev_radius/2.97, y_center - prev_radius/1.725), radius, color=colours[current_gen])
        ax.add_artist(circle)

        recursive_circles(current_gen+1, max_gen, x_center + prev_radius/2.97,
                          y_center + prev_radius/1.725, radius / ratios[current_gen+1], radius)
        recursive_circles(current_gen+1, max_gen, x_center - prev_radius/2.97,
                          y_center + prev_radius/1.725, radius / ratios[current_gen+1], radius)
        recursive_circles(current_gen+1, max_gen, x_center, y_center, radius / ratios[current_gen+1], radius)
        recursive_circles(current_gen+1, max_gen, x_center - prev_radius/1.5, y_center,
                          radius / ratios[current_gen+1], radius)
        recursive_circles(current_gen + 1, max_gen, x_center + prev_radius/1.5, y_center,
                          radius / ratios[current_gen+1], radius)
        recursive_circles(current_gen+1, max_gen, x_center + prev_radius/2.97,
                          y_center - prev_radius/1.725, radius / ratios[current_gen+1], radius)
        recursive_circles(current_gen+1, max_gen, x_center - prev_radius/2.97,
                          y_center - prev_radius/1.725, radius / ratios[current_gen+1], radius)
        return


# The n circle diagram
n = 2
base_center = 0
base_radius = 140
colours = []
ratios = []
name = "DefaultCircles.png"

# Get inputs from command line
if len(sys.argv) == 2:
    parameters = []
    i = 0
    lines = 0
    numerator = 1
    f = open(sys.argv[1], "r")
    values = []
    for val in f.read().split():
        values.append(val)
        lines += 1
    lines /= 4
    name = str(sys.argv[1][:-3]) + "png"
    f.close()
    while i < 4*lines:
        colours.append([float(values[i+1])/255, float(values[i+2])/255, float(values[i+3])/255])
        ratios.append(values[i])
        i += 4
    i = 0
    while i < lines:
        if ratios[i][1] == '/':
            ratios[i] = float(ratios[i][2:])
        else:
            ratios[i] = 1 / float(ratios[i])
        i += 1
    n = lines - 1
# Or use default values
else:
    a = 0
    while a < n+1:
        colours.append([random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)])
        ratios.append(3)
        a += 1
        lines = 3

fig, ax = plt.subplots()
recursive_circles(0, n, base_center, base_center, base_radius, 0)
axes = plt.gcf()
plt.axis('equal')
plt.axis([-200, 200, -200, 200])
plt.axis('off')

axes.set_size_inches(20, 15)
fig.savefig(name)
plt.close(fig)
