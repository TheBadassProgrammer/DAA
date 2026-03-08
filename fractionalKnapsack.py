'''
Input:
3 50                 number of items, max capacity of knapsack
60 10 100 20 120 30  (value, weight) pairs

Output:
240.000000           the maximum total value that can be obtained in the knapsack
'''

n, w = map(int, input().split())
arr = list(map(int, input().split()))
items = []

for i in range(0, 2*n, 2):
    value = arr[i]
    weight = arr[i+1]
    ratio = value / weight
    items.append((ratio, value, weight))

items.sort(reverse=True)

totalValue = 0

for ratio, value, weight in items:
    if w == 0:
        break

    if weight <= w:
        totalValue += value
        w -= weight
    else:
        totalValue += value * (w / weight)
        w = 0

print(f"{totalValue:.6f}")