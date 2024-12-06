"""
Requisitos
Clase base: Vehiculo

Atributos de clase:
cantidad_total: para llevar un registro de cuántos vehículos se han creado.
Atributos de instancia:
marca, modelo, año.
Métodos:
describir(): muestra información básica del vehículo.
Método de clase: mostrar_cantidad_total(), que imprime cuántos vehículos hay registrados.
Clases hijas: Auto y Moto

Clase Auto:
Atributos adicionales: cantidad_puertas.
Sobrescribir el método describir() para incluir la cantidad de puertas.
Clase Moto:
Atributos adicionales: cilindrada (en cc).
Sobrescribir el método describir() para incluir la cilindrada.
Funcionamiento:

Crear varios vehículos de cada tipo y llamarlos métodos.
Mostrar la cantidad total de vehículos registrados al final.
"""

class Vehiculo: #clase vehiculo
    #atributo de clase
    cantidad_total = 0
    
            
    def __init__(self, marca, modelo, ano) -> None:#metodo constructor
        self.marca = marca #defino los atributos
        self.modelo = modelo
        self.ano = ano
        
        
    @staticmethod
    def ingresar_vehiculo():
        #se solicita al usuario que ingrese datos
        marca = input("ingrese la marca del vehiculo: ")
        modelo = input("ingrese el modelo del vehiculo: ")
        ano = input("ingrese el año del modelo: ")
        return Vehiculo(marca, modelo, ano) #devuelve los argumentos ingresados por el usuario
        
        # metodo de instancia describir
    def describir(self):
        print(f"""
            Datos del  vehiculo: \n\n
            Marca: {self.marca}
            Modelo: {self.modelo}
            Año: {self.ano}
            """)
        
    @classmethod
    def mostrar_cantidad_total(cls):
        #metodo muestra la cantidad total de vehiculos usando un atributo de clase
        print(f"La cantidad total de vehiculos ingresados: {cls.cantidad_total}\n")
        
class Automovil(Vehiculo):# clase hija hereda de vehiculo
    def __init__(self, marca, modelo, ano, cantidad_puertas):
        super().__init__(marca, modelo, ano)# Llama al constructor de la clase padre, para inicializar los atributos heredados (marca, modelo, ano).
        self.cantidad_puertas = cantidad_puertas #atributo propio de la clase hija
    
    @staticmethod
    def ingresar_vehiculo():
        
        # Llama directamente al método estático de la clase padre Vehiculo.
        # Esto devuelve una instancia de Vehiculo con los atributos básicos (marca, modelo, ano).
        vehiculo = Vehiculo.ingresar_vehiculo()
        # Solicita el atributo adicional específico de la clase Automovil.
        cantidad_puertas = input("Ingrese la cantidad de puertas: ")
        # Devuelve una nueva instancia de Automovil con los datos de Vehiculo y el nuevo atributo.
        return Automovil(vehiculo.marca, vehiculo.modelo, vehiculo.ano, cantidad_puertas)
        
    def describir(self):
        # Llamar al método describir() de la clase padre para conservar su funcionalidad
        super().describir()#Llama al método describir de la clase padre. Así, el método en la clase hija hereda y conserva la funcionalidad del método de la clase padre.
        print(f"Cantidad de puertas: {self.cantidad_puertas}") #se agrega una funcionalidad de la clase hija
    
class Moto(Vehiculo):# clase hija  hereda de vehiculo
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)
        self.cilindrada = cilindrada
    
    @staticmethod
    def ingresar_vehiculo():
        vehiculo = Vehiculo.ingresar_vehiculo()
        cilindrada = input("Ingrese la cilindrada: ")
        return Moto(vehiculo.marca, vehiculo.modelo, vehiculo.ano, cilindrada)
    
    def describir(self):
        super().describir()
        print(f"La cilindrada es: {self.cilindrada}")
        
def iniciar_aplicación():  
    while True:
        tipo_vehiculo = input("""Ingrese el Tipo de vehiculo:\n
                            (1)vehiculo
                            (2)Automovil
                            (3)moto\n
                            Ingrese opcion:
                            """)
        if tipo_vehiculo not in ["1", "2", "3"]:
            print("Opción inválida. por favor elija una opción válida!")
            continue
        
        if tipo_vehiculo == "1":
            # Llama al método ingresar_vehiculo de la clase Vehiculo
            vehiculo = Vehiculo.ingresar_vehiculo()# crea la intancia de Vehiculo con los agumentos retornados
            vehiculo.describir()
            
        elif tipo_vehiculo == "2":
            automovil = Automovil.ingresar_vehiculo()
            automovil.describir()
            
        elif tipo_vehiculo == "3":
            moto = Moto.ingresar_vehiculo()
            moto.describir()
        else:
            print("vehiculo no contemplado!")
            continue
        

        Vehiculo.cantidad_total +=1 # incrementa el contador vehiculos ingresados
        Vehiculo.mostrar_cantidad_total()# llama al metodo de clase mostrar_cantidad_total
        continuar = input("Desea continuar? (s/n): ").lower()
        if continuar != "s":
            print("Cerando la aplicación")
            break
    
iniciar_aplicación()        

        
    
        
    
    
    

        
