def isbalanced(s):
    c = 0
    for i in s:
        if i == "(":
            c += 1
        elif i== ")":
            c -= 1
            
    if c != 0:
        return False
    else:
        return True
    
if __name__ == '__main__':
    s = '((()))'
    print(isbalanced(s))