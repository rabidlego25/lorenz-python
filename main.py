#!/usr/bin python3

import numpy as np
import matplotlib.pyplot as plt

from lorenz import lorenz
from rk4 import rk4

# discrete time step size
dt = 0.01

# simulation time range
time = np.arange(0.0, 60.0, dt)

# lorenz initial conditions (x, y, z) at t = 0
y0 = np.array([-8, 8, 27]); 

# propogate state
sol = np.empty((time.size + 1, 3))

# initialize yk
sol[0] = y0; 

#initialize time
t = 0

#update state variables sol[i] to sol[i+1]
for i in range(time.size):
	sol[i+1] = rk4(lorenz, time[i], sol[i], dt, sigma=10, beta=(8/3), rho=28)
	print(f'y evaluated at time t = {time[i]} seconds: {sol[i+1]}')

# plot
ax = plt.figure().add_subplot(projection='3d')

ax.plot(*sol.T, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()
