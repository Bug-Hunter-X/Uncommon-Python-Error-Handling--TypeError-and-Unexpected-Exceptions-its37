def function_with_uncommon_error(x):
    try:
        result = 10 / x
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        if isinstance(x, str):
            return "Cannot divide by string"
        else:
            return "Unknown TypeError"
except Exception as e:
        return f"An unexpected error occurred: {e}"

print(function_with_uncommon_error(0)) # Output: Division by zero
print(function_with_uncommon_error(2))  # Output: 5.0
print(function_with_uncommon_error("hello")) # Output: Cannot divide by string
print(function_with_uncommon_error([1,2])) # Output: An unexpected error occurred: unsupported operand type(s) for /: 'int' and 'list'