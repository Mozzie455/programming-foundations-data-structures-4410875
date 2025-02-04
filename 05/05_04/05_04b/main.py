from collections import deque

def print_binary_numbers(n):
  if n <= 0:
    return
  
  queue = deque()
  queue.append(1)

  for i in range(n):
    binary = queue.popleft()
    print(binary)
    queue.append(binary * 10)
    queue.append(binary * 10 + 1)

print_binary_numbers(6)
print()    
