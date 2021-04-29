def about_set():
    print('''
    Sets in Python are unordered, iterable and mutable data structures which store unique values.
    Sets give some advantage over lists that they have highly optimized search operation compared to lists.
    Given below are some implemented algorithms on Sets.
    Try them out! 
    ''')


def count_unq_num(num_list):

    num_set = set()
    for elem in num_list:
        num_set.add(elem)

    return num_set


def count_unq_char_str(string):

    char_set = set()
    for elem in string:
        char_set.add(elem)

    return char_set


def find_intersection_list(list1, list2):

    set1 = set(list1)
    set2 = set(list2)

    return set1 & set2


def find_union_list(list1, list2):

    set1 = set(list1)
    set2 = set(list2)

    return set1 | set2


def find_sym_diff_list(list1, list2):

    set1 = set(list1)
    set2 = set(list2)

    return set1 ^ set2


def find_elem_in_list1_not_in_list2(list1, list2):

    set1 = set(list1)
    set2 = set(list2)

    return set1 - set2

