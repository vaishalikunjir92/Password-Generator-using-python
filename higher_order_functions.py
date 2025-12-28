def validate(data, *validators):
    for validator in validators:
        if not validator(data):
            return False
        return True

    # Validators
is_non_empty = lambda x: bool(x)
is_alpha = lambda x: x.isalpha()

# Validate input
input_data = "Python"
is_valid =  validate(input_data, is_alpha,is_non_empty)
print(is_valid) # Output: True

