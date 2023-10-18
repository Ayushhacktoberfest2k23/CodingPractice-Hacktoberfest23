def length_of_last_word(s):
    # Strip the string to remove leading and trailing spaces
    s = s.strip()
    # Split the string into words
    words = s.split()
    # Check if there are any words in the string
    if words:
        # Return the length of the last word
        return len(words[-1])
    else:
        return 0

# Example usage
string = "Hello World"
length = length_of_last_word(string)
print(f"The length of the last word in '{string}' is {length}.")
