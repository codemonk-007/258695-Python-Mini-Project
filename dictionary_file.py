def about_dict():
    print('''
    Dictionaries are iterable unordered data structures in Python which store a key value binding of data.
    The keys in dictionaries are immutable whereas the values are mutable.
    Dictionaries help in creating a map like structure.
    Given below are some implemented algorithms on Dictionaries.
    Try them out! 
    ''')


def count_frequency_list(num_list):

    dictionary = {}
    for elem in num_list:
        if elem not in dictionary.keys():
            dictionary[elem] = 1
        else:
            dictionary[elem] += 1
    return dictionary


def count_frequency_str(string):

    dictionary = {}
    for elem in string:
        if elem != " ":
            if elem not in dictionary.keys():
                dictionary[elem] = 1
            else:
                dictionary[elem] += 1
    return dictionary


def check_pangram_num(num):

    dictionary = {}
    for d in num:
        if d not in dictionary.keys():
            dictionary[d] = 1
        else:
            dictionary[d] += 1

    for i in "0123456789":
        if i not in dictionary.keys():
            return False
    return True


def check_pangram_str(string):

    dictionary = {}
    for elem in string:
        if elem not in dictionary.keys():
            dictionary[elem.lower()] = 1
        else:
            dictionary[elem.lower()] += 1

    for elem in "abcdefghijklmnopqrstuvwxyz":
        if elem != " " and elem not in dictionary.keys():
            return False
    return True


def check_heterogram_str(string):

    dictionary = {}
    for elem in string:
        if elem != " ":
            if elem not in dictionary.keys():
                dictionary[elem] = 1
            else:
                dictionary[elem] += 1

    for keys in dictionary.keys():
        if dictionary[keys] > 1:
            return False
    return True

