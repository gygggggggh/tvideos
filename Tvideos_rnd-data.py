import random
import pygame
from gtts import gTTS

def jouer_roue_de_fortune(noms):
    # Initialisation de Pygame
    pygame.init()
    
    # Charger le son de roue de fortune
    pygame.mixer.music.load("roue_fortune.mp3")

    # Jouer le son de roue de fortune
    pygame.mixer.music.play()

    # Attendre la fin du son
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)

    # Choisir un nom aléatoire
    nom_choisi = random.choice(noms)

    # choisir une langue aléatoire
    langue_choisie = random.choice(["fr", "en", "ja", "es", "de", "it", "ru", "zh-cn", "ar", "pt", "hi"])

    # Utiliser la synthèse vocale pour lire le nom choisi
    tts = gTTS(nom_choisi, lang="fr")
    tts.save("nom_choisi.mp3")
    print(nom_choisi, langue_choisie)
    pygame.mixer.music.load("nom_choisi.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)

    # Quitter Pygame
    pygame.quit()

noms = ["Lyan", "lucas(b)", "emeric", "liam", "yorris", "aurelien","yanis","louca(z)"]
jouer_roue_de_fortune(noms)
