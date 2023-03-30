# sets : unordered, mutable, no duplicates

# myset = set("Hello")
# myset2 = ([2,1,3,4])
# print(myset)
# print(myset2)


# myset = set()
#
# myset.add(2)
# myset.add(3)
# myset.add(4)
#
# print(myset)
#
# myset.pop()
# print(myset)



# # union, intersection, difference, subset
# odds = {1, 3, 5, 7, 9, 11}
# evens = {2, 4, 6, 8, 10, 12}
# primes = {2, 3, 5, 7, 11, 13}
#
# u = odds.union(evens).union(primes)
# e = odds.intersection(evens)
# print(u)
# print(e)
#
# diff = odds.difference(primes)
# diff = odds.symmetric_difference(evens)
# print(diff)

setA = {1, 2, 4, 6, 8, 3}
setB = {2, 4, 8}

print(setB.issubset(setA))


# FROZEN SET
a = frozenset([1, 2, 3, 4])

# a.remove(2) ---> not allowed, as set is
myname = "Shashwat"
for i in myname:
    print(i)



