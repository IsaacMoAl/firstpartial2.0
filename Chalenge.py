def suma(a,b):
  x= a + b
  return x

def resta(a,b):
  x = a - b
  return x

print("Dame el primer número:")
a = int(input())
print("Dame el segundo número")
b = int(input())
print("la suma de",suma(a,b),"y l resta da", resta(a,b))








def multiplication(a,b):
  x = a * b
  return x


def divition(a,b):
  x = a / b
  return x

print("give me the firt number")
a = int(input())

print("Give me the second one")
b= int(input())

print("la multiplicacion de",multiplication(a,b),"la divition de",divition(a,b),)

def y():
  y = a * 1000
  return y

a =int(input("How many kilometers have you done?, I will give you the number meters"))
print("You have done",y(),"meters")

B= int(input("Gave me the base of your triangle:"))
H= int(input("Give me the height:"))

def triangle_area():
  w = ( B * H ) /2
  return w
  
print("Ok so your triangle have an area of",triangle_area(),"cm2")


