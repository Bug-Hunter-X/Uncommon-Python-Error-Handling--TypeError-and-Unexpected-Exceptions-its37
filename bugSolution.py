def function_with_improved_error_handling(x):
    if not isinstance(x,(int,float)):
        return "Invalid input type. Please provide an integer or a float."
    try:
        result = 10 / x
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

print(function_with_improved_error_handling(0)) # Output: Division by zero
print(function_with_improved_error_handling(2))  # Output: 5.0
print(function_with_improved_error_handling("hello")) # Output: Invalid input type. Please provide an integer or a float.
print(function_with_improved_error_handling([1,2])) # Output: Invalid input type. Please provide an integer or a float.