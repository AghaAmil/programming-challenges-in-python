class Solution(object):
    def isValid(self, s):
        """
        Determines if a string of bracket characters is valid.
        A string is considered valid if all brackets are closed in the correct order.

        :param s: str - The input string containing only bracket characters.
        :return: bool - True if the string is valid (all brackets are correctly matched), False otherwise.
        """

        # Initialize an empty list to use as a stack for tracking unmatched brackets.
        result = []

        # Iterate over each character in the input string.
        for char in s:
            # If the stack is empty, simply push the current character onto the stack.
            if not result:
                result.append(char)
            else:
                # Check if the current character matches with the last bracket in the stack.
                # If it matches, remove the last element from the stack (i.e., a valid pair is found).
                if self.charMatching(result[-1], char):
                    # Remove the last element by slicing off the end of the list.
                    result = result[:-1]
                else:
                    # If it doesn't match, push the current character onto the stack.
                    result.append(char)

        # If the stack is empty, all brackets have been successfully matched.
        # Otherwise, if there are any unmatched brackets left, the string is invalid.
        if result:
            return False
        else:
            return True

    def charMatching(self, char1, char2):
        """
        Checks if two characters are matching pairs of brackets.

        :param char1: str - The opening bracket.
        :param char2: str - The closing bracket.
        :return: bool - True if char1 and char2 form a valid pair, False otherwise.
        """
        # Check for the three valid pairs of brackets.
        if (char1 == '(' and char2 == ')') or \
                (char1 == '[' and char2 == ']') or \
                (char1 == '{' and char2 == '}'):
            return True

        return False

    def userInput(self):
        """
        Prompts the user for input and ensures that only valid bracket characters are entered.
        Note: The current logic returns the input string as soon as a valid bracket is encountered,
        which might not catch cases where invalid characters are mixed in.

        :return: str - The user-provided input string containing bracket characters.
        """
        while True:
            # Prompt the user to enter a string of bracket characters.
            input_str = input('Enter String Input: ')

            # Check each character in the input string.
            for char in input_str:
                # If a character is not one of the valid brackets, notify the user.
                if char not in ['(', '{', '[', ')', '}', ']']:
                    print("Invalid input Entered, just '(', ')', '{', '}', '[' and ']' characters are accepted")
                else:
                    # Return the input string if the character is valid.
                    # Note: This returns after encountering the first valid character,
                    # which may not be the intended behavior if there are invalid characters later.
                    return input_str


class Solution2(Solution):
    def isValid(self, s):
        """
        Determines if a string of bracket characters is valid using a stack and a mapping of pairs.
        This method improves the bracket matching by clearly defining the relationships between brackets.

        :param s: str - The input string containing only bracket characters.
        :return: bool - True if the string is valid (all brackets are correctly matched), False otherwise.
        """
        # Define a mapping where each closing bracket maps to its corresponding opening bracket.
        bracket_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # Initialize an empty stack to track the opening brackets.
        stack = []

        # Iterate over each character in the input string.
        for char in s:
            # If the character is a closing bracket...
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty; otherwise, use None.
                top_element = stack.pop() if stack else None

                # If the top element does not match the corresponding opening bracket, the string is invalid.
                if bracket_map[char] != top_element:
                    return False
            else:
                # If the character is an opening bracket, push it onto the stack.
                stack.append(char)

        # If the stack is empty after processing all characters, all brackets were properly matched.
        return not stack


# Prompt the user to enter a string containing only bracket characters.
user_input = Solution().userInput()

# Validate the input string using the first implementation.
print(Solution().isValid(user_input))
# Validate the input string using the second, improved implementation.
print(Solution2().isValid(user_input))
