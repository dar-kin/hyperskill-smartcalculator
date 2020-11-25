from _collections_abc import Hashable


objects_dict = {}
for elem in objects:
    if isinstance(elem, Hashable):
        objects_dict[elem] = hash(elem)
