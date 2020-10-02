import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import random

x_full = [[229, 29, 52, 90, 78], [228, 29, 52, 90, 79], [229, 28, 53, 89, 79], [228, 27, 52, 90, 78], [227, 28, 51, 89, 79], [227, 27, 50, 88, 78], [226, 28, 51, 88, 79], [227, 29, 51, 89, 79], [227, 30, 51, 90, 79], [228, 30, 51, 90, 79], [229, 30, 50, 89, 78], [228, 30, 49, 90, 79], [228, 30, 50, 89, 78], [228, 31, 50, 88, 78], [229, 32, 49, 87, 78], [230, 33, 50, 87, 77], [230, 34, 50, 88, 76], [231, 35, 51, 87, 75], [232, 36, 50, 87, 74], [232, 37, 51, 86, 74]]
y_full = [[37, 23, 94, 195, 90], [37, 22, 93, 194, 89], [36, 22, 94, 195, 88], [36, 22, 95, 194, 88], [35, 22, 94, 195, 88], [36, 22, 95, 196, 89], [35, 21, 94, 197, 90], [34, 20, 94, 196, 91], [34, 20, 94, 197, 90], [35, 19, 94, 196, 90], [35, 18, 95, 197, 89], [35, 18, 94, 198, 88], [35, 19, 93, 197, 89], [35, 20, 94, 196, 90], [34, 20, 95, 196, 90], [33, 19, 95, 195, 90], [33, 19, 96, 196, 91], [33, 20, 95, 196, 90], [32, 20, 94, 195, 90], [31, 19, 93, 194, 91]]

x_vals = []
y_vals = []

index = count()

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0,5))

    plt.plot(x_vals, y_vals)


ani = FuncAnimation(plt.gcf(), animate, interval=10)  # get current figure, function, interval

plt.tight_layout()
plt.show()
