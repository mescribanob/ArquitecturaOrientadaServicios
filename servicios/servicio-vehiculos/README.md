Objetivo:
----------
El principal objetivo de esta tarea consiste en consolidar los conceptos relacionados con el diseño y la especificación de un servicio. Para ello se definirá y publicará la definición de un servicio empleando el estándar OpenAPI 3. Adicionalmente se simulará el comportamiento del servicio (se propone el empleo de Swagger-UI, Stoplight Prism, Postman, ...)

Enunciado:
----------
Sistema de Gestión de talleres de mecánica rápida
Una conocida empresa que posee talleres de mecánica rápida por toda la geografía nacional nos ha encargado la realización de un sistema de gestión para una parte de su negocio. A efectos de funcionalidad, cada uno de los talleres se gestiona de forma independiente, por lo que cada uno de ellos tendrá su propio despliegue de la aplicación. 
El subsistema a desarrollar es:

* Subsistema_2: Gestión de los vehículos
    - Son propiedad de los clientes
    - Se reparan y/o revisan en el taller.
    - Cada vehículo estará identificado de forma única por su VIN.
 
Notas:
------
1. El diseño de nuestro microservicio se ha realizado con un nivel de madurez (RMM) de nivel 3: HATEOAS.

2. Se permite el lanzamiento de contenedores mediante el comando: docker-compose up. Se crearán dos contenedores. Uno el del swagger que nos permitirá ver la especificación de nuestra API y el del mock que nos permitirá ver si los accesos a los distintos endpoints se realizan correctamente. 

3. La especificación de nuestra API se adhiere a los principios REST

