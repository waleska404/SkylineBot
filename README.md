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

************AQUI IMAGENTADFSAGAGR

### Lenguaje

####Creación de skylines

##### Simple
Para crear un skyline simple con un edificio basta con especificar: ```(xmin, altura, xmax)``` donde **xmin** define la posición inicial del edificio, **xmax** la posición final, y **altura** la altura.

IMAGEN DE EJEMPLO

##### Compuesto
Para crear un skyline compuesto por diversos edificios se especifica de la siguiente manera: ```[(xmin, altura, xmax),...]``` donde los parametros se refieren a las mismas características que en el apartado anterior.

PONER IMAGEN DE EJEMLO

##### Aleatorio
Para generar un skyline aleatorio indicamos: ```{n, h, w, xmin, xmax}``` donde **n** especifica el numero de edificios,** h** que los edificios tendrán una altura aleatoria entre 0 y h, **w** que los edificios tendrán una anchura aleatoria entre 1 y w, y por ultimo **xmin** y **xmax** que los edificios tendrán una posición de x aleatoria entre estos dos valores.


PONER IMAGEN DE EJEMPLO

####Asignación
En caso de querer darle un nombre a un skyline y poder operar con él solamente espeficicando su ID podemos hacer una asignación de la forma: ```a := (1,2,3)``` donde **'a'** corresponderia al ID del skyline (1,2,3).

PONER IMAGEN DE EJEMPLO

####Operaciones
Se pueden realizar las siguientes operaciones con skylines:

- Unión: ```skyline + skyline```
- Intersección: ```skyline * skyline```
- Replicación: ```skyline * N ```
- Desplazamiento a la derecha: ```skyline + N```
- Desplazamiento a la izquierda: ```skyline - N```
- Reflexión: ```-skyline```



## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

