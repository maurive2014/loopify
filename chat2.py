import pygame
import time

# Initialize pygame mixer for audio and the display for key events
pygame.init()
pygame.mixer.init()

# Define the path to assets
ASSETS_PATH = 'assets/'

# Define the sound mapping for synthesizer, guitar, and drums
sound_mapping = {
    # Synthesizer notes (Q to U, 2, 3, 5-7)
    pygame.K_q: 'Cguitarra.wav', pygame.K_w: 'Dguitarra.wav', pygame.K_e: 'Eguitarra.wav',
    pygame.K_r: 'Fguitarra.wav', pygame.K_t: 'Gguitarra.wav', pygame.K_y: 'Aguitarra.wav', pygame.K_u: 'Bguitarra.wav',
    pygame.K_2: 'C-guitarra.wav', pygame.K_3: 'D-guitarra.wav', pygame.K_5: 'F-guitarra.wav', pygame.K_6: 'G-guitarra.wav', pygame.K_7: 'A-guitarra.wav',

    # Syn notes
    pygame.K_z: 'Csyn.wav', pygame.K_x: 'Dsyn.wav', pygame.K_c: 'Esyn.wav',
    pygame.K_v: 'Fsyn.wav', pygame.K_b: 'Gsyn.wav', pygame.K_n: 'Asyn.wav', pygame.K_m: 'Bsyn.wav',
    pygame.K_s: 'C-syn.wav', pygame.K_d: 'D-syn.wav', pygame.K_g: 'F-syn.wav', pygame.K_h: 'G-syn.wav', pygame.K_j: 'A-syn.wav',
    
    # Drums (choose keys for snare, hi-hat, crash cymbal, and bass)
    #pygame.K_a: 'snare.wav', pygame.K_k: 'hihat.wav', pygame.K_l: 'crash.wav', pygame.K_SPACE: 'bass.wav'

    pygame.K_a: 'Csyn.wav'
}

# Load all sounds into a dictionary
sounds = {key: pygame.mixer.Sound(ASSETS_PATH + sound_file) for key, sound_file in sound_mapping.items()}

# Storage for looped sounds (for drums, synth, guitar)
loop_recordings = {'drums': [], 'synth': [], 'guitar': []}
current_instrument = None  # Keeps track of which instrument is being recorded

# Function to play and store sound for the current instrument
def record_and_play(key, instrument):
    if key in sounds:
        sound = sounds[key]
        sound.play()
        if instrument == 'drums':
            loop_recordings['drums'].append((sound, time.time()))
        elif instrument == 'synth':
            loop_recordings['synth'].append((sound, time.time()))
        elif instrument == 'guitar':
            loop_recordings['guitar'].append((sound, time.time()))

# Function to loop sounds
def play_loops(instrument):
    while True:
        now = time.time()
        for sound, start_time in loop_recordings[instrument]:
            if now - start_time >= loop_duration:
                sound.play()  # Replay the sound after loop duration
                loop_recordings[instrument] = [(s, now) for s, _ in loop_recordings[instrument]]

# Main loop to capture input
def main():
    global current_instrument, loop_duration

    # Start in drums mode for recording
    current_instrument = 'drums'
    loop_duration = None  # Time to wait before loop restarts

    # Setup loop flag
    recording = True
    looping = False

    print("Press keys to record. Press 0 to loop the current instrument, and press i, o, or p to switch between drums, synth, and guitar.")

    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Key Sound Player")

    while True:
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key in sound_mapping:
                    # Play and record sound for the current instrument
                    record_and_play(event.key, current_instrument)

                elif event.key == pygame.K_0:  # Key '0' to start looping
                    if recording:
                        loop_duration = time.time() - loop_recordings[current_instrument][0][1]
                        recording = False
                        looping = True
                        print(f"{current_instrument.capitalize()} recorded. Looping now.")

                    if looping:
                        play_loops(current_instrument)

                elif event.key == pygame.K_i:  # Switch to drums
                    current_instrument = 'drums'
                    print("Switched to drums. Press keys to record.")
                    loop_recordings['drums'] = []  # Reset drum loop

                elif event.key == pygame.K_o:  # Switch to synthesizer
                    current_instrument = 'synth'
                    print("Switched to synth. Press keys to record.")
                    loop_recordings['synth'] = []  # Reset synth loop

                elif event.key == pygame.K_p:  # Switch to electric guitar
                    current_instrument = 'guitar'
                    print("Switched to guitar. Press keys to record.")
                    loop_recordings['guitar'] = []  # Reset guitar loop

if __name__ == '__main__':
    main()
