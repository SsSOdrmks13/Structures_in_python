# mytuple = {"Max", 28, "Boston"}
# print(mytuple)
#

# CREATING TUPLE USING TUPLE FUNCTION
# mytuple2 = tuple(["shashu", 12, "IT", 's', 's'])
# print(mytuple2)

# item = mytuple2[0] # we cant access element of mytuple like this because of the type of declaration
# print(item)



# WE CANT DO THIS:-
# mytuple[0] = "Ruchi"
# because tuples are immutable


# for item in mytuple:
#     print(item)
#
# if "shashu" and "Max" in mytuple2:
#     print("Yes")
# elif "shashwat" in mytuple2:
#     print("Yes")
# else:
#     print("NO")
#
# x = len(mytuple2)
# print(x)
#
# y = mytuple2.count('s')
# print(y)



# CONVERTING TUPLES TO LISTS
# mylist = list(mytuple2)
# print(mylist)
#
# name, enrol, city = mytuple
# print(name, enrol, city)

import sys
mytuple = ("SHASHWAT", 12, "LUCKNOW", 's', 'y')
i1, *i2, i3 = mytuple
print(i1)
print(i3)
print(i2)

mylist = list(mytuple)

print(sys.getsizeof(mylist), bytes)
print(sys.getsizeof(mytuple), bytes)

mylist3 = mylist.copy()
print(mylist3)



