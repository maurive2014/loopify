import pygame
import keyboard

# Inicializar el mezclador de sonido de pygame
pygame.mixer.init()

# 1. Cargar el archivo de audio
def load_audio(file_path):
    pygame.mixer.music.load(file_path)

# 2. Reproducir el audio en loop indefinidamente
def play_loop():
    pygame.mixer.music.play(loops=-1)  # loops=-1 indica que se repita indefinidamente
    print("Reproduciendo audio en loop. Presiona 'q' para detener.")

# 3. Detener el loop manualmente
def stop_loop():
    pygame.mixer.music.stop()
    print("Loop detenido.")

# 4. Flujo principal
file_path = 'input_audio.mp3'  # Ruta al archivo de audio
load_audio(file_path)

# Reproducir el loop indefinidamente
play_loop()

# Monitorear la tecla 'q' para detener el loop
try:
    while True:
        if keyboard.is_pressed('q'):
            stop_loop()
            break
except KeyboardInterrupt:
    stop_loop()

print("Programa finalizado.")
