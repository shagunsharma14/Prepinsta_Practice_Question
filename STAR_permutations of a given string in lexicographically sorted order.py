ans = []

def permute(a, l, r):
    if l==r:
        ans.append(''.join(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]

if __name__ == '__main__':
    string = input()
    a = list(string)
    permute(a, 0, len(string))
    for _ in sorted(ans):
        print(_)