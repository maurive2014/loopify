import pygame
import time
import threading

# Initialize pygame mixer for audio and pygame for key event handling
pygame.mixer.init()
pygame.init()

# Define global variables for timing
recording = {"syn": [], "guitarra": [], "drums": []}
esperaActivaLoop = True
loopSyn = False
loopGuitarra = False
loopDrums = False

contadorThreadsSyn = 0
contadorThreadsGuitarra = 0
contadorThreadsDrums = 0

# Load audio files based on instrument type
def load_audio(noteOrDrumsPart, instrument):
    return pygame.mixer.Sound(f"assets/{noteOrDrumsPart}{instrument}.wav")

# Play audio for a given instrument
def play_audio(noteOrDrumsPart, instrument):
    sound = load_audio(noteOrDrumsPart, instrument) ##TODO creo que lo carga cada vez que se toca
    sound.play()

# Function to record keypress events
def record_keypress(note, instrument):
    timestamp = time.time()
    recording[instrument].append((note, timestamp))
    
    if note is not None:
        play_audio(note, instrument)
    

# Function to loop the recordings
def loop_recording(instrument):
    while esperaActivaLoop:
        tamanio = len(recording[instrument])
        for i in range(tamanio-1): 
                play_audio(recording[instrument][i][0],instrument)
                time.sleep(recording[instrument][i+1][1]-recording[instrument][i][1])
                
        time.sleep(0.05)  # Small delay to avoid high CPU usage

# Function to handle input and record for each instrument
def handle_input():

    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Key Sound Player")


    global esperaActivaLoop
    global loopSyn
    global loopGuitarra 
    global loopDrums 
    
    currentInstrument = None
    handleInput = True
    while handleInput: 
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)

                # Guitar mapping
                if key in ['q', 'w', 'e', 'r', 't', 'y', 'u', '2', '3', '5', '6', '7']:
                    currentInstrument = 'guitarra'
                    guitar_mapping = {
                        'q': 'C', 'w': 'D', 'e': 'E', 'r': 'F', 't': 'G', 'y': 'A', 'u': 'B',
                        '2': 'C-', '3': 'D-', '5': 'F-', '6': 'G-', '7':'A-' 
                    }
                    
                    record_keypress(guitar_mapping[key], 'guitarra')

                # Synthesizer mapping
                elif key in ['z', 'x', 'c', 'v', 'b', 'n', 'm', 's', 'd', 'g', 'h', 'j']:
                    currentInstrument = 'syn'
                    syn_mapping = {
                        'z': 'C', 'x': 'D', 'c': 'E', 'v': 'F', 'b': 'G', 'n': 'A', 'm': 'B',
                        's': 'C-', 'd': 'D-', 'g': 'F-', 'h': 'G-', 'j': 'A-'
                    }
                    record_keypress(syn_mapping[key], 'syn')

                # Drums mapping
                elif key in ['k', 'l', 'i', 'o']:
                    currentInstrument = 'drums'
                    drum_mapping = {
                        'k': 'snare', 'l': 'hihat', 'i': 'crash', 'o': 'bass'
                    }
                    record_keypress(drum_mapping[key], 'drums')

                elif key == '0':
                    
                    if currentInstrument == 'syn':
                        loopSyn = True 
                    elif currentInstrument == 'guitarra':
                        loopGuitarra = True 
                    elif currentInstrument == 'drums':
                        loopDrums = True 

                    record_keypress(None, currentInstrument) #Agregamos una nota de más que contiene timestamp

                # Stop recording
                elif key == 'space':
                    esperaActivaLoop = False
                    handleInput = False
                    print("Stopping loop...")
                    break



# def hacerLoop():
#     # Loop the recordings for each instrument
#     while loop:
#         print('Pasé el flag')
#         if recording['drums']: #TODO está raro, porque desde la primera nota entonces comenzaría a loop
#             loop_recording('drums')
#         if recording['syn']:
#             loop_recording('syn') # SI alg
#         if recording['guitarra']:
#             loop_recording('guitarra')

#         time.sleep(0.1)  # Small delay to maintain sync

# Main function to start everything
def main():
    global esperaActivaLoop
    global contadorThreadsSyn 
    global contadorThreadsGuitarra 
    global contadorThreadsDrums 
    # Start the input handling in a separate thread
    input_thread = threading.Thread(target=handle_input)
    input_thread.start()

    # hacerLoop()
    # Loop the recordings for each instrument
    while esperaActivaLoop:
        
        if loopSyn and contadorThreadsSyn == 0: 
            contadorThreadsSyn +=1
            syn_thread = threading.Thread(target=loop_recording, args=('syn',))
            syn_thread.start()
        if loopGuitarra and contadorThreadsGuitarra == 0: 
            contadorThreadsGuitarra +=1
            syn_thread = threading.Thread(target=loop_recording, args=('guitarra',))
            syn_thread.start()
        if loopDrums and contadorThreadsDrums == 0: 
            contadorThreadsDrums +=1
            syn_thread = threading.Thread(target=loop_recording, args=('drums',))
            syn_thread.start()
        
        if contadorThreadsSyn ==  1 and contadorThreadsGuitarra== 1 and contadorThreadsSyn==1:
            esperaActivaLoop == False
 
        time.sleep(0.1)  # Small delay to maintain sync

if __name__ == "__main__":
    main()
