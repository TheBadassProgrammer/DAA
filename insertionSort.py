def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while(j>=0 and arr[j]>key):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

arr = [2,5,1,8,3,0]

print(insertionSort(arr))

'''
Time complexity:
Worst - n^2
Avg   - n^2
Best  - n
'''