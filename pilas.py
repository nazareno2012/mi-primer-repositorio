class Pila:
    def __init__(self):
        self.datos = []

    def push(self, dato):
        self.datos.append(dato)
        print(f"El elemento {dato} ha sido apilado")

    def pop(self):
        if not self.vacia():
            elemento = self.datos.pop()
            print(f"El elemento {elemento} ha sido desapilado")
            return elemento
        else:
            print("La pila ya se encuentra vacía")
            return

    def vacia(self):
        return len(self.datos) == 0

# Crear una instancia de la clase Pila y probarla
pila1 = Pila()
pila1.push("jesus")
