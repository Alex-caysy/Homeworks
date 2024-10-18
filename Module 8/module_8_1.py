def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        if isinstance(a, str):
            b = str(b)
        else:
            a = str(a)
    finally:
        return a + b


print(add_everything_up(10.5, 8))
print(add_everything_up('h', 7))
print(add_everything_up(7, 'h'))
print(add_everything_up('hel', 'lo'))
