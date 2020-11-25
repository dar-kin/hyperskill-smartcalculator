face = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
res = 0
for _i in range(6):
    n = input()
    if n in face:
        res += face[n]
    else:
        res += int(n)
print(res / 6)
