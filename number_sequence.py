x = (input("Give me the number: "))
arr = []
for i in range(0, len(x)):
    a = int(x[i]) + 1
    arr.append(a)
for i in range(0, len(arr)):
    print(arr[i], end="")
