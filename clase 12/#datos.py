#datos.pi
print("datos personales")
print("--------------")
vnom=str(input("ingrese su nombre"))
while True:
  try:
    vedad=int(input("ingrese edad"))
  except:
    print("valor no correspondido")  
print("----------------")
print(f"su nombre es: {vnom}")
print(f"su edad es: {vedad}")

print("programa finalizado...")