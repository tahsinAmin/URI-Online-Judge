dictionary = {
   "tesoura": ["papel", "lagarto"],
   "papel":    ["pedra", "spock"],
   "pedra":     ["lagarto", "tesoura"],
   "lagarto":   ["spock", "papel"],
   "spock":    ["tesoura", "pedra"],
}

for i in range(int(input())):
   m,n = input().split()
   if m == n:
      print("empate")
   if n in dictionary[m]:
      print("Rajesh")
   else:
      print("Sheldon")