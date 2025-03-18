import pygame
import os

pygame.init()

playlist = []
# музыкаларга path 
music_folder = r"C:\Users\User\OneDrive - aues.kz\Desktop\LAB7\musics"
allmusic = os.listdir(music_folder)

# playlist-қа .mp3 деп аяқталса қосамыз 
for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))
# вывести фон, названия фона
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("zhanerke_musics")
clock = pygame.time.Clock()

# фон енгіземіз
background = pygame.image.load(os.path.join("lements", "mosque.jpg"))

# кнопкалар тұратын жердің фоны, и тусы
bg = pygame.Surface((500, 200), pygame.SRCALPHA)
bg.fill((50,50,50,100))

# обьем названия песни и шрифт
font2 = pygame.font.SysFont(None, 20)

# кнопки
playb = pygame.image.load(os.path.join("lements", "play.png"))
pausb = pygame.image.load(os.path.join("lements", "pause.png"))
nextb = pygame.image.load(os.path.join("lements", "next.png"))
prevb = pygame.image.load(os.path.join("lements", "back.png"))

index = 0
aplay = False

pygame.mixer.music.load(playlist[index]) 
pygame.mixer.music.play(1)
aplay = True 

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN: #клавиш
            if event.key == pygame.K_SPACE: #егер пробелге тең болса
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()

            if event.key == pygame.K_RIGHT: #егер онга тең болса
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

            if event.key == pygame.K_LEFT: #егер солга тең болса
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
    #место названия песни
    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))
    
    # әр кнопканың орналасуын, көлемін көрсетеміз
    screen.blit(background, (-50, 0))
    screen.blit(bg, (155, 500))
    screen.blit(text2, (365, 520))
    playb = pygame.transform.scale(playb, (70, 70))
    pausb = pygame.transform.scale(pausb, (70, 70))
    if aplay:
        screen.blit(pausb, (370, 590))
    else: 
        screen.blit(playb, (370, 590))
    nextb = pygame.transform.scale(nextb, (70, 70))
    screen.blit(nextb, (460, 587))
    prevb = pygame.transform.scale(prevb, (75, 75))
    screen.blit(prevb, (273, 585))

    clock.tick(24)
    pygame.display.update()