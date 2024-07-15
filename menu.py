from os import system
import random
from colorama import Fore, Back ,Style

clear = lambda :system("cls")


def level_selection():
    print("please choose game's dificalty")
    print("press 'E' for easy game")
    print("press 'M' for medium game")
    print("press 'H' for hard game")
    inp = input().upper()
    rnd = random.randint(1,3)

    E1 = [['5','#','#','#','2','7','#','#','1'],['8','#','#','#','#','#','#','7','5'],['6','#','2','#','3','#','9','4','#'],['1','5','#','4','9','#','#','#','3'],['#','8','#','7','#','#','#','#','9'],['#','#','#','2','1','8','#','#','#'],['4','#','#','9','#','2','#','#','7'],['9','2','8','3','#','#','#','1','6'],['#','6','3','1','8','5','#','#','#']]
    E2 = [['#','2','#','#','#','9','5','#','#'],['9','#','#','7','#','#','3','2','#'],['6','#','#','4','5','#','1','#','#'],['8','#','1','5','#','#','#','6','2'],['3','4','#','6','#','#','#','1','#'],['2','5','6','1','#','#','4','3','#'],['1','#','#','#','#','4','#','#','8'],['#','#','4','8','3','5','2','#','#'],['5','#','8','#','#','#','7','4','#']]
    E3 = [[],[],[],[],[],[],[],[],[]]

    M1 = [[],[],[],[],[],[],[],[],[]]
    M2 = [[],[],[],[],[],[],[],[],[]]
    M3 = [[],[],[],[],[],[],[],[],[]]

    H1 = [[],[],[],[],[],[],[],[],[]]
    H2 = [[],[],[],[],[],[],[],[],[]]
    H3 = [[],[],[],[],[],[],[],[],[]]

    if inp == "E":
        return random.choice([E1,E2,E3])
    elif inp == "M":
        return random.choice([M1,M2,M3])
    elif inp == "H":
        return random.choice([H1,H2,H3])
    

def show(n):
    print(Fore.YELLOW + " 1  2  3   4  5  6   7  8  9 \n" , end="")
    print(Style.RESET_ALL , end="")
    for cnt , i in enumerate(n):
        if cnt % 3 == 0 and cnt != 0:
            print()
        print()
        for cnt2 , j in enumerate(i):
            if (cnt2 ) % 3 == 0:
                print(" ",end="")
            print(j , end="  " )
        print(Fore.YELLOW + f"  {cnt+1}" , end="")
        print(Style.RESET_ALL , end="")







# while True:
#         print("welcome to sodoko game")
#         print("press 'S' to start a new game ")
#         print("press 'R' to see rules")
#         print("press 'Q' to exit")

#         inp = input()

#         if inp.upper() == "S":
#             level_selection()
#             clear()
#         if inp.upper() == "R":
#             print()
#         if inp.upper() == "Q": 
#             break
#         input("press any key to continue")
#         clear()

E1 = [['#','2','#','#','#','9','5','#','#'],['9','#','#','7','#','#','3','2','#'],['6','#','#','4','5','#','1','#','#'],['8','#','1','5','#','#','#','6','2'],['3','4','#','6','#','#','#','1','#'],['2','5','6','1','#','#','4','3','#'],['1','#','#','#','#','4','#','#','8'],['#','#','4','8','3','5','2','#','#'],['5','#','8','#','#','#','7','4','#']]
show(E1)