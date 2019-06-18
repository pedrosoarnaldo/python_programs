import pygame

pygame.mixer.init()
pygame.mixer_music.load('example.mp3')
pygame.mixer_music.play()
pygame.event.wait()

