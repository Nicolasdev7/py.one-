import pygame

pygame.init()  # Inicializa o Pygame

# Carrega e reproduz a música
pygame.mixer.music.load('1.mp3')
pygame.mixer.music.play()

# Aguarda até que a música termine de tocar
pygame.event.wait()
