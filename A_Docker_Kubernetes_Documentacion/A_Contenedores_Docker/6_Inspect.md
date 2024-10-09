
```markdown
# Comando `docker inspect` en Docker

## Descripción

El comando `docker inspect` en Docker se utiliza para obtener información detallada sobre los objetos de Docker, como contenedores, imágenes, volúmenes o redes. El comando devuelve un conjunto de datos en formato JSON que describe la configuración del objeto, el estado actual, la red, y otros metadatos relevantes.

---

## Sintaxis del Comando

La sintaxis básica del comando `docker inspect` es la siguiente:

```bash
docker inspect [opciones] [nombre_o_id_objeto]
```

- `[opciones]`: Parámetros opcionales para modificar el comportamiento del comando.
- `[nombre_o_id_objeto]`: El nombre o ID del objeto que se desea inspeccionar (contenedor, imagen, volumen, etc.).

---

## Ejemplo de Uso

### Inspeccionar un Contenedor

Cuando queremos obtener detalles de un contenedor específico, podemos usar el ID o el nombre del contenedor. Por ejemplo, si tenemos un contenedor en ejecución con el nombre `mi_nginx`, el comando para inspeccionarlo sería:

```bash
docker inspect mi_nginx
```

Este comando devolverá una salida en formato JSON que contiene información detallada sobre el contenedor, como:

- La configuración de red.
- Los volúmenes montados.
- La configuración del entorno.
- Las rutas a los binarios.
- La imagen base del contenedor.
- El estado actual (en ejecución, detenido, etc.).

### Ejemplo Completo

Supongamos que tenemos un contenedor en ejecución con el ID `a508f1d513e1`. Para inspeccionarlo, usaríamos el siguiente comando:

```bash
docker inspect a508f1d513e1
```

El resultado sería algo similar a:

```json
[
    {
        "Id": "a508f1d513e1cbf5d6be662fd4a5d1f9d9a3f7b1129c52c1694571f2b1e038f1",
        "Created": "2024-10-03T14:51:13.6518719Z",
        "Path": "/docker-entrypoint.sh",
        "Args": [
            "nginx",
            "-g",
            "daemon off;"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 1801,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2024-10-03T14:51:15.8244536Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "NetworkSettings": {
            "IPAddress": "172.17.0.2",
            "MacAddress": "02:42:ac:11:00:02",
            ...
        }
    }
]
```

En este resultado, podemos ver:

- **Id**: El ID único del contenedor.
- **Created**: Fecha y hora en que se creó el contenedor.
- **Path**: El comando ejecutado en el contenedor.
- **State**: El estado actual del contenedor (en este caso, `running`).
- **NetworkSettings**: Información de la red, como la dirección IP asignada al contenedor.

---

## Filtrar Resultados con `--format`

Si solo necesitamos extraer una parte específica de la información, podemos utilizar la opción `--format`. Esto es útil cuando queremos ver un detalle en particular sin la necesidad de leer todo el JSON.

Por ejemplo, para obtener solo la dirección IP del contenedor `mi_nginx`, podríamos usar:

```bash
docker inspect --format='{{.NetworkSettings.IPAddress}}' mi_nginx
```

Esto devolverá algo como:

```bash
172.17.0.2
```

---

## Conclusión

El comando `docker inspect` es una herramienta poderosa para obtener detalles exhaustivos sobre los objetos de Docker. Nos permite acceder a información detallada sobre el estado, configuración, y propiedades de un contenedor o cualquier otro objeto, lo que facilita la solución de problemas y la gestión de recursos en Docker.