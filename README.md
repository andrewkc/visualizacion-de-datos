# Visualización de datos usando archivos JSON en Python

## Descripción del proyecto

¡Hola! Somos un grupo de estudiantes de Computer Science. En este proyecto usamos la librería `Matplotlib` para generar gráficos apartir de un archivo `JSON` con los datos de los `Pokemones`. 

## Nombre de los integrantes e ID de GitHub

* Kelvin Andreí Cahuana Condori - ID: `itskelvinandrei`
* Ana Maria Accilio Villanueva - ID: `anaaccilio2004`
* Margiory Alvarado Chavez - ID:  `MargioUTEC`
* Adrian Sandoval Huamani -  ID: `SandovalHuamaniUTEC`

## Instrucciones para ejecutar el proyecto

### Ejercicio 1

1. Este gráfico de barras muestra los tipos de pokemon en el eje X,
y la cantidad de pokemones que tienen dicho tipo como una debilidad, en el eje Y.
Para eso creamos un código donde utilizamos listas y diccionarios, acompañado
de estructuras de control y por últimos las funciones de la librería
`matplotlib` para mostrar la imagen resultante la cual es la siguiente:


> Imagen referencial
> ![01](https://user-images.githubusercontent.com/91230053/146286826-55c6a54f-2e8e-4dba-8a0b-5a93044e6ba9.png)

### Ejercicio 2

En nuestro ejercicio 2, realizamos una función para mostrar la altura y el peso de cada pokemon. 
- Primer Paso: Para eso es indispensable crear dos listas vacías, mostrarán la altura y el peso respectivamente.
- Segundo Paso: A continuación realizaremos una estructura de control repetitiva (for) para evaluar el diccionario.
- Tercer Paso: Crearemos variables iterativas para un diciconario, el cual tendremos que llamar a un archivo `Json`.
- Cuarto Paso: Validamos el nombre `["height"]` y `["weight"]`en dicho diccionario.
- Quinto Paso: Se utilizará el método `.replace()` y `strip` para pasar cada letra que está acompañando al peso y altura a un string vacío, esto se añadirá a las primeras listas vacías. 
- Sexto Paso: Generar el gráfico `scatterplot`, para lo cual le daremos parámetros como el peso, la altura y el color ya definido anteriormente.  

> Imagen referencial
> ![02](https://user-images.githubusercontent.com/91230053/146286849-28fb3eba-5d10-4c9f-b1b3-6a3a922ebde5.png)


### Ejercicio 3

1. Esta función, sin parámetros, grafíca en el mapa de `Kanto`, la cuál ya nos habían compartido anteriormente,
las coordenadas de aquellos pokemones cuyo `ID` es un número primo. Realizamos distintas estructuras y definimos
una función para saber cuáles son los números primos.

> Imagen referencial
> ![03](https://user-images.githubusercontent.com/91230053/146286916-3aa9e6ea-2f3e-477c-b785-25478858eea4.png)

### Ejercico 4

1.

> Imagen referencial
> ![04](https://user-images.githubusercontent.com/91230053/146286946-2dbfc5fa-cd47-4f68-acd8-729ef79f3aed.png)


