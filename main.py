import json
import os

class Automovil:
    def __init__(self, marca, modelo, combustible, potencia, traccion, cambio):
        self.configuracion = {"Marca": marca, "Modelo": modelo, "Combustible": combustible, "Potencia": potencia, "Traccion": traccion, "Cambio": cambio}

    def toString(self):
        resultado = ""
        for i in self.configuracion.keys():
            resultado += i
            resultado += ": "
            resultado += self.configuracion[i]
            resultado += ", "

        return resultado[:-2]


class Base_de_datos:
    def __init__(self, archivo):
        self.base_de_datos = []
        self.archivo = archivo.strip()

        if len(self.archivo) == 0:
            self.archivo = "default.json"

        if self.archivo[-5:] != ".json":
            self.archivo += ".json"

        if os.path.exists(self.archivo):
            print("Cargando archivo existente")
            self.cargar()
        else:
            print("Creando nuevo archivo")
            self.guardar()

    def nuevo_automovil(self, marca, modelo, combustible, potencia, traccion, cambio):
        auto = Automovil(marca, modelo, combustible, potencia, traccion, cambio)
        self.base_de_datos.append(auto)
        self.guardar()

    def buscar(self, marca, modelo):
        resultado = list(filter(lambda auto: auto.configuracion["Marca"]==marca and auto.configuracion["Modelo"]==modelo, self.base_de_datos))
        return resultado

    def to_json(self):
        items = []
        for i in self.base_de_datos:
            items.append(i.configuracion)

        return json.dumps(items, indent=4)

    def imprimir_datos(self):
        lista_ordenada = self.base_de_datos
        lista_ordenada.sort(key=lambda auto: auto.configuracion["Marca"])
        for auto in lista_ordenada:
            print(auto.toString())

    def guardar(self):
        json = self.to_json()
        with open(self.archivo, "w+") as f:
            f.write(json)

    def cargar(self):
        with open(self.archivo, "r") as f:
            data = json.loads(f.read())

        for i in data:
            auto = Automovil(i["Marca"], i["Modelo"], i["Combustible"], i["Potencia"], i["Traccion"], i["Cambio"])
            self.base_de_datos.append(auto)


if __name__ == "__main__":

    archivo = input("Nombre del archivo para la base de datos: ")

    datos = Base_de_datos(archivo)

    while True:
        print("""\nOpciones:
        1) Añadir nuevo automovil
        2) Buscar configuracion de automovil
        3) Imprimir todas las configuraciones
        4) Salir""")

        opcion = input("-> ")
        print("")

        if opcion == "4":
            break
        elif opcion == "1":
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            combustible = input("Combustible: ")
            potencia = input("Potencia: ")
            traccion = input("Traccion: ")
            cambio = input("Cambio: ")

            datos.nuevo_automovil(marca, modelo, combustible, potencia, traccion, cambio)
        elif opcion == "2":
            marca = input("Marca: ")
            modelo = input("Modelo: ")

            resultado = datos.buscar(marca, modelo)

            if len(resultado) == 0:
                print("No se ha encontrado ningun automovil con Marca: {} y Modelo: {}".format(marca, modelo))
            else:
                print("Datos encontrados:")
                for i in resultado:
                    print(i.toString())

        elif opcion == "3":
            datos.imprimir_datos()
        else:
            print("\nOpcion no valida. Seleccione un numero entre el 1 y el 4.\n")
