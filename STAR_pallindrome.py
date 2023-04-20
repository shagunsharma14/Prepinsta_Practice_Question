if __name__ == '__main__':
    ########## METHOD 1 ##############
    # num = 1221
    # temp = num
    # reverse = 0
    # while temp > 0:
    #     remainder = temp % 10
    #     reverse = (reverse * 10) + remainder
    #     temp = temp // 10
    # if num == reverse:
    #     print('Palindrome
    #     ')
    # else:
    #     print("Not Palindrome")

    ########## METHOD 2 ##############
   # print('pallindrome' if num == num[::-1] else 'not a pallindrome')

    ########## METHOD 3(PREFER) ##############
    sen = input()
    flag = 0
    mid  = int(len(sen)/2)
    for i in range(mid):#no need to traverse whole string
        if sen[i] != sen[len(sen)-1-i]: #half string is enough rest we're checking with str's original lengh in
            # reverse cse
            flag = 1
            break
    print("pallindrome" if flag==0 else "not a pallindrome")
