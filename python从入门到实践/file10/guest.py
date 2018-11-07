while True:
    name = input('plese write you name:\n')
    if name != 'exit':
        print('welcome')
        with open('guest.txt', 'a') as fwa:
            fwa.write(name + '\n')
    else:
        break

