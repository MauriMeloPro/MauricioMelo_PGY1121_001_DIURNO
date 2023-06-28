import os
os.system ("cls")


print ("BIENVENIDO A CARACOL EXPRESS")

encomiendas = []

def grabar_encomienda():
    
    nombre= input("ingrese el nombre del destinatario:")
    direccion = input("Ingrese la direccion de entrega")
    descripcion = input("ingrese una descripción de la entrega")
    peso = float(input("ingrese el peso de la encomienda (en kg):"))
    valor = float(input("ingrese el valor de la encomienda:"))


    if peso < 0.1 or valor < 2000:
       print("la encomienda no cumple con los requisitos establecidos")
       return

    encomienda = {
    
      'nombre': nombre,
     'direccion' : direccion,
     'descripcion' : descripcion,
      'RUT' : RUT,
      'peso': peso,
      'valor' : valor

      }
    
print ("Encomienda Grabada")

def buscar_encomienda():

    nombre = input ("Ingrese el nombre del destinatario a buscar:")
    for encomienda in encomiendas:
        if encomienda['nombre'] == nombre:
         print("Encomienda encontrada") 
        print (f"nombre: {encomienda ['nombre']}")
        print (f"direccion: {encomienda ['direccion']}")
        print (f"descripcion: {encomienda ['descripcion']}")
        print (f"RUT: {encomienda ['RUT']}")
        print (f"peso: {encomienda['peso']}")
        print (f"valor: {encomienda['valor']}")
        
        return
    print ("encomienda no encontrada")
        
def listar_encomienda():
    if not encomiendas:
       print("No se encuentran encomiendas ingresadas")
       return
    print ("Lista de encomiendas:")
    for encomiendas in encomiendas:
       print(f"nombre: {encomiendas ['nombre']}")
       print(f"direccion: {encomiendas ['direccion']}")
       print(f"descripcion: {encomiendas ['descripcion']}")

       print("***")


def menu():
   while True:
      print("Menu encomiendas")

      print("1. Grabar encomiendas")
      print("2. Buscar encomiendas")
      print("3. Listar encomiendas")
      print("4. SALIR DEL MENU")


opcion = input("Seleccione una opcion:")

if opcion == '1':
   grabar_encomienda()
elif opcion == '2':
   buscar_encomienda()
elif opcion == '3':
   listar_encomienda()
elif opcion == '4':
    
    print ("¡Gracias por preferir a Caracol Express!")

    break

else : 
   print("opcion invalida,compruebe los datos e intente nuevamente")

   menu()

