"""
gap = n // 2
while gap > 0:
    do insertion sort with step = gap
    gap = gap // 2
    
"""

def shellSort(arr):
    n = len(arr)
    gap = n // 2

    while(gap > 0):

        for i in range(gap, n):
            key = arr[i]
            j = i

            while(j>=gap and arr[j-gap]>key):
                arr[j] = arr[j-gap]
                j-=gap

            arr[j] = key

        gap = gap // 2

arr = [5,7,1,2,4,3,9]
shellSort(arr)
print(arr)

'''
Time complexity:
Worst - n^2
Avg   - n^1.5
Best  - nlogn
'''