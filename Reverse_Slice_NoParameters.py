
def reverse_string():
    user_input = input("Enter a string: ")
    reversed = user_input[::-1]
    print("Input :",user_input)
    print("Output :",reversed)
    return reversed
reverse_string()