### Contenedores sin Servicio en Docker

Un contenedor sin servicio es aquel que no ejecuta un proceso de fondo o servicio continuo, como lo hace un servidor web o una base de datos. Este tipo de contenedores suele utilizarse para entornos de desarrollo, pruebas o simplemente para ejecutar comandos aislados.

### Ejemplo con Ubuntu

Cuando descargamos una imagen de Ubuntu usando el comando:

```bash
docker pull ubuntu
```

Lo que estamos haciendo es **descargar la imagen** a nuestra máquina local, pero esto **no inicia un contenedor**. Solo estamos obteniendo la imagen para luego crear un contenedor basado en ella. 

---

### ¿Por qué no se ve el contenedor de Ubuntu?

Si ejecutamos el comando `docker ps -a`, no veremos ningún contenedor de Ubuntu a menos que hayamos **creado y ejecutado un contenedor basado en esa imagen**. El comando `docker pull ubuntu` no crea automáticamente un contenedor, solo descarga la imagen. Para ver la imagen en uso, debemos crear un contenedor.

---

### Creando y ejecutando un contenedor de Ubuntu

Para crear un contenedor basado en la imagen de Ubuntu y ejecutarlo de forma interactiva, puedes utilizar el siguiente comando:

```bash
docker run -d -i -t ubuntu
```

Este comando hace lo siguiente:

- `-d`: Ejecuta el contenedor en segundo plano (detached).
- `-i`: Modo interactivo, lo que permite que el contenedor continúe ejecutándose, esperando la interacción del usuario.
- `-t`: Asigna una pseudo terminal para permitir interacción con el contenedor.

En este caso, el contenedor estará ejecutando Ubuntu en modo interactivo con una shell de Bash activa, pero como no hay ningún servicio en ejecución de fondo (como un servidor web o base de datos), solo se ejecuta en segundo plano esperando recibir comandos.

### Comprobación del contenedor

Después de ejecutar el comando `docker run`, puedes verificar la existencia y el estado del contenedor con el comando `docker ps -a`:

```bash
docker ps -a
```

Salida esperada:

```bash
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                      PORTS                               NAMES
aa9be20210bc   ubuntu    "/bin/bash"              4 seconds ago    Up 3 seconds                                                    pensive_shirley
```

Aquí puedes ver que el contenedor de Ubuntu está en ejecución. El nombre **"pensive_shirley"** es un nombre asignado automáticamente por Docker, y el comando `/bin/bash` indica que se está ejecutando una shell interactiva de Bash dentro del contenedor.

### Resumen

- **docker pull ubuntu** descarga la imagen de Ubuntu, pero no crea ni ejecuta un contenedor.
- Para crear un contenedor de Ubuntu, debes usar `docker run -d -i -t ubuntu`.
- Luego de ejecutar `docker run`, puedes usar `docker ps -a` para verificar que el contenedor está en ejecución.

Este tipo de contenedores sin servicio puede ser útil para ejecutar tareas específicas en un entorno aislado, pero no estarán visibles en `docker ps` a menos que sean iniciados manualmente.