class Solution(object):
    def romanToInt(self, s):
        """
        Converts a Roman numeral string into its integer representation.

        :param s: str - A string representing a Roman numeral (e.g., "XIV").
        :return: int - The integer value of the Roman numeral.
        """

        # Initialize the total sum of the numeral values.
        total = 0
        # This variable will keep track of the value of the previous numeral processed.
        previous_value = 0

        # Define a mapping from Roman numeral characters to their corresponding integer values.
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # Reverse the string to process the numeral from right to left.
        # This makes it easier to decide whether to add or subtract each value.
        s = reversed(s)

        # Iterate over each character in the reversed Roman numeral string.
        for char in s:
            # Retrieve the integer value corresponding to the current Roman numeral.
            value = roman_map[char]

            # If the current numeral is greater than or equal to the previous numeral,
            # add its value to the total.
            # Otherwise, subtract its value (this handles cases like "IV" where I comes before V).
            if value >= previous_value:
                total += value
            else:
                total -= value

            # Update the previous_value for the next iteration.
            previous_value = value

        # Return the computed integer value.
        return total


# Prompt the user to enter a Roman numeral string.
user_input = input('Enter the Roman numerals: ')

# Create an instance of the Solution class and convert the Roman numeral to an integer.
print(Solution().romanToInt(user_input))
