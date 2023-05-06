def strReverse(str_to_reverse):
    rtn_val = str_to_reverse[-1]
    for i in range(len(str_to_reverse) - 2, -1, -1):
        primeiro = str_to_reverse[i]
        rtn_val += primeiro
    return rtn_val

s = input()
while s != "0+0=0":
    flag = True
    operands, separator, output = s.partition("=")
    first, separator, second = operands.partition("+")
    first = int(strReverse(first))
    second = int(strReverse(second))
    output = int(strReverse(output))
    print(True if first + second == output else False)

    print(flag)
    s = input()

print(True)