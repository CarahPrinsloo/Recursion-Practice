def is_integer_list(list_given):
    """Checks if the list contains only integers, returns true if it does"""
    
    for item in list_given:
        try:
            item = int(item)
        except:
            return False
    return True

def find_min(element):
    """Returns the smallest number in the list"""

    if len(element) == 0 or (not is_integer_list(element)):
        return -1
    # base case
    elif len(element) == 1:
        return element[0]
    # recursive
    else:
        min_number = find_min(element[1:])
        if (element[0] < int(min_number)):
            return element[0]
        return min_number        


def sum_all(element):
    """TODO: complete for Step 2"""
    """Returns the sum of the inetegers in the list"""
    if len(element) == 0 or (not is_integer_list(element)):
        return -1
    elif len(element) == 1:
        return element[0]
    else:
        sum = element[0] + sum_all(element[1:])
    return sum


def find_possible_strings_recursive(character_set, prefix, len_set, n, possible_strings):

    if n == 0:
        possible_strings.append(prefix)
        return
    else:
        for i in range(0, len_set):
            temp_prefix = prefix + str(character_set[i])
            find_possible_strings_recursive(character_set, temp_prefix, len_set, n - 1, possible_strings)


def is_list_of_characters(my_list):
    str_of_list = ""
    for item in my_list:
        try:
            str_of_list = str_of_list + item
        except:
            return False
    return True


def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    """Given a set of characters and a positive integer n, 
    print all possible strings of length n that can be formed 
    from the given set."""
    possible_strings = []
    if not is_list_of_characters(character_set):
        return possible_strings
    len_set = len(character_set)
    find_possible_strings_recursive(character_set, "", len_set, n, possible_strings)
    return (possible_strings)


if __name__ == "__main__":
    my_list = [1, 'b']
    print(find_possible_strings(my_list, 2))
