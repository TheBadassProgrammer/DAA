arr = [2,8,4,6,3,1,9,6,1,1,4,13,11,13,15]

max = max(arr)
countArr = [0]*(max+1)

for i in arr:
    countArr[i] += 1

for i in range(len(countArr)):
    if countArr[i] != 0:
        while countArr[i] != 0:
            print(i, end=" ")
            countArr[i] -= 1