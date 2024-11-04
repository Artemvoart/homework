calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    upper_string = string.upper()
    lower_string = string.lower()
    return (calls, upper_string, lower_string)

def is_contains(string, list_to_search):
    count_calls()
    for item in list_to_search:
        if string.lower() in item.lower():
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)