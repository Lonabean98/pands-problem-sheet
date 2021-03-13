#This program displays a plot of the functions 
# f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of 
# axes.

#Author: Lonan Keane

import numpy as np
import matplotlib.pyplot as plt

#linspace returns evenly spaced numbers over a specified interval, 
# in this case 0 to 4
x = np.linspace(0,4)
y=  x
#naming the label for each function
plt.plot(x,y, label= "f(x)= x")

#second line
x2= np.linspace(0,4)
y2= x2**2
#The 2 is superscripted
plt.plot(x2,y2, label= "g(x)= $x^2$")

#third line
x3= np.linspace(0,4)
y3= x3 **3
#3 is also superscripted
plt.plot(x3, y3, label= "h(x)= $x^3$")

plt.xlabel("x")
plt.ylabel("y")
#this places the legend on the upper left of the plot
plt.legend(loc="upper left")
#giving title to plot
plt.title("plottask.py")
#adding grid
plt.grid()
#show plot
plt.show()

