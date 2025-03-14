try:
    x = int(input('input an integer: '))
    print(x)

except ValueError:
    print('Value not an Integer')

except NameError:
    print('Variable not defined')

except TypeError:
    print('Type Error')

finally:
    print('This will always be printed')