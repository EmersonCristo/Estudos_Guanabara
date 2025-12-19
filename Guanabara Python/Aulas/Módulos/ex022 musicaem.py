import pygame 

pygame.init() #precisamos iniciar o pygame
pygame.mixer.music.load('musicaex022.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()

# Provavel falha por estar no VsCode, por pesquisas e na propria aula (via comentarios), pycharm está atualizado e não tem mais essa pygame, tambem tem o caso de estar no vscode, preciso revisar como colocar musica em python via vscode

