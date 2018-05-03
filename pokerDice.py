#       pokerDice v1.0
#       MAIN SCRIPT TO DISPLAY IMAGES IN PYGAME WINDOW
#       ESCANDE DAMIEN
#       JANUARY THE 31st 2014
import pygame
from pygame.locals import *
from roll import * # function just throwing 1d6
from results import *
d = [roll(), roll(), roll(),roll(),roll()] # initial dice roll



pygame.init() #init library
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
soundRoll = pygame.mixer.Sound("son.wav")
woosh = pygame.mixer.Sound("woosh.wav")
applause = pygame.mixer.Sound("applause.wav")
boo = pygame.mixer.Sound("boo.wav")
cowboy = pygame.mixer.Sound("cowboy.wav")

window = pygame.display.set_mode((800, 600)) #creating window
soundRoll.play() # playing the sound
background = pygame.image.load("green_carpet1.png").convert()
r1 = pygame.image.load("red_1.png").convert()
r2 = pygame.image.load("red_2.png").convert()
r3 = pygame.image.load("red_3.png").convert()
r4 = pygame.image.load("red_4.png").convert()
r5 = pygame.image.load("red_5.png").convert()
r6 = pygame.image.load("red_6.png").convert()

dice0 = pygame.image.load("dice_1.png").convert()
dice1 = pygame.image.load("dice_2.png").convert()
dice2 = pygame.image.load("dice_3.png").convert()
dice3 = pygame.image.load("dice_4.png").convert()
dice4 = pygame.image.load("dice_5.png").convert()
dice5 = pygame.image.load("dice_6.png").convert()
#DISPLAYING INITIAL ROLL
if(d[0] == 1):
        dice0 = pygame.image.load("dice_1.png").convert()
        background.blit(dice0, (200,435))
elif(d[0] == 2):
        dice0 = pygame.image.load("dice_2.png").convert()
        background.blit(dice0, (200,435))
elif(d[0] == 3):
        dice0 = pygame.image.load("dice_3.png").convert()
        background.blit(dice0, (200,435))
elif(d[0] == 4):
        dice0 = pygame.image.load("dice_4.png").convert()
        background.blit(dice0, (200,435))
elif(d[0] == 5):
        dice0 = pygame.image.load("dice_5.png").convert()
        background.blit(dice0, (200,435))
elif(d[0] == 6):
        dice0 = pygame.image.load("dice_6.png").convert()
        background.blit(dice0, (200,435))
if(d[1] == 1):
        dice1 = pygame.image.load("dice_1.png").convert()
        background.blit(dice1, (215,300))
elif(d[1] == 2):
        dice1 = pygame.image.load("dice_2.png").convert()
        background.blit(dice1, (215,300))
elif(d[1] == 3):
        dice1 = pygame.image.load("dice_3.png").convert()
        background.blit(dice1, (215,300))
elif(d[1] == 4):
        dice1 = pygame.image.load("dice_4.png").convert()
        background.blit(dice1, (215,300))
elif(d[1] == 5):
        dice1 = pygame.image.load("dice_5.png").convert()
        background.blit(dice1, (215,300))
elif(d[1] == 6):
        dice1 = pygame.image.load("dice_6.png").convert()
        background.blit(dice1, (215,300))
if(d[2] == 1):
        dice2 = pygame.image.load("dice_1.png").convert()
        background.blit(dice2, (285,275))
elif(d[2] == 2):
        dice2 = pygame.image.load("dice_2.png").convert()
        background.blit(dice2, (285,275))
elif(d[2] == 3):
        dice2 = pygame.image.load("dice_3.png").convert()
        background.blit(dice2, (285,275))
elif(d[2] == 4):
        dice2 = pygame.image.load("dice_4.png").convert()
        background.blit(dice2, (285,275))
elif(d[2] == 5):
        dice2 = pygame.image.load("dice_5.png").convert()
        background.blit(dice2, (285,275))
elif(d[2] == 6):
        dice2 = pygame.image.load("dice_6.png").convert()
        background.blit(dice2, (285,275))
if(d[3] == 1):
        dice3 = pygame.image.load("dice_1.png").convert()
        background.blit(dice3, (400,350))
elif(d[3] == 2):
        dice3 = pygame.image.load("dice_2.png").convert()
        background.blit(dice3, (400,350))
elif(d[3] == 3):
        dice3 = pygame.image.load("dice_3.png").convert()
        background.blit(dice3, (400,350))
elif(d[3] == 4):
         dice3 = pygame.image.load("dice_4.png").convert()
         background.blit(dice3, (400,350))
elif(d[3] == 5):
        dice3 = pygame.image.load("dice_5.png").convert()
        background.blit(dice3, (400,350))
elif(d[3] == 6):
        dice3 = pygame.image.load("dice_6.png").convert()
        background.blit(dice3, (400,350))
if(d[4] == 1):
        dice4 = pygame.image.load("dice_1.png").convert()
        background.blit(dice4, (465,375))
elif(d[4] == 2):
        dice4 = pygame.image.load("dice_2.png").convert()
        background.blit(dice4, (465,375))
elif(d[4] == 3):
        dice4 = pygame.image.load("dice_3.png").convert()
        background.blit(dice4, (465,375))
elif(d[4] == 4):
        dice4 = pygame.image.load("dice_4.png").convert()
        background.blit(dice4, (465,375))
        pygame.display.update()
elif(d[4] == 5):
        dice4 = pygame.image.load("dice_5.png").convert()
        background.blit(dice4, (465,375))
elif(d[4] == 6):
        dice4 = pygame.image.load("dice_6.png").convert()
        background.blit(dice4, (465,375))

pygame.display.update() #updating screen to show all the dice

count = 0
continuer = True
while continuer is not False:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     pygame.quit()
                if(count == 3):
                        value = results(d[0], d[1], d[2], d[3], d[4])
                        d[0] = roll() # dice roll for the computer
                        d[1] = roll()
                        d[2] = roll()
                        d[3] = roll()
                        d[4] = roll()
                        pc = results(d[0],d[1],d[2],d[3],d[4])
                        if(d[0] == 1):
                                r1 = pygame.image.load("red_1.png").convert()
                                background.blit(r1, (500,150))
                        if(d[0] == 2):
                                r1 = pygame.image.load("red_2.png").convert()
                                background.blit(r1, (500,150))
                        if(d[0] == 3):
                                r1 = pygame.image.load("red_3.png").convert()
                                background.blit(r1, (500,150))
                        if(d[0] == 4):
                                r1 = pygame.image.load("red_4.png").convert()
                                background.blit(r1, (500,150))
                        if(d[0] == 5):
                                r1 = pygame.image.load("red_5.png").convert()
                                background.blit(r1, (500,150))
                        if(d[0] == 6):
                                r1 = pygame.image.load("red_6.png").convert()
                                background.blit(r1, (500,150))
                        if(d[1] == 1):
                                r2 = pygame.image.load("red_1.png").convert()
                                background.blit(r2, (170,75))
                        if(d[1] == 2):
                                r2 = pygame.image.load("red_2.png").convert()
                                background.blit(r2, (170,75))
                        if(d[1]== 3):
                                r2 = pygame.image.load("red_3.png").convert()
                                background.blit(r2, (170,75))
                        if(d[1] == 4):
                                 r2 = pygame.image.load("red_4.png").convert()
                                 background.blit(r2, (170,75))
                        if(d[1] == 5):
                                r2 = pygame.image.load("red_5.png").convert()
                                background.blit(r2, (170,75))
                        if(d[1] == 6):
                                r2 = pygame.image.load("red_6.png").convert()
                                background.blit(r2, (170,75))
                        if(d[2] == 1):
                               r3 = pygame.image.load("red_1.png").convert()
                               background.blit(r3, (215,135))
                        if(d[2] == 2):
                                r3 = pygame.image.load("red_2.png").convert()
                                background.blit(r3, (215,135))
                        if(d[2] == 3):
                                r3 = pygame.image.load("red_3.png").convert()
                                background.blit(r3, (215,135))
                        if(d[2] == 4):
                                r3 = pygame.image.load("red_4.png").convert()
                                background.blit(r3, (215,135))
                        if(d[2] == 5):
                                r3= pygame.image.load("red_5.png").convert()
                                background.blit(r3, (215,135))
                        if(d[2] == 6):
                               r3 = pygame.image.load("red_6.png").convert()
                               background.blit(r3, (215,135))
                        if(d[3] == 1):
                                r4 = pygame.image.load("red_1.png").convert()
                                background.blit(r4, (300,200))
                        if(d[3] == 2):
                               r4 = pygame.image.load("red_2.png").convert()
                               background.blit(r4, (300,200))
                        if(d[3] == 3):
                                r4= pygame.image.load("red_3.png").convert()
                                background.blit(r4, (300,200))
                        if(d[3] == 4):
                                r4 = pygame.image.load("red_4.png").convert()
                                background.blit(r4, (300,200))
                        if(d[3] == 5):
                                r4 = pygame.image.load("red_5.png").convert()
                                background.blit(r4, (300,200))
                        if(d[3] == 6):
                                r4 = pygame.image.load("red_6.png").convert()
                                background.blit(r4, (300,200))
                        if(d[4] == 1):
                                r5 = pygame.image.load("red_1.png").convert()
                                background.blit(r5, (525,225))
                        if(d[4] == 2):
                                r5= pygame.image.load("red_2.png").convert()
                                background.blit(r5, (525,225))
                        if(d[4] == 3):
                                r5= pygame.image.load("red_3.png").convert()
                                background.blit(r5, (525,225))
                        if(d[4] == 4):
                                r5 = pygame.image.load("red_4.png").convert()
                                background.blit(r5, (525,225))
                        if(d[4] == 5):
                                r5 = pygame.image.load("red_5.png").convert()
                                background.blit(r5, (525,225))
                        if(d[4] == 6):
                                r5 = pygame.image.load("red_6.png").convert()
                                background.blit(r5, (525,225))

                        continuer = False
                        if(value > pc):
                         print("VICTORY")
                         win = pygame.image.load("win.png")
                         background.blit(win, (400,300))
                         applause.play()

                        elif(value == pc):
                                print("DRAW")
                                draw = pygame.image.load("draw.png").convert()
                                background.blit(draw, (400,300))
                                cowboy.play()

                        else:
                                print("DEFEAT")
                                lost = pygame.image.load("lost.png").convert()
                                background.blit(lost, (400,300))
                                boo.play()


                if(event.type == KEYDOWN and event.key == K_ESCAPE):
                        pygame.quit()
                if(event.type == KEYDOWN):
                        if(event.key == K_q): #INPUT Q
                                woosh.play()
                                d[0] = roll()
                                count += 1
                                if(d[0] == 1):
                                        dice0 = pygame.image.load("dice_1.png").convert()
                                        background.blit(dice0, (200,435))
                                        pygame.display.update()
                                elif(d[0] == 2):
                                        dice0 = pygame.image.load("dice_2.png").convert()
                                        background.blit(dice0, (200,435))
                                        pygame.display.update()
                                elif(d[0] == 3):
                                        dice0 = pygame.image.load("dice_3.png").convert()
                                        background.blit(dice0, (200,435))
                                        pygame.display.update()
                                elif(d[0] == 4):
                                        dice0 = pygame.image.load("dice_4.png").convert()
                                        background.blit(dice0, (200,435))
                                        pygame.display.update()
                                elif(d[0] == 5):
                                        dice0 = pygame.image.load("dice_5.png").convert()
                                        background.blit(dice0, (200,435))
                                        pygame.display.update()
                                elif(d[0] == 6):
                                        dice0 = pygame.image.load("dice_6.png").convert()
                                        background.blit(dice0, (200,435))
                                        pygame.display.update()
                        elif(event.key == K_w): #INPUT W
                            woosh.play()
                            d[1] = roll()
                            count += 1
                            if(d[1] == 1):
                                dice1 = pygame.image.load("dice_1.png").convert()
                                background.blit(dice1, (215,300))
                                pygame.display.update()
                            elif(d[1] == 2):
                                dice1 = pygame.image.load("dice_2.png").convert()
                                background.blit(dice1, (215,300))
                                pygame.display.update()
                            elif(d[1] == 3):
                                dice1 = pygame.image.load("dice_3.png").convert()
                                background.blit(dice1, (215,300))
                                pygame.display.update()
                            elif(d[1] == 4):
                                dice1 = pygame.image.load("dice_4.png").convert()
                                background.blit(dice1, (215,300))
                                pygame.display.update()
                            elif(d[1] == 5):
                                dice1 = pygame.image.load("dice_5.png").convert()
                                background.blit(dice1, (215,300))
                                pygame.display.update()
                            elif(d[1] == 6):
                                dice1 = pygame.image.load("dice_6.png").convert()
                                background.blit(dice1, (215,300))
                                pygame.display.update()
                        elif(event.key == K_e): #INPUT E
                            woosh.play()
                            d[2] = roll()
                            count += 1
                            if(d[2] == 1):
                                dice2 = pygame.image.load("dice_1.png").convert()
                                background.blit(dice2, (285,275))
                                pygame.display.update()
                            elif(d[2] == 2):
                                dice2 = pygame.image.load("dice_2.png").convert()
                                background.blit(dice2, (285,275))
                                pygame.display.update()
                            elif(d[2] == 3):
                                dice2 = pygame.image.load("dice_3.png").convert()
                                background.blit(dice2, (285,275))
                                pygame.display.update()
                            elif(d[2] == 4):
                                dice2 = pygame.image.load("dice_4.png").convert()
                                background.blit(dice2, (285,275))
                                pygame.display.update()
                            elif(d[2] == 5):
                                dice2 = pygame.image.load("dice_5.png").convert()
                                background.blit(dice2, (285,275))
                                pygame.display.update()
                            elif(d[2] == 6):
                                dice2 = pygame.image.load("dice_6.png").convert()
                                background.blit(dice2, (285,275))
                                pygame.display.update()
                        elif(event.key == K_r): #INPUT R
                            woosh.play()
                            d[3] = roll()
                            count += 1
                            if(d[3] == 1):
                                dice3 = pygame.image.load("dice_1.png").convert()
                                background.blit(dice3, (400,350))
                                pygame.display.update()
                            elif(d[3] == 2):
                                dice3 = pygame.image.load("dice_2.png").convert()
                                background.blit(dice3, (400,350))
                                pygame.display.update()
                            elif(d[3] == 3):
                                dice3 = pygame.image.load("dice_3.png").convert()
                                background.blit(dice3, (400,350))
                                pygame.display.update()
                            elif(d[3] == 4):
                                dice3 = pygame.image.load("dice_4.png").convert()
                                background.blit(dice3, (400,350))
                                pygame.display.update()
                            elif(d[3] == 5):
                                dice3 = pygame.image.load("dice_5.png").convert()
                                background.blit(dice3, (400,350))
                                pygame.display.update()
                            elif(d[3] == 6):
                                dice3 = pygame.image.load("dice_6.png").convert()
                                background.blit(dice3, (400,350))
                                pygame.display.update()
                        elif(event.key == K_t): #INPUT T
                            woosh.play()
                            d[4] = roll()
                            count += 1
                            if(d[4] == 1):
                                dice4 = pygame.image.load("dice_1.png").convert()
                                background.blit(dice4, (465,375))
                                pygame.display.update()
                            elif(d[4] == 2):
                                dice4 = pygame.image.load("dice_2.png").convert()
                                background.blit(dice4, (465,375))
                                pygame.display.update()
                            elif(d[4] == 3):
                                dice4 = pygame.image.load("dice_3.png").convert()
                                background.blit(dice4, (465,375))
                                pygame.display.update()
                            elif(d[4] == 4):
                                dice4 = pygame.image.load("dice_4.png").convert()
                                background.blit(dice4, (465,375))
                                pygame.display.update()
                            elif(d[4] == 5):
                                dice4 = pygame.image.load("dice_5.png").convert()
                                background.blit(dice4, (465,375))
                                pygame.display.update()
                            elif(d[4] == 6):
                                dice4 = pygame.image.load("dice_6.png").convert()
                                background.blit(dice4, (465,375))
                                pygame.display.update()
                        else:
                            count += 1
                            print("NOT EXPECTING THIS KEY")
                            continue
        window.blit(background, (0,0))
        pygame.display.flip()

go = True
while go:
        for event in pygame.event.get():
                if(event.type == KEYDOWN or event.type == pygame.QUIT):
                        pygame.quit()






        window.blit(background, (0,0))
        pygame.display.flip()


