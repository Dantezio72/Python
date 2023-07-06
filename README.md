# Estructura de Datos

## Diccionario 
```python
lista = [2,3,5];

 dic = {}

 dic = dict()
```
## Tuplas 
```python
 tupla = ()

 tupla = tuple()
```
## Lista 
```python
lista = []

lista = list()
```
# Funciones
```python
def potenciaCubo (n):
    return n**3;

def calculo (funcion, lista):
    resultado = []
    for n in lista:
        resultado.append(funcion(n))
    return resultado
```
```python
lista = [2,3,5];

print(calculo(potenciaCubo, lista));
```
# Clases 
```python
class Empleado: 
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}"
```
## Atributo 
```python
class Alumno:
    tipo = "Alumno"
    
```
## Herencia 
```python
class ClaseB(ClaseA):
    def __init__(self):
        super().__init__(self)
```