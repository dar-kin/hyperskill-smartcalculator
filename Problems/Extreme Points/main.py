# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
min_k = "a"
max_k = "b"
for elem in test_dict:
    if test_dict[elem] > test_dict[max_k]:
        max_k = elem
    if test_dict[elem] < test_dict[min_k]:
        min_k = elem
print(f"""min: {min_k}
max: {max_k}""")
dict = {}
dict.de
