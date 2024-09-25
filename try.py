## Probar que guarde cada nota que toque pero con un diferencia igual de cada nota, y cuando precione la tecla 
## la nota final qeu toque debe coincidir con el momento en que debe iniciar


import time
import pygame
import threading
loop = True
# Initialize the mixer and pygame
pygame.mixer.init()
pygame.init()

# MAPEAMOS LAS TECLAS A CADA AUDIO
key_sound_map = {
    
    ## SYNTH

    pygame.K_z: 'assets/Csyn.wav',  
    pygame.K_x: 'assets/Dsyn.wav',
    pygame.K_c: 'assets/Esyn.wav',
    pygame.K_v: 'assets/Fsyn.wav',
    pygame.K_b: 'assets/Gsyn.wav',
    pygame.K_n: 'assets/Asyn.wav',
    pygame.K_m: 'assets/Bsyn.wav',
    pygame.K_s: 'assets/C-syn.wav',
    pygame.K_d: 'assets/D-syn.wav',
    pygame.K_g: 'assets/F-syn.wav',
    pygame.K_h: 'assets/G-syn.wav',
    pygame.K_j: 'assets/A-syn.wav',
    

}

# Load all sounds
sounds = {key: pygame.mixer.Sound(sound_file) for key, sound_file in key_sound_map.items()}

record = {'syn':{'finalizado':False, 'notas':[]}} #(key, time)

# # Set up the display (optional, for capturing key events)
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Key Sound Player")

# Main loop
def handle_input():
    global loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                
                if event.key in sounds :
                    sounds[event.key].play()  # Play the corresponding sound
                    record['syn']['notas'].append((event.key, 0.5))
                    
                elif event.key == pygame.K_0:
                    record['syn']['finalizado'] = True

def loop_recording(instrument):
    while loop:
        for key, time in record[instrument]['notas']:
            sounds[key].play()
            time.sleep(time)
        time.sleep(0.05) 



def main():
    global loop

    # Start the input handling in a separate thread
    input_thread = threading.Thread(target=handle_input)
    input_thread.start()

    while loop:
        if record['syn']['finalizado']:
            loop_recording('syn')
           
        time.sleep(0.1)  # Small delay to maintain sync

if __name__ == "__main__":
    main()


handle_input()
# Quit pygame

