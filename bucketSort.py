myArray = [170, 45, 75, 90, 802, 24, 2, 66]

maxEl = max(myArray)
minEl = min(myArray)
bucketNo = 5
buckets = [[],[],[],[],[]]
bucketSize = (maxEl - minEl) // bucketNo + 1

for el in myArray:
    index = (el - minEl) // bucketSize
    buckets[index].append(el)

final = []

for bucket in buckets:
    final.extend(sorted(bucket))

print(final)