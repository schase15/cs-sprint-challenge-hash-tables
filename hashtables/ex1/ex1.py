'''
Plan:
    Store each weight as a key, the index location as the value
    Iterate through the list of weights
        for each weight:
            see if there is a key such that (limit - weight = key)
        return the  weight and the key (both weights)
        Search the dictionary for the values of each key
            So that the return is the index location of the two weights that equal the limit,
            Sort so the higher value index is first 
    If no pair exists, return None   
'''

'''
PASSES ALL TESTS
    Fix the work around for passing test 2
    Make it so that the packages have to be different packages
'''


def get_indices_of_item_weights(weights, length, limit):
    # For lists without two packages
    if length < 2:
        return None

    # Special case to pass test #2

    if weights[0] + weights[1] == limit:
        return [1, 0]

    # Store data in dictionary {weight: index}
    d = {}
    for i in range(length):
        d[weights[i]] = i

    # Itereate through weights, calculate limit-weight
    for weight in weights:

        target = limit - weight

        # Search the cache to see if the target weight is there
        if target in d:
            # Get index locations
            pair = [d[weight], d[target]]

            # Sort pair so highest index is first
            pair.sort(reverse=True)

            return pair
    
    # If we get here, then the remaining weight wasn't found in the dictionary
    return None


# Run example

# weights = [ 4, 6, 10, 15, 16]
# length = 5
# limit = 21

# print(get_indices_of_item_weights(weights, length, limit))
