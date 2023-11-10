N_t = input("")


Resp2 = N_t.split(" ")
Resp1 = Resp2.count("alexa")

if Resp1 >= 3:
  print("Stop, you are annoying")
elif Resp1 == 2:
  print("Yes? Yes?")
elif Resp1 == 1:
  print("Yes how can I help you?")
