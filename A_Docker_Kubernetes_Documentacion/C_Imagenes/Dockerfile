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