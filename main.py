import list_file as lf
import dictionary_file as df
import set_file
import string_file as sf


def hello():
    print('''
    Welcome to Data Structures with Python!
    This Project implements some useful algorithms involving the data structures in Python
    Try Them out! 
    ''')
    return


def print_list_menu():

    print('''
       These are the implemented algorithms for the list data structures :
       1. Sort List using Bubble Sort
       2. Sort List using Selection Sort
       3. Sort List Using Insertion Sort
       4. Linear Search in Lists
       5. Binary Search in Lists
       6. Separate Odd and Even numbers in List
       7. Exit
       ''')
    return


def list_menu():
    lf.about_list()
    print_list_menu()
    option_num = int(input("Enter Option Number : "))
    while option_num != 7:
        if option_num == 1:
            num_list = list(map(int, input("Enter the List values :").split()))
            print("Original List = ", num_list)
            print("Sorted List = ", lf.sort_list_bubble(num_list))
        if option_num == 2:
            num_list = list(map(int, input("Enter the List values :").split()))
            print("Original List", num_list)
            print("Sorted List = ", lf.sort_list_selection(num_list))
        if option_num == 3:
            num_list = list(map(int, input("Enter the List values :").split()))
            print("Original List", num_list)
            print("Sorted List = ", lf.sort_list_insertion(num_list))
        if option_num == 4:
            num_list = list(map(int, input("Enter the List values :").split()))
            k = int(input("Enter Value to Search : "))
            print("Original List", num_list)
            found = lf.search_in_list_linear(num_list, k)
            if found == -1:
                print(k, " not Found in list")
            else:
                print(k, "Found in List at position ", found)

        if option_num == 5:
            num_list = list(map(int, input("Enter the List values :").split()))
            k = int(input("Enter Value to Search : "))
            print("Original List", num_list)
            found = lf.search_in_list_binary(num_list, k)
            if found == -1:
                print(k, " not Found in list")
            else:
                print(k, " Found in List")

        if option_num == 6:
            num_list = list(map(int, input("Enter the List values :").split()))
            print("Original List = ", num_list)
            print("Sorted List = ", lf.separate_odd_even(num_list))

        option_num = input("Try another List function? [Y/y : N/n]: ")
        if option_num == 'Y' or option_num == 'y':
            print_list_menu()
            option_num = int(input("Enter Option Number : "))
            continue
        else:
            break
    return


def print_dictionary_menu():
    print('''
        These are the implemented algorithms for the dictionary data structures :
        1. Count Frequency of characters in a list of numbers
        2. Count frequency of characters in a string
        3. Check if a number is Pangram
        4. Check if a string is Pangram
        5. Check if a string is Heterogram
        6. Exit
        ''')
    return


def dictionary_menu():
    df.about_dict()
    print_dictionary_menu()
    option_num = int(input("Enter Option Number : "))

    while option_num != 6:

        if option_num == 1:
            num_list = list(map(int, input("Enter the List values :").split()))
            dictionary = df.count_frequency_list(num_list)
            print("Element : Count")
            for key in dictionary.keys():
                print(key, ":", dictionary[key])

        if option_num == 2:
            string = input("Enter String : ")
            dictionary = df.count_frequency_str(string)
            print("Element : Count")
            for key in dictionary.keys():
                print(key, ":", dictionary[key])

        if option_num == 3:
            number = input("Enter an Integer: ")
            if df.check_pangram_num(number):
                print(number, " is a Pangram")
            else:
                print(number, " is not a Pangram")

        if option_num == 4:
            string = input("Enter a string : ")
            if df.check_pangram_str(string):
                print(string, " is a Pangram")
            else:
                print(string, " is not a Pangram")

        if option_num == 5:
            string = input("Enter a string : ")
            if df.check_heterogram_str(string):
                print(string, " is a Heterogram")
            else:
                print(string, " is not a Heterogram")

        option_num = input("Try another Dictionary function? [Y/y : N/n]: ")
        if option_num == 'Y' or option_num == 'y':
            print_dictionary_menu()
            option_num = int(input("Enter Option Number : "))
            continue
        else:
            break
    return


def print_string_menu():
    print('''
        These are the implemented algorithms on strings :
        1. Insert Character at Nth position in a string
        2. Replace Every Nth Character in string with another Character (Circular)
        3. Replace Vowels in string with Hash 
        4. Reverse A string
        5. Check if a string is a Subsequence of another string 
        6. Exit
        ''')
    return


def string_menu():

    sf.about_strings()
    print_string_menu()
    option_num = int(input("Enter Option Number : "))

    while option_num != 6:

        if option_num == 1:
            string = input("Enter main string : ")
            k = input("Enter Character to insert: ")
            n = int(input("Enter Position from 0 to {length}: ".format(length=len(string))))
            print("Original string : ", string)
            print("Formatted string : ", sf.insert_char_at_pos(string, k, n))

        if option_num == 2:
            string = input("Enter main string : ")
            k = input("Enter Character to be replaced by  : ")
            n = int(input("Enter Nth position : "))
            print("Original string : ", string)
            print("Formatted string : ", sf.replace_nth_char_with(string, k, n))

        if option_num == 3:
            string = input("Enter main string : ")
            print("Original string : ", string)
            print("Formatted string : ", sf.replace_vow_in_string_with_hash(string))

        if option_num == 4:
            string = input("Enter main string : ")
            print("Original string : ", string)
            print("Formatted string : ", sf.reverse_string(string))

        if option_num == 5:
            string1 = input("Enter Main string : ")
            string2 = input("Enter Subsequence string : ")
            if sf.check_subsequence(string1, string2):
                print(string2, " is a subsequence of ", string1)
            else:
                print(string2, " is a not a subsequence of ", string1)

        option_num = input("Try another String function? [Y/y : N/n]: ")
        if option_num == 'Y' or option_num == 'y':
            print_string_menu()
            option_num = int(input("Enter Option Number : "))
            continue
        else:
            break
    return


def print_set_menu():
    print('''
        These are the implemented algorithms on strings :
        1. Count Unique Numbers in a List Using Sets
        2. Count Unique Characters in a String Using Sets
        3. Find Intersection of 2 Lists using Sets
        4. Find Union of 2 Lists using Sets
        5. Find Symmetric Difference of 2 Lists using sets 
        6. Find Element(s) in List1 not in List2 using sets
        7. Exit
    ''')
    return


def set_menu():
    set_file.about_set()
    print_set_menu()
    option_num = int(input("Enter Option Number : "))

    while option_num != 7:

        if option_num == 1:
            num_list = list(map(int, input("Enter a list of numbers: ").split()))
            unq = set_file.count_unq_num(num_list)
            print(len(unq), " Unique elements was found in number list ")
            print("The Unique Elements are : ", unq)

        if option_num == 2:
            string = input("Enter a String: ")
            unq = set_file.count_unq_char_str(string)
            print(len(unq), " Unique elements was found in string ")
            print("The Unique Elements are : ", unq)

        if option_num == 3:
            list1 = list(map(int, input("Enter a List1 of numbers: ").split()))
            list2 = list(map(int, input("Enter a List2 of numbers: ").split()))
            intersection = set_file.find_intersection_list(list1, list2)
            print("The Intersection Elements are : ", intersection)

        if option_num == 4:
            list1 = list(map(int, input("Enter a List1 of numbers: ").split()))
            list2 = list(map(int, input("Enter a List2 of numbers: ").split()))
            union = set_file.find_union_list(list1, list2)
            print("The Union Elements are : ", union)

        if option_num == 5:
            list1 = list(map(int, input("Enter a List1 of numbers: ").split()))
            list2 = list(map(int, input("Enter a List2 of numbers: ").split()))
            sym_diff = set_file.find_sym_diff_list(list1, list2)
            print("The Symmetric Difference of the two lists is : ", sym_diff)

        if option_num == 6:
            list1 = list(map(int, input("Enter a List1 of numbers: ").split()))
            list2 = list(map(int, input("Enter a List2 of numbers: ").split()))
            diff = set_file.find_elem_in_list1_not_in_list2(list1, list2)
            print("The Intersection Elements are : ", diff)

        option_num = input("Try another Set function? [Y/y : N/n]: ")
        if option_num == 'Y' or option_num == 'y':
            print_set_menu()
            option_num = int(input("Enter Option Number : "))
            continue
        else:
            break
    return


def print_main_menu():
    print('''
            Choose The Options below to Explore:
            1. List
            2. Dictionary
            3. String 
            4. Set
            5. Exit
        ''')
    return


def main_menu():
    hello()
    print_main_menu()
    option_num = int(input("Enter Option Number : "))
    while option_num != 5:
        if option_num == 1:
            list_menu()
        if option_num == 2:
            dictionary_menu()
        if option_num == 3:
            string_menu()
        if option_num == 4:
            set_menu()
        option_num = input("Try another Data Structure ? [Y/y : N/n]: ")
        if option_num == 'Y' or option_num == 'y':
            print_main_menu()
            option_num = int(input("Enter Option Number : "))
            continue
        else:
            break
    print('''
        Good Bye!
     ''')
    return


main_menu()
