# def binary_search(arr,key):
#     low = 0
#     high = len(arr)-1
#     while low<=high:
#         mid = (low+high)//2
#         if arr[mid]==key:
#             return mid
#         elif arr[mid]<key:
#             low = mid+1
#         elif arr[mid]>key:
#             high = mid-1
#     return -1

# arr = list(map(int,input().split()))
# arr.sort()
# key = int(input())
# if binary_search(arr,key):
#     print(f'found at {binary_search(arr,key)}')
# else:
#     print('Not found!')

################## Recurssive Method ################## 
# def binary_search(arr, key, left, right):
#     while left<=right:
#         mid = (left+right)//2
#         if arr[mid]==key:
#             return mid
#         elif arr[mid]<key:
#             return binary_search(arr,key,mid+1,right)
#         elif arr[mid]>key:
#             return binary_search(arr,key,left,mid-1)
#     return -1

# arr = list(map(int,input().split()))
# key = int(input())
# arr.sort()
# print(arr)
# res = binary_search(arr,key,0,len(arr)-1)
# if res!=-1:
#     print(f'found at {res}')
# else:
#     print('Not found!')