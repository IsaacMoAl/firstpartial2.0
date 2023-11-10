print("Hello worker, let´s start")


C = 0
N_W = 0
elder = 0
happy = 0
dragon = 0
super = 0
client = input("Is there any client? (yes/no)")
while client == "yes":
  C += 1
  wand = input("Has a wand has been sold? (yes/no)")
  if wand == "yes":
    print("""
    1. Elder wand 
    2. happy wand
    3. dragon wand 
    4. super wand
    """)
    type_of_wand = int(input("witch one have you bought?"))
    if type_of_wand == 1:
      elder += 1
    elif type_of_wand == 2:
      happy += 1
    elif type_of_wand == 3:
      dragon += 1
    elif type_of_wand == 4:
      super += 1 
  client = input("Is there any client? (yes/no)")

print(f"The number of clients was {C}")

print(f"number of elder wands {elder}")
print(f"number of elder wands {happy}")
print(f"number of elder wands {dragon}")
print(f"number of elder wands {super}")

