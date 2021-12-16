import matplotlib.pyplot as plt
import random as rd
from aux_functions import *

""" VARIABLES GLOBALES """

# Lista de diccionarios
pokms = getAllPokemons()

# El tamaño de la lista anterior
tam = len(pokms)


""" EJERCICIOS """

def ejercicio1():
    """
    Esta función crea un gráfico de barras en el cual se muestra los tipos de pokemon en el eje X, y la cantidad de pokemones que tienen dicho tipo como una debilidad en el eje Y.
    """
    # El ejeX muestra los tipos de pokemon
    ejeX = ['Grass', 'Poison', 'Fire', 'Flying', 'Water', 'Bug', 'Normal', 'Electric', 'Ground', 'Fighting', 'Psychic', 'Rock', 'Ice', 'Ghost', 'Dragon']

    # Lista de debilidades por separado extraido del json.
    weaknesses = [] 
    for pkm in pokms: 
        for wks in pkm["weaknesses"]:
            weaknesses.append(wks) # Se agrega las debilidades por separado 

    # Diccionario con la clasificación de las conteo de pokemones por tipo como debilidad
    cantidades = {} 
    for tipo in ejeX:
        i = 0
        for wks in weaknesses:
            if tipo == wks:
                i += 1  
        cantidades[tipo] = i  

    # El ejeY muestra las cantidades de pokemon por tipo
    ejeY = []  
    for cant in cantidades.values():
        ejeY.append(cant) # Se agrega cada valor del diccionario

    colors = ['green', 'blueviolet', 'orange', 'lightblue',
                'cyan', 'slategray',
                'red', 'royalblue', 'sandybrown', 'brown', 'lightgreen', 'gray',
                'aqua', 'thistle', 'coral']
    

    # Generamos la gráfica
    plt.bar(ejeX, ejeY, color=colors)

    plt.xlabel("Tipos de pokemon (debilidades)", size=14, color='darkcyan')
    plt.ylabel("Cantidad de Pokemones", size=14, color='darkcyan')
    plt.title("CANTIDAD DE POKEMONES QUE TIENEN CIERTO TIPO DE DEBILIDAD", size=15, color='mediumblue')

    # Mostramos la gráfica
    plt.show()



def ejercicio2():
    """
    Esta función sin parámetros realiza una gráfica de dispersión
    que muestra la altura de los pokemones en centimetros en el eje X, y el peso de los pokemones en kg en el eje Y.

    """
    # Esta lista almacena las alturas de los pokemones 
    alturas = []

    # Esta lista almacena las pesos de los pokemones
    pesos = []

    # Iteramos en el rango de la lista de diccionarios 
    for i in range(tam):

        height = pokms[i]["height"]
        height = height.replace("m","")
        height = height.strip()
        cm_height = float(height) * 100

        weight = pokms[i]["weight"]
        weight = weight.replace("g","")
        weight = weight.replace("k","")
        weight = float(weight.strip())

        alturas.append(cm_height)
        pesos.append(weight)

    # Generamos la gráfica
    plt.style.use("seaborn")
    plt.scatter(alturas, pesos, c = pesos, cmap = "Spectral", edgecolor = "k")
    plt.colorbar()
    plt.xlabel("Alturas (cm)", size=14, color='darkcyan')
    plt.ylabel("Pesos (kg)", size=14, color='darkcyan')
    plt.title("ALTURAS Y PESOS DE LOS POKEMONES", size=14, color='mediumblue')

    # Mostramos la gráfica
    plt.show()



def ejercicio3():
    """
    Esta función sin parámetros gráfica en el mapa de 'Kanto' las
    coordenadas de aquellos pokemones cuyo 'id' es primo.
    """

    # Leemos la imagen
    img = plt.imread("Kanto.png")
    plt.imshow(img)
    
    # Listas de las coordenadas
    coordenadas_x = []
    coordenadas_y = []

    # Iteramos en el rango de la lista de diccionarios 
    for i in range(2, tam):
        id = pokms[i]["id"]
        if es_primo(id) == True:
            nombre = pokms[i]["name"]
            cordx, cordy = getLocationsByName(nombre)
            
            # Concatenamos listas o añadimos elementos dependiendo el caso
            coordenadas_x += cordx
            coordenadas_y += cordy

    col = ['red', 'blue', 'yellow', 'orange', "cyan"]

    # Generamos la gráfica
    plt.plot(coordenadas_x, coordenadas_y, 'o', color=rd.choice(col))
    plt.xlabel("Eje x", size=14, color='red')
    plt.ylabel("Eje y", size=14, color='red')
    plt.title("UBICACIONES DE LOS POKEMONES", size=14, color='green')
    
    # Mostramos la gráfica
    plt.show()



def ejercicio4(): 
    '''
    Utilizaremos un gráfico pie, en donde clasificaremos a los pokemones mediante el rango de sus indice de "avg_Spawns".
    '''
    # Rangos
    m_0_25 = []
    m_25_50 = []
    m_50_100 = []
    m_100_200 = []
    m_200_mas = []

    # Iteramos y separamos en listas por rango
    for pkmn in pokms:
        avg = pkmn["avg_spawns"]

        # De 0 a 50:
        if 0 <= avg <= 25:
            m_0_25.append(avg)

        # De 50 a 100:
        elif 25 < avg <= 50:
            m_25_50.append(avg)

        # De 100 a 150:
        elif 50 < avg <= 100:
            m_50_100.append(avg)

        # De 150 a 200:
        elif 100 < avg <= 200:
            m_100_200.append(avg)
        
        # De 200 a más:
        else:
            m_200_mas.append(avg)

    # Cantidad de pokemones que pertenecen a cierto rango de avg_spawns

    c1 = len(m_0_25)
    c2 = len(m_25_50)
    c3 = len(m_50_100)
    c4 = len(m_100_200)
    c5 = len(m_200_mas)

    # Sectores circulares
    cantidades = [c1,c2,c3,c4,c5]
    rangos = ["De 0 a 25","De 25 a 50","De 50 a 100","De 100 a 200","De 200 a más"]

    colores = ["royalblue","lightgreen","orange","orangered","aqua"]
    externo = [0.04, 0.04, 0.04, 0.04, 0.04]
    
    # Leyenda
    leyenda = []
    for r, c in zip(rangos, cantidades):
        leyenda.append(r + ' (' + str(c) + ' pokemones)')
    titulo = "Rangos de avg_spawns"

    # Generamos la gráfica
    plt.pie(cantidades, labels= rangos, explode= externo, autopct= "%0.1f %%", pctdistance= 0.7, colors= colores, shadow= True)
    plt.title("CANTIDAD DE POKEMONES PERTENECIENTES A CIERTO RANGO DE 'AVG_SPAWNS'", size=13, color='green')
    plt.legend(leyenda, title= titulo ,bbox_to_anchor=(0, 1))

    # Mostramos la gráfica
    plt.show()


#####################
###### Pruebas ######
#####################
# Puede elegir aca la función que quiere probar

#ejercicio1()
#ejercicio2()
#ejercicio3()
#ejercicio4()
