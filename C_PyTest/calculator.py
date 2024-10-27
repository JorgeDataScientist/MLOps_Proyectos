# Clase que define una calculadora básica con operaciones matemáticas simples
class Calculator:

    # Método para sumar dos números
    def add(self, a, b):
        value = a + b  # Realiza la suma
        print(f"Adding {a} and {b} equals {value}")  # Imprime el resultado de la operación
        return value  # Retorna el resultado de la suma

    # Método para restar el segundo número del primero
    def subtract(self, a, b):
        value = a - b  # Realiza la resta
        print(f"Subtracting {b} from {a} equals {value}")  # Imprime el resultado de la operación
        return value  # Retorna el resultado de la resta

    # Método para multiplicar dos números
    def multiply(self, a, b):
        value = a * b  # Realiza la multiplicación
        print(f"Multiplying {a} by {b} equals {value}")  # Imprime el resultado de la operación
        return value  # Retorna el resultado de la multiplicación

    # Método para dividir el primer número por el segundo
    def divide(self, a, b):
        if b == 0:  # Comprueba si el divisor es cero para evitar una excepción
            raise ValueError("Cannot divide by zero")  # Lanza un error si se intenta dividir por cero
        value = a / b  # Realiza la división
        print(f"Dividing {a} by {b} equals {value}")  # Imprime el resultado de la operación
        return value  # Retorna el resultado de la división


# Clase que define una calculadora basada en operaciones de texto
class TextualCalculator:

    # Método que interpreta una operación en formato de texto y la ejecuta
    def perform_operation(self, operation):
        try:
            # Divide la operación en tres partes: el primer número (a), el operador (op), y el segundo número (b)
            a, op, b = operation.split()

            calculator = Calculator()  # Crea una instancia de la clase Calculator

            # Dependiendo del operador (+, -, *, /), llama al método correspondiente de Calculator
            if op == "+":
                return calculator.add(int(a), int(b))  # Convierte los valores a enteros y llama al método de suma
            elif op == "-":
                return calculator.subtract(int(a), int(b))  # Convierte los valores a enteros y llama al método de resta
            elif op == "*":
                return calculator.multiply(int(a), int(b))  # Convierte los valores a enteros y llama al método de multiplicación
            elif op == "/":
                return calculator.divide(int(a), int(b))  # Convierte los valores a enteros y llama al método de división
            else:
                return "Invalid operation"  # Retorna un mensaje de error si el operador no es válido

        except ValueError:
            return "Invalid operation"  # Retorna un mensaje de error si los valores no son válidos o hay algún problema con la operación



# # ----------------------------------------------

# # Crear una instancia de la clase Calculator
# calculator = Calculator()
# # Realizar operaciones directamente usando los métodos de la clase Calculator
# result_add = calculator.multiply(10, 5)

# # ----------------------------------------------
# # Crear una instancia de la clase TextualCalculator
# textual_calculator = TextualCalculator()
# # Realizar algunas operaciones de ejemplo
# result_add = textual_calculator.perform_operation("10 + 5")  # Realiza la suma de 10 + 5
