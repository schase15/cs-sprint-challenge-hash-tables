'''
Understand:
    Go through up to 10 lists, return any numbers that exist in all of the lists
    The lists can contain up to 1,000,000 elements
    Input is a list of lists

Plan:
    Put the first list in a dictionary
    Go through the next list, if the key is already in the first dictionary, add it to a third new dictionary
    If it is not there, do nothing
        This will move all the repeated keys to a new dictionary 
            New dictionary includes only the values that appear in both lists
    Repeat with each list
    Return the keys of the finalized dictionary in list form

    Maybe do recursively - add recursive loop inside the function
'''

'PASSES ALL TESTS'


def intersection(arrays):

    # Put the first list in a dictionary
    first_d = {}

    for item in arrays[0]:
        first_d[item] = 0

    ## Recursion
    # loop that will take in a dictionary, compare the next list to it, 
    # populate a new dictionary when keys matched, pass that dictionary to the next call
    # Continue until there is no next list

    def dict_build(temp_dict, count):
        # Save count
        count = count

        # Count how many lists it has processed, end when the count surpasses the length of the input list
        while count < len(arrays): 
            # Take in the temp_dict, compare the next list to 
            d = temp_dict

            # Grab the next list
            compare_list = arrays[count]

            # Create an empty new dict
            new_dict = {}

            # If the value in the compare list is in d, save it in a new dict
            for value in compare_list:
                if value in d:
                    new_dict[value] = 0
            
            # Increase count by 1
            count += 1

            # Pass the new_dict and the updated count to the recursive call
            return dict_build(new_dict, count)

        # After all of the inner lists have go through the call
        # Return the last dictaionary to be passed through
        return temp_dict


    # Call the recursive function using the first dictionary and count=1
    final_dict = dict_build(first_d, 1)

    # Return the keys of the final dict in list form
    values_in_all = list(final_dict.keys())

    return values_in_all


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
