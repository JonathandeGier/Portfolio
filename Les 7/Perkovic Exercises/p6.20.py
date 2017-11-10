def reverse(dictionary):
    reversed_dictionary = dict
    for item in dictionary.items():
        reversed_dictionary[item[1]] = item[0]
    return reversed_dictionary

phonebook = {'Smith, Jane':'123-45-67', 'Doe, John':'987-65-43','Baker,David':'567-89-01'}

print(reverse(phonebook))