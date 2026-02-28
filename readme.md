# 🎮 Proyecto Lingo - Juego de Adivinanza de Palabras

Este proyecto consiste en la implementación del juego **Lingo** en Python. El objetivo es adivinar una palabra oculta de 5 letras mediante un sistema de pistas visuales, desarrollado bajo una metodología de control de versiones profesional.

## 📋 Requisitos del Ejercicio
El desarrollo cumple con los siguientes puntos clave solicitados:
1. **Control de versiones**: Gestión completa mediante Git.
2. **Estructura de Ramas**: Uso de ramas `feature-lingo`, `develop` y `main`.
3. **GitHub con Pull Request (PR)**: Integración de cambios desde la rama de características a desarrollo y finalmente a producción.
4. **Programación con Funciones**: Lógica encapsulada para una mejor organización.
5. **Uso del Depurador**: Código optimizado para seguimiento de variables en VS Code.

## 💡 Lógica del Juego
El programa utiliza un sistema de comparación de caracteres para guiar al usuario:

* **Bucle Infinito (`while True`)**: El juego solicita palabras continuamente hasta que el usuario acierta la palabra secreta.
* **Validación de Entrada**: Se asegura de que el usuario introduzca exactamente 5 letras antes de procesar el intento.
* **Sistema de Pistas**:
    * `[x]`: La letra es correcta y está en la posición exacta.
    * `(x)`: La letra existe en la palabra secreta pero en una posición diferente.
    * `x`: La letra no forma parte de la palabra secreta.



## 🛠️ Cómo Ejecutar
1. Asegúrate de tener instalado Python 3.
2. Clona el repositorio.
3. Ejecuta el archivo principal:
   ```bash
   python lingo.py