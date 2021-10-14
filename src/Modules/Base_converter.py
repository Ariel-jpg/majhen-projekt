def get_hex_character(value):
    value = str(value)
    equivalences = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    }

    if value in equivalences:
        return equivalences[value]
    else:
        return value

def decimal_to_hexadecimal(decimal):
    hexadecimal = ""

    while decimal > 0:
        residue = decimal % 16
        true_character = get_hex_character(residue)
        hexadecimal = true_character + hexadecimal
        decimal = int(decimal / 16)

    return hexadecimal