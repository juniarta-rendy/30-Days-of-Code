x = int(input())

arr = {}

for i in range(x):
    inpt = input().split()
    arr[inpt[0]] = inpt[1]
    
while True:
    try:
        search = input()
        if search in arr:
            print(search +'=' +arr[search])
        else:
            print('Not found')
    except EOFError:
        break