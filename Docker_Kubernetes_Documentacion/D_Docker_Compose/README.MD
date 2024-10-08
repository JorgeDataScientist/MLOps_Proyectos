## Guía Completa de Estudio: Docker Compose

### 1. **Introducción a Docker Compose**

**Docker Compose** es una herramienta que permite definir y ejecutar aplicaciones Docker multicontenedor. Con Compose, puedes usar un archivo YAML para definir los servicios, redes y volúmenes de una aplicación. Luego, con un solo comando, puedes crear e iniciar todos los servicios definidos en tu archivo.

### 2. **Flujo de Trabajo con Docker Compose**

El flujo de trabajo con Docker Compose sigue estos pasos básicos:

1. Definir el entorno de la aplicación en un archivo `docker-compose.yml`.
2. Ejecutar `docker-compose up` para crear e iniciar los servicios definidos en el archivo.
3. Usar `docker-compose down` para detener y eliminar los contenedores y redes definidos.

---

### 3. **Estructura del archivo `docker-compose.yml`**

El archivo YAML (`.yml`) es el corazón de Docker Compose. A continuación, te explico la estructura básica y la funcionalidad de cada sección:

```yaml
version: "3.8" # Versión de Docker Compose
services:      # Define los servicios que se ejecutarán
  nginx:       # Nombre del servicio Nginx
    image: nginx        # Imagen Docker de Nginx
    container_name: nginx_server # Nombre del contenedor
    ports:              # Mapeo de puertos
      - "80:80"
    volumes:            # Montaje de volúmenes
      - ./nginx:/usr/share/nginx/html
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
    networks:
      - app_network     # Red en la que el servicio opera

  php-fpm: # Servicio PHP-FPM para ejecutar código PHP
    image: php:fpm
    container_name: php_fpm
    volumes:
      - ./nginx:/usr/share/nginx/html
    networks:
      - app_network

  mysql:      # Servicio MySQL para base de datos
    image: mysql:5.7
    container_name: mysql_db
    ports:
      - "3312:3306"
    volumes:
      - db-data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
    networks:
      - app_network

  phpmyadmin: # Interfaz web de administración de MySQL
    image: phpmyadmin/phpmyadmin
    container_name: phpmyadmin_ui
    ports:
      - "8085:80"
    environment:
      PMA_HOST: mysql
    networks:
      - app_network

  redis: # Servicio de Redis (cache)
    image: redis
    container_name: redis_cache
    ports:
      - "6379:6379"
    networks:
      - app_network

volumes:
  db-data:    # Define volúmenes para persistencia de datos

networks:
  app_network: # Red definida para conectar los contenedores
    driver: bridge
```

---

### 4. **Comandos útiles de Docker Compose**

- **`docker-compose up -d`**: Crea y arranca los contenedores en segundo plano.
- **`docker-compose down`**: Detiene y elimina los contenedores y redes.
- **`docker-compose ps`**: Muestra el estado de los contenedores definidos en `docker-compose.yml`.
- **`docker-compose exec -it <nombre_contenedor> bash`**: Permite ejecutar comandos en un contenedor en ejecución (por ejemplo, para acceder al shell de un contenedor Ubuntu).
- **`docker-compose logs`**: Muestra los logs generados por los contenedores.

### 5. **Creación del Archivo `.env`**

Es buena práctica almacenar las variables de entorno en un archivo `.env` separado. Puedes crear un archivo `.env` con las siguientes variables:

**Archivo `.env`**

```
MYSQL_ROOT_PASSWORD=123456
```

Este archivo permitirá que el contenedor de MySQL use la variable `MYSQL_ROOT_PASSWORD` para la contraseña root, que será accesible en el contenedor.

### 6. **Uso del Comando `build`**

En Docker Compose, puedes usar el comando `build` para construir tus propias imágenes Docker a partir de un `Dockerfile`. Esto es útil cuando necesitas personalizar la configuración del contenedor o agregar dependencias específicas.

Ejemplo:

```yaml
services:
  web:
    build: ./myapp
    ports:
      - "5000:5000"
```

En este caso, Docker Compose construirá una imagen desde el directorio `./myapp`, donde debe haber un `Dockerfile`.

---

### 7. **Árbol de Archivos y Directorios**

Para ejecutar esta práctica completa, necesitas crear la siguiente estructura de archivos:

```
├── docker-compose.yml
├── .env
├── nginx/
│   ├── index.html
│   ├── formulario.php
│   └── nginx.conf
```

- **docker-compose.yml**: Archivo principal que define los servicios Docker.
- **.env**: Archivo de variables de entorno.
- **nginx/index.html**: Formulario HTML para registrar usuarios.
- **nginx/formulario.php**: Script PHP que maneja el formulario y guarda los datos en MySQL.
- **nginx/nginx.conf**: Configuración de Nginx para manejar archivos PHP.

---

### 8. **Pasos para visualizar un formulario con una base de datos MySQL**

#### Paso 1: **Crear un archivo PHP para manejar el formulario**

```php
<?php
$servername = "mysql";
$username = "root";
$password = getenv("MYSQL_ROOT_PASSWORD");
$dbname = "test_db";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $email = $_POST["email"];
    $sql = "INSERT INTO usuarios (nombre, email) VALUES ('$name', '$email')";
    if ($conn->query($sql) === TRUE) {
        echo "Registro exitoso";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

$conn->close();
?>
```

Este archivo se encarga de conectarse a MySQL y guardar los datos enviados desde el formulario.

#### Paso 2: **Crear el formulario HTML**

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario de Registro</title>
</head>
<body>
    <h1>Registro de Usuario</h1>
    <form action="formulario.php" method="POST">
        <label for="name">Nombre:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        <input type="submit" value="Registrar">
    </form>
</body>
</html>
```

#### Paso 3: **Modificar `docker-compose.yml` para incluir PHP-FPM**

```yaml
services:
  nginx:
    image: nginx
    container_name: nginx_server
    ports:
      - "80:80"
    volumes:
      - ./nginx:/usr/share/nginx/html
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
    networks:
      - app_network

  php-fpm:
    image: php:fpm
    container_name: php_fpm
    volumes:
      - ./nginx:/usr/share/nginx/html
    networks:
      - app_network
```

#### Paso 4: **Configurar Nginx para manejar archivos PHP**

```nginx
server {
    listen 80;
    root /usr/share/nginx/html;
    index index.html index.php;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~ \.php$ {
        fastcgi_pass php_fpm:9000;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }
}
```

#### Paso 5: **Crear la base de datos y la tabla**

```sql
CREATE DATABASE test_db;
USE test_db;

CREATE TABLE usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  email VARCHAR(100)
);
```

#### Paso 6: **Acceder al Formulario desde el Navegador**

Accede al formulario en tu navegador en `http://localhost`.

#### Paso 7: **Ver los Datos con PHPMyAdmin**

Accede a PHPMyAdmin en `http://localhost:8085` y verifica los datos insertados en la base de datos `test_db`.

---

### 9. **Comandos Finales**

- **`docker-compose down`**: Detener y eliminar los contenedores.
- **`docker-compose exec -it <nombre_contenedor> bash`**: Acceder a un contenedor.
- **`docker-compose build`**: Crear imágenes personalizadas si usas un `Dockerfile`.

---

Este documento está diseñado para que practiques desde la creación de un entorno multicontenedor hasta la implementación de una aplicación web básica con base de datos, utilizando Docker Compose.

<br>
<br>
<br>
---
---
Aquí tienes un árbol de directorios completo con todos los archivos que debes crear y utilizar para implementar el formulario con una base de datos MySQL, usando Docker Compose:

```
proyecto/
│
├── docker-compose.yml
├── Dockerfile
├── .env
├── nginx/
│   ├── formulario.php
│   ├── index.html
│   └── nginx.conf
└── sql/
    └── init.sql
```

### Descripción de cada archivo:

1. **docker-compose.yml**: Archivo principal que define los servicios Docker (Nginx, PHP-FPM, MySQL, PHPMyAdmin y Redis).
2. **.env**: Archivo de variables de entorno para configurar, por ejemplo, la contraseña de MySQL.
3. **nginx/**: Carpeta que contiene los archivos del servidor web y del formulario:
    - **index.html**: Archivo HTML que contiene el formulario básico para registrar usuarios.
    - **formulario.php**: Script PHP que recibe los datos del formulario y los guarda en la base de datos.
    - **nginx.conf**: Archivo de configuración de Nginx que define cómo manejar los archivos PHP y HTML.
4. **sql/init.sql**: Script SQL que crea la base de datos y las tablas necesarias para el formulario (opcional, pero útil si deseas que la base de datos se inicialice automáticamente).

### Contenido de los archivos:

#### **docker-compose.yml**
```yaml
version: "3.8"
services:
  nginx:
    image: nginx
    container_name: nginx_server
    ports:
      - "80:80"
    volumes:
      - ./nginx:/usr/share/nginx/html
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
    networks:
      - app_network

  php-fpm:
    image: php:fpm
    container_name: php_fpm
    volumes:
      - ./nginx:/usr/share/nginx/html
    networks:
      - app_network

  mysql:
    image: mysql:5.7
    container_name: mysql_db
    ports:
      - "3312:3306"
    volumes:
      - db-data:/var/lib/mysql
      - ./sql/init.sql:/docker-entrypoint-initdb.d/init.sql
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
    networks:
      - app_network

  phpmyadmin:
    image: phpmyadmin/phpmyadmin
    container_name: phpmyadmin_ui
    ports:
      - "8085:80"
    environment:
      PMA_HOST: mysql
    networks:
      - app_network

  redis:
    image: redis
    container_name: redis_cache
    ports:
      - "6379:6379"
    networks:
      - app_network

volumes:
  db-data:

networks:
  app_network:
    driver: bridge
```

#### **.env**
```env
MYSQL_ROOT_PASSWORD=123456
```

#### **nginx/index.html**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario de Registro</title>
</head>
<body>
    <h1>Registro de Usuario</h1>
    <form action="formulario.php" method="POST">
        <label for="name">Nombre:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        <input type="submit" value="Registrar">
    </form>
</body>
</html>
```

#### **nginx/formulario.php**
```php
<?php
$servername = "mysql";
$username = "root";
$password = getenv("MYSQL_ROOT_PASSWORD");
$dbname = "test_db";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $email = $_POST["email"];
    $sql = "INSERT INTO usuarios (nombre, email) VALUES ('$name', '$email')";
    if ($conn->query($sql) === TRUE) {
        echo "Registro exitoso";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

$conn->close();
?>
```

#### **nginx/nginx.conf**
```nginx
server {
    listen 80;
    root /usr/share/nginx/html;
    index index.html index.php;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~ \.php$ {
        fastcgi_pass php_fpm:9000;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }
}
```

#### **sql/init.sql** (opcional, para inicializar la base de datos)
```sql
CREATE DATABASE test_db;
USE test_db;

CREATE TABLE usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  email VARCHAR(100)
);
```

### **Instrucciones**

1. **Crear los archivos**: Asegúrate de crear todos los archivos mencionados en la estructura y colocarlos en los directorios adecuados.
2. **Ejecutar los contenedores**: Ejecuta el comando `docker-compose up -d` en el directorio donde se encuentra el archivo `docker-compose.yml`.
3. **Acceder al formulario**: En tu navegador, abre `http://localhost` para acceder al formulario de registro de usuario.
4. **Verificar los datos en PHPMyAdmin**: Accede a `http://localhost:8085` para ingresar a PHPMyAdmin y revisar los datos que se han guardado en la base de datos `test_db`.

Con este árbol de directorios y los archivos correctos, podrás visualizar el formulario, interactuar con la base de datos MySQL y manejar datos desde PHP.

<br>
<br>
<br>
---
---
Para ejecutar los contenedores con Docker Compose, sigue estos pasos y comandos:

### 1. **Construir y levantar los contenedores**

Si es la primera vez que vas a levantar los contenedores, o si hiciste cambios en los archivos, utiliza el siguiente comando para construir y ejecutar todos los servicios definidos en el archivo `docker-compose.yml`:

```bash
docker-compose up -d --build
```

- `up`: Levanta todos los servicios definidos en el archivo `docker-compose.yml`.
- `-d`: Ejecuta los contenedores en segundo plano (detached mode).
- `--build`: Fuerza la reconstrucción de las imágenes de los contenedores antes de iniciarlos (esto es útil si hiciste cambios en los archivos).

### 2. **Verificar los contenedores en ejecución**

Después de levantar los servicios, puedes verificar que todos los contenedores estén en ejecución utilizando el siguiente comando:

```bash
docker-compose ps
```

Este comando mostrará una lista de los contenedores y su estado.

### 3. **Ver los registros de los contenedores**

Si deseas ver los registros de los contenedores en ejecución para depurar o verificar el estado de los servicios, puedes usar:

```bash
docker-compose logs
```

O puedes especificar un servicio en particular para ver los registros de ese contenedor:

```bash
docker-compose logs nginx
```

### 4. **Acceder a un contenedor en ejecución (por ejemplo, PHP o MySQL)**

Para acceder a un contenedor en ejecución con una terminal interactiva (bash), usa el siguiente comando:

```bash
docker-compose exec [nombre_del_servicio] bash
```

Por ejemplo, si deseas acceder al contenedor `nginx`:

```bash
docker-compose exec nginx bash
```

Si deseas acceder al contenedor de MySQL:

```bash
docker-compose exec mysql bash
```

### 5. **Detener y eliminar los contenedores**

Para detener y eliminar todos los contenedores, redes y volúmenes creados por Docker Compose, utiliza el siguiente comando:

```bash
docker-compose down
```

Si también deseas eliminar los volúmenes asociados (que contienen los datos persistentes como las bases de datos), agrega la opción `-v`:

```bash
docker-compose down -v
```

### 6. **Eliminar todos los contenedores existentes**

Si necesitas eliminar todos los contenedores que se estén ejecutando o que estén detenidos, puedes usar el siguiente comando de Docker:

```bash
docker rm -f $(docker ps -aq)
```

### 7. **Volver a levantar los contenedores usando el volumen**

Si ya creaste los volúmenes (que almacenan los datos de manera persistente), puedes volver a levantar los contenedores con el comando habitual:

```bash
docker-compose up -d
```

El volumen guardará los datos de la base de datos, por lo que los contenedores volverán a funcionar con los datos existentes.

### Resumen de Comandos:

1. **Construir y levantar los contenedores**:
   ```bash
   docker-compose up -d --build
   ```

2. **Verificar los contenedores en ejecución**:
   ```bash
   docker-compose ps
   ```

3. **Ver registros de los contenedores**:
   ```bash
   docker-compose logs
   ```

4. **Acceder a un contenedor en ejecución**:
   ```bash
   docker-compose exec nginx bash
   ```

5. **Detener y eliminar los contenedores**:
   ```bash
   docker-compose down -v
   ```

6. **Eliminar todos los contenedores existentes**:
   ```bash
   docker rm -f $(docker ps -aq)
   ```

### ¡Con estos comandos podrás manejar todo el ciclo de vida de tus contenedores en Docker Compose!