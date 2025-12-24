
# Count vowels, consonants, digits, and special characters

s = "Hello@2025!"
vowels = "aeiouAEIOU"
v = c = d = sp = 0

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1
    elif ch.isdigit():
        d += 1
    else:
        sp += 1

print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Special:", sp)
