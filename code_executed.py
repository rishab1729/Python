# import os
# from gtts import gTTS
#
# text = 'Your code has been executed.'
# language = 'en' #english
# speech = gTTS(text = text, lang = language, slow = False)
#
# speech.save('executed.wav') # this will save the format

# subprocess.run(["dos2unix", 'executed.wav'])
file_path = 'executed.wav'
import pygame

def code_executed():
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound('executed.wav')
    my_sound.play()
    pygame.time.wait(int(my_sound.get_length() * 1000))


for i in range(2, 10000):
    print(i)
    
    
code_executed()
