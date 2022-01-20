################ trial 2 ##################
a,b,c = map(int, input().split())
def solver(lev, index, n):
    if lev == 1:
        return n
        
    if index%2 == 1:
        half = index//2
        if half%2 == 1:
            return solver(lev-1, (index-1)//2, n)//2
        else:
            return solver(lev-1, (index+1)//2, n)//2
    else:
        return solver(lev-1, index//2, n)%2
            

count = 0
level = 1
root = a
while root > 1:
    level += 1
    root //= 2
for i in range(b, c+1):
    count += solver(level, i, a)

print(count)
################ trial 1: MLE #############
# a,b,c = map(int, input().split())
# def dfs(x: int):
#     if x == 0:
#         return 0
#     if x == 1:
#         return 1
    
#     y = dfs(x//2)
#     return str(y) + str(x%2) + str(y)
    
# def codeForOne(n:int, l:int, r:int)-> int:
#     x = dfs(n)
#     count = 0
#     for i in range(l-1, r):
#         if x[i] == '1':
#             count += 1
#     return count

# print(codeForOne(a, b, c))
