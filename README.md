# AOS_Taller_Equipo_3

Infraestructura y despliegue de la aplicación del **gestor de talleres de mecánica rápida** para la asignatura de Arquitecturas Orientadas a Servicios.

Esta aplicación combina los servicios de la primera práctica:
1. Clientes (`servicios/servicio-clientes`)
2. Vehículos (`servicios/servicio-vehiculos`)
3. Trabajos (`servicios/servicio-trabajos`)
4. Notificaciones (`servicios/servicio-notificaciones`)
5. Facturas (`servicios/servicio-facturas`)
6. Recambios (`servicios/implementacion-recambios`)
7. Logs (`servicios/servicio-logs`)

# Características
- Despliegue con Docker Compose
- Despliegue con Kubernetes
- Implementación de la API de Recambios escrita en Python, utilizando:
  - FastAPI
  - MongoDB
- Imagen Docker de la implementación de la API de Recambios subida a [DockerHub](https://hub.docker.com/r/alejandrochirinos/recambios)
- Memoria del proyecto

# Requisitos para el despliegue
- Docker
- Kubernetes

# Instrucciones para el despliegue
Antes de nada, se debe clonar el repositorio e ir a la raíz del repositorio local.

## Docker Compose
1. Ir a `despliegue-compose/`
2. Ejecutar el comando `docker compose up`

## Kubernetes
1. Ir a `k8s/`
2. Ejecutar el comando `kubectl apply -f .`

# URLs

## Docker Compose

### Interfaz gráfica para las distintas especificaciones
- http://127.0.0.1/clientes
- http://127.0.0.1/vehículos
- http://127.0.0.1/trabajos
- http://127.0.0.1/notificaciones
- http://127.0.0.1/facturas
- http://127.0.0.1/recambios
- http://127.0.0.1/logs

### Ejemplos de petición
```
curl --request GET \
  --url http://127.0.0.1/api/v1/cliente
```
```
curl --request GET \
  --url http://127.0.0.1/api/v1/notificaciones/masivas
```
```
curl --request POST \
  --url http://127.0.0.1/api/v1/recambios \
  --header 'Content-Type: application/json' \
  --data '{
		"numero_serie": "Z0000009-Z",
		"nombre": "nombre",
		"descripcion": "descripción",
		"proveedor": "proveedor",
		"equivalencias": {
			"nombre": "nombre",
			"fabricante": "fabricante",
			"modelo": "modelo"
		},
		"garantia": "garantía",
		"precio": "100.0",
		"iva": "21%",
		"importe": "121.0",
		"cantidad": "5",
		"links": {
			"parent": {
				"href": "http://127.0.0.1:4000/api/v1/recambios",
				"rel": "recambio_post recambio_cget"
			},
			"self": {
				"href": "http://127.0.0.1:4000/api/v1/recambios/Z0000009-Z",
				"rel": "recambio_get recambio_delete recambio_put"
			}
		}
	}'
```
```
curl --request OPTIONS \
  --url http://127.0.0.1/api/v1/recambios \
  --header 'Access-Control-Request-Method: GET' \
  --header 'Origin: 127.0.0.1:4000'
```
