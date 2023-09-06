def sort_by_frequency(arr):
    dic = {}
    for i in arr:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i]+=1
    
    ls = []
    for el,feq in dic.items():
        ls.append((feq,el))
    ls.sort(reverse=True)
    return [el for feq,el in ls]
a = [4, 2, 2, 8, 3, 3, 1, 1, 1, 8]
print(sort_by_frequency(a))
