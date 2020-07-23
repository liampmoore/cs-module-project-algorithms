'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    # create a map
    num_map = {}

    # loop through the input array O(n)
    for num in arr:
        # increment occurences of given value to the corresponding key on the map
        if num in num_map:
            num_map[num] += 1
        else:
            num_map[num] = 1
    # loop through the map (O(n) - 1) /2
    for key in num_map:
        # if count is one return the key
        if num_map[key] == 1:
            return key


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")