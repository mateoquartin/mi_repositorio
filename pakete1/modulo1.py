import datetime
class cliente:
    def __init__(self, edad, nombre, correo, intereses):
        self.edad = edad
        self.nombre = nombre
        self.correo = correo
        self.intereses = intereses
        self.compras = []

    
    def comprar(self, producto, lugar):
        if not isinstance(producto, str) or not isinstance(lugar, str):#comprobamos que sea un string y no otro type
            print("El producto y el lugar deben ser cadenas de texto.")
        else:
            hora_compra = datetime.datetime.now()# Capturar la hora actual
            compra = {"producto": producto, "lugar": lugar, "hora": hora_compra}
            self.compras.append(compra)
            print(f'El cliente {self.nombre} ha comprado {producto} en {lugar} a las {hora_compra}')

    
    def historial_compras(self):
        if not self.compras:
            print(f'El hisotrial de compras de {self.nombre} esta vacio')
        else:
            print(f'historial de compras de {self.nombre}: ')
            for compra in self.compras:
                print(f'Producto: {compra["producto"]}, Lugar: {compra["lugar"]}')
    
    def actualizar_información_cuenta(self, nuevo_nombre, nueva_edad, nuevo_correo, nuevos_intereses):
        if nuevo_nombre:
            self.nombre = nuevo_nombre
        if nueva_edad:
            self.edad = nueva_edad
        if nuevo_correo:
            self.correo = nuevo_correo
        if nuevos_intereses:
            self.intereses = nuevos_intereses
    
    def __str__(self):
        return f'Cliente: {self.nombre}\nEdad: {self.edad}\nCorreo: {self.correo}\nIntereses: {", ".join(self.intereses)}'


cliente1 = cliente(32, 'mateo','mateoquartin@gmail.com',['ropa','tecnologia'])        
