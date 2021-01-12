def assert_expectation(name, calculated, expected):
    if calculated != expected:
        raise AssertionError(f'Function: {name} EXPECTED: {expected} CALCULATED: {calculated}')
