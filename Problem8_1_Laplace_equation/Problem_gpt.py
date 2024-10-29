#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

t1 = 30.
t2 = 20.
t3 = 15.
t4 = 15.
tg = np.mean([t1, t2, t4, t4])
N = 50

yy, xx = np.mgrid[0:N, 0:N]

# Initialize the temperature array using broadcasting
t = np.zeros((N, N))
t[0, :] = t1
t[-1, :] = t4
t[:, 0] = t2
t[:, -1] = t3
t[1:-1, 1:-1] = tg

told = np.zeros_like(t)
tol = 1e-4
err = np.mean(np.abs(told - t))

# Iterate until the error is less than the tolerance
while(err>tol):
    told = t.copy()
    # Vectorized update using NumPy slicing
    t[1:-1, 1:-1] = 0.25 * (told[2:, 1:-1] + told[:-2, 1:-1] + told[1:-1, 2:] + told[1:-1, :-2])
    # Calculate the error
    err = np.mean(np.abs(told - t))


print('Final error:', err)

# Visualization
cm='inferno'
fig1 = plt.figure()
ax = fig1.add_subplot(projection='3d')
ax.scatter(xx, yy, t,marker='x',color='black')
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('T (ºC)')
ax.set_title('3D Scatter Plot of Temperature Distribution')

fig2 = plt.figure()
bx = fig2.add_subplot()
grid = bx.scatter(xx, yy, c=t, cmap=cm)
bx.set_xlabel('X (m)')
bx.set_ylabel('Y (m)')
bx.set_title('2D Heatmap of Temperature')
fig2.colorbar(grid, label='Temperature (ºC)')



fig3 = plt.figure()
cx = fig3.add_subplot(projection='3d')
dgrid = cx.scatter(xx, yy, t, c=t, cmap=cm)
cx.set_xlabel('X (m)')
cx.set_ylabel('Y (m)')
cx.set_zlabel('T (ºC)')
cx.set_title('3D Colored Scatter Plot of Temperature')
# Change the view angle to show the y-axis in front
cx.view_init(elev=7, azim=15)
fig3.colorbar(dgrid, label='Temperature (ºC)')

'''
# Downsample by a factor of 100
downsample_factor = 100
yy_downsampled = yy[::downsample_factor, ::downsample_factor]
xx_downsampled = xx[::downsample_factor, ::downsample_factor]
t_downsampled = t[::downsample_factor, ::downsample_factor]

fig3 = plt.figure()
cx = fig3.add_subplot(projection='3d')
dgrid = cx.scatter(xx_downsampled, yy_downsampled, t_downsampled, c=t_downsampled, cmap='inferno')
cx.set_xlabel('X Label')
cx.set_ylabel('Y Label')
cx.set_zlabel('T Label')
fig3.colorbar(dgrid, label='Temperature (ºC)')
'''
# Save fig1 as PNG
#fig1.savefig("3d_scatter.png", format='png', dpi=300, bbox_inches='tight')
#fig2.savefig("2d_heatmap.png", format='png', dpi=300, bbox_inches='tight')
#fig3.savefig("3d_colored_scatter.png", format='png', dpi=300, bbox_inches='tight')
plt.show()


# -----------------------------------------------------------------------------
# Vectorization Explanation:
# -----------------------------------------------------------------------------
# In the original implementation of this code, the update of the grid `t` was performed
# using a nested loop:
#
# for i in range(1, len(t) - 2):
#     for j in range(1, len(t) - 2):
#         t[j][i] = (told[i + 1][j] + told[i - 1][j] + told[i][j + 1] + told[i][j - 1]) / 4
#
# This approach iterates over each interior point `(j, i)` of the grid and updates its 
# value based on the average of its four neighbors:
# - `told[i + 1][j]` (right neighbor)
# - `told[i - 1][j]` (left neighbor)
# - `told[i][j + 1]` (top neighbor)
# - `told[i][j - 1]` (bottom neighbor)
#
# While this approach is straightforward, it becomes very slow for large grids (`N`), 
# because the time complexity is O(N^2) due to the nested loops. 
#
# -----------------------------------------------------------------------------
# Vectorized Approach:
# -----------------------------------------------------------------------------
# To optimize the performance, we can use vectorization with NumPy. Vectorization allows 
# us to perform batch operations on entire arrays or slices of arrays, avoiding the need 
# for explicit Python loops. This leverages the highly optimized C implementations under 
# the hood of NumPy, making the code faster and more efficient.
#
# The vectorized update of the grid can be done using NumPy slicing:
#
# t[1:-1, 1:-1] = 0.25 * (told[2:, 1:-1] + told[:-2, 1:-1] + told[1:-1, 2:] + told[1:-1, :-2])
#
# Let's break this down:
#
# 1. `t[1:-1, 1:-1]`:
#    - This selects the interior of the grid `t`, excluding the boundary rows and columns.
#    - The slice notation `1:-1` means "start from the second element (index 1) and go up 
#      to (but not including) the last element." 
#    - For a 5x5 grid, `t[1:-1, 1:-1]` would give us a 3x3 array representing the interior 
#      points.
#
# 2. `told[2:, 1:-1]`, `told[:-2, 1:-1]`, `told[1:-1, 2:]`, `told[1:-1, :-2]`:
#    - These are slices of `told` used to access the four neighboring cells for each 
#      interior point in `t`.
#    - `told[2:, 1:-1]`: This selects the values directly **below** each interior point.
#    - `told[:-2, 1:-1]`: This selects the values directly **above** each interior point.
#    - `told[1:-1, 2:]`: This selects the values **to the right** of each interior point.
#    - `told[1:-1, :-2]`: This selects the values **to the left** of each interior point.
#
# These slices return arrays of the same shape as `t[1:-1, 1:-1]`, so we can use them 
# directly in a vectorized operation to update all interior points at once:
#
# t[1:-1, 1:-1] = 0.25 * (told[2:, 1:-1] + told[:-2, 1:-1] + told[1:-1, 2:] + told[1:-1, :-2])
#
# This line of code performs the same averaging operation as the original nested loops, 
# but it does so without explicitly looping through each index. Instead, NumPy processes 
# the entire array at once, which is significantly faster and more memory-efficient.
#
# -----------------------------------------------------------------------------
# Benefits of Vectorization:
# -----------------------------------------------------------------------------
# 1. **Speed**: 
#    - Vectorized operations are executed in compiled C code, which runs much faster than 
#      interpreted Python loops. The performance improvement is especially noticeable for 
#      large arrays.
# 2. **Code Simplicity**: 
#    - The code is cleaner and easier to read, as the vectorized approach reduces several 
#      lines of nested loops into a single line of calculation.
# 3. **Memory Efficiency**: 
#    - Operating directly on slices avoids the need for temporary variables or additional 
#      looping constructs, reducing the memory overhead.
#
# -----------------------------------------------------------------------------
# Example:
# -----------------------------------------------------------------------------
# Consider a smaller 5x5 grid with boundaries set to specific temperatures:
#
# Initial Grid (`told`):
# [[30, 30, 30, 30, 30],  # t1 (top boundary)
#  [20, tg, tg, tg, 15],  # interior row
#  [20, tg, tg, tg, 15],  # interior row
#  [20, tg, tg, tg, 15],  # interior row
#  [15, 15, 15, 15, 15]]  # t4 (bottom boundary)
#
# After applying the vectorized operation, `t[1:-1, 1:-1]` will be updated:
# - `told[2:, 1:-1]`: takes the row below each interior cell.
# - `told[:-2, 1:-1]`: takes the row above each interior cell.
# - `told[1:-1, 2:]`: takes the column to the right of each interior cell.
# - `told[1:-1, :-2]`: takes the column to the left of each interior cell.
#
# The resulting values are averaged and assigned to `t[1:-1, 1:-1]` all at once, without 
# the need for a nested loop.
# -----------------------------------------------------------------------------
