if __name__ == '__main__':
    st = input()
################ METHOD 1 ################
    # new_st = ''
    # for i in st:
    #     if i!=' ' and i!='\n':
    #         new_st += i
    # print(new_st)

################ METHOD 2 ################
    print(''.join(list(st.split())))