matches = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
n_matches = []

j = 0
for i in range(15):
    m, n = map(int, input().split())
    
    result = j if m > n else j+1
    n_matches.append(matches[result])

    if (j is len(matches) - 2):
        j = 0
        matches,n_matches = n_matches,[]
    else:
        j +=2

print(matches[0])