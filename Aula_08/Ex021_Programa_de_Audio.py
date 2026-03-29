#faça um programa em python que abra e reproduza um áudio de arquivo MP3.
import pygame
pygame.mixer.init()
pygame.mixer.music.load('retrositive-tutoriel-simple-237930.mp3')
pygame.mixer.music.play()
input('Aperte ENTER para encerrar a música...')
