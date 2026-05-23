#MATRIZ DE TITULOS
videoteca = [["Intensamente, 2015, 4", " Animacion"], ["Encanto, 2021, 3", "Musical"], ["Harry Potter, 2001, 4", "Aventura"],
             ["Buscando a Dory, 2016, 4", " Animacion"], ["Lilo & Stitch, 2002, 4", " Animacion"], ["Finding Nemo, 2003, 4", " Animacion"], ["Shrek, 2001, 4", " Animacion"],
             ["Frozen, 2013, 4", "Musical"], ["Moana, 2016, 4", "Musical"], ["Coco, 2017, 4", "Musical"], ["Zootopia, 2016, 4", "Comedia"]]
# FUNCION PARA CONTAR LOS TITULOS
def Contar_Titulos(matriz, clasificacacion_minima, año_minimo):

    Contador = 0

for titulo in videoteca:

    año = titulo[1]
    calificacion = titulo[2]

    if calificacion >= clasificacacion_minima and año >= año_minimo:
        contador+= 1

        "return contador"
        
    # VALORES DE LA BUSQUEDA
clasificacion_minima = 4
año_minimo = 2010

# LLAMADA A LA FUNCION
resultado = Contar_Titulos(videoteca, clasificacion_minima, año_minimo)

#MOSTRAR RESULTADO
print("El numero de titulos que cumplen con los criterios es:", resultado)
