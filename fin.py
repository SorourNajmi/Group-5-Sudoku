
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
    inp = input().upper()

    if inp == "E":
        game = random.choice([E1,E2,E3])
    elif inp == "M":
        game = random.choice([M1,M2,M3])
    elif inp == "H":
        game = random.choice([H1,H2,H3])

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


def add(number, list9x9, row_index, column_index):

    row_index = int(row_index)
    column_index = int(column_index)

    repeated_in_box = None
    repeated_in_row = None
    repeated_in_column = None
    
    
    def check_row(row_index: int, list9x9: list, number: int) -> bool:
        """ for checking for a repeated number in a row in the table and 
            assigning the tuple of indexes of that number to a local variable if any

        Args:
            row_index (int): a number according to user choice for row position
            list9x9 (list): the table of numbers 
            number (int): the number that must not be repeated

        Returns:
            bool: True if there is NO repeated number in the current row else False
        """
        nonlocal repeated_in_row
        for i, num in enumerate(list9x9[row_index]):
            if num == number:
                repeated_in_row = (row_index + 1, i + 1)
                return False
        return True
    
    def check_column(column_index: int, list9x9: list, number: int) -> bool:
        """ for checking for a repeated number in a column in the table and 
            assigning the tuple of indexes of that number to a local variable if any

        Args:
            column_index (int): a number according to user choice for column position
            list9x9 (list): the table of numbers 
            number (int): the number that must not be repeated

        Returns:
            bool: True if there is NO repeated number in the current column else False
        """
        nonlocal repeated_in_column
        for i, row in enumerate(list9x9):
            if row[column_index] == number:
                repeated_in_column = (i + 1, column_index + 1)
                return False
        return True

    def check_box(row_index: int, column_index: int, list9x9: list, number: int) -> bool:
        """ for checking for a repeated number in the corresponding box in the table and 
            assigning the tuple of indexes of that number to a local variable if any

        Args:
            row_index (int): a number according to user choice for row position
            column_index (int): a number according to user choice for column position
            list9x9 (list): the table of numbers _description_
            number (int): the number that must not be repeated
            
        Returns:
            bool: True if there is NO repeated number in the current box else False
        """
        nonlocal repeated_in_box
        boxes = create_boxes()
        current_cell = (row_index, column_index)
        for box in boxes:
            if current_cell in box:
                for cell in box:
                    row_index, column_index = cell[0], cell[1]
                    if number == list9x9[row_index][column_index]:
                        repeated_in_box = (row_index + 1, column_index + 1)
                        return False
                else:
                    return True
                
    if list9x9[row_index][column_index] == "#":
        list_temp = list9x9.copy()
        list_temp[row_index][column_index] = number
        
        check_b = check_box(row_index, column_index, list9x9, number)
        check_r = check_column(column_index, list9x9, number)
        check_c = check_row(row_index, list9x9, number)
        if check_b and check_r and check_c:
            list9x9[row_index][column_index] = number
        else:
            print("Mistake! number = {number}")
            if repeated_in_box:
                print(f"Repeat in the box: cell-row = {repeated_in_box[0]} cell-column = {repeated_in_box[1]}")
            if repeated_in_row:
                print(f"Repeat in the row: cell-row = {repeated_in_row[0]} cell-column = {repeated_in_row[1]}")
            if repeated_in_column:
                print(f"Repeat in the column: cell-row = {repeated_in_column[0]} cell-column = {repeated_in_column[1]}")
    else:
        print("Error! This cell is not empty.")



def reset(list_9x9 , unchangable_list):
    "به جز اون مقدارای ثایت بقیه رو پاک می کنه"
    list_9x9 = game 

    return "list_9x9_new"

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


def delete(list_9x9 , unchangable_list, X , Y):
    "list_9x9[x][y] = # اگه مختصات قابل تغییر نبود ارور بده اگه نبود به جای عددش # بزاره" 

    return "list_9x9_new"
    
def win_check():
    pass

# def add(number ,list_9x9 , X , Y):
#     "اگه خونه  ای که گفت خالی بود یعنی برابر # بود عدد داده شده رو ثبت کنه اگر نه خظا بده"
#     if list_9x9[X][Y] == "#":
#         list_temp = list_9x9.copy()
#         list_temp[X][Y] = number

#         "اگه هر سه نای این چک ها درست بودن اد کنه اگر نه ارور بده"
#         if check_box(list_temp) and check_column(list_temp) and check_raw(list_temp):
#             list_9x9[X][Y] = number
#         else:
#             "eror bede"
#     else:
#         "eror bede"



def start_game(list_9x9 , unchangable_list):
    while True:
        clear()
        show(list_9x9)
        print("\n\npress 'D' to delete a cell")
        print("press 'A' to add a cell")
        print("press 'R' to reset the game")
        inp = input().upper()
        
        if  inp == "D":
            pass
            # list_9x9 = delete(list_9x9 , unchangable_list , "X" , "Y")
        elif inp == "A":
            Y = input("please enter row number: ")
            X = input("please enter column number: ")
            numb = input("please enter a number")
            list_new = add(numb ,list_9x9 ,Y,X)
            
        elif inp == "R":
            pass
            # list_9x9 = reset(list_9x9 , unchangable_list)
        if win_check():
            pass
           
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
            print()
        if inp.upper() == "Q": 
            break
        input("press any key to continue")
        clear()