class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Finds the longest common prefix string amongst a list of strings.

        :param strs: List[str] - A list of strings to check.
        :return: str - The longest common prefix shared among the strings. Returns an empty
                       string if there is no common prefix.
        """

        # If the list of strings is empty, return an empty string as there is no common prefix.
        if not strs:
            return ""

        # Initialize the prefix to be the first string in the list.
        prefix = strs[0]

        # Iterate over each of the remaining strings in the list.
        for s in strs[1:]:
            # Reduce the current prefix until it is a prefix of the current string 's'.
            while not s.startswith(prefix):
                # Remove the last character from the prefix.
                prefix = prefix[:-1]
                # If the prefix becomes empty, it means there is no common prefix.
                if not prefix:
                    return ""

        # After checking all strings, 'prefix' contains the longest common prefix.
        return prefix

    def listMaking(self, strs):
        """
        Converts a string representation of a list of strings (e.g., '["flower","flow","flight"]')
        into an actual Python list of strings.

        :param strs: str - The string input containing the list of strings.
        :return: List[str] - A list of strings parsed from the input.
        """

        # Remove the enclosing square brackets '[' and ']'.
        remove_brackets = strs[1:-1]

        # Initialize an empty string to accumulate characters excluding quotes.
        remove_quotes = ""

        # Iterate over each character in the string without the brackets.
        for char in remove_brackets:
            # Append the character if it is not a double quote.
            if char != '"':
                remove_quotes += char

        # Split the string by commas to create a list of strings.
        list_of_strs = remove_quotes.split(',')

        return list_of_strs


# Prompt the user to enter a list of strings in the required format.
user_input = input('Enter the list of strings (e.g. ["flower","flow","flight"]): ')

# Convert the user input into an actual list of strings using the listMaking method.
list_of_strs = Solution().listMaking(user_input)

# Find and print the longest common prefix among the list of strings.
print(f'"{Solution().longestCommonPrefix(list_of_strs)}"')
