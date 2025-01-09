from collections import deque

def check_matching_parenthesis(s):
  stack = deque()
  for char in s:
    if char == "(":
      stack.append(char)
    elif char == ")":
      if not stack:
        return False
      stack.pop()
  return len(stack) == 0

print(check_matching_parenthesis("()"))
print(check_matching_parenthesis("(hi there)"))
print(check_matching_parenthesis("(hell)o"))
print(check_matching_parenthesis("((linkedin)) learning"))

print(check_matching_parenthesis("(hi(there"))
print(check_matching_parenthesis("()ok)"))
print(check_matching_parenthesis("((increment)"))
print(check_matching_parenthesis(")linkedin()"))    
