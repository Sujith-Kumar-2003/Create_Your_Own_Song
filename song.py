import pygame
import numpy as np
import math

# Initialize Pygame Mixer
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()

# Function to play a tone
def play_tone(frequency, duration, volume=0.5):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 32767 * volume * np.sin(2 * np.pi * frequency * t)
    wave = wave.astype(np.int16)
    
    # Convert mono to stereo
    stereo_wave = np.stack((wave, wave), axis=-1)
    
    sound = pygame.sndarray.make_sound(stereo_wave)
    sound.play()
    pygame.time.delay(int(duration * 1000))
    sound.stop()

# "Jingle Bells" song using the above tones
def jingle_bells():
    # First part: "Jingle bells, jingle bells"
    play_tone(220.00, 0.5)  # A
    play_tone(220.00, 0.5)  # A
    play_tone(220.00, 0.5)  # A
    play_tone(220.00, 0.5)  # A
    play_tone(220.00, 0.5)  # A
    play_tone(220.00, 0.5)  # A
    play_tone(196.00, 0.5)  # G
    play_tone(220.00, 0.5)  # A
    play_tone(246.94, 0.5)  # B
    play_tone(220.00, 0.5)  # A 
    play_tone(220.00, 0.5)  # A
    play_tone(220.00, 0.5)  # A

    # Second part: "Oh! what fun it is to ride"
    play_tone(220.00, 0.5)  # A
    play_tone(220.00, 0.5)  # A
    play_tone(220.00, 0.5)  # A
    play_tone(220.00, 0.5)  # A
    play_tone(220.00, 0.5)  # A
    play_tone(220.00, 0.5)  # A
    play_tone(196.00, 0.5)  # G
    play_tone(220.00, 0.5)  # A
    play_tone(246.94, 0.5)  # B

    # Ending: "In a one horse open sleigh"
    play_tone(220.00, 0.5)  # A
    play_tone(220.00, 0.5)  # A
    play_tone(220.00, 0.5)  # A
    play_tone(220.00, 0.5)  # A
    play_tone(220.00, 0.5)  # A
    play_tone(220.00, 0.5)  # A
    play_tone(196.00, 0.5)  # G

# Play the "Jingle Bells" melody
jingle_bells()

# Quit pygame mixer after the song is played
pygame.mixer.quit()
