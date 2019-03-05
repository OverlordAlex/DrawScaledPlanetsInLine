from matplotlib import pyplot as plt

# name, size, distance from sun
heavens = [ ('sun', 696342, 0),
            ('mercury', 2439, 57),
            ('venus', 6052, 108),
            ('earth', 6371, 150),
            ('mars', 3390, 228),
            ('jupiter', 69911, 779),
            ('saturn', 58232, 1430),
            ('uranus', 25362, 2570),
            ('neptune', 24622, 4500),
            ]

# For the future
moons = {
        'mercury': (0, []),
        'venus': (0, []),
        'earth': (1, []),
        'mars': (2, []),
        'jupiter': (67, []),
        'saturn': (62, []),
        'uranus': (27, []),
        'neptune': (14, []),
        }

# Remove the sun because it blows out the calculation
planets = heavens[1:]
# Re-format for use
plan_dict = {name: [size, dist] for name, size, dist in planets}

#TODO
# The desired size of earth
desired_size = 5.0
moon_size=desired_size / 2.0
#size_ratio = desired_size / plan_dict['earth'][0]

# The desired length of all the planets lined up
desired_length = 10.0
ss = sum([size for name,size,dist in planets])
# halve the length for the ratio due to diameter=2*radius
length_ratio = (desired_length / 2) / ss

# Re-format the planets size and distance using the new ratio
new_planets = [ (name, length_ratio * size, length_ratio * dist, moons[name][0])  for name, size, dist in planets]

# Create a new plotting area
fig, ax = plt.subplots()

# the offset where to plot the next planet
x_offset = 0
for name, size, dist, moons in new_planets:
    # x_offset is used to move the center of the circle for drawing it
    x_offset += size
    ax.add_patch(plt.Circle((x_offset, 0), radius=size, fill=False))
    x_offset += size

ax.set_aspect(1.0)
ax.autoscale_view()
plt.show()
