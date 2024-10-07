import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

# #3D
# x = np.linspace(-5, 5, 100)
# y = np.linspace(-5, 5, 100)
# x, y = np.meshgrid(x, y)
# z = np.sin(x+y)
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(x, y, z, cmap='cool')
# ax.set_xlabel('X axis')
# ax.set_ylabel('Y axis')
# ax.set_zlabel('Z axis')
# plt.show()

#Pie Chart
labels = ['Piano', 'Visual Arts', 'Strings', 'Comm Arts']
sizes = [215, 130, 245, 210]
colors = ['purple', 'lightcoral', 'yellowgreen', 'lightblue']
explode = (0.1, 0.3, 0.1 , 0.1)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()

#Histogram
data = [28, 14, 23, 34, 56, 37, 47, 69, 47, 33, 51, 55, 63, 45]
plt.hist(data, bins=15)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()

#Scatter Plot
x = [1, 2, 3, 4, 5, 2, 6, 4, 1, 3, 3, 5, 2, 4.5]
y = [10, 23, 13, 19, 18, 21, 14, 17, 19, 22, 11, 9, 16, 11.5]
# scatter plot is used to display 2 variables or a set of data
plt.scatter(x, y)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Scatter Plot")
plt.show()

# Line Graph
customers = [11, 16, 14, 14, 19, 14]
customers2 = [10, 15, 12, 20, 17, 18]
customers3 = [9, 12, 16, 15, 11, 13]
days = range(len(customers))
plt.plot(days, customers, label='Line 1', color = 'k')
plt.plot(days, customers2, label='Line 2', color = 'r')
plt.plot(days, customers3, label='Line 3')
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend(loc = 'upper left')
plt.title("Line Graph")
plt.show()