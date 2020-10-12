# -----------------------------------------------------------------------
# Misc Plots for Random Classes and Things
# -----------------------------------------------------------------------


# %%
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# %%
darr = np.array([(300, 400, 325, 250, 150, 90, 50, 10, 5, 2), 
            (0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2)])
darr[1] = darr[1]/1000 

print(darr)


# %%
# plot number of capillaries against the diameter of the tubes
fig, ax = plt.subplots()
ax.plot(darr[0],darr[1])
ax.set_xlabel("# capillaries")
ax.set_ylabel("D of tubes (in m)")
fig.show()

# %%
# Calculate Capillary Rise
# surface tension (N/m) (at 20 degC)
s = 0.078
# contact angle
w = 0
# rho (density) (kg/m3) (at 20 degc)
r = 998
# gravity
g = 9.8
# Radius (variable) (in meters)
Ra = darr[1]/2

# Length of Capillary Rise (in meters)
L = 2*s*np.cos(w)/(r*g*Ra)
print(Ra)
print(L)

# %%
# plot radius against the capillary rise of the tubes
fig, ax = plt.subplots()
ax.plot(Ra,L)
ax.set_xlabel("radius (in meters)")
ax.set_ylabel("Capillary rise (in meters)")
fig.show()


# %%
# calculate the water volume for given elevations

# set up an array of elevations (z, variable) from capillary rise
L

# (possible water valume) calculate total volume along each step 0, to zmax
## area = [num.pores*area.pores] constant
## z = height variable
## z*area 
area_c = sum(darr[0]*Ra*Ra*3.14)
v_sat= area_c*L


# (measured water volume) calculate water at each elevation
# area = [num.pores.sat*area.pores.sat] variable
# z = height variable
# z*area 
v_meas = np.array([])
for i in range(len(L), 0, -1):
    wetarea = sum(darr[0,0:i]*Ra[0:i]*Ra[0:i]*3.14)
    v_meas = np.append(v_meas,wetarea*L[i-1])

v_meas = np.flip(v_meas)

# (water content) 
## measured water volume / possible water volume
water_cont = v_meas/v_sat*100
print(water_cont)

# visualize the above
fig, ax = plt.subplots()
ax.plot(L,water_cont)
ax.set_xlabel("Capillary rise (in meters)")
ax.set_xscale("log")
ax.set_ylabel("water content, in percent")
ax.set_yscale("log")
fig.show() 




s# %%
