# Sistema de recopilación de comentarios y sugerencias

def main():
    comentarios = []
    
    while True:
        print("\n--- EVALUACIÓN Y SUGERENCIAS ---")
        print("1. Registrar comentario de una actividad")
        print("2. Ver todos los comentarios recopilados")
        print("3. Salir")
        opcion = input("Elige una opción (1-3): ").strip()
        
        if opcion == "1":
            actividad = input("Nombre de la actividad evaluada: ").strip().title()
            participante = input("Nombre del participante (o déjalo en blanco si es anónimo): ").strip().title()
            if not participante:
                participante = "Anónimo"
            sugerencia = input("Escribe el comentario o sugerencia de mejora: ").strip()
            
            if actividad and sugerencia:
                registro = {
                    "actividad": actividad,
                    "participante": participante,
                    "comentario": sugerencia
                }
                comentarios.append(registro)
                print("¡Comentario guardado con éxito!")
            else:
                print("La actividad y el comentario son obligatorios.")
                
        elif opcion == "2":
            if not comentarios:
                print("Aún no hay comentarios registrados.")
            else:
                print("\n" + "="*60)
                print(f"{'ACTIVIDAD':<20} | {'PARTICIPANTE':<15} | {'COMENTARIO'}")
                print("="*60)
                for c in comentarios:
                    print(f"{c['actividad']:<20} | {c['participante']:<15} | {c['comentario']}")
                print("="*60)
                
        elif opcion == "3":
            print("Saliendo del módulo de sugerencias.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()