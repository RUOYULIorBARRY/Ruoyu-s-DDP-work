the_dict = {
    "brand": "Apple",
    "product": "13 promax",
    "electric": True,
    "year": 2022,
    "colour": ["blue", "white", "black"]
}
print(the_dict)

# loop through a dict
for x in the_dict:
    print(x)            # print the keys
    print(the_dict[x])  # print the value

for x in the_dict.values():  # another way to print the value
    print(x)

for x in the_dict.keys():    # another way to print the keys
    print(x)

# way to print both keys and values
for x, y in the_dict.items():
    print(x, y)


the_dict = {
    "brand": "XIAOMI",
    "product": "SU7",
    "electric": True,
}
print(the_dict)

# copy dict
cp_dict = the_dict.copy
print(cp_dict)

# another way to copy
cp2_dict = dict(the_dict)
print(cp2_dict)

# nested dict
myfamliy = {
    "papa": {
        "year": 1972
    },
    "mama": {
        "year": 1975
    },
    "me": {
        "year": 2001
    }
}
print(myfamliy)

# add serveral dicts into a new dict
child1 = {
    "name": "Ian",
    "age": 2
}
child2 = {
    "name": "Leo",
    "age": 3
}
myfamliy = {
    "child1": child1,
    "child2": child2
}
print(myfamliy)
