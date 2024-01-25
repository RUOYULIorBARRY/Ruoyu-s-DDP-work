thedict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thedict)

# print ford
print(thedict["brand"])

# print brand : Ford, use f-string
print(f"brand : {thedict['brand']}")

# add string in dict
thedict["color"] = "blue", "yellow", "red"
thedict["size"] = "big"
print(thedict)

# delete string in dict
del thedict["size"]
print(thedict)

# no repetitive values, new value will take over
thedict["year"] = 2001
print(thedict)

# dict length (how many items)
print(len(thedict))

# dict items includes String, int, boolean, list
the_dict = {
    "brand": "Apple",
    "product": "13 promax",
    "electric": True,
    "year": 2022,
    "colour": ["blue", "white", "black"]
}
print(the_dict)

# print the data type of a dict
print(type(the_dict))
print(type(the_dict["electric"]))

# other way to built constructor
the_dict2 = dict(brand="XIAOMI", product="SU7", price=19.99)
print(the_dict2)
