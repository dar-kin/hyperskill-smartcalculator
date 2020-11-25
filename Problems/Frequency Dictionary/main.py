# put your python code here
words = {}
a = [x.lower() for x in input().split()]
for elem in a:
    if elem in words:
        words[elem] += 1
    else:
        words[elem] = 1
for elem in words:
    print(elem, words[elem])
