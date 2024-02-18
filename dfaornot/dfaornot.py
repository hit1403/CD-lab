s = input("enter list of states: ")
states = s.split(",")
sym = input("enter list of symbols: ")
symbols = sym.split(",")
S = input("enter start state: ")
F = input("enter final states: ").split(",")

table = []
for i in range(len(states)):
  st = input(f"enter for state {i}: ")
  table.append(st.split(","))

string = input("enter string to check:")
tempF = S
for s in string:
  ind = symbols.index(s) + 1
  for subt in table:
    if subt[0] == tempF:
      tempF = subt[ind]
      #print(tempF)
if tempF in F:
  print("the string is valid\n")
else:
  print("the string is not valid\n")


