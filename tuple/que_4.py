# Create a tuple with mutable elements and modify them


t = ([1, 2, 3], [4, 5, 6])
t[0].append(99)
print(t)