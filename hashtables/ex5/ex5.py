'''
Plan:
    Split the paths on the backslashes
    Use the last item as the key, the entire path as the value

    Use the queries to search if the key exists
        If it does, return the corresponding value (the path) in an output array

    # There can be multiple different file paths that have the ending, 
    # we need to return them all, append to lists at each key
'''
'PASSES ALL TESTS'

def finder(files, queries):
    # Dictionary to store filepath info
    file_path = {}

    # Iterate through each file path
    for path in files:
    # Split the file paths on the backslash
        split_path = path.split("/")
    # Use the last split as the key and the whole file path as the value
        file_end = split_path[-1]
    # Store data in dictionary
        # If the key doesn't exist add it with an empty list
        if file_end not in file_path:
            file_path[file_end] = []
        # Add the ending as the key and the file path as the value
        file_path[file_end].append(path)
    
    # Create outout array
    output_array = []

    # Search to see if the query is in the dictionary
    for query in queries:
        # If the query is in the path dictionary, append the full file path
        if query in file_path:
            output_array.append(file_path[query])

    result = []

    # Output array is a nested list, need to return a 2-D list
    for inner_list in output_array:
        for item in inner_list:
            result.append(item)

    # Return result
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
