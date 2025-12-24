# Demonstrate string immutability


s = "ravi"
try:
    s[0] = "R"   # This will cause error
except TypeError as e:
    print("Error:", e)

# Correct way
s = "R" + s[1:]
print(s)
