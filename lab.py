numLis = [1,2,3,4,5];
#Conti controla el bucle while
conti = 0;
#
suma = 0;
"""
while conti < len(numLis) - 1:
    suma += numLis[conti];
    conti +=1;
print(suma," Contador: ",conti);
"""

#Otra forma de hacerlo es
"""
for n in numLis[:-1]:
    suma += n;
print(suma);
"""

#Mostrar y eliminar datos
"""
while  len(numLis) > 0 :
    print("El indice: ", conti, " almacena el valor: ", numLis[0]);
    numLis.remove(numLis[0]);
    #del numLis[0];

print(numLis);
"""
#Funcion fibonachi 
"""
def fib(valor) :

    if valor >= 2 :
        lista = [0,1];
        while len(lista) < valor :
            lista.append(lista[-1]+lista[-2]);
    else :
        print("El valor ingresado debe ser mayor a 2.");
    return print(lista);

fib(10);
"""
#Promedio Variable
"""
def promedioVarible(*args):
    total = 0;
    for n in args:
        total += n;
    return total / len(args)

print(promedioVarible(1,2,3,4,5,6));
"""
#Desafio 1
"""
primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2];
segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2];
tercera = [];

for n in primera:
    if n in segunda and n not in tercera:
        tercera.append(n);

print(tercera);
"""
"""
#Concersion 
def conversion(segundos):
    minutos = int(segundos / 60)
    horas = int(minutos / 60)
    minutos_resto = minutos - (horas*60) 
    segundos_resto = segundos - (horas*60*60) - (minutos_resto *60)
    if horas<10:
        horast = "0" + str(horas)
    else:
        horast = str(horas)
    if minutos_resto < 10:
        minutost = "0" + str(minutos_resto)
    else:
        minutost = str(minutos_resto)
    if segundos_resto < 10:
        segundost = "0" + str(segundos_resto)
    else:
        segundost = str(segundos_resto)

    return(horast + ":" + minutost + ":" + segundost)

#####################################################

print(conversion(1000))
"""
#MODULO 2
#------------------------------------------#
"""
def potenciaCubo (n):
    return n**3

def calculo (funcion, lista):
    resultado = []
    for n in lista:
        resultado.append(funcion(n));
    
    return resultado;


lista = [2, 3 ,5];


print(calculo(potenciaCubo,lista));

#------------------------------------------#
"""
"""
def solicitarNumero(mensaje):
    while True:
        try:
            
            return float(input(mensaje)) 
        except ValueError:
            print("Ingrese un numero, por favor");

a= solicitarNumero("Escriba un numero: ")
b = solicitarNumero("Escriba otro numero: ")

print("a + b: ", a + b)
print("a - b: ", a - b)
print("a * b: ", a * b)

try:
    print("a / b: ", a / b);
except ZeroDivisionError:
    print("No se puede dividir por cero.");
"""
#Codigo Paises 
"""
paises = {
    "ar" : "Argentina",
    "es" : "España",
    "us" : "Estados Unidos",
    "fr" : "Francia"
}
while True:
    codigo = input ("Ingrese un codigo \n (Para salir ponga Exit): ")
    if  codigo.capitalize() == "Exit":
        break;
try:
    print(paises[codigo])
except KeyError:
    print("El codigo no existe, vuelva a intentarlo")
"""

#Ejercicio 1 Mayuscula 
"""

res = ["juan salvo", "henry courtney", "elizabeth bennet", "aylen barria"];

def capi(lista):
    resultado = list()
    for n in lista:
        resultado.append(n.title());
    return resultado;

print(capi(res))
"""


#------------------------------------------#

#Guardar Datos 
"""
personas = {"Juan": 20, "Romina": 32, "Tamara":25, "Melanie":19}


def mostrar (diccionario):
    with open("texto.txt","a") as t:

        for f in diccionario:
            t.write(f.lower()+"-"+str(diccionario[f])+"\n");

mostrar(personas);

try:
    with open("personas.txt","w") as f:
        for n in personas:
            texto = f.write(f"{n.lower()}-{personas[n]}"+"\n")
    print("Salvado")
except FileNotFoundError:
    print("No se puede grabar")
"""








