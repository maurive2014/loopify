import pygame

# Initialize the mixer and pygame
pygame.mixer.init()
pygame.init()

# Define key-sound mappings
key_sound_map = {
    pygame.K_a: 'assets/C4.mp3',  # Map 'A' key to 'sound_a.wav'
}

# Load all sounds
sounds = {key: pygame.mixer.Sound(sound_file) for key, sound_file in key_sound_map.items()}

# Set up the display (optional, for capturing key events)
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
