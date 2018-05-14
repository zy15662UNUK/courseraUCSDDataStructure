# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def isBalanced(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        index = i + 1
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            bracket = Bracket(next, i)
            opening_brackets_stack.append(bracket)

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                return index
            if opening_brackets_stack[-1].Match(next):
                del(opening_brackets_stack[-1])
            else:
                return index
    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return opening_brackets_stack[-1].position + 1
if __name__ == "__main__":
    text = sys.stdin.read()
    print(isBalanced(text))
# print(isBalanced('[](()'))
# print("input is [](() " + str(isBalanced('[](()') == 3)) # middle unmatched open bracket
