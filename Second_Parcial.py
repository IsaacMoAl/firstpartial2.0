https://replit.com/@Isaac-JoaquinJo/Healthy-Diet#main.py
A = int(input("Give me you age"))
W = int(input("Your weight (in Kg)"))
PA = input("Introduce your physical activity (sedentary, moderate, active) ")
H = float(input("Your High (in meters)"))

def P(H):
  X = W / ((H)**2)
  return X


if A <= 18:
  print("We recommend a high carbohydrate diet.")
  
elif A > 25:
  print("We recommend a low sugar diet.")

else:
  print("introduce the data right")


if A >= 18 and A <= 25 and (PA == "moderate" or PA == "active" ):
  print("We recommend a high protein and lowercarbohydrate diet.")
   
elif A >= 18 and A <= 30 and (PA == "sedentary" or PA == "moderate"):
  print("You need more aerobic exercises.")

else:
  print("introduce the data right")
  
if P(H) < 18 and (PA == "sedentary"):
  print("You need to consult a nutritionist and increase your physical activity")

elif P(H) >= 18 and P(H) <= 25 and (PA == "moderate" or PA == "active"):
  print("You are in good condition")

elif P(H) > 25 and (PA == "sedentary"):
  print("Consult a nutrionist, increase physical activity, reduce your weight")

else:
  print("introduce the data right")
