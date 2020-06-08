# SkylineBot

[![](https://media.istockphoto.com/vectors/long-city-skyline-silhouette-in-a-flat-style-for-the-footer-modern-vector-id1218805861?k=6&m=1218805861&s=170667a&w=0&h=M8QNfXr724X3ToeEGNHL7tFaVxo12ratZSfJHwJi7Mc=)](https://media.istockphoto.com/vectors/long-city-skyline-silhouette-in-a-flat-style-for-the-footer-modern-vector-id1218805861?k=6&m=1218805861&s=170667a&w=0&h=M8QNfXr724X3ToeEGNHL7tFaVxo12ratZSfJHwJi7Mc=)

Proyecto para la asignatura Lenguajes de Programación de la FIB (edición primavera 2020).

Bot de Telegram con el que puedes interactuar para generar y operar con skylines.

Desarrollado con Python y ANTLR.

## Antes de empezar

A continuación se especifican las instrucciones para poder ejecutar el bot e interactuar con él.

### Prerequisitos

Las librerias necesarias estan especificadas en el archivo *requeriments.txt*,  para instalarlas ejecutar:

```
$ pip3 install -r requeriments.txt
```

### Instalación

Una vez instaladas las librerias necesarias hace falta token.

 1. Instalar Telegram en caso de no tenerlo.
 1. Visitar a @BotFather.
 1. Utilizar el comando ** /newbot **  y proporcionar la información requerida para obtener un token.  (Para información mas detallada ver https://core.telegram.org/bots#6-botfather. )

Copia el token y pegalo en archivo **token.txt** en la misma carpeta que **bot.py**.

Ahora ya es posible ejecutar el bot:

```
$ python3  bot.py
```
Ahora con el link que @BotFather ha proporcionado podemos ir al chat del bot e interactuar con él.


## Interacciones con el bot



### Comandos

- **/start**: Inicia la conversación conmigo.
- **/help: **Obten una lista de todos los comandos que me puedes enviar.
- **/author:** Información sobre el autor de este bot.
- **/lst:** Muestra los identificadores definidos y su correspondiente area.
- **/clean:** Borra todos los identificadores definidos.
- **/save id:** Guarda un skyline definido con id: id.
- **/load id:** Carga un skyline que hayas guardado previamente con id: id.

[![](https://raw.githubusercontent.com/waleska404/SkylineBot/master/fotosReadme/Captura%20de%20pantalla%20de%202020-06-08%2020-20-26.png?token=AGIVB626XROCZIXFJBBXIAS647CCU)](https://raw.githubusercontent.com/waleska404/SkylineBot/master/fotosReadme/Captura%20de%20pantalla%20de%202020-06-08%2020-20-26.png?token=AGIVB626XROCZIXFJBBXIAS647CCU)

### Lenguaje

####Creación de skylines

##### Simple
Para crear un skyline simple con un edificio basta con especificar: ```(xmin, altura, xmax)``` donde **xmin** define la posición inicial del edificio, **xmax** la posición final, y **altura** la altura.

[![](https://raw.githubusercontent.com/waleska404/SkylineBot/master/fotosReadme/Captura%20de%20pantalla%20de%202020-06-08%2020-45-34.png?token=AGIVB65XRJZ3XFLLOI2SS6S647CF2)](https://raw.githubusercontent.com/waleska404/SkylineBot/master/fotosReadme/Captura%20de%20pantalla%20de%202020-06-08%2020-45-34.png?token=AGIVB65XRJZ3XFLLOI2SS6S647CF2)

##### Compuesto
Para crear un skyline compuesto por diversos edificios se especifica de la siguiente manera: ```[(xmin, altura, xmax),...]``` donde los parametros se refieren a las mismas características que en el apartado anterior.

[![](https://raw.githubusercontent.com/waleska404/SkylineBot/master/fotosReadme/Captura%20de%20pantalla%20de%202020-06-08%2020-46-33.png?token=AGIVB622EJ4HDIDD7ZDI7S2647CHY)](https://raw.githubusercontent.com/waleska404/SkylineBot/master/fotosReadme/Captura%20de%20pantalla%20de%202020-06-08%2020-46-33.png?token=AGIVB622EJ4HDIDD7ZDI7S2647CHY)

##### Aleatorio
Para generar un skyline aleatorio indicamos: ```{n, h, w, xmin, xmax}``` donde **n** especifica el numero de edificios,** h** que los edificios tendrán una altura aleatoria entre 0 y h, **w** que los edificios tendrán una anchura aleatoria entre 1 y w, y por ultimo **xmin** y **xmax** que los edificios tendrán una posición de x aleatoria entre estos dos valores.


[![](https://raw.githubusercontent.com/waleska404/SkylineBot/master/fotosReadme/Captura%20de%20pantalla%20de%202020-06-08%2020-47-03.png?token=AGIVB647FYCF7FBW74ZSX6C647CMC)](https://raw.githubusercontent.com/waleska404/SkylineBot/master/fotosReadme/Captura%20de%20pantalla%20de%202020-06-08%2020-47-03.png?token=AGIVB647FYCF7FBW74ZSX6C647CMC)

####Asignación
En caso de querer darle un nombre a un skyline y poder operar con él solamente espeficicando su ID podemos hacer una asignación de la forma: ```a := (1,2,3)``` donde **'a'** corresponderia al ID del skyline (1,2,3).

[![](https://raw.githubusercontent.com/waleska404/SkylineBot/master/fotosReadme/Captura%20de%20pantalla%20de%202020-06-08%2020-47-25.png?token=AGIVB6YS7HN6QAYPTAXCEG2647CSI)](https://raw.githubusercontent.com/waleska404/SkylineBot/master/fotosReadme/Captura%20de%20pantalla%20de%202020-06-08%2020-47-25.png?token=AGIVB6YS7HN6QAYPTAXCEG2647CSI)

####Operaciones
Se pueden realizar las siguientes operaciones con skylines:

- Unión: ```skyline + skyline```
- Intersección: ```skyline * skyline```
- Replicación: ```skyline * N ```
- Desplazamiento a la derecha: ```skyline + N```
- Desplazamiento a la izquierda: ```skyline - N```
- Reflexión: ```-skyline```

[![](https://raw.githubusercontent.com/waleska404/SkylineBot/master/fotosReadme/Captura%20de%20pantalla%20de%202020-06-08%2020-48-06.png?token=AGIVB63HOE6FHKUBLPTKRH2647CUE)](https://raw.githubusercontent.com/waleska404/SkylineBot/master/fotosReadme/Captura%20de%20pantalla%20de%202020-06-08%2020-48-06.png?token=AGIVB63HOE6FHKUBLPTKRH2647CUE)



## Autora

Paula Boyano Ivars

