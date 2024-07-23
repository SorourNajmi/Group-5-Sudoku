from copy import deepcopy
from os import system
import random
from colorama import Fore, Back ,Style
clear = lambda :system("cls")


E1 = [['5','#','#','#','2','7','#','#','1'],['8','#','#','#','#','#','#','7','5'],['6','#','2','#','3','#','9','4','#'],['1','5','#','4','9','#','#','#','3'],['#','8','#','7','#','#','#','#','9'],['#','#','#','2','1','8','#','#','#'],['4','#','#','9','#','2','#','#','7'],['9','2','8','3','#','#','#','1','6'],['#','6','3','1','8','5','#','#','#']]
E2 = [['8','7','1','#','#','2','#','4','#'],['#','#','#','8','1','5','#','#','6'],['#','5','#','#','4','3','#','#','1'],['1','#','#','6','5','8','#','7','9'],['7','6','#','#','#','#','5','#','#'],['#','9','8','#','4','3','#','6','#'],['#','#','7','#','8','#','#','#','3'],['9','1','5','#','#','#','#','#','#'],['#','8','3','1','7','#','2','#','#']]
E3 = [['#','#','2','3','#','#','#','#','4'],['#','8','#','#','6','9','#','#','#'],['4','5','9','2','#','7','1','6','#'],['1','4','5','#','9','2','#','3','8'],['6','7','#','#','1','#','#','4','#'],['2','#','#','#','#','#','6','5','1'],['#','1','7','#','#','6','3','#','#'],['#','#','#','#','#','#','#','7','5'],['8','#','4','5','#','#','#','1','#']]

M1 = [['4','#','#','#','#','#','1','#','#'],['#','6','8','7','3','#','#','#','#'],['#','#','#','#','4','6','#','7','#'],['6','#','9','#','#','#','5','8','#'],['#','#','#','3','#','#','#','6','#'],['#','4','1','#','#','5','7','#','#'],['7','#','6','1','5','3','#','2','4'],['#','#','#','8','#','#','#','1','9'],['8','1','2','#','6','9','#','5','7']]
M2 = [['6','#','#','3','8','#','#','#','2'],['#','#','3','#','#','#','#','4','9'],['8','#','2','#','5','#','#','#','#'],['#','#','6','#','4','5','#','#','3'],['1','#','#','#','7','#','#','#','4'],['#','4','#','2','9','#','#','#','5'],['#','#','5','8','#','#','9','6','1'],['#','#','#','#','3','#','#','#','#'],['#','#','9','#','#','7','3','#','#']]
M3 = [['#','8','#','4','7','#','1','#','2'],['2','#','#','5','3','8','#','#','#'],['#','#','#','#','#','#','#','9','#'],['1','#','7','2','#','4','6','8','#'],['#','#','#','6','8','#','#','#','#'],['#','6','#','9','#','3','4','2','#'],['9','#','6','3','#','5','8','7','1'],['#','5','1','7','#','6','#','#','#'],['4','#','#','8','9','#','2','#','#']]

H1 = [['#','#','#','4','2','#','#','#','8'],['#','#','7','#','#','5','#','#','#'],['2','5','4','6','#','#','#','1','#'],['#','6','#','5','9','#','3','7','4'],['5','#','8','#','#','#','#','2','9'],['#','7','#','1','#','#','#','#','#'],['#','#','#','#','7','#','#','#','6'],['#','#','#','3','#','#','#','8','1'],['#','#','1','#','#','6','#','4','#']]
H2 = [['9','#','2','3','#','#','8','#','1'],['#','1','5','#','#','#','3','#','#'],['4','#','7','#','#','#','#','5','6'],['#','#','8','#','#','7','1','#','2'],['#','#','#','#','2','6','5','9','#'],['#','#','#','5','8','#','#','#','4'],['#','#','#','#','#','#','#','#','#'],['#','2','#','6','#','#','#','#','5'],['#','7','9','2','#','5','#','#','#']]
H3 = [['#','#','2','#','#','1','#','#','8'],['#','#','#','7','#','6','#','2','9'],['3','#','#','#','#','2','5','6','#'],['#','#','#','#','#','5','8','#','#'],['2','#','8','#','#','#','#','4','#'],['7','5','#','#','#','8','#','#','#'],['5','3','#','6','#','7','9','#','#'],['#','2','7','5','#','#','6','#','#'],['6','4','#','#','#','#','#','#','#']]


def level_selection() -> list:
    print("please choose game's dificalty")
    print("press 'E' for easy game")
    print("press 'M' for medium game")
    print("press 'H' for hard game")
    

    while True:
        inp = input().upper()
        if inp == "E":
            game = random.choice([E1,E2,E3])
            break
        elif inp == "M":
            game = random.choice([M1,M2,M3])
            break
        elif inp == "H":
            game = random.choice([H1,H2,H3])
            break

    unchangable_list = []
    for Y , i in enumerate(game):
        for X , j in enumerate(i):
            if j != "#":
                unchangable_list.append([Y,X])

    return game , unchangable_list
    


def create_boxes() -> list:
        """ for storing tupels of indexes of cells in each box of a Sudoku table """
        boxes = list()
        index_ranges = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
        for i in range(3):
            row_indexs_range = index_ranges[i]
            for j in range(3):
                box = []
                column_indexes_range = index_ranges[j]
                for x in row_indexs_range:
                    for y in column_indexes_range:                        
                        box.append((x, y))
                boxes.append(box)
        return boxes


def check_row(row_index: int, list9x9: list, number: int) -> bool:

        for i in range(9):
            if list9x9[row_index][i] == number:
                print(Fore.RED + "conflict in row" , end="")
                print(Style.RESET_ALL )
                return False
        return True

def check_column(column_index: int, list9x9: list, number: int) -> bool:

        for i in range(9):
            if list9x9[i][column_index] == number:
                print(Fore.RED + "conflict in column" , end="")
                print(Style.RESET_ALL )
                return False
        return True


def check_box(row_index: int, column_index: int, list9x9: list, number: int) -> bool:
        
        boxes = create_boxes()

        for i in boxes:
            for j in i:
                if j == (row_index,column_index):
                    box = i
        for i in box:
            if list9x9[i[0]][i[1]] == number:
                print(Fore.RED + "conflict in box" , end="")
                print(Style.RESET_ALL )
                return False
        return True


def add(number, list9x9, row_index, column_index):

                
    if list9x9[row_index][column_index] == "#":
        list_temp = deepcopy(list9x9)
        
        check_b = check_box(row_index, column_index, list9x9, number)
        check_r = check_column(column_index, list9x9, number)
        check_c = check_row(row_index, list9x9, number)
        bg = check_box(row_index, column_index, list9x9, str(number) + "G")
        rg = check_column(column_index, list9x9, str(number) + "G")
        cg = check_row(row_index, list9x9, str(number) + "G")


        if check_b and check_r and check_c and bg and cg and rg:
            list9x9[row_index][column_index] = number + "G"
            show(list9x9)
        else:
            list_temp[row_index][column_index] = number + "R"
            show(list_temp)

    else:
        print(Fore.YELLOW + "This cell is already filled" , end="")
        print(Style.RESET_ALL )
    
    return list9x9


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
            if len(j) == 2:
                if j[1] == "R":
                    print(Fore.RED + f"{j[0]}  " , end="")
                    print(Style.RESET_ALL , end="")
                    continue
                elif j[1] == "G":
                    print(Fore.GREEN + f"{j[0]}  " , end="")
                    print(Style.RESET_ALL , end="")
                    continue
            print(j , end="  ")
        print(Fore.YELLOW + f"  {cnt+1}" , end="")
        print(Style.RESET_ALL , end="")
    print("\n")


def delete(list_9x9 , unchangable_list, X , Y):
    for i in unchangable_list:
        if Y == i[0] and X == i[1]:
            print("you can not change this cell")
            return list_9x9
    list_9x9[Y][X] = "#"
    return list_9x9


    
def win_check(n):
    for i in n:
        for j in i:
            if j.isnumeric():
                pass
            else:
                return False
    return True





def start_game(list_9x9 , unchangable_list):

    base_game = deepcopy(list_9x9)

    while True:

        clear()
        show(list_9x9)
        print("\n\npress 'D' to delete a cell")
        print("press 'A' to add a cell")
        print("press 'R' to reset the game")
        inp = input().upper()
        
        if  inp == "D":
            while True:
                Y = input("please enter row number: ") 
                X = input("please enter column number: ")
                numb = input("please enter a number: ")
                if X.isnumeric() and Y.isnumeric() and numb.isnumeric():
                    Y = int(Y) - 1
                    X = int(X) - 1
                    numb = int(numb)
                    if 0 <= X < 9 and 0 <= Y < 9 and 0 < numb < 10:
                        break
                    else:
                        print("enter row , column and number correctly")
                else:
                    print("row , column and number must be integers")
            list_9x9 = delete(list_9x9 , unchangable_list , X , Y)
            print(Fore.MAGENTA + "press any key to continue" , end="")
            print(Style.RESET_ALL , end="")
            input()
        elif inp == "A":
            while True:
                Y = input("please enter row number: ") 
                X = input("please enter column number: ")
                numb = input("please enter a number: ")
                if X.isnumeric() and Y.isnumeric() and numb.isnumeric():
                    Y = int(Y) - 1
                    X = int(X) - 1
                    if 0 <= X < 9 and 0 <= Y < 9 and 0 < int(numb) < 10:
                        break
                    else:
                        print("enter row , column and number correctly")
                else:
                    print("row , column and number must be integers")
            
            list_9x9 = add(numb ,list_9x9 ,Y,X)
            
            print(Fore.MAGENTA + "press any key to continue" , end="")
            print(Style.RESET_ALL , end="")
            input()
            clear()

            
        elif inp == "R":
            list_9x9 = base_game

        if win_check(list_9x9):
            clear()
            print("!!!!!!!You won!!!!!!!")
            break
           
#=========================================================== menu asli ===========================================================

while True:
        print("welcome to sodoko game")
        print("press 'S' to start a new game ")
        print("press 'R' to see rules")
        print("press 'Q' to exit")

        inp = input()

        if inp.upper() == "S":
            game , unchangable_list = level_selection()
            start_game(game , unchangable_list)
            clear()
        if inp.upper() == "R":
            print("There is'nt any rule")
        if inp.upper() == "Q": 
            clear()
            exit()
        input("press any key to continue")
        clear()