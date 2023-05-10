def check_disjoint(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                return False
    return True

if __name__ == '__main__':
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    
    if check_disjoint(l1, l2):
        print("Disjoint")
    else:
        print("Not Disjoint")