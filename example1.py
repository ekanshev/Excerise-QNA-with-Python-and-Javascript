# Problem #1

# Implement a group_by_owners function that:

#  Accepts a dictionary containing the file owner name for each file name.

# Returns a dictionary containing a list of file names for each owner name, in any order.

# For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.


# Solution1 ->


files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
# Function to group the files.   
def group_by_owners(files):

    # Dictionary object to hold the result.
    result = {}

    for key, value in files.items():

        if value not in result.keys():

            # Insert the values into the resulting dictionary
            # by interchanging the key, values.
            result[value] = [key]
        else:

            # Append the othet file name if the owner is same.
            result[value].append(key)

    return result

print(group_by_owners(files))