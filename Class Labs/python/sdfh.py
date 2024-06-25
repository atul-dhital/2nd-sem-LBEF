def check(s):
    for i in s:
        if i == 6:
            return True
        elif type(i) == list:
            if check(i):
                return True
    return False
s = [10, 20, 30, [2, 4, 3, [3, 6], 8]]
print(check(s))
