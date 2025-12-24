# Reverse each word individuallyRemove common elements from two sets


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Remove common elements
set1 -= set2
set2 -= {1, 2, 3, 4}
print("Set1:", set1)
print("Set2:", set2)
