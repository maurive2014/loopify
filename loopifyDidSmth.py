import pygame
import time
import threading

# Initialize pygame mixer for audio and pygame for key event handling
pygame.mixer.init()
pygame.init()

# Define global variables for timing
recording = {"syn": [], "guitarra": [], "drums": []}
start_time = None
loop = True

# Load audio files based on instrument type
def load_audio(noteOrDrumsPart, instrument):
    return pygame.mixer.Sound(f"assets/{noteOrDrumsPart}{instrument}.wav")

# Play audio for a given instrument
def play_audio(noteOrDrumsPart, instrument):
    sound = load_audio(noteOrDrumsPart, instrument) ##TODO creo que lo carga cada vez que se toca
    sound.play()

# Function to record keypress events
def record_keypress(note, instrument):
    global start_time
    if start_time is None:
        start_time = time.time()

    timestamp = time.time() - start_time
    recording[instrument].append((note, timestamp))
    play_audio(note, instrument)

# Function to loop the recordings
def loop_recording(instrument):
    while loop:
        current_time = time.time() - start_time
        for note, timestamp in recording[instrument]: # TODO NO ME CUADRA, PERO ME PUEDE SERVIR
            if current_time >= timestamp:
                play_audio(note, instrument)
        time.sleep(0.05)  # Small delay to avoid high CPU usage

# Function to handle input and record for each instrument
def handle_input():

    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Key Sound Player")


    global loop
    while True: #TODO creo que por este no trabaja
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)

                # Guitar mapping
                if key in ['q', 'w', 'e', 'r', 't', 'y', 'u', '2', '3', '5', '6', '7']:
                    guitar_mapping = {
                        'q': 'C', 'w': 'D', 'e': 'E', 'r': 'F', 't': 'G', 'y': 'A', 'u': 'B',
                        '2': 'C-', '3': 'D-', '5': 'F-', '6': 'G-', '7':'A-' 
                    }
                    record_keypress(guitar_mapping[key], 'guitarra')

                # Synthesizer mapping
                elif key in ['z', 'x', 'c', 'v', 'b', 'n', 'm', 's', 'd', 'g', 'h', 'j']:
                    syn_mapping = {
                        'z': 'C', 'x': 'D', 'c': 'E', 'v': 'F', 'b': 'G', 'n': 'A', 'm': 'B',
                        's': 'C-', 'd': 'D-', 'g': 'F-', 'h': 'G-', 'j': 'A-'
                    }
                    record_keypress(syn_mapping[key], 'syn')

                # Drums mapping
                elif key in ['k', 'l', 'i', 'o']:
                    drum_mapping = {
                        'k': 'snare', 'l': 'hihat', 'i': 'crash', 'o': 'bass'
                    }
                    record_keypress(drum_mapping[key], 'drums')

                # Stop recording
                elif key == 'space':
                    loop = False
                    print("Stopping loop...")
                    break



def hacerLoop():
    # Loop the recordings for each instrument
    while loop:
        if recording['drums']: #TODO está raro, porque desde la primera nota entonces comenzaría a loop
            loop_recording('drums')
        if recording['syn']:
            loop_recording('syn')
        if recording['guitarra']:
            loop_recording('guitarra')

        time.sleep(0.1)  # Small delay to maintain sync

# Main function to start everything
def main():
    global loop

    # Start the input handling in a separate thread
    input_thread = threading.Thread(target=handle_input)
    input_thread.start()

    hacerLoop()
    # Loop the recordings for each instrument
    # while loop:
    #     if recording['drums']: #TODO está raro, porque desde la primera nota entonces comenzaría a loop
    #         loop_recording('drums')
    #     if recording['syn']:
    #         loop_recording('syn')
    #     if recording['guitarra']:
    #         loop_recording('guitarra')

    #     time.sleep(0.1)  # Small delay to maintain sync

if __name__ == "__main__":
    main()
