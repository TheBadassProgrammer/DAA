'''
Input Format:

    The first line contains an integer representing the number of activities.
    The second line contains space separated integers representing the start days.
    The third line contains space separated integers representing the end days.


Output Format:

    Print the total number of activities that a person can do.

'''

# Read input
n = int(input().strip())
start = list(map(int, input().split()))
end = list(map(int, input().split()))

# Combine activities as (start, end) pairs
activities = list(zip(end,start))

# Sort activities by end time
activities.sort()

count = 0
last_end = -1

# Greedy selection
for e, s in activities:
	if s > last_end:
		count += 1
		last_end = e

# Output result
print(count)