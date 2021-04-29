import pytest
import list_file as lf
import set_file
import dictionary_file as df
import string_file as sf


# test lists
def test_sort_list_bubble():
    num_list = [2, 3, 4, 5, 3, 5]
    assert lf.sort_list_bubble(num_list) == [2, 3, 3, 4, 5, 5]
    num_list = [0, 0, 0, 1, 2, 3, 4, -1, -2, -3]
    assert lf.sort_list_bubble(num_list) == [-3, -2, -1, 0, 0, 0, 1, 2, 3, 4]
    num_list = [1, 2, 3, 4, 5, 6, 7, 8]
    assert lf.sort_list_bubble(num_list) == [1, 2, 3, 4, 5, 6, 7, 8]
    num_list = [0, 0, 0, 0, 0, 0, 0, 0]
    assert lf.sort_list_bubble(num_list) == [0, 0, 0, 0, 0, 0, 0, 0]
    num_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert lf.sort_list_bubble(num_list) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num_list = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
    assert lf.sort_list_bubble(num_list) == [-9, -8, -7, -6, -5, -4, -3, -2, -1]


def test_sort_list_insertion():
    num_list = [2, 3, 4, 5, 3, 5]
    assert lf.sort_list_insertion(num_list) == [2, 3, 3, 4, 5, 5]
    num_list = [0, 0, 0, 1, 2, 3, 4, -1, -2, -3]
    assert lf.sort_list_insertion(num_list) == [-3, -2, -1, 0, 0, 0, 1, 2, 3, 4]
    num_list = [1, 2, 3, 4, 5, 6, 7, 8]
    assert lf.sort_list_insertion(num_list) == [1, 2, 3, 4, 5, 6, 7, 8]
    num_list = [0, 0, 0, 0, 0, 0, 0, 0]
    assert lf.sort_list_insertion(num_list) == [0, 0, 0, 0, 0, 0, 0, 0]
    num_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert lf.sort_list_insertion(num_list) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num_list = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
    assert lf.sort_list_insertion(num_list) == [-9, -8, -7, -6, -5, -4, -3, -2, -1]


def test_sort_list_selection():
    num_list = [2, 3, 4, 5, 3, 5]
    assert lf.sort_list_selection(num_list) == [2, 3, 3, 4, 5, 5]
    num_list = [0, 0, 0, 1, 2, 3, 4, -1, -2, -3]
    assert lf.sort_list_selection(num_list) == [-3, -2, -1, 0, 0, 0, 1, 2, 3, 4]
    num_list = [1, 2, 3, 4, 5, 6, 7, 8]
    assert lf.sort_list_selection(num_list) == [1, 2, 3, 4, 5, 6, 7, 8]
    num_list = [0, 0, 0, 0, 0, 0, 0, 0]
    assert lf.sort_list_selection(num_list) == [0, 0, 0, 0, 0, 0, 0, 0]
    num_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert lf.sort_list_selection(num_list) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num_list = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
    assert lf.sort_list_selection(num_list) == [-9, -8, -7, -6, -5, -4, -3, -2, -1]


def test_search_linear():
    num_list = [2, 3, 4, 5, 3, 5]
    assert lf.search_in_list_linear(num_list, 5) == 3
    num_list = [0, 0, 0, 1, 2, 3, 4, -1, -2, -3]
    assert lf.search_in_list_linear(num_list, -3) == 9
    num_list = [1, 2, 3, 4, 5, 6, 7, 8]
    assert lf.search_in_list_linear(num_list, 6) == 5
    num_list = [0, 0, 0, 0, 0, 0, 0, 0]
    assert lf.search_in_list_linear(num_list, 1) == -1
    num_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert lf.search_in_list_linear(num_list, 10) == -1
    num_list = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
    assert lf.search_in_list_linear(num_list, -9) == 8


def test_search_binary():

    num_list = [2, 3, 4, 5, 3, 5]
    assert lf.search_in_list_binary(num_list, 5) != -1
    num_list = [0, 0, 0, 1, 2, 3, 4, -1, -2, -3]
    assert lf.search_in_list_binary(num_list, -3) != -1
    num_list = [1, 2, 3, 4, 5, 6, 7, 8]
    assert lf.search_in_list_binary(num_list, 6) != -1
    num_list = [0, 0, 0, 0, 0, 0, 0, 0]
    assert lf.search_in_list_binary(num_list, 1) == -1
    num_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert lf.search_in_list_binary(num_list, 10) == -1
    num_list = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
    assert lf.search_in_list_binary(num_list, -9) != -1


def test_odd_even():

    num_list = [2, 3, 4, 5, 3, 5]
    assert lf.separate_odd_even(num_list) == [2, 4, 3, 5, 3, 5]
    num_list = [0, 0, 0, 1, 2, 3, 4, -1, -2, -3]
    assert lf.separate_odd_even(num_list) == [0,0,0,2,4,-2,1,3,-1,-3]
    num_list = [1, 2, 3, 4, 5, 6, 7, 8]
    assert lf.separate_odd_even(num_list) == [2, 4, 6, 8, 1, 3, 5, 7]
    num_list = [0, 0, 0, 0, 0, 0, 0, 0]
    assert lf.separate_odd_even(num_list) == [0, 0, 0, 0, 0, 0, 0, 0]
    num_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert lf.separate_odd_even(num_list) == [8, 6, 4, 2, 0, 9, 7, 5, 3, 1]
    num_list = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
    assert lf.separate_odd_even(num_list) == [-2, -4, -6, -8, -1, -3, -5, -7, -9]


# test set
def test_set_unq():

    num_list = [1,1,1,2,2,-1,-1,0,0,3]
    assert set_file.count_unq_num(num_list) == {1,2,-1,-0,3}
    num_list = [0 , 0, 0, 0 ,0 , 0, 0, 0]
    assert set_file.count_unq_num(num_list) == {0}
    num_list = [1,2,3,4,5,6,7,8,9,0]
    assert set_file.count_unq_num(num_list) == {1,2,3,4,5,6,7,8,9,0}


def test_set_unq_string():
    string = "abcdeeffgghh"
    assert set_file.count_unq_char_str(string) == {'a','b','c','d','e','f','g','h'}
    string = "abbcccddddeeeee"
    assert set_file.count_unq_char_str(string) == {'a', 'b', 'c','d','e'}
    string = "AAAAABBBBcccDDe "
    assert set_file.count_unq_char_str(string) == {'A','B','c','D','e',' '}


def test_find_intersection_list():
    list1 = [1,2,3,4,5]
    list2 = [2,3,5,6]
    assert set_file.find_intersection_list(list1, list2) == {2,3,5}

    list1 = [1,2,3,4,5]
    list2 = [6,7,8,9,0]
    empty_set = set()
    assert set_file.find_intersection_list(list1, list2) == empty_set

    list1 = [1,2,3,4,5]
    list2 = [1,2,3,4,5]
    assert set_file.find_intersection_list(list1, list2) == {1,2,3,4,5}

    list1 = [0,1,0,1,0]
    list2 = [0,1,2]
    assert set_file.find_intersection_list(list1, list2) == {0,1}


def test_find_union_list():

    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 3, 5, 6]
    assert set_file.find_union_list(list1, list2) == {1, 2, 3, 4, 5, 6}

    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 0]
    assert set_file.find_union_list(list1, list2) == {1,2,3,4,5,6,7,8,9,0}

    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 5]
    assert set_file.find_union_list(list1, list2) == {1, 2, 3, 4, 5}

    list1 = [0, 1, 0, 1, 0]
    list2 = [0, 1, 2]
    assert set_file.find_union_list(list1, list2) == {0, 1, 2}


def test_find_sym_diff_list():

    empty_set = set()
    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 3, 5, 6]
    assert set_file.find_sym_diff_list(list1, list2) == {1,4,6}

    list1 = [1, 2, 3, 4, 5,6]
    list2 = [6, 7, 8, 9, 0]
    assert set_file.find_sym_diff_list(list1, list2) == {1, 2, 3, 4, 5, 7, 8, 9, 0}

    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 5]
    assert set_file.find_sym_diff_list(list1, list2) == empty_set

    list1 = [0, 1, 0, 1, 0]
    list2 = [0, 1, 2]
    assert set_file.find_sym_diff_list(list1, list2) == {2}


def test_find_elem_in_list1_not_in_list2():
    empty_set = set()
    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 3, 5, 6]
    assert set_file.find_elem_in_list1_not_in_list2(list1, list2) == {1, 4}

    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [6, 7, 8, 9, 0]
    assert set_file.find_elem_in_list1_not_in_list2(list1, list2) == {1, 2, 3, 4, 5}

    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 5]
    assert set_file.find_elem_in_list1_not_in_list2(list1, list2) == empty_set

    list1 = [0, 1, 0, 1, 0]
    list2 = [0, 1, 2]
    assert set_file.find_elem_in_list1_not_in_list2(list1, list2) == empty_set


# test dictionaries
def test_count_frequency_list():
    num_list = [1, 1, 1, 2, 2, -1, -1, 0, 0, 3]
    assert df.count_frequency_list(num_list) == {1: 3, 2: 2, -1: 2, 0: 2 , 3: 1}

    num_list = [0, 0, 0, 0, 0, 0, 0, 0]
    assert df.count_frequency_list(num_list) == {0: 8}

    num_list = [0, 0, 0, 1, 2, 3, 4, -1, -2, -3]
    assert df.count_frequency_list(num_list) == {0: 3, 1: 1, 2: 1, 3: 1, 4: 1, -1: 1, -2: 1, -3: 1}


def test_count_freq_str():

    string = "abcdeeffgghhabcdefgh"
    assert df.count_frequency_str(string) == {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 3, 'f': 3, 'g': 3, 'h': 3}

    string = "abbcccddddeeeee"
    assert df.count_frequency_str(string) == {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

    string = "AAAAABBBBcccDDe "
    assert df.count_frequency_str(string) == {'A': 5, 'B': 4, 'D': 2, 'c': 3, 'e': 1}


def test_check_pangram_str():
    yes = True
    no = False

    string = "A quick brown fox jumps over the lazy dog"
    assert df.check_pangram_str(string) == yes

    string = "A zenith of Xvurj’s cwm KL Gybdq"
    assert df.check_pangram_str(string) == no

    string = "Mr. Jock, TV quiz PhD., bags few lynx"
    assert df.check_pangram_str(string) == yes


def test_check_pangram_num():
    yes = True
    no = False

    num = "1234567890"
    assert df.check_pangram_num(num) == yes

    num = "9876543210"
    assert df.check_pangram_num(num) == yes

    num = "12345678900987654321"
    assert df.check_pangram_num(num) == yes

    num = "12344556"
    assert df.check_pangram_num(num) == no

    num = "0"
    assert df.check_pangram_num(num) == no


def test_check_heterogram_str():
    yes = True
    no = False

    string = "the big dwarf only jumps"
    assert df.check_heterogram_str(string) == yes

    string = "geeksforgeeks"
    assert df.check_heterogram_str(string) == no

    string = "A quick brown fox jumps over the lazy dog"
    assert df.check_heterogram_str(string) == no


# test strings
def test_insert_char_at_pos():

    string = "abcdefghijklmnopqrstuvwxyz"

    assert sf.insert_char_at_pos(string, '$', 10) == "abcdefghij$klmnopqrstuvwxyz"
    assert sf.insert_char_at_pos(string, '#', 26) == "abcdefghijklmnopqrstuvwxyz#"
    assert sf.insert_char_at_pos(string, "%", 15) == "abcdefghijklmno%pqrstuvwxyz"
    assert sf.insert_char_at_pos(string, "*", 0) == "*abcdefghijklmnopqrstuvwxyz"

    string = "Hello World"
    assert sf.insert_char_at_pos(string, "!", 11) == 'Hello World!'


def test_replace_nth_char_with():

    string = "abcdefghijklmnopqrstuvwxyz"

    assert sf.replace_nth_char_with(string, "$", 5) == 'abcde$ghij$lmno$qrst$vwxy$'
    assert sf.replace_nth_char_with(string, "#", 10) == 'abcdefghij#lmnopqrst#vwxyz'
    assert sf.replace_nth_char_with(string, "*", 25) == 'abcdefghijklmnopqrstuvwxy*'
    assert sf.replace_nth_char_with(string, "&", 1) == 'a&&&&&&&&&&&&&&&&&&&&&&&&&'
    assert sf.replace_nth_char_with(string, "@",0) == 'abcdefghijklmnopqrstuvwxyz'


def test_replace_vow_with_hash():

    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert sf.replace_vow_in_string_with_hash(string) == '#bcd#fgh#jklmn#pqrst#vwxyz#BCD#FGH#JKLMN#PQRST#VWXYZ'
    string = "the big dwarf only jumps"
    assert sf.replace_vow_in_string_with_hash(string) == 'th# b#g dw#rf #nly j#mps'
    string = 'geeksforgeeks'
    assert sf.replace_vow_in_string_with_hash(string) == 'g##ksf#rg##ks'
    string = 'Hello World'
    assert sf.replace_vow_in_string_with_hash(string) == 'H#ll# W#rld'


def test_rev_string():
    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert sf.reverse_string(string) == 'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'

    string = "the big dwarf only jumps"
    assert sf.reverse_string(string) == 'spmuj ylno frawd gib eht'

    string = "geeksforgeeks"
    assert sf.reverse_string(string) == 'skeegrofskeeg'

    string = "A quick brown fox jumps over the lazy dog"
    assert sf.reverse_string(string) == 'god yzal eht revo spmuj xof nworb kciuq A'


def test_check_subsequence():
    yes = True
    no = False
    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert sf.check_subsequence(string, "abbc") == no
    assert sf.check_subsequence(string, "opqrst") == yes
    assert sf.check_subsequence(string, "azAZ") == yes
    assert sf.check_subsequence(string, "zyx") == no
    assert sf.check_subsequence(string, "") == yes

    string = "A quick brown fox jumps over the lazy dog"

    assert sf.check_subsequence(string, "ck br fox") == yes
    assert sf.check_subsequence(string, "qdog") == yes
    assert sf.check_subsequence(string, "jumps over the quick brown fox") == no