def about_strings():
    print('''
    Strings are a sequence of unicode characters stored in a contiguous fashion. 
    Every element in string has a byte size.
    Since Python does not su[port character datatype, a single character in Python is a string of length 1.
    Strings are extremely powerful data types in Python
    Given below are some algorithms/operations on strings.
    Try them out! 
    ''')


def insert_char_at_pos(string, char, pos):

    temp_string = list(string)
    temp_string.insert(pos, char)
    temp_string = "".join(temp_string)
    return temp_string


def replace_nth_char_with(string, char, n):

    ans = ""
    if n == 0:
        return string
    for i in range(len(string)):
        if i % n == 0 and i != 0:
            ans += char
        else:
            ans += string[i]
    return str(ans)


def replace_vow_in_string_with_hash(string):

    ans = ""
    for elem in string:
        if elem in "aeiouAEIOU":
            ans += '#'
        else:
            ans += elem
    return str(ans)


def reverse_string(string):

    ans = string[::-1]
    return str(ans)


def check_subsequence(str1, str2):

    i = 0
    j = 0
    n, m = len(str1), len(str2)

    while i < n and j < m:
        if str2[j] == str1[i]:
            j += 1
        i += 1
    if j < m:
        return False
    return True
