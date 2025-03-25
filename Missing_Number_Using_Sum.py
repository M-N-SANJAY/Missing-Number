'''

Intuition:

    We know that the summation of the first N numbers is (N*(N+1))/2. We can say this S1. Now, in the given array, every number between 1 to N except one number is present. So, if we add the numbers of the array (say S2), the difference between S1 and S2 will be the missing number. Because, while adding all the numbers of the array, we did not add that particular number that is missing.

Approach:

    We will first calculate the summation of first N natural numbers(i.e. 1 to N) using the specified formula.
    Then we will add all the array elements using a loop.
    Finally, we will consider the difference between the summation of the first N natural numbers and the sum of the array elements.

'''
def missingNumber(nums):
    # Summation of all array elements and length : 
    sum = N = 0
    for num in nums:
        N += 1
        sum += num

    # Summation of first N numbers:
    summation = (N * (N + 1)) // 2

    missingNum = summation - sum
    return missingNum

#Time Complexity : O(N)
#Space Complexity :  O(1)