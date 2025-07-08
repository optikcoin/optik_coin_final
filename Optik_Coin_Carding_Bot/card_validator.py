def luhn_checksum(card_number):
    """
    Compute the Luhn checksum for a card number.
    Returns True if the card number is valid, False otherwise.
    """
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10 == 0

def is_valid_card(card_number):
    """
    Validate a card number using the Luhn algorithm.
    """
    card_number = card_number.replace(" ", "")
    return card_number.isdigit() and 13 <= len(card_number) <= 19 and luhn_checksum(card_number)