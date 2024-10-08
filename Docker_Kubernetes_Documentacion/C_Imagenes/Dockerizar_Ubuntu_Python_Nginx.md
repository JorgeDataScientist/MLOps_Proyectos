
---

# **Guía Completa para Dockerizar Ubuntu con Python y Nginx**

## **Introducción**
Esta guía te llevará paso a paso a través del proceso de "dockerizar" una imagen de **Ubuntu** que incluya **Python**, **Nginx** y permita desplegar una página web con un mensaje simple como "Hola Mundo". El propósito es enseñarte a crear un contenedor que funcione de manera eficiente y esté listo para su ejecución en cualquier entorno con Docker.

---

## **1. Crear un archivo Dockerfile**
El `Dockerfile` es un archivo de texto que contiene las instrucciones para crear una imagen Docker. En este archivo definiremos los pasos necesarios para instalar los paquetes requeridos (Python, Nginx, etc.).

### **Paso 1: Crear el Dockerfile**
1. Abre tu editor de código (Visual Studio Code u otro de tu preferencia).
2. Crea un archivo llamado `Dockerfile` en tu proyecto.
3. Agrega el siguiente contenido básico:

```Dockerfile
# Usamos la imagen base de Ubuntu
FROM ubuntu

# Definimos el entorno para evitar preguntas interactivas durante la instalación de paquetes
ENV DEBIAN_FRONTEND=noninteractive

# Actualizamos los repositorios e instalamos Python, Curl, Nginx y Nano (editor de texto)
RUN apt-get update && apt-get install -y \
    python3 \
    curl \
    nginx \
    nano

# Definimos el directorio de trabajo donde se copiarán nuestros archivos
WORKDIR /app

# Copiamos los archivos de la carpeta local al directorio /app en el contenedor
COPY . /app

# Expone el puerto 80 para que Nginx pueda ser accesible
EXPOSE 80

# Configura Nginx para que se ejecute en modo no daemon (foreground)
CMD ["nginx", "-g", "daemon off;"]
```

### **Explicación de cada directiva**:
- **`FROM ubuntu`**: Especifica la imagen base sobre la que trabajaremos. En este caso, es Ubuntu.
- **`ENV DEBIAN_FRONTEND=noninteractive`**: Configura el entorno de Debian para evitar que el instalador de paquetes haga preguntas interactivas.
- **`RUN`**: Ejecuta comandos dentro de la imagen. Aquí estamos instalando Python, Curl, Nginx y Nano.
- **`WORKDIR /app`**: Define el directorio de trabajo donde se ejecutarán los comandos y se colocarán los archivos dentro del contenedor.
- **`COPY . /app`**: Copia todos los archivos desde el directorio local al contenedor.
- **`EXPOSE 80`**: Expone el puerto 80 para que Nginx pueda recibir tráfico HTTP.
- **`CMD`**: Define el comando por defecto que se ejecutará al iniciar el contenedor. Aquí ejecutamos Nginx en primer plano (foreground).

---

## **2. Construir la imagen Docker**
Una vez que hayas creado tu `Dockerfile`, es hora de construir la imagen.

### **Paso 2: Construir la imagen con Docker**
En la terminal, navega hasta el directorio donde se encuentra tu `Dockerfile` y ejecuta el siguiente comando:

```bash
docker build -t ubuntu-with-python-nginx .
```

- **`docker build`**: Inicia el proceso de construcción de la imagen.
- **`-t ubuntu-with-python-nginx`**: Le damos un nombre a la imagen, en este caso `ubuntu-with-python-nginx`.
- **`.`**: El punto indica que el `Dockerfile` se encuentra en el directorio actual.

---

## **3. Verificar que la imagen ha sido creada**
Una vez que se haya completado el proceso de construcción, puedes verificar que la imagen se ha creado correctamente listando las imágenes disponibles en Docker:

```bash
docker image ls
```

El resultado debería mostrar la nueva imagen creada:

```
REPOSITORY                TAG       IMAGE ID       CREATED         SIZE
ubuntu-with-python-nginx   latest    <image_id>     a few seconds ago    270MB
```

---

## **4. Crear un archivo HTML para mostrar "Hola Mundo"**
Para que Nginx pueda servir una página web, necesitamos crear un archivo HTML simple.

### **Paso 3: Crear un archivo `index.html`**
En el mismo directorio de tu `Dockerfile`, crea una carpeta llamada `app` y dentro de ella, un archivo `index.html` con el siguiente contenido:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hola Mundo</title>
</head>
<body>
    <h1>Hola Mundo desde Nginx y Docker</h1>
    <p>Este contenedor está corriendo Python y Nginx en Ubuntu.</p>
</body>
</html>
```

Este archivo mostrará el mensaje "Hola Mundo desde Nginx y Docker" cuando accedas al servidor Nginx.

---

## **5. Modificar el Dockerfile para incluir el archivo HTML**

Debemos asegurarnos de que el archivo `index.html` se copie en el directorio correcto para que Nginx pueda servirlo.

### **Paso 4: Modificar Dockerfile para incluir HTML**
Modifica tu `Dockerfile` para que se vea de la siguiente manera:

```Dockerfile
# Usamos la imagen base de Ubuntu
FROM ubuntu

# Definimos el entorno para evitar preguntas interactivas durante la instalación de paquetes
ENV DEBIAN_FRONTEND=noninteractive

# Actualizamos los repositorios e instalamos Python, Curl, Nginx y Nano (editor de texto)
RUN apt-get update && apt-get install -y \
    python3 \
    curl \
    nginx \
    nano

# Copiamos el archivo HTML a la carpeta por defecto de Nginx
COPY ./app/index.html /var/www/html/index.html

# Expone el puerto 80 para que Nginx sea accesible
EXPOSE 80

# Configura Nginx para que se ejecute en modo no daemon (foreground)
CMD ["nginx", "-g", "daemon off;"]
```

### **Explicación**:
- **`COPY ./app/index.html /var/www/html/index.html`**: Copiamos nuestro archivo `index.html` a la carpeta donde Nginx espera encontrar los archivos web por defecto.

---

## **6. Reconstruir la imagen con Nginx**
Después de realizar los cambios en el `Dockerfile`, debemos volver a construir la imagen:

```bash
docker build -t ubuntu-with-python-nginx .
```

Esto reconstruirá la imagen con el archivo HTML incluido.

---

## **7. Ejecutar el contenedor**
Ahora que la imagen está lista, puedes ejecutarla y acceder a tu aplicación web.

### **Paso 5: Ejecutar el contenedor**
Ejecuta el siguiente comando para correr el contenedor y asignar el puerto 80 del contenedor al puerto 8082 de tu máquina local:

```bash
docker run -d -p 8082:80 ubuntu-with-python-nginx
```

- **`-d`**: Ejecuta el contenedor en modo "detached" (en segundo plano).
- **`-p 8082:80`**: Mapea el puerto 8082 de tu máquina al puerto 80 del contenedor (donde Nginx está escuchando).

---

## **8. Verificar la Aplicación**
Finalmente, abre tu navegador y dirígete a `http://localhost:8082`. Deberías ver el mensaje "Hola Mundo desde Nginx y Docker".

Si prefieres usar `curl`, también puedes verificarlo en la terminal con:

```bash
curl http://localhost:8082
```

---

## **Conclusión**

Has creado exitosamente un contenedor de Docker basado en Ubuntu que incluye Python y Nginx, y has desplegado una página web simple. Este flujo te ha permitido aprender:

1. Cómo escribir un archivo `Dockerfile` desde cero.
2. Cómo construir y ejecutar imágenes de Docker.
3. Cómo servir contenido con Nginx dentro de un contenedor.

¡Felicidades por completar esta práctica!

--- 

Este documento está diseñado para ofrecer un paso a paso claro, enfocado en la creación de contenedores Docker con Ubuntu, Python y Nginx, y el despliegue de una página web simple.