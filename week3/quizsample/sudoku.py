sorted_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def is_true_block(block):
    elems = []
    for row in block:
        for elem in row:
            elems.append(elem)
    if sorted(elems) != sorted_row:
        return False
    return True
                
def is_true(sudoku):
    for i in sudoku:
        if sorted(i) != sorted_row:
            return False
    for i in range(9):
        column = []
        for j in sudoku:
            column.append(j[i])
        if sorted_row != sorted(column):
            return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [row[j:j+3] for row in b[i:i+3]]
            return is_true_block(block)

b = [[int(i) for i in input().split()] for j in range(9)]
print(is_true(b))