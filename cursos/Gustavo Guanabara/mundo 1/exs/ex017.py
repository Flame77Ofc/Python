# Tocando música
import pygame
pygame.init()
pygame.mixer.music.load('exs/ex017mario.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()