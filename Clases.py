class Persona: 
    def __init__(self, nom,ape):
        self.nom = nom
        self.ape = ape
    def nombreCompleto(self):
        return f"Hola, soy {self.nom} {self.ape}\n";

class Estudiante(Persona): 
    def __init__(self, nom, ape, carrera): 
        super().__init__(nom, ape)
        self.carrera = carrera

    def mostrarCarrera(self):
        return f"La carrera que estudio es: {self.carrera}"

estudiante = Estudiante("Franco", "Gomez", "Analista Programador Universitario")

print(estudiante.nombreCompleto(),estudiante.mostrarCarrera());

