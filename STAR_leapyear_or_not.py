if __name__ == '__main__':
    yr = int(input())
    # if yr%400==0:
    #     print("Leap Year")
    # else:
    #     if yr%100!=0:
    #         if yr%4==0:
    #             print("Leap Year")
    #         else:
    #             print("Not a Leap Year")
    #     else:
    #         print("Not a Leap Year")
    if (yr%400==0) or (yr%100!=0 and yr%4==0):
        print("Leap Year")
    else:
        print("Not a Leap Year")