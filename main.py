import math

age = 16
taille = 1.68
prenom = "Inès"
demi_pensionnaire = True

print("Variables Types : \n", type(age), "\n", type(taille), "\n",
      type(prenom), "\n", type(demi_pensionnaire))

print("-------ACTIVITE 2-------")

a = 5
b = 16
c = 3.14 / 2
d = b / a
e = b // a
f = b % a
g = math.pow(a, 2)
h = math.sqrt(b)
i = math.sin(c)

print("Results : \n", "d = ", d, "\n", "e = ", e, "\n", "f = ", f, "\n",
      "g = ", g, "\n", "h = ", h, "\n", "i = ", i)

print("-------ACTIVITE 3-------")

a = "Hello"
b = "World"
mon_expression = a + b

print(mon_expression)

print("-------ACTIVITE 4-------")
a = "Nombre de pommes : "
b = 4
c = a + str(b)

print(c)
print("-------ACTIVITE 5-------")
v1 = "Hello"
v2 = "World"

print((v1 + v2) * 4)
print("-------ACTIVITE 6-------")
temps = "pluvieux"
temperature = 12
meteo = f"Demain, le temps sera {temps} et la température de {temperature}°C"

print(meteo)
print("-------ACTIVITE IMAD-------")
prompt = input("give me you soul")

if prompt == "NO":
  print("ok")
elif prompt == "YES":
  print("thanks")
else:
  print("what")