### Creación, Gestión y Eliminación de un Pod Nginx en Kubernetes con PowerShell

A continuación, se detalla el proceso para trabajar con un Pod de Nginx en Kubernetes utilizando `kubectl` en PowerShell. Estos pasos incluyen desde la creación del Pod hasta su eliminación.

---

### 1. Iniciar Minikube
Primero, asegúrate de que `minikube` esté en ejecución para que puedas interactuar con el clúster de Kubernetes.

1. **Abrir PowerShell**.
2. **Iniciar Minikube** con el comando:

   ```bash
   minikube start
   ```

Este comando inicia el clúster de Kubernetes dentro de Minikube.

---

### 2. Crear un Pod con Nginx

Para crear un Pod llamado `nginx-pod` usando la imagen oficial de Nginx:

1. **Ejecuta el siguiente comando en PowerShell**:

   ```bash
   kubectl run nginx-pod --image=nginx --restart=Never
   ```

   Este comando hace lo siguiente:
   - **`kubectl run`**: Crea un nuevo recurso en Kubernetes.
   - **`nginx-pod`**: Nombre asignado al Pod.
   - **`--image=nginx`**: Especifica la imagen de Nginx de Docker Hub.
   - **`--restart=Never`**: Define que el Pod no se reiniciará si el contenedor falla (solo se ejecutará una vez).

---

### 3. Verificar el Estado del Pod

Una vez creado el Pod, es útil verificar su estado.

1. **Ejecuta el siguiente comando**:

   ```bash
   kubectl get pods

   # Para ver mas informacion del pod puedes escribir:
   kubectl get pods -o wide
   ```

   Este comando muestra todos los Pods en el clúster junto con su estado. Verás algo similar a lo siguiente:
   
   ```bash
   NAME         READY   STATUS    RESTARTS   AGE
   nginx-pod    1/1     Running   0          1m
   ```

---

### 4. Ver Información Detallada del Pod

Para obtener más detalles sobre el Pod que acabas de crear:

1. **Ejecuta el siguiente comando**:

   ```bash
   kubectl describe pod nginx-pod
   ```

   Esto te dará información detallada como:
   - Eventos recientes del Pod.
   - Configuraciones del contenedor.
   - Recursos asignados.

---

### 5. Acceder al Contenedor del Pod

Si necesitas acceder a la terminal dentro del contenedor Nginx para ejecutar comandos:

1. **Ejecuta el siguiente comando**:

   ```bash
   kubectl exec -it nginx-pod -- /bin/bash
   ```

   Este comando te otorga acceso a la shell del contenedor donde puedes interactuar directamente con el entorno de Nginx.

---

### 6. Exponer el Pod como un Servicio

Para acceder al servidor Nginx a través de tu navegador, puedes exponer el Pod como un servicio:

1. **Ejecuta el siguiente comando**:

   ```bash
   kubectl expose pod nginx-pod --type=NodePort --port=80
   ```

   Esto expone el puerto 80 del Pod en el clúster de Kubernetes.

2. **Obtener la URL del servicio**:

   ```bash
   minikube service nginx-pod --url
   ```

   Este comando te proporciona una URL que puedes abrir en tu navegador para acceder al servidor Nginx.

---

### 7. Eliminar el Pod

Una vez que ya no necesites el Pod, puedes eliminarlo para liberar recursos:

1. **Ejecuta el siguiente comando**:

   ```bash
   kubectl delete pod nginx-pod
   ```

   Esto eliminará el Pod de tu clúster.

---
