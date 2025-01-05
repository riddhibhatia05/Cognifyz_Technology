def reverse_string(input_string):
    """
    Takes a string as input and returns the reverse of that string.
    :param input_string: str - The string to be reversed.
    :return: str - The reversed string.
    """
    # Use slicing to reverse the string. 
    # [::-1] means start from the end of the string and step backwards.
    reversed_string = input_string[::-1]
    
    # Return the reversed string
    return reversed_string

# Example usage
input_text = input("Enter a string: ")  # Define the input string
reversed_text = reverse_string(input_text)  # Call the function to reverse the string
print("Reversed string:", reversed_text)  # Print the result
