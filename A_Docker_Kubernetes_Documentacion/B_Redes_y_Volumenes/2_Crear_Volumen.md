### Práctica con Volúmenes en Docker

A continuación, se detalla un ejercicio práctico sobre cómo trabajar con volúmenes en Docker, desde la creación de un volumen, su inspección, y la integración con un contenedor de MySQL. Los pasos a seguir están documentados paso a paso con los comandos utilizados.

#### 1. Crear un Volumen en Docker

El primer paso es crear un volumen que será utilizado por un contenedor de MySQL para almacenar los datos de la base de datos. Para esto se usa el siguiente comando:

```bash
PS C:\Windows\system32> docker volume create curso_mlops
```

Resultado:

```bash
curso_mlops
```

Este comando crea un volumen llamado `curso_mlops` que puede ser utilizado por los contenedores.

#### 2. Listar los Volúmenes

Después de crear el volumen, puedes listar todos los volúmenes presentes en el sistema con el siguiente comando:

```bash
PS C:\Windows\system32> docker volume ls
```

Resultado:

```bash
DRIVER    VOLUME NAME
local     a3315a097756c3032e6a0421933d85357b90a57d9c36d928670a67e3ecf7fd29
local     curso_mlops
```

En este caso, se listan dos volúmenes, uno de ellos es el recién creado `curso_mlops`.

#### 3. Inspeccionar el Volumen

Para obtener más detalles sobre el volumen, como el punto de montaje y otras configuraciones, puedes usar el comando `inspect`:

```bash
PS C:\Windows\system32> docker inspect curso_mlops
```

Resultado:

```json
[
    {
        "CreatedAt": "2024-10-03T18:40:58Z",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/curso_mlops/_data",
        "Name": "curso_mlops",
        "Options": null,
        "Scope": "local"
    }
]
```

Este comando muestra información detallada sobre el volumen, como la ruta de montaje en el sistema de archivos del host (`Mountpoint`), el nombre del volumen, y el controlador (`Driver`) que lo gestiona.

#### 4. Crear un Contenedor de MySQL con el Volumen

El siguiente paso es crear un contenedor de MySQL que utilice el volumen `curso_mlops` para almacenar los datos de la base de datos en la ruta `/var/lib/mysql` dentro del contenedor. Esto se realiza con el siguiente comando:

```bash
PS C:\Windows\system32> docker run -d --name mysql-volumen -v curso_mlops:/var/lib/mysql -p 3311:3306 -e MYSQL_ROOT_PASSWORD=testrood mysql
```

Resultado:

```bash
8f2967fe74a0313c6b88f8c17b37e138449a35da20ab6b9483ba96e8466437c5
```

Este comando hace lo siguiente:
- Crea un contenedor de MySQL llamado `mysql-volumen`.
- Monta el volumen `curso_mlops` en la ruta `/var/lib/mysql` dentro del contenedor.
- Exponer el puerto 3311 del host al puerto 3306 del contenedor (puerto estándar de MySQL).
- Establece la contraseña del usuario root de MySQL como `testrood`.

#### 5. Verificar el Contenedor en Ejecución

Para verificar que el contenedor de MySQL está en ejecución, puedes listar los contenedores activos con el siguiente comando:

```bash
PS C:\Windows\system32> docker ps
```

Resultado:

```bash
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                               NAMES
8f2967fe74a0   mysql     "docker-entrypoint.s…"   50 seconds ago   Up 49 seconds   33060/tcp, 0.0.0.0:3311->3306/tcp   mysql-volumen
```

Esto indica que el contenedor `mysql-volumen` está activo y escuchando en el puerto 3311 del host.

#### 6. Detener y Eliminar el Contenedor

Para detener el contenedor en ejecución, utiliza el siguiente comando:

```bash
PS C:\Windows\system32> docker stop 8f2967fe74a0
```

Resultado:

```bash
8f2967fe74a0
```

Luego, para eliminar el contenedor detenido, puedes usar el siguiente comando:

```bash
PS C:\Windows\system32> docker rm 8f2967fe74a0
```

Resultado:

```bash
8f2967fe74a0
```

#### 7. Reiniciar el Contenedor con el Mismo Volumen

Finalmente, puedes crear de nuevo el contenedor `mysql-volumen` usando el mismo volumen `curso_mlops`, lo que asegura que los datos almacenados en el volumen no se pierdan, incluso después de eliminar el contenedor anterior:

```bash
PS C:\Windows\system32> docker run -d --name mysql-volumen -v curso_mlops:/var/lib/mysql -p 3311:3306 -e MYSQL_ROOT_PASSWORD=testrood mysql
```

Resultado:

```bash
e76ec68beb5bd11b48962a43066232d83b7c9039f300e8bbe996296c3c7f6337
```

Este comando vuelve a crear el contenedor y reutiliza el volumen para los datos de MySQL.

#### 8. Verificar el Contenedor Nuevo

Puedes verificar que el nuevo contenedor está en ejecución usando el comando `docker ps`:

```bash
PS C:\Windows\system32> docker ps
```

Resultado:

```bash
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                               NAMES
e76ec68beb5b   mysql     "docker-entrypoint.s…"   2 minutes ago    Up 2 minutes    33060/tcp, 0.0.0.0:3311->3306/tcp   mysql-volumen
```

#### Conclusión

En esta práctica, se demostró cómo:
- Crear un volumen en Docker.
- Listar y obtener información detallada sobre los volúmenes.
- Montar un volumen en un contenedor de MySQL para persistir los datos.
- Detener y eliminar un contenedor sin perder los datos almacenados en el volumen.
- Volver a utilizar el volumen con un nuevo contenedor.

Los volúmenes son una herramienta esencial en Docker para la gestión de datos persistentes, especialmente en bases de datos y aplicaciones que requieren almacenamiento duradero a lo largo de múltiples ciclos de vida de contenedores.