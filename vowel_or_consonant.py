def lower_case_vowel(ch):
    if ch=='a' or ch=='e' or ch=='i'or ch=='o' or ch=='u':
        return True
    return False

def upper_case_vowel(ch):
    if ch=='A' or ch=='E' or ch=='I'or ch=='O' or ch=='U':
        return True
    return False
if __name__ == '__main__':
    ch = input()
    if ch.isalpha():
        if  lower_case_vowel(ch) or upper_case_vowel(ch):
            print('Vowel')
        else:
            print('consonant')
    else:
        print('Invalid Input')
