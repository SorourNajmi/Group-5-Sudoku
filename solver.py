import sys
from os import system
from colorama import Fore, Back ,Style
clear = lambda :system("cls")


sys.setrecursionlimit(1000)

def create_boxes() -> list:
        
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
                return False
        return True

def check_column(column_index: int, list9x9: list, number: int) -> bool:

        for i in range(9):
            if list9x9[i][column_index] == number:
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
                return False
        return True

def find_empty(game):
    cords = []
    for Y , i in enumerate(game):
        for X , j in enumerate(i):
            if j == "#":
                cords.append((Y,X))

    return cords

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


def solve(game):
     
    zero = find_empty(game)
    if len(zero) == 0:
        return True  
      
    row = zero[0][0]
    col = zero[0][1]

    for i in range(1,10):
            
        if check_box(row ,col ,game ,str(i)) and check_column(col ,game ,str(i)) and check_row(row ,game ,str(i)):
                 
            game[row][col] = str(i)

            if solve(game):
                 return True
            
            game[row][col] = "#"

    return False


lst = [['5','#','#','#','2','7','#','#','1'],['8','#','#','#','#','#','#','7','5'],['6','#','2','#','3','#','9','4','#'],['1','5','#','4','9','#','#','#','3'],['#','8','#','7','#','#','#','#','9'],['#','#','#','2','1','8','#','#','#'],['4','#','#','9','#','2','#','#','7'],['9','2','8','3','#','#','#','1','6'],['#','6','3','1','8','5','#','#','#']]
   

  
solve(lst)
for i in lst:
     for j in i:
          if j == "#":
               print("unsolvable")
               exit()
show(lst)

          


