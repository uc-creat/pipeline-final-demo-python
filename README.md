Write a function that takes an array of integers and returns the length of the longest peak in the array.

A Peak is defined as adjecent integers in the array that are strictly increasing until they reach the tip ( the highest value in the peak ), at which point they become strictly decreasing. Atleast three integers are required to form a peak.

For Eg:
the integers -> 1,4,10,2  forms a peak, while
4,0,10 and 1,2,2,0 don't.
1,2,3 -> also do not form a peak -> as there is no strictly decreasing integer after 3.

1. Sample Input:

array = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]

1. Sample output:
6

explanation: 0,10,6,5,-1,-3 
