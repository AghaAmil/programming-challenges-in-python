class Solution(object):
    def twoSum(self, nums, target):
        """
        Finds two indices in 'nums' such that the numbers at these indices add up to 'target'.

        :param nums: List[int] - The list of integers to search through.
        :param target: int - The target sum to find.
        :return: List[int] - A list containing the two indices of the numbers that add up to the target.
        """
        # Loop over each index in the list
        for i in range(len(nums)):
            # For each index 'i', check all indices 'j' that come after 'i'
            for j in range(i + 1, len(nums)):
                # If the sum of the numbers at indices 'i' and 'j' equals the target...
                if nums[i] + nums[j] == target:
                    # ...return the pair of indices as the solution.
                    return [i, j]

    def listMaking(self, user_input):
        """
        Converts a string representation of a list (e.g., "[1, 2, 3]") into an actual list of integers.

        :param user_input: str - The input string provided by the user.
        :return: List[int] - A list of integers parsed from the input string.
        """
        # Remove any leading/trailing whitespace and the enclosing square brackets.
        # This assumes the input always starts with '[' and ends with ']'.
        remove_brackets = user_input.strip()[1:-1]

        # Split the string by commas to obtain individual number strings.
        split_numbers = remove_brackets.split(',')

        # Convert each number string to an integer after stripping any extra whitespace.
        list_of_nums = [int(num.strip()) for num in split_numbers]

        return list_of_nums


# Prompt the user to enter a list of numbers in the format "[1, 2, 3, 4, 5, 6, 7]".
user_input = input('Enter the list of numbers (e.g., [1, 2, 3, 4, 5, 6, 7]): ')

# Prompt the user to enter the target sum and convert it from string to integer.
target = int(input('Enter the target sum: '))

# Create an instance of the Solution class and convert the user input string to a list of integers.
input_array = Solution().listMaking(user_input)

# Use the twoSum method to find the two indices that add up to the target sum.
result = Solution().twoSum(input_array, target)

# Print the result (the list of indices).
print(result)