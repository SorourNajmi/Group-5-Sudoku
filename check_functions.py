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
                    if number == list9x9[row_index, column_index]:
                        repeated_in_box = (row_index + 1, column_index + 1)
                        return False
                else:
                    return True
                
    if list9x9[row_index, column_index] == "#":
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