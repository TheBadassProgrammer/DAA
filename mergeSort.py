def mergeSort(arr):
    if(len(arr)<=1):
        return arr
    
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)
    return merge(sortedLeft,sortedRight)

def merge(left, right):
    result = []
    i = j = 0
    while(i<len(left) and j<len(right)):
        if(left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result

arr = [3,5,6,3,2,7,1]
print(mergeSort(arr))

'''
Merge sort has a time complexity of nlogn for best, avg and worst case.
Space complexity of O(n) because its not inplace.
'''