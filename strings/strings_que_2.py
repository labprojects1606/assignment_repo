# Reverse each word individually


s = "This is a beautiful day"
words = s.split()
rev_words = [w[::-1] for w in words]
print(" ".join(rev_words))
