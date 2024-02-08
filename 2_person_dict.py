person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# print out the name of the second child
list_of_children = person["children"]
print(list_of_children[1]) # betty
print(person["children"][1]) # betty


# print out the name of the cat

pet_dictionary = person["pets"]
print(type[pet_dictionary])

print(pet_dictionary["cat"]) # sox
print(person["pets"]["cat"]) # sox

# use a loop to print out the names of each child



# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido
