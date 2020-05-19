# Quiz Solution: Zip Coordinates
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []

for x, y, z, label in zip(x_coord, y_coord, z_coord, labels):
    points.append('{}: {}, {}, {}'.format(label, x, y, z))

print(points)



# Quiz Solution: Zip Lists to a Dictionary
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

dic = dict(zip(cast_names, cast_heights))
print(dic)



# Quiz Solution: Unzip Tuples
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
cast_names, cast_heights = zip(*cast)
print(cast_names)
print(cast_heights)



# Quiz Solution: Enumerate
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, s in enumerate(cast):
    cast[i] = s + ' ' + str(heights[i])

print(cast)