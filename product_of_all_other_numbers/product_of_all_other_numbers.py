'''
Input: a List of integers
Returns: a List of integers
'''
# # Naive solution using division, against the constraint of no division but works perfectly.
# def product_of_all_other_numbers(arr):
#     # Your code here
#     # Save a variable which will hold the product of all numbers in original array
#     total_product = 1
#     # Loop through the array.
#     for i in range(len(arr)):
#         # Multiply the total product by each item in the array.
#         total_product = total_product * arr[i]
#     # New array to contain numbers which are product of all numbers except the number arr[i]
#     products = [0] * len(arr)
#     for i in range(len(arr)):
#         # Calculate the product of all numbers except for arr[i] using division.
#         products[i] = total_product/arr[i]
#     return products


def product_of_all_other_numbers(arr):

    # Create an array to hold products of all numbers to left of i
    left = [0] * len(arr)
    # Loop through arr to populate array containing the product of all values to the left of the value n. O(n) speed
    for index in range(len(arr)):
        # If the index is zero, there are no numbers to the left so it is None
        if index == 0:
            left[index] = None
        elif index == 1:
            left[index] = arr[index - 1]
        elif index == 2:
            left[index] = arr[index - 1] * arr[index - 2]
        else:
            left[index] = arr[index - 1] * left[index - 1]

    # Create an array to hold all products of numbers to the right of i
    right = [0] * len(arr)
    # Loop through arr to populate right O(n) speed, going from right to left
    for index in reversed(range(len(arr))):
        if index == len(arr) - 1:
            right[index] = None
        elif index == len(arr) - 2:
            right[index] = arr[index + 1]
        elif index == len(arr) - 3:
            right[index] = arr[index + 1] * arr[index + 2]
        else:
            right[index] = arr[index + 1] * right[index + 1]

    # Create an array to hold all the output products, space O(n)
    products = [0] * len(arr)
    for index in range(len(products)):
        if index == 0:
            products[index] = right[index]
        elif index == len(arr) - 1:
            products[index] = left[index]
        else:
            products[index] = left[index] * right[index]

    return products


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
