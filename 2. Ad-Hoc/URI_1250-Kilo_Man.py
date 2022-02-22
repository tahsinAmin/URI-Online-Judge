for _ in range(int(input())):
    tasks = int(input())
    height = [int(i) for i in input().split()]
    action = input()
    cnt = 0
    for i in range(tasks):
        cnt += 1 if ((height[i] > 2 and action[i:i+1] == "J")
                     or (height[i] <= 2 and action[i:i+1] == "S")) else 0

    print(cnt)
