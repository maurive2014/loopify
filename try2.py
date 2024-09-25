import numpy as np
import time
import os
from pydub import AudioSegment
from pydub.playback import play

# Dictionary to map keys to sound files
sound_files = {
    'a': 'assets/Csyn.wav',

}

# Store the pressed keys
recorded_notes = []

def play_sound(note_key):
    """Play the sound corresponding to the given key."""
    if note_key in sound_files:
        sound = AudioSegment.from_wav(sound_files[note_key])
        play(sound)
        return sound
    else:
        print(f"No sound mapped to key: {note_key}")
        return None

print("Press a key to play a note (e.g., 'a', 'b', 'c'), or '0' to stop and start looping.")

while True:
    key = input("Press a key: ").lower()

    if key == '0':  # Stop recording and start looping
        print("Stopping recording. Looping notes...")
        break
    elif key in sound_files:  # If valid key, play the sound and store the key
        sound = play_sound(key)
        if sound is not None:
            recorded_notes.append(key)
    else:
        print(f"Invalid key: {key}. Try again.")

# Loop through recorded notes with a 1-second pause
while True:
    for note_key in recorded_notes:
        play_sound(note_key)
        time.sleep(1)  # Pause for 1 second between notes
