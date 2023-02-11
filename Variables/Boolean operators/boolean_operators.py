two = 2
three = 3

is_equal = two == three
print(f"is_equal = {is_equal}")

is_false = is_equal is not is_equal
print(f"is_false = {is_false}")

is_true = is_false is is_equal
print(f"is_true = {is_true}")
