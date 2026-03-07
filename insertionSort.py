def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while(j>=0 and arr[j]>key):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

arr = [2,5,1,8,3,0]
insertionSort(arr)
print(arr)

'''
Time complexity:
Worst - n^2
Avg   - n^2
Best  - n
'''