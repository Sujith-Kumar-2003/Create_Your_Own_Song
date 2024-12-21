import pygame
import numpy as np

pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
pygame.init()

def play_tone(frequency, duration, volume=0.5):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 32767 * volume * np.sin(2 * np.pi * frequency * t)
    wave = wave.astype(np.int16)  
    sound = pygame.sndarray.make_sound(wave)
    sound.play()
    pygame.time.delay(int(duration * 1000))
    sound.stop()

# gebneratedf wiht random values, need to change to set tot eh theme.
def s1():
    play_tone(164.81, 1)  
    play_tone(110.00, 1)  
    play_tone(130.81, 0.5)  
    play_tone(146.83, 0.5) 

def s2():
    play_tone(164.81, 1)
    play_tone(110.00, 1)
    play_tone(138.59, 0.5)  
    play_tone(146.83, 0.5)

def s3():
    play_tone(164.81, 3)
    play_tone(110.00, 3)
    play_tone(130.81, 0.5)
    play_tone(146.83, 0.5)

def s4():
    play_tone(123.47, 1)  
    play_tone(82.41, 1)  
    play_tone(98.00, 0.5)  
    play_tone(110.00, 0.5)  

def s5():
    play_tone(146.83, 3)  
    play_tone(98.00, 3)   
    play_tone(130.81, 0.5)
    play_tone(123.47, 0.5)

for _ in range(4):
    s1()

for _ in range(4):
    s2()

s3()

for _ in range(4):
    s4()

s5()

pygame.mixer.quit()
