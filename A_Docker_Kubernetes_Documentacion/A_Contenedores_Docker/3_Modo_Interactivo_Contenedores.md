```markdown
# Modo Interactivo en Docker

Docker permite interactuar con contenedores de manera directa utilizando comandos que facilitan la administración y exploración de los mismos. El modo interactivo es útil para ejecutar comandos dentro de un contenedor en ejecución, verificar su estado, inspeccionar su sistema de archivos y manipular archivos y procesos internos.

A continuación, se explica cómo utilizar el modo interactivo en Docker a través de PowerShell.

## Comando `docker exec`

El comando `docker exec` se utiliza para ejecutar comandos dentro de un contenedor que está en ejecución. Permite interactuar directamente con el sistema de archivos y los procesos que están corriendo en ese contenedor. Es útil para realizar tareas de administración y depuración.

### Ejemplo de uso

En este ejemplo, primero se inicia el contenedor llamado `mi_nginx` y luego se ejecuta el comando `ls` dentro del contenedor para listar el contenido de su sistema de archivos.

```bash
docker start mi_nginx
```

El comando anterior reinicia el contenedor detenido `mi_nginx`.

Luego, puedes verificar que el contenedor está en ejecución con el siguiente comando:

```bash
docker ps
```

El resultado será similar a este:

```bash
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
a508f1d513e1   nginx     "/docker-entrypoint.…"   54 minutes ago   Up 2 seconds   0.0.0.0:8080->80/tcp   mi_nginx
```

Esto muestra que el contenedor `mi_nginx` está en ejecución y se expone en el puerto `8080`.

Ahora, para ejecutar un comando dentro del contenedor, se usa `docker exec` junto con el ID del contenedor o su nombre. En este caso, ejecutamos el comando `ls` para listar el contenido del sistema de archivos dentro del contenedor:

```bash
docker exec a508f1d513e1 ls
```

El resultado será algo como esto:

```bash
bin
boot
dev
docker-entrypoint.d
docker-entrypoint.sh
etc
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
```

Este listado muestra las carpetas dentro del sistema de archivos del contenedor, permitiéndote explorar qué directorios y archivos están presentes.

### Comandos útiles en modo interactivo

Puedes usar `docker exec` para ejecutar diversos comandos dentro de un contenedor, por ejemplo:

- **Ver contenido de archivos:** Puedes inspeccionar archivos de configuración o logs.
  
  ```bash
  docker exec a508f1d513e1 cat /etc/nginx/nginx.conf
  ```

- **Navegar por el sistema de archivos:** Puedes acceder a diferentes directorios dentro del contenedor y verificar su contenido.

  ```bash
  docker exec a508f1d513e1 bash -c "cd /var && ls"
  ```

- **Ejecutar comandos de administración:** Puedes ejecutar cualquier comando compatible con el sistema operativo dentro del contenedor, como reiniciar servicios o procesos.

### Modo Interactivo Completo

Si necesitas acceso completo a la terminal dentro del contenedor, puedes utilizar el modo interactivo con el flag `-it` para abrir una sesión de shell dentro del contenedor. Esto te da una interfaz interactiva en la que puedes ejecutar múltiples comandos:

```bash
docker exec -it a508f1d513e1 /bin/bash
```

Este comando te da acceso a una shell interactiva en el contenedor `mi_nginx`, permitiéndote trabajar dentro del contenedor como si fuera un sistema Linux.

### Conclusión

El comando `docker exec` es una herramienta poderosa para ejecutar comandos dentro de contenedores en ejecución. Te permite inspeccionar y administrar los procesos y archivos internos de un contenedor, lo que es muy útil para depuración y administración. El modo interactivo proporciona acceso completo a una terminal dentro del contenedor, ofreciendo la flexibilidad necesaria para realizar tareas avanzadas.