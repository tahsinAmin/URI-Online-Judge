while True:
    alumni, dinners = list(map(int, input().split()))
    if alumni == dinners == 0:
        break

    list_cnt = [0]*alumni
    for _ in range(dinners):
        a1 = list(map(int, input().split()))
        for i in range(alumni):
            list_cnt[i] += 1 if a1[i] == 1 else 0
    print("yes" if dinners in list_cnt else "no")
