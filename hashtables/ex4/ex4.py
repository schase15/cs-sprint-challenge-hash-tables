'''
Plan:
    Sort the input list into two lists, negative and positive
    Put the negatives into a dictionary
    Check if the negative of the positive values -[1] exists in the dictionary
        If it does, save it to an output list
'''

'PASSES ALL TESTS'

def has_negatives(a):

    # Sort the input list 
    pos = []
    neg = []

    for value in a:
        if value >= 0:
            pos.append(value)
        else:
            neg.append(value)

    d = {}

    # Put the negatives into a dictionary
    for value in neg:
        d[value] = 0
    
    output_arr = []

    # Check to see if the positives of the negative values are in the dictionary
    for value in pos:
        if (value * -1) in d:
            output_arr.append(value)

    return output_arr


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
