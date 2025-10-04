cuenta=1
print("cuenta del 1 al 10 :")
while(cuenta<11):
    print(cuenta)
    cuenta+=1

print("contar solo pares ")
def es_par(numero):
    if numero % 2 == 0:
        print(numero)
        return True
    
    else:
        return False

print("sumar numeros del 1 al 5 ")
ini=1
for ini in range(5):
    op1=ini+(ini+1)
    if ini == 0:
       print() 
    elif ini >0:
        print(ini," + ", ini+1," = ", op1)

print("3 intentos a un usuario ")