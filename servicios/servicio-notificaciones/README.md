# **Practica-AOS** Subsistema de Notificaciones
## Grupo 13: Javier Ye Zhang y Pablo Torija Martínez
<br>

Para poder desplegar el proyecto:

 1. Tener Docker y Docker Compose instalados
 2. Iniciar Docker
 3. Abrir la terminal e ir al directorio que contiene el docker-compose.yaml:

    `\Practica-AOS`
 4. Ejecutar:
    
        $ docker-compose build

        $ docker-compose up
 5. Abrir: `http://localhost:8000/` en un navegador
    
<br><br>

Servicios que hemos desarrollado para la creación de nuestro subsistema de notificaciones: 

 - Envío de notificaciones por correo 

 - Envío de notificaciones por teléfono 
 - Envío de notificaciones masivas 
 - Obtención de una notificación 
 - Obtención de las notificaciones de un trabajo 
 - Obtención de las notificaciones de un cliente 
 - Actualización de la suscripción a notificaciones de un cliente 

<br><br>

Aclaraciones sobre la creación de nuestro subsistema de Notificaciones:
 - Hemos considerado que para actualizar la información de una notificación, se crea una nueva en vez de modificar la existente
 
 - Con notificaciones masivas nos referimos a notificaciones que se envían a todos los clientes que tengan algún trabajo pendiente, ya que pueden afectar a los trabajos en desarrollo (p.ej: Cierre de la empresa por vacaciones)

 - Hemos decidido separar el envío de notificaciones en dos servicios, uno para envío por correo y otro por teleéfono. De forma que se pueda elegir el medio por el cuál enviar las notificaciones, o usar los dos medios mediante el uso de los dos servicios
