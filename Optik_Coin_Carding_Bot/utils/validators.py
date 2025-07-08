def is_valid_bin(bin_str):
    """
    Validate if the input string is a valid BIN (6 to 8 digits).
    """
    return bin_str.isdigit() and 6 <= len(bin_str) <= 8

def is_valid_username(username):
    """
    Validate if the username is alphanumeric and 3-32 characters.
    """
    return username.isalnum() and 3 <= len(username) <= 32