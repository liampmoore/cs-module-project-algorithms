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
    # Create an array to hold all products of numbers to the right of i
    right = [0] * len(arr)

    # Loop through arr to populate left O(n) speed
    for index, value in enumerate(arr):
        # If the index is zero, we need that first value to simply be the first value
        if index == 0:
            left[index] = value
        else:
            left[index] = value * left[index - 1]
    # Loop through arr to populate right O(n) speed, going from right to left
    for index in range(1, len(arr)):
        if index == 1:
            right[-1] = arr[-1]
        else:
            right[index * -1] = value * right[(index * -1) + 1]
        print(index, right[index])

    # Create an array to hold all the output products, space O(n)
    products = [0] * len(arr)
    for i in range(len(products)):
        if index == 0:
            products[i] == right[i]
        elif index == len(arr) - 1:
            products[i] == left[i]
        else:
            products[i] = left[i] * right[i]

    return products

    # Couldn't complete the solution with no division in sufficient time.
    # The error was with debugging and reverse indexing, spent too much time on this one and got worn out.


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
