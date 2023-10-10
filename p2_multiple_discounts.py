print("Welcome to the smart waldmart, Here there are the new products for today")
print("Eeeeeeeyyy, we have new discounts, pear section")
print("The product belog to an specific section: A, B, C. Each of the have discount")

P = int(input("What is the price of the product?"))
A = input("What is the section? (A, B, C): ")
N = int(input("The amount of the products"))

if N >= 10:
  N3= .5

elif N <= 10:
  N3 =  0
  
N3 = int(input("click tap to continue"))

if A == "A":
  print("The discount is 10%")
  print("The total price is: ", P * N - (0.9 * (P*N)) * -N3)
elif A == "B":
  print("The discount is 5%")
  print("The total price is: ", P * N - (0.95* (P*N)) * -N3)
elif A == "C":
  print("The discount is 2%")
  print("The total price is: ", P * N - (0.98 * (P*N)) * -N3)
else:
  print("The discount is 0%")
  print("The total price is: ", P * N * N3)
