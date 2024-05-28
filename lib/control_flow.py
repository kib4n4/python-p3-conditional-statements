def admin_login(username, password):
    """
    Check if the given username and password match the admin credentials.

    Args:
        username (str): The username to be checked.
        password (str): The password to be checked.

    Returns:
        str: "Access granted" if the credentials are valid, "Access denied" otherwise.
    """
    # Convert the username to lowercase to make the check case-insensitive
    if (username.lower() == "admin") and (password == "12345"):
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    """
    Determine the weather description based on the given temperature.

    Args:
        temperature (float): The temperature value.

    Returns:
        str: The weather description based on the temperature.
    """
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    """
    Implement the FizzBuzz logic for the given number.

    Args:
        num (int): The number to be processed.

    Returns:
        str or int: "FizzBuzz" if the number is a multiple of 3 and 5,
                    "Fizz" if the number is a multiple of 3,
                    "Buzz" if the number is a multiple of 5,
                    the number itself for all other cases.
    """
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def calculator(operation, num1, num2):
    """
    Perform the specified arithmetic operation on the given numbers.

    Args:
        operation (str): The arithmetic operation to be performed (+, -, *, /).
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float or None: The result of the arithmetic operation, or None if the operation is not supported.
    """
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
