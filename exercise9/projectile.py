import math

# check math has been imported
print("pi = ", math.pi)

# Variables given
g = 9.81
yo = 1
x = 0.5
deg = 80
theta = deg * (math.pi/180)
# Check line 10
print("theta = ", theta)
vo = 44

# Formula
y = yo + (x*(math.tan(theta)))-(g*(x**2))/(2*(vo*(math.cos(theta)))**2)
print("y = ", y)




