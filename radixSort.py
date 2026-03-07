myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)

radixArray = [[],[],[],[],[],[],[],[],[],[]] # to store elements of myArray based on their digits place. Hence ten arrays in this 2-d array for digit 0-9. 
maxEl = max(myArray)
exp = 1

while maxEl // exp > 0: # so that the loop does not run for the thousand place here. because 802//1000 = 0

    for i in myArray:
        index = (i // exp) % 10
        radixArray[index].append(i)
    
    myArray = []

    for arr in radixArray:
        myArray.extend(arr)

    radixArray = [[],[],[],[],[],[],[],[],[],[]]

    exp *= 10

print(myArray)


'''
after sorting by ones place. The arrays would look like this:
myArray = [ ]
radixArray = [ [40], [], [], [33], [24], [45, 25], [], [17], [], [] ]

then we zip the radix array back into myArray maintaining their order.
do the same again for tens and hundreds place.

For explanation - https://www.w3schools.com/dsa/dsa_algo_radixsort.php
'''