def assert_expectation(name, calculated, expected):
    if calculated != expected:
        print(f'Function: {name} EXPECTED: {expected} CALCULATED: {calculated}')
        raise AssertionError(f'Function: {name} EXPECTED: {expected} CALCULATED: {calculated}')

# 1.
# Create a function that takes temperature in degrees celsius as a parameter and returns fahrenheit
# Formula: (degree_celsius/5) * 9 + 32
def to_fahrenheit(degree_celsius):
    return degree_celsius / 5 * 9 + 32

to_fahrenheit(5)


assert_expectation('to_fahrenheit', calculated=to_fahrenheit(10), expected=50)
assert_expectation('to_fahrenheit', calculated=to_fahrenheit(-25), expected=-13)
assert_expectation('to_fahrenheit', calculated=to_fahrenheit(103), expected=217.4)
# write your own test
assert_expectation('to_fahrenheit', calculated=to_fahrenheit(5), expected=41)
assert_expectation('to_fahrenheit', calculated=to_fahrenheit(20), expected=68)
assert_expectation('to_fahrenheit', calculated=to_fahrenheit(13), expected=55.400000000000006)
#--------------------------------------------------------------------

# 2.
# Create a function that takes temperature in fahrenheit as a parameter and returns degrees celcius
# Formula: (fahrenheit - 32)/9*5
def to_degree_celsius(fahrenheit):
    return (fahrenheit - 32) / 9 * 5

assert_expectation('to_degree_celsius', calculated=to_degree_celsius(32),   expected=0)
assert_expectation('to_degree_celsius', calculated=to_degree_celsius(-13), expected=-25)
assert_expectation('to_degree_celsius', calculated=to_degree_celsius(217.4), expected=103)
# write your own test
assert_expectation('to_degree_celsius', calculated=to_degree_celsius(52), expected=11.11111111111111)
assert_expectation('to_degree_celsius', calculated=to_degree_celsius(33), expected=0.5555555555555556)
assert_expectation('to_degree_celsius', calculated=to_degree_celsius(56), expected=13.333333333333332)

#--------------------------------------------------------------------

# 3.
# Create a function that takes two numbers as parameters and returns the largest
def max(number_one, number_two):
    if number_one > number_two:
        return number_one
    else:
        return number_two

max(1234, 123)



assert_expectation('max', calculated=max(1, 2),   expected=2)
assert_expectation('max', calculated=max(-13, 102), expected=102)
assert_expectation('max', calculated=max(-1234, -2345), expected=-1234)
# write your own test
assert_expectation('max', calculated=max(3, 4), expected=4)
assert_expectation('max', calculated=max(22, 14), expected=22)
assert_expectation('max', calculated=max(13, 1256), expected= 1256)
#--------------------------------------------------------------------

# 4.
# Create a function that takes three numbers as parameters and returns the sum
def sum(number_one, number_two, number_three):
    return number_one + number_two + number_three
    
sum(1, 2, 5)

assert_expectation('sum', calculated=sum(1, 0, 2),   expected=3)
assert_expectation('sum', calculated=sum(-13, -2, 102), expected=87)
assert_expectation('sum', calculated=sum(-1234, 0, -2345), expected=-3579)
# write your own test
assert_expectation('sum', calculated=sum(5, 5, 5), expected=15)
assert_expectation('sum', calculated=sum(22, 33 ,44), expected=99)
assert_expectation('sum', calculated=sum(2, 3, 0), expected=5)

#--------------------------------------------------------------------

# 5.
# Create a function that takes a string and returns it size
def size(string):
    counter = 0
    for letter in string:
        counter += 1
    return counter

size('Hello Darragh')
     

assert_expectation('size', calculated=size('Z'),   expected=1)
assert_expectation('size', calculated=size('A simple string'), expected=15)
assert_expectation('size', calculated=size('ho ho ho'), expected=8)
# write your own test
assert_expectation('size', calculated=size('Joe Wicks'), expected=9)
assert_expectation('size', calculated=size('Donald Trump'), expected=12)
assert_expectation('size', calculated=size('Conor Fennell'), expected=13)
#--------------------------------------------------------------------

# 6.
# Create a function that takes a list and returns its size
def list_size(list):
    counter = 0
    for y in list:
        counter += 1
    return counter

list_size([12])
    


assert_expectation('list_size', calculated=list_size([100]),   expected=1)
assert_expectation('list_size', calculated=list_size(['a', 'b', 'c']), expected=3)
assert_expectation('list_size', calculated=list_size([1, 'b', 'c', 10]), expected=4)
# write your own test
#assert_expectation('list_size', calculated=list_size([100]), expected=1)
#assert_expectation('list_size', calculated=list_size(['h', 'e', 'l', 'l', 'o'], expected=5)
#--------------------------------------------------------------------

# 7.
# Create a function that takes a map and returns the number of keys
def map_size(maps):
    counter = 0
    for x in maps:
        counter += 1
    return counter
 
map_size({'liv': 1})

assert_expectation('map_size', calculated=map_size({'a': 1}),   expected=1)
assert_expectation('map_size', calculated=map_size({'a': 1, 'b': 2, 'c': 3}), expected=3)
assert_expectation('map_size', calculated=map_size({'cd': 1, 'll': 2, 'gg': 3, 'hh': 5}), expected=4)
# write your own test
assert_expectation('map_size', calculated=map_size({'og': 1}), expected=1)
assert_expectation('map_size', calculated=map_size({'yc': 1}), expected=1)
assert_expectation('map_size', calculated=map_size({'gc': 1}), expected=1)