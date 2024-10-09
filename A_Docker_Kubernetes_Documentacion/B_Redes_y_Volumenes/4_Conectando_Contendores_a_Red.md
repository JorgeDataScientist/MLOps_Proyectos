
---

# REDES CON DOCKER

### Índice
- [REDES CON DOCKER](#redes-con-docker)
    - [Índice](#índice)
  - [Introducción a las redes en Docker](#introducción-a-las-redes-en-docker)
  - [Tipos de redes en Docker](#tipos-de-redes-en-docker)
    - [Bridge](#bridge)
    - [Host](#host)
    - [None](#none)
    - [Overlay](#overlay)
    - [Macvlan](#macvlan)
  - [Comandos básicos para la gestión de redes en Docker](#comandos-básicos-para-la-gestión-de-redes-en-docker)
  - [Ejemplo práctico: Creación y uso de redes en Docker](#ejemplo-práctico-creación-y-uso-de-redes-en-docker)
  - [Inspección y administración de redes](#inspección-y-administración-de-redes)
  - [Conclusión](#conclusión)

---

## Introducción a las redes en Docker

Docker permite a los contenedores comunicarse entre sí y con el mundo exterior a través de redes. Docker proporciona varias opciones de redes, y cada contenedor se puede conectar a una o más redes según sea necesario. El sistema de redes es esencial en arquitecturas de microservicios, donde múltiples servicios pueden estar ejecutándose en contenedores y necesitan intercambiar información entre ellos.

Docker abstrae las redes de los contenedores, permitiendo a los usuarios configurarlas y gestionarlas de manera eficiente sin necesidad de preocuparse por los detalles del sistema operativo.

---

## Tipos de redes en Docker

Docker soporta varios tipos de redes para proporcionar diferentes niveles de aislamiento y control de la comunicación entre contenedores. Los principales tipos de redes en Docker son:

### Bridge
La red por defecto cuando se lanza un contenedor sin especificar ninguna red es `bridge`. Es una red virtual privada que permite que los contenedores conectados a ella se comuniquen entre sí. Es ideal para escenarios donde los contenedores deben interactuar dentro del mismo host.

- **Ventaja**: Aísla los contenedores entre sí y permite la comunicación entre ellos sin exponerlos directamente a la red externa.
- **Uso**: Para pequeños clusters de contenedores en el mismo host.

### Host
En esta red, los contenedores comparten la red del host, es decir, los contenedores no tendrán su propio namespace de red, sino que compartirán el namespace de red del host.

- **Ventaja**: Reducción de la sobrecarga de red al no necesitar NAT entre el host y el contenedor.
- **Uso**: Ideal para casos donde el contenedor debe tener un alto rendimiento de red.

### None
Esta opción elimina por completo cualquier tipo de red para un contenedor, es decir, el contenedor no estará conectado a ninguna red.

- **Ventaja**: Aislamiento completo de red.
- **Uso**: Contenedores que no necesitan ninguna conectividad de red.

### Overlay
Las redes Overlay permiten que los contenedores que se ejecutan en diferentes hosts se comuniquen entre sí. Es utilizado en entornos Docker Swarm o Kubernetes.

- **Ventaja**: Comunicación entre contenedores distribuidos en varios hosts.
- **Uso**: Escenarios de clusters o orquestación de contenedores.

### Macvlan
Este tipo de red permite asignar una dirección MAC a cada contenedor, haciendo que el contenedor aparezca en la red física como un dispositivo real.

- **Ventaja**: El contenedor se comporta como si estuviera directamente conectado a la red física.
- **Uso**: Para integrarse con redes físicas preexistentes.

---

## Comandos básicos para la gestión de redes en Docker

Docker proporciona varios comandos para crear y gestionar redes. Aquí tienes los comandos básicos que debes conocer:

1. **Listar redes disponibles**:
   ```bash
   docker network ls
   ```

2. **Crear una nueva red**:
   ```bash
   docker network create <nombre_red>
   ```

3. **Eliminar una red**:
   ```bash
   docker network rm <nombre_red>
   ```

4. **Conectar un contenedor a una red existente**:
   ```bash
   docker network connect <nombre_red> <contenedor>
   ```

5. **Desconectar un contenedor de una red**:
   ```bash
   docker network disconnect <nombre_red> <contenedor>
   ```

---

## Ejemplo práctico: Creación y uso de redes en Docker

Vamos a ver cómo crear una red, lanzar varios contenedores y conectarlos a la red para que se comuniquen entre ellos.

1. **Crear una red personalizada**
   ```bash
   docker network create mi_red_bridge
   ```
   Este comando crea una red tipo `bridge` llamada `mi_red_bridge`.

2. **Ejecutar dos contenedores y conectarlos a la red**
   ```bash
   docker run -d --name contenedor1 --network mi_red_bridge nginx
   docker run -d --name contenedor2 --network mi_red_bridge nginx
   ```
   Ambos contenedores están conectados a la red `mi_red_bridge`.

3. **Comprobar la comunicación entre los contenedores**
   Para verificar que los contenedores se comunican correctamente, puedes entrar en uno de ellos e intentar hacer ping al otro:
   ```bash
   docker exec -it contenedor1 ping contenedor2
   ```

4. **Inspeccionar la red**
   Para ver los detalles de la red `mi_red_bridge`, como qué contenedores están conectados, utiliza el siguiente comando:
   ```bash
   docker network inspect mi_red_bridge
   ```

---

## Inspección y administración de redes

Docker proporciona el comando `inspect` para revisar detalles específicos de una red. Aquí te mostramos cómo obtener información detallada de una red.

1. **Inspección detallada de una red**:
   ```bash
   docker network inspect <nombre_red>
   ```
   Este comando muestra la configuración de la red, incluyendo los contenedores conectados, las IP asignadas, el tipo de red, entre otros.

   **Salida del comando inspect**:
   ```json
   [
       {
           "Name": "mi_red_bridge",
           "Id": "7d82b61683ef",
           "Created": "2024-09-30T12:34:56.789123456Z",
           "Scope": "local",
           "Driver": "bridge",
           "EnableIPv6": false,
           "IPAM": {
               "Driver": "default",
               "Options": {},
               "Config": [
                   {
                       "Subnet": "172.18.0.0/16",
                       "Gateway": "172.18.0.1"
                   }
               ]
           },
           "Containers": {
               "f87bdcd4863b8": {
                   "Name": "contenedor1",
                   "EndpointID": "e5e4c1db3c52",
                   "MacAddress": "02:42:ac:11:00:02",
                   "IPv4Address": "172.18.0.2/16",
                   "IPv6Address": ""
               }
           }
       }
   ]
   ```

   Como se puede observar, `inspect` da detalles específicos de la red y de los contenedores conectados a ella.

---

## Conclusión

El uso de redes en Docker es esencial para crear arquitecturas de microservicios eficientes. Con la capacidad de crear diferentes tipos de redes, puedes gestionar la conectividad y el aislamiento de tus contenedores según los requerimientos de tu aplicación. Docker ofrece comandos simples para la gestión de redes, lo que permite crear entornos de desarrollo y producción flexibles.

Aprender a crear y manejar redes te ayudará a desplegar aplicaciones que requieren de múltiples contenedores comunicándose de manera eficiente y segura.

--- 

Este material es un resumen de las funcionalidades más importantes de Docker en relación con las redes. Practicar estos ejemplos te permitirá dominar el uso de redes y preparar aplicaciones más avanzadas en entornos Dockerizados.

