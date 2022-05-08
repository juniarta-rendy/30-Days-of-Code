T = int(input())

for i in range(0,T):
    s = input()
    even = []
    odd = []
    for i in range(len(s)):
        if i%2 == 0:
            even.append(s[i])
        else:
            odd.append(s[i])
    print(''.join(even) +' ' +''.join(odd))
