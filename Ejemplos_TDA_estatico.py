
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

# Lista estática (tamaño fijo de 3 automóviles)
autos_estaticos = [None] * 3

# Crear objetos Automovil
autos_estaticos[0] = Automovil("Toyota", "Corolla", 2020)
autos_estaticos[1] = Automovil("Honda", "Civic", 2019)
autos_estaticos[2] = Automovil("Ford", "Focus", 2018)

# Mostrar información
for auto in autos_estaticos:
    print(f"Marca: {auto.get_marca()}, Modelo: {auto.get_modelo()}, Año: {auto.get_año()}")

