from assertive import assert_expectation

# 1. 
# Create a function that takes a number and returns True if it is positive
# -3 -> False
# 4 -> True
# 0 -> True
# -13 -> False
def is_positive(number):
    pass


assert_expectation('is_positive', calculated=is_positive(-3), expected=False)
assert_expectation('is_positive', calculated=is_positive(4), expected=True)
assert_expectation('is_positive', calculated=is_positive(0), expected=True)

# 2. 
# Create a function that takes a number and returns a True if it is negative
# -3 -> True
# 4 -> False
# 0 -> False
# -13 -> True
def is_negative(number):
    pass


assert_expectation('is_negative', calculated=is_negative(-3), expected=True)
assert_expectation('is_negative', calculated=is_negative(4), expected=False)
assert_expectation('is_negative', calculated=is_negative(0), expected=False)

# 3.
# Create a function that takes a string and reverses it
def reverse_a_string(string):
    pass
    

reverse_a_string('hi')

assert_expectation('reverse_a_string', calculated=reverse_a_string('conor'), expected='ronoc')
assert_expectation('reverse_a_string', calculated=reverse_a_string('jam'), expected='maj')
assert_expectation('reverse_a_string', calculated=reverse_a_string('slept'), expected='tpels')
# write your own test
assert_expectation('reverse_a_string', calculated=reverse_a_string('darragh'), expected='hgarrad')
assert_expectation('reverse_a_string', calculated=reverse_a_string('seán'), expected='náes')
assert_expectation('reverse_a_string', calculated=reverse_a_string('saoirse'), expected='esrioas')



# 4. 
# Create a function that takes a decimal and returns a number rounded down to the nearest natural(whole) number
# 1.22324 -> 1
# 4.999 -> 4
# 123.123 -> 123
def floor(decimal):
    pass


assert_expectation('floor', calculated=floor(1.22324), expected=1)
assert_expectation('floor', calculated=floor(4.999), expected=4)
assert_expectation('floor', calculated=floor(123.123), expected=123)
# write your own test


# 5. 
# Create a function that takes a decimal and returns a the number rounded up to the nearest natural(whole) number
# 1.22324 -> 2
# 4.999 -> 5
# 123.123 -> 124
def ceil(decimal):
    pass


assert_expectation('ceil', calculated=ceil(1.22324), expected=2)
assert_expectation('ceil', calculated=ceil(4.999), expected=5)
assert_expectation('ceil', calculated=ceil(123.123), expected=124)
# write your own test


# 6. 
# Create a function that takes a number and returns if it is prime or not
# 1 -> False
# 4 -> False
# 3 -> True
# 17 -> True
# 123 -> False
def is_prime(number):
    pass


assert_expectation('is_prime', calculated=is_prime(1), expected=False)
assert_expectation('is_prime', calculated=is_prime(4), expected=False)
assert_expectation('is_prime', calculated=is_prime(17), expected=True)
assert_expectation('is_prime', calculated=is_prime(123), expected=False)
assert_expectation('is_prime', calculated=is_prime(3), expected=True)
# write your own test
