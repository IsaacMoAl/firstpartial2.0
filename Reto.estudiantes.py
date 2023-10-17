https://replit.com/@Isaac-JoaquinJo/Chalenge-1#main.py

def C(A):
  C_A = A - (A * (10 / 100)) - (A * (5 / 100))
  return C_A

def V(A):
  V_A = A - (A * 10 / 100)
  return V_A

def G(A):
  G_A = A - (A * 5 / 100)
  return G_A

A = int(input("What is your Purchase amount?"))
A2 = input("You Have a Membership card) (Yes/No)")

if A >= 100 and (A2 == "Yes") :
  print("Give me a moment")
  print("You will have a discount of 10%")
  print("And 5% more because you have a membership Card")
  print("Your final pay will be of", C(A))

elif A <= 100 and (A2 == "Yes"):

  print("Give me a moment")
  print("You will have a descount of 5% because of your membership card")
  print("Your final cost will be of",V(A))

elif A <= 100 and (A2 == "No"):
  print("Give me a moment")
  print("You wont resive any descount")
  print("Your final cost will be of",A)

elif A >= 100 and (A2 == "No"):
  print("Give me a moment")
  print("You will resive 10% because of your membership card")
  print("Your final cost will be of",G(A))

else:
  print("*Answer not definded*")
