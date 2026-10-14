# Sistema de registro de asistencia de participantes
# Tarea escolar - Ordenado y fácil de usar

def mostrar_menu():
    print("\n--- SISTEMA DE ASISTENCIA ---")
    print("1. Agregar participante")
    print("2. Registrar asistencia")
    print("3. Ver lista y asistencias")
    print("4. Salir")

def main():
    # Diccionario para almacenar: {"Nombre del participante": "Estado"}
    participantes = {}
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ").strip()
        
        if opcion == "1":
            nombre = input("Ingresa el nombre completo del participante: ").strip().title()
            if nombre:
                if nombre not in participantes:
                    participantes[nombre] = "Sin registro"
                    print(f"¡Éxito! '{nombre}' fue agregado a la lista.")
                else:
                    print("Este participante ya se encuentra registrado.")
            else:
                print("El nombre no puede estar vacío.")
                
        elif opcion == "2":
            if not participantes:
                print("Aún no hay participantes en la lista. Agrega uno primero.")
                continue
            
            print("\nLista de participantes:")
            for nombre in participantes:
                print(f"- {nombre}")
                
            nombre_marcar = input("¿A quién deseas registrarle asistencia?: ").strip().title()
            if nombre_marcar in participantes:
                estado = input("¿Asistió? (Escribe 's' para presente o 'n' para ausente): ").strip().lower()
                if estado == 's':
                    participantes[nombre_marcar] = "Presente"
                    print(f"Asistencia guardada: {nombre_marcar} -> Presente.")
                elif estado == 'n':
                    participantes[nombre_marcar] = "Ausente"
                    print(f"Asistencia guardada: {nombre_marcar} -> Ausente.")
                else:
                    print("Opción inválida. Usa 's' o 'n'.")
            else:
                print("No se encontró a ese participante en el sistema.")
                
        elif opcion == "3":
            if not participantes:
                print("No hay registros para mostrar todavía.")
            else:
                print("\n" + "="*40)
                print(f"{'PARTICIPANTE':<25} | {'ESTADO'}")
                print("="*40)
                # Se usa sorted() para mantener la lista ordenada alfabéticamente
                for nombre, estado in sorted(participantes.items()):
                    print(f"{nombre:<25} | {estado}")
                print("="*40)
                
        elif opcion == "4":
            print("Saliendo del sistema de asistencia. ¡Buen trabajo con la tarea!")
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 4.")

if __name__ == "__main__":
    main()