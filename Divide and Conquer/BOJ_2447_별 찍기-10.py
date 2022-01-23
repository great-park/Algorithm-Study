# n = int(input())


# def star(n):
#     # base case
#     if n == 3:
#         return [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']]
#     x = [[0]*n for _ in range(n)]

#     prev = star(n//3)

#     for i in range(n):
#         for j in range(n):
#             if i//(n//3) == j//(n//3) == 1:
#                 x[i][j] = ' '
#             else:
#                 x[i][j] = prev[i % (n//3)][j % (n//3)]
#     return x


# ans = star(n)

# for i in range(n):
#     for j in range(n):
#         print(ans[i][j], end='')
#     print(end='\n')

def star(n):
    if n == 3:
        star_list = ['***', '* *', '***']
        return star_list
    else:
        new_star_list = [x * 3 for x in star(n//3)] + [x + ' '*(
            n//3) + x for x in star(n//3)] + [x * 3 for x in star(n//3)]
        return new_star_list


for i in star(int(input())):
    print(i)
