# Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame

print('=' * 6 + ' DESAFIO 21 ' + '=' * 6)

pygame.mixer.init()
pygame.mixer.music.load("media/music/aranha.mp3")
pygame.mixer.music.play()
teste = input('')