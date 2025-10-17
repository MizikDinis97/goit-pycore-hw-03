import re

def normalize_phone(phone_number):
    phone_number = phone_number.strip()
    phone_number = re.sub(r"[^0-9+]", "", phone_number)
    if phone_number.startswith("+38"):
        return phone_number
    elif phone_number.startswith("38"):
        return "+" + phone_number
    elif phone_number.startswith("0"):
        return "+38" + phone_number
    else:
        return "+38" + phone_number
    
numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11 ",
    "  +380501112233  ",
    "  0501112233",
    "  +380501112233 ",
    "  38(050)1112233 ",
]
for number in numbers:
    print(normalize_phone(number))