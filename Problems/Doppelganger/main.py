from _collections_abc import Hashable


lib = {}
for elem in object_list:
    if isinstance(elem, Hashable):
        key = hash(elem)
        if key in lib:
            lib[key] += 1
        else:
            lib[key] = 1
count = 0
for elem in lib:
    if lib[elem] > 1:
        count += lib[elem]
print(count)
