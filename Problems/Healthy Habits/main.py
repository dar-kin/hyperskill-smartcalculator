# the list "walks" is already defined
# your code here
res = 0
for elem in walks:
    res += elem["distance"]
print(int(res / len(walks)))
