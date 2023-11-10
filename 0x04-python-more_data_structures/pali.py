#!/usr/bin/python3
def is_palindrome(num):
    # Check if a number is a palindrome
    return str(num) == str(num)[::-1]

def find_largest_palindrome():
    largest_palindrome = 0

    # Iterate through all possible 3-digit numbers
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j

            # Check if the product is a palindrome and larger than the current largest palindrome
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome

# Find and print the largest palindrome made from the product of two 3-digit numbers
result = find_largest_palindrome()
print("The largest palindrome made from the product of two 3-digit numbers is:", result)
