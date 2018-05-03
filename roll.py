import random
def roll():
    number = random.randint(1, 6)
    return number

def roll5():
    d0 = random.randint(1, 6)
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6)
    d4 = random.randint(1, 6)
    print(d0, d1, d2, d3, d4)
    return {'d0':d0, 'd1':d1 ,'d2':d2 ,"d3":d3 ,"d4":d4 }

