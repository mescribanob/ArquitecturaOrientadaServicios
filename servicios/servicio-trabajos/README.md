# AosMicroservicio
Este repositorio contiene los archivos necesarios para ejecutar y probar una API REST dedicada a los trabajos que se realizan en un taller, encontrada en el archivo openapi.yaml. 

Para poner en funcionamiento esta api se debe ejecutar el archivo 'docker-compose.yml', que contiene las imagenes usadas. Estas son:

1. Swagger_ui -> Como su nombre indica, ofrece una interfaz para visualizar la API en un entorno más "user friendly".
2. Prism -> Esta imagen crea un 'mock' de la API que permite ofrecer respuestas cuando se realizan llamadas siguiendo los paths especificados en la API.
