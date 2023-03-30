# iterTools: product , permutations , combinations, groupby, and infinite iterators
# from itertools import product
#
# a = [1, 2]
# b = [3, 4]
# prod = product(a, b) # cartesian product of two sets
# print(prod)
# print(list(prod))
#
# c = [5, 6]
# d = [7]
# prod2 = product(c, d, repeat = 2)
# print(list(prod2))
#
#
# from itertools import permutations
#
# f = [4, 1, 8]
# perm = permutations(f)
# print(list(perm))
# # permutations of only two elements
# perm2 = permutations(f, 2)
# print(list(perm2))


# COMBINATIONS

# from itertools import combinations, combinations_with_replacement
# a = [1, 2, 3, 4]
# comb = combinations(a, 2)
# print(list(comb))
#
# comb_wr = combinations_with_replacement(a, 2)
# print(list(comb_wr))


# ACCUMULATIONS
# from itertools import accumulate
# import operator
# a = [1, 2, 3, 4]
# acc = accumulate(a)
# print(a)
# print(list(acc))
#
# acc2 = accumulate(a, func=operator.mul)
# print(list(acc2))
#
# b = [4, 6, 2, 7, 3, 5]
# acc3 = accumulate(b, func=max)
# print(list(acc3))



# GROUPING
from itertools import groupby
def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key= smaller_than_3)
for key, value in group_obj:
    print(key, list(value))
