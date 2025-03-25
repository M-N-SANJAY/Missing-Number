'''
Intuition:
    Two important properties of XOR are the following:

    XOR of two same numbers is always 0 i.e. a ^ a = 0. ←Property 1.
    XOR of a number with 0 will result in the number itself i.e. a ^ 0 = a.  ←Property 2

    Now, let’s XOR all the numbers between 1 to N.
    xor1 = 0^1^2^.......^N

    Let’s XOR all the numbers in the given array.
    xor2 = 0^1^2^......^N (contains all the numbers except the missing one).

    Now, if we again perform XOR between xor1 and xor2, we will get:
    xor1 ^ xor2 = (0^0)^(1^1)^(2^2)^........^(missing Number)^.....^(N^N)

    Here all the numbers except the missing number will form a pair and each pair will result in 0 according to the XOR property. The result will be = 0 ^ (missing number) = missing number (according to property 2).

    So, if we perform the XOR of the numbers 1 to N with the XOR of the array elements, we will be left with the missing number.

Approach:

    We will first run a loop(say i) from 0 to N-1(as the length of the array = N).
    Inside the loop, xor2 variable will calculate the XOR of array elements
    i.e. xor2 = xor2 ^ a[i].

    And the xor1 variable will calculate the XOR of 0 to N-1 i.e. xor1 = xor1 ^ i.
    After the loop ends we will XOR xor1 and N to get the total XOR of 0 to N.
    Finally, the answer will be the XOR of xor1 and xor2.
'''
def missingNumber(nums):

    xor1 = 0
    xor2 = 0
    N = len(nums)

    for i in range(N):
        xor2 = xor2 ^ nums[i]  # XOR of array elements
        xor1 = xor1 ^ i  # XOR up to [1...N-1]
    
    xor1 = xor1 ^ N  # XOR up to [1...N]

    return xor1 ^ xor2  # the missing number

#Time Complexity : O(N)
#Space Complexity : O(1)