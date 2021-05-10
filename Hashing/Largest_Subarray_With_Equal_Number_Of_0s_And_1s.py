"""
Given an array of integers A consisting of only 0 and 1.

Find the maximum length of a contiguous subarray with equal number of 0 and 1.



Input Format

The only argument given is the integer array A.
Output Format

Return the maximum length of a contiguous subarray with equal number of 0 and 1.
Constraints

1 <= length of the array <= 100000
0 <= A[i] <= 1
For Example

Input 1:
    A = [1, 0, 1, 0, 1]
Output 1:
    4
    Explanation 1:
        Subarray from index 0 to index 3 : [1, 0, 1, 0]
        Subarray from index 1 to index 4 : [0, 1, 0, 1]
        Both the subarrays have equal number of ones and equal number of zeroes.

Input 2:
    A = [1, 1, 1, 0]
Output 2:
    2
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        hash_map = {0:-1}
        curr_sum = 0
        max_len = 0
        
        for i in range(len(A)):
            if A[i] == 0:
                curr_sum = curr_sum -1
            else:
                curr_sum = curr_sum + 1 
            
            if curr_sum in hash_map:
                if max_len < i-hash_map[curr_sum]:
                    max_len = i - hash_map[curr_sum]
            else:
                hash_map[curr_sum] = i
        return max_len
