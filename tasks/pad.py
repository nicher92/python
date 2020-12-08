import numpy as np

def pad(input_list):
    """
    Given a input list of nested list of integers:

    input_list = [[1,2,3], [1,2,3,4,5], [1,2], [1,2,3,4,5,6,7,8]]

    return a matrix where
    
    1) matrix[i][:len(input_list[i])] == input_list[i]
    and
    #padding
    2) matrix[i][len(input_list[i]):] == [0,0, ..., 0]

    """
    
    maxlength = len(max(input_list, key=len))
    matrix =[]
    for item in input_list:
        extra_zeroes = maxlength - len(item)
        matrix.append(list(np.pad(item, (0, extra_zeroes), 'constant')))
    
    
    return(np.array(matrix))






input_list = [[1,2,3], [1,2,3,4,5], [1,2], [1,2,3,4,5,6,7,8]]
print(pad(input_list))
