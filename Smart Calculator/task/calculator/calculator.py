from string import ascii_letters, digits


operations = {"+", "-", "="}
high_priority_operations = {"*", "/", "(", ")"}
replacements = {"++": "+", "--": "+", "+-": "-", "-+": "-"}
variables = {}


def replace_parse(n):
    while True:
        done = True
        for elem in replacements.keys():
            if elem in n:
                done = False
                n = n.replace(elem, replacements[elem])
        if done:
            break
    return n


def parser(n):
    n = replace_parse(n)
    express = []
    i = 0
    k = 0
    first_sign = False
    if n[0] in operations:
        express.append(n[0])
        first_sign = True
        k += 1
        n = n.lstrip(n[0])
    op_count = 0
    ints_count = 0
    while i < len(n):
        if n[i].isnumeric():
            num = first_integer(n[i:])
            express.append(int(num))
            i += len(num)
            ints_count += 1
        elif n[i] in operations or n[i] in high_priority_operations:
            express.append(n[i])
            if n[i] not in "()":
                op_count += 1
            i += 1
        elif n[i] == " ":
            i += 1
            continue
        else:
            key = first_variable(n[i:])
            num = variables[key]
            express.append(num)
            i += len(key)
            ints_count += 1

    if first_sign:
        f_s = express.pop(0)
        if f_s == "+":
            pass
        elif f_s == "-":
            express[0] = -express[0]
        else:
            raise ValueError
    if ints_count - 1 != op_count:
        raise ValueError
    return post_fix(express)


def post_fix(nums):
    stack = []
    res = []
    for i in range(len(nums)):
        if isinstance(nums[i], int):
            res.append(nums[i])
        elif len(stack) == 0 or stack[len(stack) - 1] == "(" or nums[i] == "(":
            stack.append(nums[i])
        elif nums[i] == ")":
            if stack.count("(") == 0:
                raise ValueError("Invalid expression")
            while stack[len(stack) - 1] != "(":
                res.append(stack.pop())
            stack.pop()
        elif lower_prec(nums[i], stack[len(stack) - 1]):
            while lower_prec(nums[i], stack[len(stack) - 1]):
                res.append(stack.pop())
                if len(stack) == 0:
                    break
            stack.append(nums[i])
        elif not lower_prec(nums[i], stack[len(stack) - 1]):
            stack.append(nums[i])
    while len(stack) != 0:
        elem = stack.pop()
        if not isinstance(elem, int) and elem in "()":
            raise ValueError("Invalid expression")
        res.append(elem)
    return res


def lower_prec(a, b):
    if a in operations and b in high_priority_operations and b not in "()" or a in operations and b in operations:
        return True
    else:
        return False


def first_integer(n):
    res = ""
    for i in n:
        if i.isnumeric():
            res += i
        else:
            break
    return res


def basic_operation(a, b, op):
    if op == "+":
        return b + a
    elif op == "-":
        return b - a
    elif op == "*":
        return b * a
    elif op == "/":
        return b / a
    else:
        raise ValueError("Unknown operator")


def solve_from_string(n):
    if n in variables:
        return variables[n]
    express = parser(n)
    stack = [express[0]]
    i = 1
    for i in range(1, len(express)):
        if isinstance(express[i], int):
            stack.append(express[i])
        else:
            stack.append(basic_operation(stack.pop(), stack.pop(), express[i]))
    return stack.pop()


def check_letter_syntax(n):
    if n.find("**") != -1 or n.find("//") != -1:
        raise ValueError("Invalid expression")
    for elem in n:
        if elem in digits or elem in operations or elem in ascii_letters or elem == " " or elem in high_priority_operations:
            continue
        else:
            print("check")
            raise ValueError("Invalid identifier")


def is_assignment(n):
    return "=" in n


def assignment(n):
    n = replace_parse(n)
    n = n.strip()
    exist = n.find("=")
    if exist != -1:
        key = first_variable(n[:exist])
        string_value = n[exist + 1:].strip()
        is_negative = False
        if string_value[0] == "-":
            string_value = string_value[1:]
            is_negative = True
        elif string_value[0] == "+":
            string_value = string_value[1:]
        if string_value.isnumeric():
            value = int(first_integer(string_value))
            if is_negative:
                value = -value
            variables[key] = value
        elif string_value in variables:
            value = variables[string_value]
            variables[key] = int(value)
        elif string_value.isalpha():
            raise KeyError
        else:
            raise ValueError("Invalid assignment")


def first_variable(n):
    res = ""
    for elem in n:
        if elem in ascii_letters:
            res += elem
        elif elem == " " or elem in operations or elem in high_priority_operations:
            break
        else:
            print("variables")
            raise ValueError("Invalid identifier")
    return res


def run():
    while True:
        n = input().lstrip(" +")
        if n == "/exit":
            break
        elif n == "/help":
            print("The program calculates the sum of numbers")
            continue
        elif n.startswith("/"):
            print("Unknown command")
            continue
        elif len(n) == 0:
            continue
        try:
            check_letter_syntax(n)
            if is_assignment(n):
                assignment(n)
            else:
                print(int(solve_from_string(n)))
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print("Unknown variable")
    print("Bye!")


run()

