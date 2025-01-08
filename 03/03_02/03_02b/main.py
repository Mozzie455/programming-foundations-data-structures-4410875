# Key: State
# Value: Capital

state_to_capital = {
  "Texas": "Austin",
  "New York": "Albany",

}
print(state_to_capital['New York'])

for key in state_to_capital.keys():
  print(key)

for key, value in state_to_capital.items():
  print(key + " | " + value)  