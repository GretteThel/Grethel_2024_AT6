from main import UserInputValidator

# Create instances of UserInputValidator
validator1 = UserInputValidator()
validator2 = UserInputValidator()

# Example
print(validator1.validate_positive_integers(["12", "-4", "0", "45", "abc"]))
print(validator2.validate_positive_integers(["100", "xyz", "34", ""]))
