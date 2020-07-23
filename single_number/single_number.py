'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# total runtime complexity n * (n - 1)/2 or just n
def single_number(arr):
    # Your code here

    # create a map
    num_map = {}

    # Loop through the input array O(n)
    for num in arr:
        # If the number is already in map, delete that number the map
        if num in num_map:
            del num_map[num]
        # If the number isn't in the map add it to the map
        else:
            num_map[num] = 1
    # At this point there is only one key, return that number
    for key in num_map:
            return key
    
    # There is an alternative solution using the bitwise operator ^ that requires only O(1) space
    # For now the above solution has the best possible speed, O(n) speed and O(n) space 
    # Once you've finished some other problems come back to this one and use it to learn bitwise operations
    # It definitely feels like this should be simpler for a computer to figure out
    # Seems like bitwise operations are simpler ways of accomplishing very small binary logic


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")