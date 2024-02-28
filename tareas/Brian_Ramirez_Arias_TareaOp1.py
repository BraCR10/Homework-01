print('¡Contador de digitos pares en una cifra entera!')
print('-------------------------------------------------')
#num=int(input('Digite un numero entero en la consola: '))
num=128882


def verificadorPares(num):
    cont=0
    if num==0:
        print('Has digitado 0, se considera un numero par.')
    else:
        while num!=0:
            ultimoDigito=num%10#Obtiene el ultimo digito del numero 
            if ultimoDigito%2==0:
                cont+=1
            num//=10#Quita el ultimo digito del numero hasta dejarlo en 0
        print(f'La cantidad de digitos pares en el numero es: {cont}')

verificadorPares(num)

'''Otra opcion

#Ver el ultimo digito de un numero
def ultimoDigito(num):
    temp=num%10
    return temp

#Quitar el ultimo digito de un numero
def quitarUltimoDigito(num):
    temp=num//10
    return temp

print('¡Contador de digitos pares en una cifra entera!')
print('-------------------------------------------------')
num=int(input('Digite un numero entero en la consola: '))
cont=0
if num==0:
    print('Has digitado 0, se considera un numero par.')
else:
    while num!=0:
        check = ultimoDigito(num)
        if check%2==0:
            cont+=1
        num= quitarUltimoDigito(num)
    print(f'La cantidad de digitos pares en el numero es: {cont}')'''