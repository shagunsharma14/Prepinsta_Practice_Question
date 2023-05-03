# arr = [1, 2, 3, 2, 3, 3, 4, 4, 4, 4]
# arr = [10, 20, 10, 10, 20, 30, 30, 30, 30, 0]

freq = {}
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

sorted_arr = []
while freq:
    
    max_key = None
    for key in freq:
        if max_key is None or freq[key] > freq[max_key]:
            max_key = key
    for i in range(freq[max_key]):
        sorted_arr.append(max_key)
    del freq[max_key]

print(sorted_arr)
