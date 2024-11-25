from main import UserInputValidator

# Create instances of UserInputValidator
validator1 = UserInputValidator()
validator2 = UserInputValidator()

# Example usage
result1 = validator1.validate_positive_integers(["12", "-4", "0", "45", "abc"])
result2 = validator2.validate_positive_integers(["100", "xyz", "34", ""])

# Display results
validator1.display_message()
print("Validator 1 Results:", result1)

validator2.display_message()
print("Validator 2 Results:", result2)
