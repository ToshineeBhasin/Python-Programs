def say_hello(name='World', greeting=None):
    if greeting == None:
        print(f'Hello {name}!')
    else:
        print(f'{greeting} {name}!')

say_hello()
say_hello('Toshi')
say_hello(greeting = 'Bhasin')
say_hello('Toshi', 'Bhasin')
'''
Hello World!
Hello Toshi!
Bhasin World!
Bhasin Toshi!
'''