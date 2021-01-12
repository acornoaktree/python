from assertive import assert_expectation

# 1.
# Create a function that takes a number and returns its possible take_five
# 1 -> [1]
# 2 -> [1, 2]
# 3 -> [1, 3]
# 4 -> [1, 2, 4]
# 5 -> [1, 5]
# 6 -> [1, 2, 3, 6]
def factors(number):
    pass


assert_expectation('factors', calculated=factors(1), expected=[1])
assert_expectation('factors', calculated=factors(2), expected=[1, 2])
assert_expectation('factors', calculated=factors(4), expected=[1, 2, 4])
# write your own test


# 2.
# Create a function that takes a number and takes away 5 from it
def take_five(number):
    pass


assert_expectation('take_five', calculated=take_five(1), expected=-4)
assert_expectation('take_five', calculated=take_five(2), expected=-3)
assert_expectation('take_five', calculated=take_five(4), expected=-1)
# write your own test


# 3.
# Create a function that takes a string and reverses it
def reverse_a_string(string):
    pass


assert_expectation('reverse_a_string', calculated=reverse_a_string('conor'), expected='ronoc')
assert_expectation('reverse_a_string', calculated=reverse_a_string('jam'), expected='maj')
assert_expectation('reverse_a_string', calculated=reverse_a_string('slept'), expected='tpels')
# write your own test


# 4.
# Create a function that takes a string and reverses it
def reverse_a_string(string):
    pass


assert_expectation('reverse_a_string', calculated=reverse_a_string('conor'), expected='ronoc')
assert_expectation('reverse_a_string', calculated=reverse_a_string('jam'), expected='maj')
assert_expectation('reverse_a_string', calculated=reverse_a_string('slept'), expected='tpels')
# write your own test


# 5.
# Create a function that takes a string and returns all the letters as uppercase
def to_uppercase(string):
    pass


assert_expectation('to_uppercase', calculated=to_uppercase('conor'), expected='CONOR')
assert_expectation('to_uppercase', calculated=to_uppercase('jam'), expected='JAM')
assert_expectation('to_uppercase', calculated=to_uppercase('slept'), expected='SLEPT')
# write your own test



# 6.
# Create a function that that multiplies a number 4 then adds 6 then divides by 3 and multiples by 5
def do_maths(number):
    pass


assert_expectation('do_maths', calculated=do_maths(3), expected=30)
assert_expectation('do_maths', calculated=do_maths(4), expected=36.666666666666664)
assert_expectation('do_maths', calculated=do_maths(5), expected=43.33333333333333)
# write your own test
