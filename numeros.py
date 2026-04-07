def decimal_a_binario(numero):
    if numero == 0:
        return 0

    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    return binario


def decimal_a_octal(numero):
    if numero == 0:
        return 0

    octal = ""
    while numero > 0:
        octal = str(numero % 8) + octal
        numero = numero // 8
    return octal

def decimal_a_hexadecimal(numero):
    if numero == 0:
        return 0

    hexadecimal = ""
    while numero > 0:
        resto = numero % 16
        # caso 10 = A
        match resto:
            case 10:
                hexadecimal = "A" + hexadecimal
            case 11:
                hexadecimal = "B" + hexadecimal
            case 12:
                hexadecimal = "C" + hexadecimal
            case 13:
                hexadecimal = "D" + hexadecimal
            case 14:
                hexadecimal = "E" + hexadecimal
            case 15:
                hexadecimal = "F" + hexadecimal
            case _:
                hexadecimal = str(resto) + hexadecimal

        numero = numero // 16
    return hexadecimal
