def assert_expectation(name, calculated, expected):
    if calculated != expected:
        raise AssertionError(f'Function: {name} EXPECTED: {expected} CALCULATED: {calculated}')

# 1.
# Create a function that takes temperature in degrees celsius as a parameter and returns fahrenheit
# Formula: (degree_celsius/5) * 9 + 32
def to_fahrenheit(degree_celsius):


assert_expectation('to_fahrenheit', calculated=to_fahrenheit(0),   expected=32)
assert_expectation('to_fahrenheit', calculated=to_fahrenheit(-25), expected=-13)
assert_expectation('to_fahrenheit', calculated=to_fahrenheit(103), expected=217.4)
# write your own test

#--------------------------------------------------------------------

# 2.
# Create a function that takes temperature in fahrenheit as a parameter and returns degrees celcius
# Formula: (fahrenheit - 32)/9*5
def to_degree_celsius(fahrenheit):


assert_expectation('to_degree_celsius', calculated=to_degree_celsius(32),   expected=0)
assert_expectation('to_degree_celsius', calculated=to_degree_celsius(-13), expected=-25)
assert_expectation('to_degree_celsius', calculated=to_degree_celsius(217.4), expected=103)
# write your own test

#--------------------------------------------------------------------

# 3.
# Create a function that takes two numbers as parameters and returns the largest
def max(number_one, number_two):



assert_expectation('max', calculated=max(1, 2),   expected=2)
assert_expectation('max', calculated=max(-13, 102), expected=102)
assert_expectation('max', calculated=max(-1234, -2345), expected=-1234)
# write your own test

#--------------------------------------------------------------------

# 4.
# Create a function that takes three numbers as parameters and returns the sum
def sum(number_one, number_two, number_three):


assert_expectation('sum', calculated=sum(1, 0, 2),   expected=3)
assert_expectation('sum', calculated=sum(-13, -2, 102), expected=87)
assert_expectation('sum', calculated=sum(-1234, 0, -2345), expected=-3579)
# write your own test

#--------------------------------------------------------------------

# 5.
# Create a function that takes a string and returns it size
def size(string):


assert_expectation('size', calculated=size('Z'),   expected=1)
assert_expectation('size', calculated=size('A simple string'), expected=15)
assert_expectation('size', calculated=size('ho ho ho'), expected=8)
# write your own test


# 6.
# Create a function that takes a list and returns its size
def list_size(list):


assert_expectation('list_size', calculated=list_size([100]),   expected=1)
assert_expectation('list_size', calculated=list_size(['a', 'b', 'c']), expected=3)
assert_expectation('list_size', calculated=list_size([1, 'b', 'c', 10]), expected=4)
# write your own test

# 6.
# Create a function that takes a map and returns the number of keys
def map_size(map):


assert_expectation('map_size', calculated=map_size({'a': 1}),   expected=1)
assert_expectation('map_size', calculated=map_size({'a': 1, 'b': 2, 'c': 3}), expected=3)
assert_expectation('map_size', calculated=map_size({'cd': 1, 'll': 2, 'gg': 3, 'hh': 5}), expected=4)
# write your own test