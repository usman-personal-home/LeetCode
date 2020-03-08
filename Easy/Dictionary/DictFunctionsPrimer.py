

def dictget():

    my_dict = {'name': 'Jack', 'age': 26}

    # Output: Jack
    print(my_dict['name'])

    # Output: 26
    print(my_dict.get('age'))

    # Trying to access keys which doesn't exist throws error
    my_dict.get('address', 0)

    print my_dict

    person = {'name': 'Phill', 'age': 22}

    print('Name: ', person.get('name'))
    print('Age: ', person.get('age'))

    person['salary'] = person.get('salary', 100)
    print(person['salary'])


if __name__ == '__main__':
    dictget()