# Python:
# TEMA 13: FUNCIONES
import os

# SUBTEMA 3 Y 5: Declaración y Parámetros
def procesar_registro(nombre, cedula, carrera):
    print("\n" + "="*35)
    print("      REGISTRO EXITOSO")
    print("="*35)
    print(f"ESTUDIANTE: {nombre}")
    print(f"ID: {cedula}")
    print(f"CARRERA: {carrera}")
    print("="*35)
    return "✅ Base de Datos Actualizada."

# SUBTEMA 4: Llamada a la función
def menu_principal():
    print("--- SISTEMA DE ADMISIÓN UNEMI 2026 ---")
    nom = input("Nombre completo: ")
    id_est = input("Cédula: ")
    car = input("Carrera: ")
    
    # Envío de parámetros a la función
    resultado = procesar_registro(nom, id_est, car)
    print(resultado)
    
    input("\nPresione ENTER para empaquetar y subir a GitHub...")

if __name__ == "__main__":
    menu_principal()

