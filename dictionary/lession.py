# Dictionary = a collection of {key : value} pairs
#  ordered and changeable, allows duplicate values but not duplicate keys

# capitals = {"USA": "Washington D.C.",
#             "France": "Paris",
#             "Japan": "Tokyo",
#             "russia": "Moscow"}
# dir() function returns a list of all the methods and attributes of the specified object
# print(capitals.get("USA"))  # returns the value of the specified key
# print(capitals.get("France"))  # returns the value of the specified key
# print(capitals.get("Japan"))  # returns the value of the specified key
# print(capitals.get("russia"))  # returns the value of the specified key

# if capitals.get("Germany"):  # returns None if the key does not exist
#     print("Germany is not in the dictionary")
# else:
#     print("Japan is in the dictionary")

# capitals.update({"Germany": "Berlin"})  # adds a new key-value pair to the dictionary
# capitals.update({"USA": "Washington"})  # updates the value of an existing key
# capitals.pop("russia")  # removes the key-value pair with the specified key
# print(capitals)  # prints the updated dictionary
# for key , value in capitals.items():  # iterates through the key-value pairs in the dictionary
#     print(key, value)  # prints the key and value of each pair
# exercice 01
exo01 = {"key1": "value1", "key2": "value2", "key3": "value1"}


def inv_exo1(dictionary):
    inv_exo1 = {}
    for key, value in dictionary.items():
        if value in inv_exo1:
            inv_exo1[value].append(key)
        else:
            inv_exo1[value] = [key]
    return inv_exo1


print(inv_exo1(exo01))
