calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    my_tuple = len(string), string.upper(), string.lower()
    return my_tuple


def is_contains(string, list_to_search):
    count_calls()
    for str_ in list_to_search:
        if string.lower() == str_.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)