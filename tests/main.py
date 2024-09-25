import pygame

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

# # Set up the display (optional, for capturing key events)
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Key Sound Player")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in sounds:
                sounds[event.key].play()  # Play the corresponding sound

# Quit pygame
pygame.quit()
