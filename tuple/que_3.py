# Count occurrence of an element in a tuple (without built-in count)

t = (1, 2, 3, 2, 4, 2)
element = 2
count = 0
for i in t:
    if i == element:
        count += 1
print(f"Occurrence of {element}:", count)
