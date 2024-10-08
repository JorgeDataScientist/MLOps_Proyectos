```markdown
# Explicación de los Comandos de Docker

Este documento describe el uso de varios comandos de Docker. Estos comandos permiten interactuar y gestionar contenedores en diferentes estados, desde la creación y ejecución hasta el monitoreo y eliminación.

## Comandos para Gestión de Contenedores

### `attach`
Permite conectar las entradas y salidas estándar locales (input, output y error) a un contenedor que está en ejecución.

```bash
docker attach <nombre_del_contenedor>
```

### `commit`
Crea una nueva imagen a partir de los cambios realizados en un contenedor.

```bash
docker commit <nombre_del_contenedor> <nombre_de_la_nueva_imagen>
```

### `cp`
Copia archivos o carpetas entre un contenedor y el sistema de archivos local.

```bash
docker cp <nombre_del_contenedor>:<ruta_dentro_del_contenedor> <ruta_local>
```

### `create`
Crea un nuevo contenedor sin iniciarlo.

```bash
docker create --name <nombre_del_contenedor> <imagen>
```

### `diff`
Inspecciona los cambios realizados en archivos o directorios dentro del sistema de archivos de un contenedor.

```bash
docker diff <nombre_del_contenedor>
```

### `exec`
Ejecuta un comando dentro de un contenedor en ejecución.

```bash
docker exec -it <nombre_del_contenedor> <comando>
```

### `export`
Exporta el sistema de archivos de un contenedor como un archivo tar.

```bash
docker export <nombre_del_contenedor> > <archivo.tar>
```

### `inspect`
Muestra información detallada sobre uno o más contenedores.

```bash
docker inspect <nombre_del_contenedor>
```

### `kill`
Mata uno o más contenedores en ejecución.

```bash
docker kill <nombre_del_contenedor>
```

### `logs`
Obtiene los logs de un contenedor.

```bash
docker logs <nombre_del_contenedor>
```

### `ls`
Lista los contenedores en ejecución. Para listar todos los contenedores, incluyendo los detenidos, usa `ls -a`.

```bash
docker ps
```

```bash
docker ps -a
```

### `pause`
Pausa todos los procesos dentro de uno o más contenedores.

```bash
docker pause <nombre_del_contenedor>
```

### `port`
Muestra las asignaciones de puertos de un contenedor específico.

```bash
docker port <nombre_del_contenedor>
```

### `prune`
Elimina todos los contenedores detenidos.

```bash
docker container prune
```

### `rename`
Renombra un contenedor existente.

```bash
docker rename <nombre_actual> <nuevo_nombre>
```

### `restart`
Reinicia uno o más contenedores.

```bash
docker restart <nombre_del_contenedor>
```

### `rm`
Elimina uno o más contenedores. Si el contenedor está corriendo, primero debe ser detenido.

```bash
docker rm <nombre_del_contenedor>
```

### `run`
Crea y ejecuta un nuevo contenedor desde una imagen.

```bash
docker run -d --name <nombre_del_contenedor> <imagen>
```

### `start`
Inicia uno o más contenedores detenidos.

```bash
docker start <nombre_del_contenedor>
```

### `stats`
Muestra un flujo en vivo de las estadísticas de uso de recursos de los contenedores.

```bash
docker stats
```

### `stop`
Detiene uno o más contenedores en ejecución.

```bash
docker stop <nombre_del_contenedor>
```

### `top`
Muestra los procesos en ejecución dentro de un contenedor.

```bash
docker top <nombre_del_contenedor>
```

### `unpause`
Reanuda los procesos dentro de uno o más contenedores que hayan sido pausados.

```bash
docker unpause <nombre_del_contenedor>
```

### `update`
Actualiza la configuración de uno o más contenedores en ejecución.

```bash
docker update <opciones> <nombre_del_contenedor>
```

### `wait`
Bloquea el proceso hasta que uno o más contenedores se detengan, luego imprime sus códigos de salida.

```bash
docker wait <nombre_del_contenedor>
```