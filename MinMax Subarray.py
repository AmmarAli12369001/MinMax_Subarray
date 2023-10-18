"""
MinMax Subarray
You are given an array of size N. The elements of the array are not necessarily distinct.
Find the shortest subarray that contains at least one of the minimum and one of the maximum values.

Standard input
The first line contains a single integer value N.
The second line contains N integer values representing the elements of the array.

Standard output
The output should contain a single integer representing the length of the wanted subarray.
"""

n = int(input())
array = list(map(int, input().split()))

min_list = []

if __name__ == "__main__":
    minimum = min(array)
    maximum = max(array)

    shortest_distance = n+1

    for i in range(n):
        if array[i] == minimum:
            min_list.append(i)

    for i in range(n):
        if array[i] == maximum:
            for j in min_list:
                if abs(j - i) < shortest_distance:
                    shortest_distance = abs(j - i) + 1
    print(shortest_distance)
