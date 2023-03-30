# dictionaries: key-value pairs, unordered, mutable
mydict = {"name":"Max", "age":28, "city":"Lucknow"}
print(mydict)

mydict2 = dict(name="Shashu", age = 21, city = "Boston")
print(mydict2)

value1 = mydict2["name"]
print(value1)

value2 = mydict2["city"]
print(value2)

mydict["name"] = "Ruchi"
print(mydict)

mydict["email"] = "saran24.eng@homail.com"
print(mydict)

# mydict2.pop("age")
# print(mydict2)

# for key in mydict.values():
#     print(key)

for key, values in mydict.items():
    print(key, values)


# COPYING A DICTIONARY
# mydict_cpy = mydict.copy()
# mydict_cpy["name"] = "shashwat"
# print(mydict_cpy)
# print(mydict)

mydict.update(mydict2)
print(mydict)

mytuple = (8, 7) # tuples can be done like this but not lists
mydict = {mytuple: 15}

print(mydict)