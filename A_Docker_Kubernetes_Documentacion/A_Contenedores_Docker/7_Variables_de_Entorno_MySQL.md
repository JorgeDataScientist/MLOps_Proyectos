
```markdown
# Uso de Variables de Entorno en Docker

## Descripción

Las variables de entorno en Docker permiten configurar parámetros importantes dentro de un contenedor durante su ejecución. Estas variables pueden definir contraseñas, nombres de bases de datos, configuraciones específicas del entorno de la aplicación, entre otras. Docker permite definir estas variables usando el flag `-e` cuando ejecutamos un contenedor.

En este documento, usaremos un ejemplo práctico configurando un contenedor de MySQL utilizando variables de entorno para definir:

- La contraseña del usuario root (`MYSQL_ROOT_PASSWORD`).
- El nombre de la base de datos a crear (`MYSQL_DATABASE`).

---

## Comando para Ejecutar el Contenedor con Variables de Entorno

Para iniciar un contenedor de MySQL y configurarlo con variables de entorno, ejecutamos el siguiente comando:

```bash
docker container run -d -p 3309:3306 -e MYSQL_ROOT_PASSWORD=12345 -e MYSQL_DATABASE=test_01 mysql
```

### Explicación del Comando

- **`docker container run`**: Ejecuta un nuevo contenedor.
- **`-d`**: Ejecuta el contenedor en segundo plano (modo desacoplado).
- **`-p 3309:3306`**: Asocia el puerto 3306 del contenedor (puerto por defecto de MySQL) al puerto 3309 del host, permitiendo acceder a la base de datos desde el host en el puerto 3309.
- **`-e MYSQL_ROOT_PASSWORD=12345`**: Establece la variable de entorno `MYSQL_ROOT_PASSWORD` con el valor `12345`, que es la contraseña del usuario root de MySQL.
- **`-e MYSQL_DATABASE=test_01`**: Define la variable de entorno `MYSQL_DATABASE` con el valor `test_01`, lo que crea una base de datos llamada `test_01` al inicializar el contenedor.
- **`mysql`**: La imagen base que se va a usar para el contenedor.

---

## Comprobación de los Contenedores Activos

Para verificar que el contenedor MySQL está ejecutándose correctamente, utilizamos el comando:

```bash
docker ps
```

Este comando mostrará una lista de los contenedores en ejecución junto con información relevante, como el ID del contenedor, el nombre de la imagen, el puerto asignado, y el estado. El resultado debería ser algo similar a esto:

```bash
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                     NAMES
5c61f6c3d2d4   mysql     "docker-entrypoint.s…"   5 seconds ago   Up 3 seconds   0.0.0.0:3309->3306/tcp    ecstatic_morse
```

### Explicación de la Salida

- **CONTAINER ID**: El identificador único del contenedor.
- **IMAGE**: La imagen base del contenedor (en este caso, `mysql`).
- **COMMAND**: El comando que está ejecutando el contenedor.
- **PORTS**: Aquí podemos ver que el puerto 3309 en el host está asignado al puerto 3306 dentro del contenedor.
- **NAMES**: El nombre del contenedor generado automáticamente (`ecstatic_morse` en este ejemplo).

---

## Detalles de las Variables de Entorno Usadas

### `MYSQL_ROOT_PASSWORD`

Esta variable es **obligatoria** al ejecutar un contenedor de MySQL. Define la contraseña del usuario root, que es el administrador principal de la base de datos MySQL. Si no se proporciona esta variable, el contenedor MySQL no se iniciará y devolverá un error.

### `MYSQL_DATABASE`

Esta variable es opcional y se utiliza para crear automáticamente una base de datos con el nombre especificado cuando se inicia el contenedor por primera vez. En nuestro caso, hemos configurado la base de datos `test_01`.

---

## Verificación de la Configuración

Una vez que el contenedor está en ejecución, podemos conectarnos a él para verificar que las variables de entorno configuradas funcionaron correctamente. Esto se puede hacer ejecutando un comando dentro del contenedor para conectarse a MySQL, como por ejemplo:

```bash
docker exec -it [container_id] mysql -u root -p
```

Te pedirá la contraseña, que en este caso es `12345`. Luego, puedes verificar que la base de datos `test_01` se ha creado:

```sql
SHOW DATABASES;
```

---

## Conclusión

El uso de variables de entorno en Docker es una herramienta esencial para configurar contenedores de manera rápida y flexible. En este ejemplo con MySQL, vimos cómo definir la contraseña de root y crear una base de datos inicial, permitiéndonos lanzar un contenedor configurado automáticamente sin necesidad de intervención manual.
