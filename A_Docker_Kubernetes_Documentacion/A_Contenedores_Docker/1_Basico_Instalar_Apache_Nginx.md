```markdown
# Guía de Instalación de Apache y Nginx usando Docker en PowerShell

Este documento describe los pasos para instalar y ejecutar servidores Apache y Nginx en contenedores Docker, utilizando **PowerShell** en un sistema operativo **Windows**.

## Prerrequisitos

- Tener **Docker Desktop** instalado y funcionando en Windows.
- Asegúrate de tener Docker ejecutándose. Puedes verificar esto ejecutando el siguiente comando en PowerShell:

```powershell
docker version
```

Si Docker está instalado correctamente, verás tanto la versión del cliente como del servidor.

---

## 1. Instalación y Ejecución de Apache

### Paso 1: Descargar la imagen de Apache

Para descargar la imagen oficial de Apache (`httpd`), ejecuta el siguiente comando en PowerShell:

```powershell
docker pull httpd
```

- **`docker pull httpd`**: Este comando descarga la imagen oficial de Apache HTTP Server desde Docker Hub.

### Paso 2: Crear y ejecutar un contenedor de Apache

Después de descargar la imagen, puedes crear y ejecutar un contenedor con el siguiente comando:

```powershell
docker run -d -p 8080:80 --name mi_apache httpd
```

- **`docker run`**: Inicia un nuevo contenedor.
- **`-d`**: Ejecuta el contenedor en modo "detached" (en segundo plano).
- **`-p 8080:80`**: Mapea el puerto `80` del contenedor al puerto `8080` de tu máquina local, permitiendo el acceso desde el navegador a través de `http://localhost:8080`.
- **`--name mi_apache`**: Asigna el nombre `mi_apache` al contenedor.
- **`httpd`**: Especifica la imagen de Apache que estamos utilizando.

### Paso 3: Verificar que Apache está corriendo

Para verificar que el contenedor se está ejecutando correctamente, utiliza el siguiente comando:

```powershell
docker ps
```

Esto mostrará una lista de contenedores activos, incluyendo el contenedor `mi_apache`. **Nota**: El comando `docker ps` solo lista los contenedores en ejecución. Si deseas ver todos los contenedores, incluidos los que no están corriendo, utiliza:

```powershell
docker ps -a
```

### Paso 4: Acceder al servidor Apache

Abre tu navegador y dirígete a la siguiente URL:

```
http://localhost:8080
```

Deberías ver la página de bienvenida de Apache.

---

## 2. Instalación y Ejecución de Nginx

### Paso 1: Descargar la imagen de Nginx

Para descargar la imagen oficial de Nginx desde Docker Hub:

```powershell
docker pull nginx
```

- **`docker pull nginx`**: Descarga la imagen oficial de Nginx.

### Paso 2: Crear y ejecutar un contenedor de Nginx

Ejecuta el siguiente comando para crear y ejecutar un contenedor de Nginx:

```powershell
docker run -d -p 8081:80 --name mi_nginx nginx
```

- **`docker run`**: Crea y ejecuta un nuevo contenedor.
- **`-d`**: Ejecuta el contenedor en segundo plano.
- **`-p 8081:80`**: Mapea el puerto `80` del contenedor al puerto `8081` de tu máquina local, permitiendo el acceso desde `http://localhost:8081`.
- **`--name mi_nginx`**: Asigna el nombre `mi_nginx` al contenedor.
- **`nginx`**: Especifica la imagen de Nginx.

### Paso 3: Verificar que Nginx está corriendo

Para comprobar que Nginx está corriendo:

```powershell
docker ps
```

Recuerda que este comando solo muestra los contenedores en ejecución. Si el contenedor está detenido, no aparecerá aquí. Para ver todos los contenedores (activos y detenidos), utiliza:

```powershell
docker ps -a
```

### Paso 4: Acceder al servidor Nginx

Accede a Nginx desde tu navegador utilizando:

```
http://localhost:8081
```

### Paso 5: Volver a ejecutar un contenedor detenido

Si el contenedor `mi_nginx` ha sido detenido y deseas volver a ejecutarlo, usa:

```powershell
docker start mi_nginx
```

Este comando inicia el contenedor detenido sin necesidad de crear uno nuevo.

---

## 3. Manejo de Contenedores

### Detener un contenedor

Si deseas detener un contenedor en ejecución, puedes usar:

```powershell
docker stop <nombre_del_contenedor>
```

Ejemplo para detener Apache:

```powershell
docker stop mi_apache
```

### Eliminar un contenedor

Para eliminar un contenedor, primero debes asegurarte de que está detenido. Luego, puedes eliminarlo con:

```powershell
docker rm <nombre_del_contenedor>
```

Ejemplo para eliminar Nginx:

```powershell
docker rm mi_nginx
```

Si intentas eliminar un contenedor que está en ejecución, obtendrás un error. En ese caso, primero debes detenerlo:

```powershell
docker stop mi_nginx
docker rm mi_nginx
```

### Listar imágenes descargadas

Para ver todas las imágenes descargadas localmente:

```powershell
docker image ls
```

### Listar contenedores activos

Para listar todos los contenedores que están corriendo actualmente:

```powershell
docker ps
```

### Listar todos los contenedores (activos y detenidos)

Para ver todos los contenedores, incluidos los que no están en ejecución:

```powershell
docker ps -a
```
