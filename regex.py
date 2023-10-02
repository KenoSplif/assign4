import re


def validate_email(email_address):
    criteria = r'^[A-Za-z0-9]+([._][a-z0-9]+)*@[A-Za-z0-9]+\.[A-Za-z0-9]{2,3}$'
    if re.match(criteria, email_address):
        print(f"{email_address} is a valid email address.")
        return True
    else:
        print(f"{email_address} is not a valid email address.")
        return False


def validate_phone_number(phone_number):
    criteria = r"^\(\d{3}\) \d{3}-\d{4}$|^\d{3}-\d{3}-\d{4}$"
    if re.match(criteria, phone_number):
        print(f"{phone_number} is a valid phone number.")
        return True
    else:
        print(f"{phone_number} is not a valid phone number.")
        return False

email1 = "example1@gmail.com"
email2 = "invalid.Example@email.cm"

status1 = validate_email(email1)
status2 = validate_email(email2)

phone1 = "(123) 456-7890"
phone2 = "78787888887777"
status3 = validate_phone_number(phone1)
status4 = validate_phone_number(phone2)

