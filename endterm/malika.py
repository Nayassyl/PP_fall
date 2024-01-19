def ref_form(sample_matrix):
    row_num = len(sample_matrix)
    col_num = len(sample_matrix[0])
    cnt_row = 0
    cnt_col = 0

    while cnt_row < row_num and cnt_col < col_num:
        key_row = cnt_row
        while key_row < row_num and sample_matrix[key_row][cnt_col] == 0:
            key_row += 1
        if key_row == row_num:
            cnt_col += 1
        else:
            temp_row = sample_matrix[cnt_row]
            sample_matrix[cnt_row] = sample_matrix[key_row]
            sample_matrix[key_row] = temp_row

            key_value = sample_matrix[cnt_row][cnt_col]
            new_row = []
            for elem in sample_matrix[cnt_row]:
                new_value = elem / key_value
                new_row.append(new_value)
            sample_matrix[cnt_row] = new_row

            for n in range(row_num):
                if n != cnt_row:
                    factor = sample_matrix[n][cnt_col]
                    new_row = []
                    for elem_index, elem in enumerate(sample_matrix[n]):
                        new_value = elem - factor * sample_matrix[cnt_row][elem_index]
                        new_row.append(new_value)

                    sample_matrix[n] = new_row


            cnt_row += 1
            cnt_col += 1

    return sample_matrix

def rref(sample_matrix):
    row_num = len(sample_matrix)
    col_num = len(sample_matrix[0])
    cnt_row, cnt_col = 0, 0

    while cnt_row < row_num and cnt_col < col_num:
        key_row = cnt_row
        while key_row < row_num and sample_matrix[key_row][cnt_col] == 0:
            key_row += 1

        if key_row == row_num:
            cnt_col += 1
        else:
            temp_row = sample_matrix[cnt_row]
            sample_matrix[cnt_row] = sample_matrix[key_row]
            sample_matrix[key_row] = temp_row

            key_value = sample_matrix[cnt_row][cnt_col]
            sample_matrix[cnt_row] = [elem / key_value for elem in sample_matrix[cnt_row]]
            for n in range(row_num):
                if n != cnt_row:
                    factor = sample_matrix[n][cnt_col]
                    new_row = []
                    for elem_index, elem in enumerate(sample_matrix[n]):
                        new_value = elem - factor * sample_matrix[cnt_row][elem_index]
                        new_row.append(new_value)

                    sample_matrix[n] = new_row
            for i in range(cnt_row):
                factor = sample_matrix[i][cnt_col]
                new_row = []
                for elem_index, elem in enumerate(sample_matrix[i]):
                    new_value = elem - factor * sample_matrix[cnt_row][elem_index]
                    new_row.append(new_value)

                sample_matrix[i] = new_row

            cnt_row += 1
            cnt_col += 1

    return sample_matrix