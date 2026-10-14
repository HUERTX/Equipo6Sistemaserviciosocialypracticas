# Sistema de envío de recordatorios

def enviar_recordatorio():
    print("\n--- ENVÍO DE RECORDATORIOS ---")
    destinatario = input("Ingresa el correo o número del participante: ").strip()
    actividad = input("Nombre de la actividad: ").strip()
    fecha = input("Fecha y hora del evento: ").strip()
    
    medio = input("¿Por dónde deseas enviarlo? (1: Correo electrónico / 2: Mensaje de texto): ").strip()
    
    if medio == "1":
        print(f"\n[CORREO ENVIADO con éxito]")
        print(f"Para: {destinatario}")
        print(f"Asunto: Recordatorio de actividad - {actividad}")
        print(f"Cuerpo: Hola, te recordamos que tienes programada la actividad '{actividad}' para el día {fecha}.")
    elif medio == "2":
        print(f"\n[MENSAJE ENVIADO con éxito]")
        print(f"Para: {destinatario}")
        print(f"Texto: ¡Hola! Te recordamos asistir a '{actividad}' el {fecha}. ¡Te esperamos!")
    else:
        print("Opción de medio no válida.")

def main():
    while True:
        print("\n1. Enviar nuevo recordatorio")
        print("2. Salir")
        opcion = input("Elige una opción (1-2): ").strip()
        if opcion == "1":
            enviar_recordatorio()
        elif opcion == "2":
            print("Saliendo del sistema de recordatorios.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()