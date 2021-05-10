"""
Problem Description

You are given two strings A and B of size N and M respectively.

You have to find the count of all permutations of A present in B as a substring. You can assume a string will have only lowercase letters.



Problem Constraints
1 <= N < M <= 105



Input Format
Given two argument, A and B of type String.



Output Format
Return a single Integer, i.e number of permutations of A present in B as a substring.



Example Input
Input 1:

 A = "abc"
 B = "abcbacabc"
Input 2:

 A = "aca"
 B = "acaa"


Example Output
Output 1:

 5
Output 2:

 2


Example Explanation
Explanation 1:

 Permutations of A that are present in B as substring are:
    1. abc
    2. cba
    3. bac
    4. cab
    5. abc
    So ans is 5.
Explanation 2:

 Permutations of A that are present in B as substring are:
    1. aca
    2. caa 
"""

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self,A, B):
        freq_a = [0]*26
        freq_b = [0]*26
        ind = 0
        ans = 0
        for i in range(len(A)):
            ind = ord(A[i])-97
            freq_a[ind] += 1
        
        for i in range(len(A)):
            ind = ord(B[i])-97
            freq_b[ind] += 1
        
        if Solution.compare(freq_a,freq_b):
            ans += 1
        
        
        
        for i in range(len(A),len(B)):
            ind = ord(B[i-len(A)])-97
            freq_b[ind] = freq_b[ind] -1
            ind = ord(B[i])-97
            freq_b[ind] += 1
            if Solution.compare(freq_a,freq_b):
                ans += 1
        
        return ans
        
        
    def compare(freq_a,freq_b):
        for i in range(26):
            if freq_a[i] != freq_b[i]:
                return False
        return True
            
