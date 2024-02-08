import random

phonebook = {
    'Chris':'555−1111',
    'Katie':'555−2222',
    'Joanne':'555−3333'
}

print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(len(phonebook))

# this creates an empty dictionary
mydictionary1 = { "m": 8, "n": 9 }
print(mydictionary1)

# `m` and `n` are keys; `8` and `9` are values
mydictionary2 = dict(m=8, n=9)
print(mydictionary2)

print()
print('*****  end section 1 ********')
print()

#-----------------------------------------------------------------

print()
print('*****  start section 2 - search dictionary ********')
print()

person = "chris"

# if you access a non-existent key, you get a KeyError
def check_name(name):
    if name in phonebook:
        print(f"Name: {name} Phone Number: {phonebook[name]}")
    else:
        print(f"{name} is not in the phone book")

check_name(person)

print()
print('*****  end section 2 ********')
print()

#-----------------------------------------------------------------

print()
print('*****  start section 3 - edit/append dictionary ********')
print()

# you cannot update the key of a dictionary
# if you provide a new value for an existing key, it will update the key with that value
phonebook["Joe"] = "555-0123"
phonebook["Chris"] = "555-4444"

print(phonebook)

print()
print('*****  end section 3 ********')
print()

#-----------------------------------------------------------------

print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

del phonebook["Chris"]
print(phonebook)

print()
print('*****  end section 4 ********')
print()

#-----------------------------------------------------------------

print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

# iterate through keys
for key in phonebook:
    print(f"{key}: {phonebook[key]}")

# iterate through values using `.values()`
for value in phonebook.values():
    print(f"{value}")

print()
print('*****  end section 5 ********')
print()

#-----------------------------------------------------------------

print()
print('*****  start section 6 - using get and clear ********')
print()

print(phonebook.get("Chris"))
print(phonebook.clear())

print()
print('*****  end section 6 ********')
print()

#-----------------------------------------------------------------

print()
print('*****  start section 7 - using pop method ********')
print()

print(phonebook)
phone = phonebook.pop("Chris", "Name not found") # grab value in dic (first index) and replace it with valie in second index
print(phone, phonebook)

print()
print('*****  end section 7 ********')
print()

#-----------------------------------------------------------------

print()
print('*****  start section 8 - using popitem ********')
print()

# `popitem` selects random key-value pair from dic, pops it out, then processes it
# however, the "randomness" doesn't work. <- MAYBE FIX THIS??
phone = phonebook.popitem("Chris")
print(phone, phonebook)

print()
print('*****  end section 8 ********')
print()

#-----------------------------------------------------------------

print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)
print(list_of_keys)

randome_key = random.choice(list_of_keys)
print(randome_key) # key
print(phonebook[randome_key]) #value
print(phonebook[(random.choice(list(phonebook)))]) 

print()
print('*****  end section 9 ********')
print()

#-----------------------------------------------------------------
