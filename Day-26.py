returned = input()
due = input()

x = list(map(int, returned.split()))
y = list(map(int, due.split()))

pay = 0

if x[2] > y[2]:
    pay = 10000
elif x[2] == y[2]:
    if x[1] > y[1]:
        pay = (x[1] - y[1]) * 500
    elif x[0] > y[0]:
        pay = (x[0] - y[0]) * 15

print(pay)