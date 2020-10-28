# https://electronut.in/simple-python-matplotlib-implementation-of-conways-game-of-life/

import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0, 2*np.pi, 10)
# y = np.sin(x)
#
# x=[1,2,3,4,5]
# y = [4,5,6,7,8]
#
# plt.scatter(x, y)1
#
#
# plt.show()


import matplotlib.pyplot as plt
import time

class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def location(self):
        return (self.x,self.y)

pointa = point(2,3)

first_x = [1,2,3,4]
first_y = [2,4,6,10]

sec_x = [2,4,1,9]
sec_y = [4,2,1,4]

x = [[1,2,3,4],[2,4,1,9]]
y = [[2,4,6,10], [4,2,1,4]]

# plt.scatter(pointa.location[0], pointa.location[1])
# plt.show()

# graph = plt.scatter(first_x, first_y)
# time.sleep(5)
# plt.clear()
# plt.scatter(sec_x, sec_y)
# graph.plt.show()

import matplotlib.pyplot as plt
import numpy as np

# plt.ion()
for i in range(2):
    plt.scatter(x[i], y[i])
    plt.draw()
    plt.pause(1)
    plt.clf()
