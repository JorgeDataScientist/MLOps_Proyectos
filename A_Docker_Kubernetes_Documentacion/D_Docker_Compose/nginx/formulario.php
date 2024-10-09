<?php
// Definición de parámetros de conexión a la base de datos
$servername = "mysql"; // Nombre del servidor de la base de datos
$username = "root"; // Nombre de usuario para conectarse a la base de datos
$password = getenv("MYSQL_ROOT_PASSWORD"); // Obtiene la contraseña del usuario root
$dbname = "test_db"; // Nombre de la base de datos

// Crear conexión con la base de datos
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificación de errores de conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
} else {
    echo "Conexión exitosa"; // Mensaje de depuración
}


// Crear la tabla 'usuarios' si no existe
$tableSQL = "CREATE TABLE IF NOT EXISTS usuarios (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, // Identificador único
    nombre VARCHAR(50) NOT NULL,                   // Nombre del usuario
    email VARCHAR(50) NOT NULL                     // Email del usuario
)";

if ($conn->query($tableSQL) === TRUE) {
    // echo "Tabla usuarios creada o ya existe."; // Mensaje opcional
} else {
    echo "Error creando tabla: " . $conn->error;
}

// Verificar si se recibió una solicitud POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtener los datos del formulario
    $name = $_POST["name"]; // Obtener el nombre
    $email = $_POST["email"]; // Obtener el email

    // Preparar la consulta SQL para insertar los datos en la tabla 'usuarios'
    $stmt = $conn->prepare("INSERT INTO usuarios (nombre, email) VALUES (?, ?)");
    $stmt->bind_param("ss", $name, $email); // 'ss' significa que ambos son strings

    // Ejecutar la consulta
    if ($stmt->execute()) {
        echo "Registro exitoso";
    } else {
        echo "Error: " . $stmt->error; // Imprimir error si hay
    }

    // Cerrar la declaración
    $stmt->close();
}

// Cerrar la conexión a la base de datos
$conn->close(); // Cerrar conexión
?>
