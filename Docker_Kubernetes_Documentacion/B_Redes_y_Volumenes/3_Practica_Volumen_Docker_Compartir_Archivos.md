
---

## Documentación detallada: Uso de Volúmenes en Docker

### 1. Crear un volumen llamado `almacen`
```bash
docker volume create almacen
```
Este comando crea un volumen de Docker llamado `almacen`. Los volúmenes son útiles para almacenar datos persistentes que no se eliminan cuando el contenedor se detiene o se borra. En este caso, el volumen será utilizado para compartir datos entre contenedores.

### 2. Listar los volúmenes disponibles
```bash
docker volume ls
```
Este comando muestra una lista de los volúmenes disponibles en Docker. En este punto, solo debería aparecer el volumen `almacen`, que acabas de crear.

### 3. Ver las imágenes de Docker
```bash
docker images
```
Este comando lista las imágenes descargadas localmente en tu sistema. Inicialmente, no tienes imágenes en tu sistema, por lo que el comando no muestra ninguna salida.

### 4. Descargar la imagen de Ubuntu
```bash
docker pull ubuntu
```
Este comando descarga la imagen más reciente de Ubuntu desde el repositorio de Docker Hub. Docker buscará la imagen llamada `ubuntu` y descargará la versión más reciente disponible (en este caso, `latest`).

### 5. Ver las imágenes nuevamente
```bash
docker images
```
Ahora que has descargado la imagen de Ubuntu, este comando te mostrará la lista actualizada de imágenes. Verás la imagen `ubuntu:latest` junto con su ID y tamaño.

### 6. Ejecutar un contenedor Ubuntu con el volumen `almacen`
```bash
docker run --rm -it -v almacen:/home ubuntu
```
Este comando inicia un contenedor usando la imagen `ubuntu` y monta el volumen `almacen` en el directorio `/home` del contenedor. Las opciones del comando son las siguientes:
- `--rm`: Elimina el contenedor automáticamente después de que se detiene.
- `-it`: Permite la interacción con el contenedor a través de la terminal.
- `-v almacen:/home`: Monta el volumen `almacen` en la ruta `/home` dentro del contenedor. Esto permite que cualquier archivo creado o modificado en `/home` se almacene de forma persistente en el volumen.

#### Crear el archivo `index.html`
Dentro del contenedor, se crea un archivo HTML en el volumen compartido:
```bash
touch index.html
```
Este comando crea un archivo vacío llamado `index.html` dentro del directorio `/home` del contenedor. Dado que `/home` está vinculado al volumen `almacen`, este archivo persiste en el volumen incluso después de que el contenedor se detenga.

### 7. Descargar la imagen de Fedora
```bash
docker pull fedora
```
Este comando descarga la imagen más reciente de Fedora desde Docker Hub. Fedora es una distribución de Linux diferente a Ubuntu, y la usaremos para mostrar cómo se puede compartir el volumen `almacen` entre diferentes contenedores.

### 8. Ejecutar un contenedor Fedora con el volumen `almacen`
```bash
docker run --rm -it -v almacen:/home fedora
```
Este comando inicia un contenedor usando la imagen `fedora`, con el volumen `almacen` montado en el directorio `/home`, igual que en el contenedor Ubuntu. Al listar el contenido del directorio `/home`, puedes ver que el archivo `index.html` sigue presente porque está almacenado en el volumen `almacen` compartido entre los contenedores.

### 9. Editar el archivo `index.html`

Ahora que ya has creado el archivo `index.html` en el volumen `almacen`, el siguiente paso es agregar contenido estructurado en formato HTML para mostrar en el navegador.

#### Editar el archivo `index.html`
```bash
docker run --rm -it -v almacen:/home ubuntu
```
Este comando inicia un contenedor basado en la imagen `ubuntu` con el volumen `almacen` montado en el directorio `/home`. De esta forma, puedes editar el archivo `index.html` dentro del volumen.

```bash
cd /home
echo "<!DOCTYPE html>
<html lang='es'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Docker y Volúmenes</title>
</head>
<body>
    <h1>Hola Mundo</h1>
    <h2>¿Qué es un volumen en Docker?</h2>
    <p>Un <strong>volumen</strong> en Docker es una forma de almacenar datos persistentes que pueden compartirse entre varios contenedores.</p>
    <p>Los volúmenes son la mejor opción para almacenar datos que deben persistir incluso cuando un contenedor es eliminado.</p>
    <p>El volumen se almacena en el sistema de archivos del host fuera del ciclo de vida de los contenedores, lo que asegura que los datos no se pierdan cuando el contenedor se detiene o se borra.</p>
    <h3>Ventajas de usar volúmenes en Docker:</h3>
    <ul>
        <li>Permiten la persistencia de datos.</li>
        <li>Pueden ser compartidos entre varios contenedores.</li>
        <li>Facilitan el respaldo y la migración de datos.</li>
    </ul>
    <footer>
        <p>Ejemplo de uso de volúmenes en Docker con Nginx.</p>
    </footer>
</body>
</html>" > index.html
```
Este comando sobrescribe el archivo `index.html` con un HTML estructurado que incluye:
- Un encabezado principal (`<h1>`) con "Hola Mundo".
- Una sección de explicación sobre los volúmenes en Docker con subtítulos (`<h2>` y `<h3>`).
- Un párrafo explicativo y una lista de las ventajas de usar volúmenes.

#### Verificar el contenido del archivo `index.html`
```bash
cat index.html
```
Este comando muestra el contenido del archivo `index.html`, que ahora tiene un documento HTML más estructurado.

### 10. Visualizar el contenido HTML en el navegador con Nginx

Ahora que has editado el archivo `index.html`, el siguiente paso es usar un contenedor de Nginx para servir ese archivo a través de un navegador web.

#### Descargar y ejecutar Nginx con el volumen `almacen`
```bash
docker run --rm -d -v almacen:/usr/share/nginx/html -p 8080:80 nginx
```
Este comando ejecuta un contenedor basado en la imagen `nginx` con las siguientes opciones:
- `-d`: Inicia el contenedor en segundo plano (modo "detached").
- `-v almacen:/usr/share/nginx/html`: Monta el volumen `almacen` en el directorio `/usr/share/nginx/html`, que es donde Nginx busca los archivos estáticos para servir.
- `-p 8080:80`: Mapea el puerto 80 del contenedor (Nginx) al puerto 8080 en la máquina host, permitiéndote acceder al contenido a través del puerto 8080 en tu navegador.

#### Visualizar el contenido en el navegador
Abre tu navegador y navega a `http://localhost:8080/index.html`.

Ahora deberías ver un sitio web sencillo que muestra "Hola Mundo" en un encabezado `<h1>`, seguido de una explicación sobre los volúmenes en Docker y una lista con las ventajas de su uso.

### 11. Resumen de la última parte:

1. **Editar el archivo `index.html`:** Creaste un archivo HTML estructurado con un "Hola Mundo" en `<h1>` y una explicación sobre los volúmenes en Docker.
2. **Servir el archivo con Nginx:** Usaste un contenedor basado en la imagen `nginx` para servir el archivo `index.html` en el navegador.
3. **Ver el archivo en el navegador:** Navegando a `http://localhost:8080/index.html`, puedes visualizar el contenido del archivo HTML estructurado.

---

Este documento explica detalladamente los comandos que ejecutaste y cómo usar volúmenes en Docker para compartir y persistir datos entre diferentes contenedores. Además, muestra cómo usar Nginx para servir un archivo HTML estructurado almacenado en un volumen Docker.

