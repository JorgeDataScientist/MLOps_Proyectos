
### Creación, Gestión y Eliminación de un Pod Nginx en Kubernetes usando un archivo YAML

---

### 1. Crear un archivo YAML para el Pod

Primero, crearemos un archivo YAML que defina el Pod de Nginx.

1. **Crear un archivo llamado `nginx-pod.yaml`** en tu editor de texto favorito (puedes hacerlo desde PowerShell con `notepad nginx-pod.yaml`).
   
2. **Añadir el siguiente contenido YAML** en el archivo:

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: nginx-pod
   spec:
     containers:
     - name: nginx
       image: nginx
       ports:
       - containerPort: 80
   ```

   Explicación del contenido:
   - **`apiVersion: v1`**: Especifica la versión de la API de Kubernetes.
   - **`kind: Pod`**: Define que el recurso es un Pod.
   - **`metadata`**: Contiene información sobre el Pod, como su nombre.
   - **`spec`**: Define las especificaciones del Pod, incluidos los contenedores.
   - **`containers`**: Lista de contenedores dentro del Pod (en este caso, solo hay uno).
   - **`name: nginx`**: Nombre del contenedor.
   - **`image: nginx`**: Imagen Docker de Nginx.
   - **`ports`**: Define el puerto 80 que expondrá el contenedor.

---

### 2. Crear el Pod desde el archivo YAML

1. **Abre PowerShell y navega al directorio donde guardaste el archivo `nginx-pod.yaml`**.
   
2. **Aplica el manifiesto YAML** para crear el Pod con el siguiente comando:

   ```bash
   kubectl apply -f nginx-pod.yaml
   ```

   Este comando lee el archivo YAML y crea el Pod en el clúster.

---

### 3. Verificar el Estado del Pod

Para verificar que el Pod se haya creado correctamente:

1. **Ejecuta el siguiente comando**:

   ```bash
   kubectl get pods
   ```

   Verás una salida similar a la siguiente si el Pod está corriendo:

   ```bash
   NAME         READY   STATUS    RESTARTS   AGE
   nginx-pod    1/1     Running   0          1m
   ```

---

### 4. Ver Información Detallada del Pod

Para obtener más detalles sobre el Pod que creaste con el archivo YAML:

1. **Ejecuta el siguiente comando**:

   ```bash
   kubectl describe pod nginx-pod
   ```

   Esto te mostrará detalles como eventos, configuraciones y el estado actual del Pod.

---

### 5. Acceder al Contenedor del Pod

Si necesitas acceder a la terminal del contenedor de Nginx dentro del Pod:

1. **Ejecuta el siguiente comando**:

   ```bash
   kubectl exec -it nginx-pod -- /bin/bash
   ```

   Esto te otorgará acceso a la shell del contenedor.

---

### 6. Exponer el Pod como un Servicio

Para acceder al Pod de Nginx desde tu navegador:

1. **Ejecuta el siguiente comando** para exponer el puerto 80 del contenedor:

   ```bash
   kubectl expose pod nginx-pod --type=NodePort --port=80
   ```

2. **Obtener la URL para acceder al servicio**:

   ```bash
   minikube service nginx-pod --url
   ```

   Abre la URL en tu navegador para ver el servidor Nginx en acción.

---

### 7. Eliminar el Pod y el Servicio

Cuando ya no necesites el Pod y el servicio, puedes eliminarlos:

1. **Eliminar el Pod usando el archivo YAML**:

   ```bash
   kubectl delete -f nginx-pod.yaml
   ```

2. **Eliminar el servicio**:

   ```bash
   kubectl delete service nginx-pod
   ```

---

Este procedimiento te permite gestionar la infraestructura de Kubernetes usando archivos YAML, lo que es una práctica común y recomendable cuando gestionas múltiples Pods y otros recursos en un clúster.