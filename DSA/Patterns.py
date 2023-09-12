# Pattern 1

# *
# * *
# * * *
# * * * *
# * * * * *

# n = int(input())
# for row in range(1,n+1):
#     for col in range(1,row+1):
#         print('*',end=' ')
#     print()

# Pattern 2

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# n = int(input())
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         print('*',end=' ')
#     print()

# Pattern 3

# * * * * *
# * * * *
# * * *
# * *
# *

# n = int(input())
# for row in range(1,n+1):
#     for col in range(1,n-row+2):
#         print('*',end=' ')
#     print()
# for row in range(n,0,-1):
#     for col in range(row):
#         print('*',end=' ')
#     print()

# Pattern 4

#  1
#  1  2
#  1  2  3
#  1  2  3  4
#  1  2  3  4  5

# n = int(input())
# for row in range(1,n+1):
#     for col in range(1,row+1):
#         print('',col,end=' ')
#     print()

# Pattern 5

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# n = int(input())
# for row in range(1,n*2+1):
#     col_count = n-(row-n) if row>n else row
#     for col in range(1,col_count+1):
#         print('*',end=' ')
#     print()

# Pattern 6

#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *

# n = int(input())
# for row in range(1,n*2+1):
#     col_count = n-(row-n) if row>n else row
#     space_count = n-row if row<n else row-n
#     for space in range(space_count+1):
#         print(end=' ')
#     for col in range(1,col_count+1):
#         print('*',end=" ")
#     print()

# Pattern 7

#         1
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5

# n = int(input())
# for row in range(1,n+1):
#     space_count = n-row
#     for space in range(1,space_count+1):
#         print(' ',end=' ')
#     for col in range(row,0,-1):
#         print(col,end=' ')
#     for col in range(2,row+1):
#         print(col,end=' ')
#     print()

# Pattern 8

#       1
#     2 1 2
#   3 2 1 2 3
# 4 3 2 1 2 3 4
#   3 2 1 2 3
#     2 1 2
#       1 

# n = int(input())
# for row in range(1,n*2):
#     space_count = abs(n-row)
#     for space in range(1,space_count+1):
#         print('',end='  ')
#     col_count = 2*n-row if row>n else row
#     for col in range(col_count,0,-1):
#         print(col,end=' ')
#     for col in range(2,col_count+1):
#         print(col,end=' ')
#     print()

# Pattern 9
# n = int(input())
# for row in range(1,2*n):
#     for col in range(1,2*n):
#         col_count = min(min(row,col),min((n-row),(n-col)))
#         print(col_count,end='')
#     print()
    
