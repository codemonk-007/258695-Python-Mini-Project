def about_list():
    print('''
    Lists are mutable,iterable ordered data structures in Python which store contiguous homogenous/heterogeneous data.
    This property of lists in Python makes this data structure very powerful to use.
    Given below are some implemented algorithms on Lists.
    Try them out! 
    ''')


def sort_list_bubble(num_list):
    n = len(num_list)
    for i in range(n-1):
        for j in range(n-i-1):
            if num_list[j+1] < num_list[j]:
                temp = num_list[j]
                num_list[j] = num_list[j+1]
                num_list[j+1] = temp
    return num_list


def sort_list_insertion(num_list):

    n = len(num_list)
    for i in range(1, n):
        j = i - 1
        next_elem = num_list[i]

        while (num_list[j] > next_elem) and (j >= 0):
            num_list[j + 1] = num_list[j]
            j = j - 1
        num_list[j + 1] = next_elem
    return num_list


def sort_list_selection(num_list):

    n = len(num_list)
    for i in range(n):

        min_i = i
        for j in range(i + 1, n):
            if num_list[min_i] > num_list[j]:
                min_i = j

        temp = num_list[i]
        num_list[i] = num_list[min_i]
        num_list[min_i] = temp
    return num_list


def search_in_list_linear(num_list, key):

    pos = -1
    for elem in num_list:
        if elem == key:
            pos = num_list.index(elem)
            break
    return pos


def search_in_list_binary(num_list, key):
    sorted_list = sorted(num_list)
    pos = -1
    hi = len(sorted_list) - 1
    low = 0
    while low <= hi:
        mid = (low + hi)//2
        if sorted_list[mid] == key:
            pos = mid
            break
        elif sorted_list[mid] < key:
            low = mid + 1
        else:
            hi = mid - 1
    return pos


def separate_odd_even(num_list):

    new_list = []
    for elem in num_list:
        if elem % 2 == 0:
            new_list.append(elem)
    for elem in num_list:
        if elem % 2 != 0:
            new_list.append(elem)
    return new_list
