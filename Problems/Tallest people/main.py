def tallest_people(**params):
    res = {}
    tall = 0
    for elem in params:
        if params[elem] > tall:
            res.clear()
            tall = params[elem]
            res[elem] = tall
        elif params[elem] == tall:
            res[elem] = tall
    names = list(res.keys())
    names.sort()
    for elem in names:
        print(f"{elem} : {res[elem]}")
