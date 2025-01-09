primary_colors: str = set(["red", "blue", "yellow"])

color: str = "green"

if color in primary_colors:
  print(f"{color} is a primary color")
else:
  print(f"{color} is not a primary color")

letters:str = set(['a','b'])
letters.add('c')
print(letters)  