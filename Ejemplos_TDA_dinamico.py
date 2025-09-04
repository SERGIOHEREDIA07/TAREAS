
class Automovil:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año

    # Getters
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_año(self):
        return self.__año

    # Setters
    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_año(self, año):
        self.__año = año

# Lista dinámica
autos_dinamicos = []

# Función para agregar automóviles
def agregar_automovil(marca, modelo, año):
    auto = Automovil(marca, modelo, año)
    autos_dinamicos.append(auto)

# Agregar autos dinámicamente
agregar_automovil("Tesla", "Model S", 2021)
agregar_automovil("BMW", "Serie 3", 2020)
agregar_automovil("Audi", "A4", 2019)

# Mostrar información
for auto in autos_dinamicos:
    print(f"Marca: {auto.get_marca()}, Modelo: {auto.get_modelo()}, Año: {auto.get_año()}")

