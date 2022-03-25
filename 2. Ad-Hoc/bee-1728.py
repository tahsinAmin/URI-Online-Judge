while True:
    try:
        flag = True
        s = input().split("=")
        output = s[1].rstrip("0") if len(s[1]) > 1 else s[1]
        first = s[0].split(
            "+")[0].rstrip("0") if len(s[0].split("+")[0]) > 1 else s[0].split("+")[0]
        second = s[0].split(
            "+")[1].rstrip("0") if len(s[0].split("+")[1]) > 1 else s[0].split("+")[1]

        if(first == second == output):
            print(True)
            break
        remain = 0
        first_len = len(first)
        second_len = len(second)
        output_len = len(output)
        min_val = min(first_len, second_len)
        max_val = max(first_len, second_len)

        variable_with_max_len = first if first_len > second_len else second
        i = 0
        while i < min_val:
            result = int(first[i]) + int(second[i]) + remain
            if(result > 9):
                remain = 1
            if result % 10 != int(output[i]):
                flag = False
                break
            i += 1

        while i < max_val:
            if int(variable_with_max_len[i]) != int(output[i]):
                flag = False
                break
            i += 1

        print(flag)
    except(EOFError):
        break
