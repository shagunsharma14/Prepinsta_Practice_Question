from collections import Counter

# Two strings S1 and S2 are anagrams of one another if –
#
# By re-arranging characters of string1 (s1) we can form string2 (s2) and vice versa
def sort_method(st1, st2):
    if sorted(st1.lower()) == sorted(st2.lower()):
        print('anagram')
    else:
        print('not a anagram')

def counter_method(st1, st2):
    if Counter(st1.lower()) == Counter(st2.lower()):
        print('anagram')
    else:
        print('not a anagram')


if __name__ == '__main__':
    st1, st2 = input().split()
    sort_method(st1, st2)
    counter_method(st1, st2)