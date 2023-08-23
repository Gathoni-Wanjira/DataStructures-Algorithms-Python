# Dictionaries are used to store data in key:value pairs.

testDict = {
    "Country":"Kenya",
    "Brand":"Toyota",
    "School":"USIU",
    "Year":"2010"
}
print(testDict)


# Dictionary Items
# They are ordered, changable and doesn't allow duplicates.

print(testDict["Brand"])


# Dictionary Length 
# You get to use the len function

print(len(testDict))

# Type()
# Dictionaries are defined as objects with the data type 'dict':

print(type(testDict))

# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.

school_data = dict(name = "Noni", town = "Narok",Height = "5'3")
print(school_data)


# 1. Access Dictionary Items


# You can access the items of a dictionary by referring to its key name, inside square brackets:

Y = testDict["School"]
print(Y)

# There is also a method called get() that will give you the same result:

Z = testDict.get("Country")
print(Z)


# Get Keys
# You can access all the keys in a dictionary using the .keys as shown

All_keys = testDict.keys()
print(All_keys)


# Get Values
# You can access all the values in a dictionary using the .values as shown

All_values = testDict.values()
print(All_values)


# Get Items
# It returns each item in a dictionary as tuples in a list

dict_items = testDict.items()
print(dict_items)

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword

if "Brand" in testDict:
    print("We have the car brand now!")


