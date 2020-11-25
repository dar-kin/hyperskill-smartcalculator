def select_dates(potential_dates):
    res = ""
    for elem in potential_dates:
        if elem["age"] > 30 and elem["city"] == "Berlin" and "art" in elem["hobbies"]:
            res += elem["name"] + ", "
    return res[:len(res) - 2]
