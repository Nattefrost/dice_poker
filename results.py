#   Module handling the results, looking for dice combinations
#   ESCANDE DAMIEN
#   FEBRUARY THE 4th 2014
import pygame
from pygame.locals import *


def results(d0,d1,d2,d3,d4):
    d = [d0,d1,d2,d3,d4]
    occ1 = d.count(1);
    print("How many 1 : ", occ1)
    occ2 = d.count(2)
    print("How many 2 : ", occ2)
    occ3 = d.count(3)
    print("How many 3 : ", occ3)
    occ4 = d.count(4)
    print("How many 4 : ", occ4)
    occ5 = d.count(5)
    print("How many 5 : ", occ5)
    occ6 = d.count(6)
    print("How many 6 : ", occ6)
    print(d)
    
    if( d0 == d1 == d2 == d3 ==d4):
        print("FIVE OF A KIND")
        value = 8
    elif(occ1== 4 or occ2== 4 or occ3== 4 or occ4== 4 or occ5== 4 or occ6== 4):
        print("FOUR OF A KIND")
        value = 7
    elif(occ1== 3 or occ2== 3 or occ3== 3 or occ4== 3 or occ5== 3 or occ6== 3) and (occ1== 2 or occ2== 2  or occ3== 2 or occ4== 2 or occ5== 2 or occ6== 2):
        print("FULL HOUSE")
        value = 6
    elif(occ1 == 0 and occ2== 1 and occ3 == 1 and occ4 ==1 and occ5== 1 and occ6== 1):
        print("SIX HIGH STRAIGHT")
        value = 5
    elif(occ1 == 1 and occ2 == 1 and occ3 == 1 and occ4 == 1 and occ5 == 1 and occ6 == 0):
        print("FIVE HIGH STRAIGHT")
        value = 4
    elif(occ1== 3 or occ2== 3 or occ3== 3 or occ4== 3 or occ5== 3 or occ6== 3):
        print("THREE OF A KIND")
        value = 3
    elif((occ1 == 2) and (occ2 == 2 or occ3 ==2 or occ4 ==2 or occ5 ==2 or occ6== 2)) or ((occ2 == 2) and (occ3== 2 or occ4 == 2 or occ5 ==2 or occ6== 2)) or ((occ3== 2) and (occ1== 2 or  occ2== 2 or occ4== 2 or occ5==2 or occ6==2)) or ((occ4== 2) and (occ1==2 or occ2== 2 or occ3== 2 or occ5== 2 or occ6== 2)):
         print("TWO PAIRS")
         value = 2
    elif(occ1== 2 or occ2== 2  or occ3== 2 or occ4== 2 or occ5== 2 or occ6== 2):
        print("A PAIR")
        value = 1
    else:
        print("NOTHING")
        value = 0
    return value
