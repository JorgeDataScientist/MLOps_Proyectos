
```markdown
# Configuración y Uso de Puertos en Docker

## Introducción
Docker permite exponer puertos desde los contenedores para que puedan interactuar con el mundo exterior. Esto es esencial para los contenedores que ejecutan aplicaciones web o servicios que necesitan ser accesibles desde fuera del contenedor. Docker proporciona dos flags para trabajar con puertos: `-p` y `-P`.

---

## Uso del Flag `-p`
El flag `-p` permite mapear un puerto específico del host (tu máquina) a un puerto específico del contenedor.

### Sintaxis
```bash
docker run -p [puerto_host]:[puerto_contenedor] [imagen]
```

### Ejemplo
Si queremos ejecutar un contenedor de `nginx` y exponer el puerto 8080 del host al puerto 80 del contenedor (que es donde `nginx` escucha por defecto), usaríamos:
```bash
docker run -d -p 8080:80 nginx
```

En este caso:
- `8080` es el puerto en tu host (tu computadora).
- `80` es el puerto en el contenedor donde `nginx` está sirviendo su contenido.

Ahora, puedes acceder al servidor web desde el navegador en `http://localhost:8080`.

---

## Uso del Flag `-P`
El flag `-P` asigna automáticamente puertos aleatorios del host a los puertos expuestos del contenedor. Docker examina los puertos que están definidos en el `Dockerfile` del contenedor (usando la instrucción `EXPOSE`) y asigna puertos dinámicamente.

### Sintaxis
```bash
docker run -P [imagen]
```

### Ejemplo
Si tenemos una imagen que expone el puerto 80, podemos ejecutar el siguiente comando:
```bash
docker run -d -P nginx
```

Docker asignará un puerto disponible aleatorio en el host y lo mapeará al puerto 80 del contenedor. Para ver qué puerto ha sido asignado, puedes usar:
```bash
docker port [nombre_contenedor]
```

---

## Configurar un Puerto en un Contenedor
Configurar un puerto al crear un contenedor es muy simple, usando el flag `-p`. Este flag te permite especificar tanto el puerto de tu host como el puerto dentro del contenedor que quieres mapear.

### Ejemplo
Para crear un contenedor de Apache y mapear el puerto 8080 del host al puerto 80 del contenedor:
```bash
docker run -d -p 8080:80 httpd
```
Ahora, puedes acceder a Apache en `http://localhost:8080`.

---

## Modificar el Puerto de un Contenedor
No es posible cambiar directamente el puerto mapeado de un contenedor ya existente. Sin embargo, hay dos soluciones:

### Opción 1: Detener y Eliminar el Contenedor, Luego Recrear con Nuevo Puerto
Debes eliminar el contenedor y crear uno nuevo con los puertos mapeados correctos. Para eliminar un contenedor:
```bash
docker stop [nombre_contenedor]
docker rm [nombre_contenedor]
```

Luego, puedes recrear el contenedor con los nuevos puertos. Por ejemplo:
```bash
docker run -d -p 9090:80 httpd
```

### Opción 2: Usar Docker Compose
Si usas `docker-compose`, puedes modificar los puertos en el archivo `docker-compose.yml` y luego reiniciar los contenedores con:
```bash
docker-compose up -d
```

---

## Verificación de Puertos Asignados
Para verificar qué puertos han sido mapeados en un contenedor en ejecución, puedes usar el siguiente comando:
```bash
docker port [nombre_contenedor]
```
Este comando te mostrará los puertos del host que están mapeados a los puertos del contenedor.

### Ejemplo
Si ejecutas:
```bash
docker port mi_nginx
```
El resultado será algo como:
```
80/tcp -> 0.0.0.0:8080
```
Esto significa que el puerto 8080 en el host está mapeado al puerto 80 del contenedor.

---

## Listar Contenedores en Ejecución con Puertos Expuestos
Para ver qué contenedores están en ejecución y sus puertos mapeados, puedes utilizar el comando:
```bash
docker ps
```
Este comando mostrará una lista de todos los contenedores en ejecución y sus detalles, incluyendo los puertos mapeados.

---

## Conclusión
El uso de los puertos en Docker es esencial para hacer accesibles los servicios y aplicaciones que corren dentro de contenedores. El flag `-p` permite un control preciso sobre los puertos, mientras que `-P` asigna puertos de manera automática. Si deseas cambiar los puertos, es necesario eliminar el contenedor y crearlo nuevamente con el nuevo mapeo.
