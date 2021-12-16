# Visualización de datos usando archivos JSON en Python

## Descripción del proyecto

¡Hola! Somos un grupo de estudiantes de Computer Science. En este proyecto usamos la librería `Matplotlib` para generar gráficos apartir de un archivo `JSON` con los datos de los `Pokemones`. 

## Nombre de los integrantes e ID de GitHub

* Kelvin Andreí Cahuana Condori - ID: `itskelvinandrei`
* Ana Maria Accilio Villanueva - ID: `anaaccilio2004`
* Margiory Alvarado Chavez - ID:  `MargioUTEC`
* Adrian Sandoval Huamani -  ID: `Sandovl0593`

## Instrucciones para ejecutar el proyecto

### Ejercicio 1

1. Este gráfico de barras muestra los tipos de pokemon en el `eje X`
y la cantidad de pokemones que tienen dicho tipo como una debilidad, en el `eje Y`.
Para eso creamos un código donde utilizamos listas y diccionarios, acompañado
de estructuras de control y por últimos las funciones de la librería
`matplotlib` para mostrar la imagen resultante, la cual es la siguiente:


> Imagen referencial
> ![01](https://user-images.githubusercontent.com/91230053/146286826-55c6a54f-2e8e-4dba-8a0b-5a93044e6ba9.png)

### Ejercicio 2

En nuestro ejercicio 2, realizamos una función para mostrar la altura y el peso de cada pokemon. 
- Paso 1: Es indispensable crear dos listas vacías, mostrarán la altura y el peso respectivamente.
- Paso 2: A continuación realizaremos una estructura de control repetitiva `for` para evaluar el diccionario.
- Paso 3: Crearemos variables iterativas para un diciconario, el cual tendremos que llamar al archivo `pokemon.json`.
- Paso 4: Validamos el nombre `["height"]` y `["weight"]`en dicho diccionario.
- Paso 5: Utilizamos el método `.replace()` y `strip` para pasar cada letra que está acompañando al peso y altura a un string vacío, esto se añadirá a las primeras listas vacías. 
- Paso 6: Generamos el gráfico `scatterplot`, para lo cual le daremos parámetros como el peso, la altura y el color ya definido anteriormente.  

> Imagen referencial
> ![02](https://user-images.githubusercontent.com/91230053/146286849-28fb3eba-5d10-4c9f-b1b3-6a3a922ebde5.png)


### Ejercicio 3

En el ejercicio 3, mostramos el mapa de Kanto con las coordenadas de cada pokémon, solo cuya "id" sea un número primo:
- Paso 1: Insertamos la imagen `Kanto.png`.
- Paso 2: Creamos dos listas: `coordenadas_x` y `coordenadas_y`. 
- Paso 3: Creamos una iteración: ```for i in range(2, tam)``` donde la iteración empieza por `2`, porque `0` y `1` no son números primos y que la variable `tam` es la cantidad de diccionarios de la lista `getAllPokemons`.
- Paso 4: En la iteración seleccionamos la clave `"id"` de cada diccionario, siempre y cuando que sea un número primo, gracias a la funcion `es_primo`.
- Paso 5: En caso de que sí lo sea, le asignamos a cada diccionario la función `getLocationsByName` que retorna las coordenadas `cordx` y `cordy` y al final los juntamos con las listas del principio.
- Paso 6: Finalmente completamos la estructura del gráfico con `plt.plot` que asigna las coordenadas respectivas, con `plt.title`, `plt.xlabel` y `plt.ylabel` que asignan los titulos y con `plt.show()` que nos mostrará el gráfico final.

> Imagen referencial
> ![03](https://user-images.githubusercontent.com/91230053/146286916-3aa9e6ea-2f3e-477c-b785-25478858eea4.png)

### Ejercico 4

En el ejercicio 4, mostraremos la cantidad de Pokemones en un rango determinado, para dicho problema nos basamos de su indice de `"avg_Spawns"`.
- Paso 1: Creamos listas vacías para determinar el rango del gráfico.
- Paso 2: Realizamos una estructura repetitiva para los rangos: `for pkmn in pokms:`, de esa forma daremos paso al `key:` `"avg_Spawns"`.
- Paso 3: Insertamos una estructura de control selectiva para determinar los rangos.
- Paso 4: Le damos los valores a los intervalos, usando el `len`
- Paso 5: Hacemos una lista de: cantitades, rangos, colores, los bordes, para el `Gráfico circular`.
- Paso 6: Determinamos la leyenda con una lista vacías, además iteramos con un bucle. Hacemos uso del método `zip` y `append` para determinar los intervalos. El título de la leyenda será `"Rangos de avg_spawns"`.
- Paso 7: Realizamos la gráfica `pie`, en el cual insertaremos los valores definidos anteriormente, mostrando la leyenda, los títulos y la gráfica en sí. 

> Imagen referencial
> ![04](https://user-images.githubusercontent.com/91230053/146286946-2dbfc5fa-cd47-4f68-acd8-729ef79f3aed.png)


### Librerías utilizadas
1. `Matplotlib`
2. Utilizamos el gráfico llamado `Pie` (en donde clasificamos el key `<avg_Spawns>` mediante rangos)
3. `pctdistance` es un parámetro de esta función `pie` que nos permite distanciar los porcentajes.
