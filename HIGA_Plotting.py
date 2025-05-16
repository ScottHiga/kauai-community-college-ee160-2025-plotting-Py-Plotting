# # # # # # # # # # # # # # #
# HIGA_Plotting.py shows basic functions of matplotlib and numpy
#
# Created by Scott Higa, 2025-05-06
# Last edit: 2025-05-06
# # # # # # # # # # # # # # #

import matplotlib.pyplot as plt
import numpy as np

x_10 = np.linspace(0,2*np.pi,10)
x_100 = np.linspace(0,2*np.pi,100)
x_10000 = np.linspace(0,2*np.pi,10000)
x_mil = np.linspace(0,2*np.pi,1000000)
# Defining three x-value arrays; x_100, 1_10000, & x_mil. All three arrays have the domain of [0,2pi] but each will show a different number of points; 100, 10,000, & 1,000,000 respectively.

y_10 = np.exp(x_10)
y_100 = np.exp(x_100)
y_10000 = np.exp(x_10000)
y_mil = np.exp(x_mil)
# Defining three y-value arrays.  In all cases, the function will show y=e^x.

plt.plot(x_10000,y_10000, color = 'violet', label = 'y=e^x' )
# Creating a 2D plot of the function y=e^x
# It shows 10,000 points of this function from 0 to 2pi
# Setting the color of the function to violet and labeling it y=e^x

plt.title("Exponential Function")
# Setting a title for the plot

plt.legend()
# setting a legend for the plot

plt.grid()
# setting a grid for the plot

plt.show()
# This will make a pop-up that will show the plot

print ("")

plt.plot(x_mil,y_mil, color = 'violet', label = 'y=e^x' )
plt.title("Exponential Function")
plt.legend()
plt.grid()
plt.show()

#They both showed very fast.  Also just wanting to see what a 10 point plot would look like...

plt.plot(x_10,y_10, color = 'violet', label = 'y=e^x' )
plt.title("Exponential Function")
plt.legend()
plt.grid()
plt.show()

print ('Done')

#Scratch work

#fig, ax = plt.subplots()
#ax.plot(x_100,y_100)
#plt.show()

#x_10000 = np.linspace(0,2*np.pi,10000)
#y_10000 = np.exp(x_10000)

#x_mil = np.linspace(0,2*np.pi,1000000)
#y_mil = np.exp(x_mil)
#plt.plot(x_mil,y_mil)
#plt.show()

#x_100 = list(range(101))
#y_100 = np.exp2(x_100)
#plt.plot(x_100,y_100)
#plt.show()

#x_100 = np.array(0, 2 * np.pi, 100)
#x_10000 = np.array(0, 2 * np.pi, 10000)
#x_1000000 = np.linspace(0, 2 * np.pi, 1000000)

#y_100 = np.sin(x_100)
#y_10000 = np.sin(x_10000)
#y_1000000 = np.sin(x_1000000)

#fig, ax = plt.subplots()
#ax.plot(x_10000,y_10000)
#plt.show()

#x = np.linspace(0, 2 * np.pi, 200)
#y = np.sin(x)

#fig, ax = plt.subplots()
#ax.plot(x, y)
#plt.show()
