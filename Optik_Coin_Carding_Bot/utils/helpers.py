from datetime import datetime
import re
import locale
locale.setlocale(locale.LC_ALL, '')  # Use system locale for currency formatting

def format_timestamp(timestamp, format_str="%Y-%m-%d %H:%M:%S"):
    """
    Format a timestamp into a readable string.

    :param timestamp: A datetime object or a string that can be parsed into a datetime
    :param format_str: The desired output format (default: YYYY-MM-DD HH:MM:SS)
    :return: Formatted timestamp string
    """
    if isinstance(timestamp, str):
        timestamp = datetime.fromisoformat(timestamp)
    return timestamp.strftime(format_str)

def validate_card_number(card_number):
    """
    Validate a credit card number using the Luhn algorithm.

    :param card_number: The card number to validate
    :return: True if valid, False otherwise
    """
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10 == 0

def mask_card_number(card_number):
    """
    Mask a credit card number, showing only the last 4 digits.
    If less than 4 digits, returns masked version of input.

    :param card_number: The full card number
    :return: Masked card number string
    """
    if not isinstance(card_number, str):
        card_number = str(card_number)
    if len(card_number) < 4:
        return "X" * len(card_number)
    return "X" * (len(card_number) - 4) + card_number[-4:]

def is_valid_expiry(month: str, year: str) -> bool:
    """
    Validate expiration month and year.

    :param month: Expiration month (string)
    :param year: Expiration year (2-digit string)
    :return: True if valid future expiry date
    """
    if not (month.isdigit() and year.isdigit()):
        return False
    month = int(month)
    year = int(year)
    if not (1 <= month <= 12):
        return False
    current_year = int(datetime.now().strftime("%y"))
    return year >= current_year

def parse_card_info(card_string):
    """
    Parse a card string in the format XXXXXXXXXXXXXXXX|MM|YY|CVV.

    :param card_string: The card information string
    :return: A dictionary with parsed information or None if invalid format
    """
    parts = card_string.split("|")
    if len(parts) != 4:
        return None

    card_number, month, year, cvv = parts
    if not (card_number.isdigit() and month.isdigit() and year.isdigit() and cvv.isdigit()):
        return None

    if not is_valid_expiry(month, year):
        return None

    return {
        "card_number": card_number,
        "expiry_month": month,
        "expiry_year": year,
        "cvv": cvv
    }

def is_valid_bin(bin_number):
    """
    Check if a BIN (Bank Identification Number) is valid.

    :param bin_number: The BIN to check
    :return: True if valid, False otherwise
    """
    return bool(re.match(r"^\d{6}$", bin_number))

def format_currency(amount, currency="USD"):
    """
    Format a currency amount using locale if possible.

    :param amount: The amount to format
    :param currency: The currency code (default: USD)
    :return: Formatted currency string
    """
    try:
        return locale.currency(amount, grouping=True)
    except Exception:
        return f"{amount:.2f} {currency}"

def truncate_text(text, max_length=100, ellipsis="..."):
    """
    Truncate text to a maximum length.

    :param text: The text to truncate
    :param max_length: Maximum length of the truncated text
    :param ellipsis: String to append if text is truncated
    :return: Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(ellipsis)] + ellipsis

def obfuscate_email(email):
    """
    Obfuscate an email address by hiding the part before '@'.
    e.g., jdoe@example.com → ****@example.com

    :param email: The email to obfuscate
    :return: Obfuscated email string
    """
    if "@" in email:
        name, domain = email.split("@", 1)
        return "*" * len(name) + "@" + domain
    return email

def clean_input(input_str):
    """
    Strip extra whitespace and normalize input string.

    :param input_str: Raw user input
    :return: Cleaned input
    """
    return input_str.strip()

def normalize_bin(bin_str):
    """
    Normalize BIN string to 6-digit format.

    :param bin_str: Input BIN string
    :return: Normalized BIN string or None
    """
    digits = re.sub(r"\D", "", bin_str)
    return digits[:6] if len(digits) >= 6 else None

# Add more utility functions as needed
