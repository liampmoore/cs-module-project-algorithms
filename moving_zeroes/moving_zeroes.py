'''
Input: a List of integers
Returns: a List of integers
'''

# Naive solution using list comprehensions
# def moving_zeroes(arr):
#     nonzeroes = [num for num in arr if num != 0]
#     for i in range(len(arr)):
#         if i < len(nonzeroes):
#             arr[i] = nonzeroes[i]
#         else:
#             arr[i] = 0
#     return arr

def moving_zeroes(arr):
    # Your code here
    # Create a variable to save the first zero, O(1) space
    first_zero = None
    # Loop until you find the first zero. O(n) speed
    for index, value in enumerate(arr):
        # If you find the first zero, save the location.
        if value == 0 and first_zero is None:
            first_zero = index
        # If you have already found the first zero and you come across a nonzero.
        elif first_zero is not None and value != 0:
            # switch the nonzero value location with the first zero.
            arr[index], arr[first_zero] = 0, value
            # Increment the first zero to the next space, which will always be zero if it has reached this clause.
            first_zero += 1
    # Returns the same array with all zeroes moved to the right of all nonzero values
    return arr
        


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")