"""import pygame
import time

pygame.init()

# Экран параметрлері
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

# Кадрлар жылдамдығы
clock = pygame.time.Clock()

#Суреттерді жүктеу
background = pygame.transform.scale(pygame.image.load("image/clock.png"), (WIDTH, HEIGHT))
left_hand = pygame.image.load("image/leftarm.png")   # Секунд
right_hand = pygame.image.load("image/rightarm.png") # Минут

#Негізгі цикл
running = True
while running:
    #Оқиғаларды тексеру (окно жапса - шығу)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Нақты уақытты алу
    current_time = time.localtime()
    minute = current_time.tm_min  # Минуттар
    second = current_time.tm_sec  # Секундтар

    #Бұрыштарды есептеу (1 минут = 6°, 1 секунд = 6°)
    minute_angle = minute * 6 + (second / 60) * 6
    second_angle = second * 6

    #Экранды жаңарту
    screen.blit(background, (0, 0))

    #Минуттық стрелканы (оң қол) бұру және экранға шығару
    rotated_right_hand = pygame.transform.rotate(
        pygame.transform.scale(right_hand, (150, 400)), -minute_angle
    )
    right_hand_rect = rotated_right_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(rotated_right_hand, right_hand_rect)

    #Секундтық стрелканы (сол қол) бұру және экранға шығару
    rotated_left_hand = pygame.transform.rotate(
        pygame.transform.scale(left_hand, (50, 500)), -second_angle
    )
    left_hand_rect = rotated_left_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(rotated_left_hand, left_hand_rect)

    #Экранды жаңарту және FPS шектеу
    pygame.display.flip()
    clock.tick(60)

# Бағдарламаны жабу
pygame.quit()
"""

import pygame 
import time
import math
pygame.init()

#пайда болатын экран ұзындықтары
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

#пайда болған экранның жоғар жағындағы атау
pygame.display.set_caption("Mickey clock")

#суреттерді пайда болған экранға енгіземіз
leftarm = pygame.image.load("image/leftarm.png") #sec
rightarm = pygame.image.load("image/rightarm.png") #min
mainclock = pygame.transform.scale(pygame.image.load("image/clock.png"), (800, 600))

done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #localtime арқылы минут пен сикундты анықтап аламыз
    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    #минут пен сикундтың бұрышын алып аламыз
    #қазіргі минут * 360 градус / 60 минут + қазіргі секундты қосамыз 
    minute_angle = minute * 6+ (second / 60) * 6   
    second_angle = second * 6  
    
    #экран бетіне пайда фонмен болуы
    screen.blit(mainclock, (0,0))
    
    #оң қол минутты орналастыру
    rotated_rightarm = pygame.transform.rotate(pygame.transform.scale(rightarm, (800, 600)), -minute_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(800 // 2, 600 // 2 + 12))
    screen.blit(rotated_rightarm, rightarmrect)
    
    #сол қол секундты орналастыру
    rotated_leftarm = pygame.transform.rotate(pygame.transform.scale(leftarm, (40.95, 682.5)), -second_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(800 // 2, 600 // 2 + 10))
    screen.blit(rotated_leftarm, leftarmrect)
    
    pygame.display.flip() #окноны жаңартады
    clock.tick(60) #fps
    
pygame.quit()
