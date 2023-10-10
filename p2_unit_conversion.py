C = int(input("Put the cuantity"))

A2 = input("kilometers, galons, fahrenhein?")
  
if A2 == "kilometers":
  W1 = input("meters, centimeters")
  if W1 == "meters":
    W2 = C * 1000
    print(C,"in",W1,"is",W2,)
  elif W1 == "centimeters":
    W4 = C * 100000
    print(C,"in",W1,"is",W4,)
  else:
    print("Invalid option")

elif A2 == "galons":
  Q1 = input("liters, mililiters")
  if Q1 == "liters":
    Q2 = C * 3.78541
    print(C,"in",Q1,"is",Q2,)
  elif Q1 == "mililiters":
    Q2 = C * 3785.41
    print(C,"in",Q1,"is",Q2,)
  else:
    print("Invalid option")
    
elif A2 == "fahrenhein":
  T1 = input("celsius, kelvin")
  if T1 == "celsius":
    T2 = (C * 1.60934 * 9/5 + 32)
    print(C,"in",T1,"is",T2,)
  elif T1 == "kelvin":
    T3 = (C * 9/5 + 459.67)
    print(C,"in",T1,"is",T3,)
  else:
    print("Invalid option")
