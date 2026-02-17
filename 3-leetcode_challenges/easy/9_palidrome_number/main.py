class Solution(object):
    def isPalindrome(self, x):
        """
        Determines if the provided string 'x' is a palindrome.

        :param x: str - The string to check for palindromic property.
        :return: bool - Returns True if 'x' is a palindrome, False otherwise.
        """
        # Reverse the string using slicing. The slice [::-1] creates a new string
        # that is the reverse of 'x'.
        reverse_x = x[::-1]

        # Compare the reversed string with the original string.
        if reverse_x == x:
            return True
        else:
            return False


class Solution2(object):
    def isPalindrome(self, x):
        """
        Determines if the provided integer 'x' is a palindrome by reversing its digits.

        :param x: int - The integer to check for palindromic property.
        :return: bool - Returns True if 'x' is a palindrome, False otherwise.
        """
        # Store the original value of x before modifying it.
        original_x = x

        # Initialize a variable to build the reversed number.
        reverse_x = 0

        # Process each digit until all digits have been reversed.
        while x != 0:
            # Extract the last digit of x.
            digit = x % 10

            # Append the digit to reverse_x by shifting its current digits left and adding the new digit.
            reverse_x = reverse_x * 10 + digit

            # Remove the last digit from x.
            x = x // 10

        # Compare the reversed number with the original number.
        # Return True if they are the same (palindrome), otherwise False.
        if reverse_x == original_x:
            return True
        else:
            return False


# Prompt the user to enter a number.
input_num = input('Enter a number: ')

# Use the string-based palindrome check.
# Note: The input is taken as a string, so it checks if the string is the same
# when reversed.
print(Solution().isPalindrome(input_num))

# Convert the input string to an integer and use the integer-based palindrome check.
# As explained above, the integer-based method might not work as intended because
# it modifies the input number without storing its original value.
print(Solution2().isPalindrome(int(input_num)))
