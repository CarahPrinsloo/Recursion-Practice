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


def power_of_number(base, power):
    """Calculates the power of a number"""
    if (power == 1):
        return base
    else:
        return (base * power_of_number(base, power-1))

def swap(char_list, index_a, index_b):
    temp = char_list[index_a]
    char_list[index_a] = char_list[index_b]
    char_list[index_b] = temp
    return(char_list)


def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    total_number_sets = power_of_number(n, len(character_set))
    size_set = len(character_set)
    if (size_set == 1):
        for j in range(0, n):
            character_set


def main():
    ch_str = "ab"
    find_possible_strings(ch_str, 3)

if __name__ == "__main__":
    main()
