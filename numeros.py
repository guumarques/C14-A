
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


def binario_a_decimal(numero):
    decimal = 0
    potencia = 0
    while numero > 0:
        decimal += (numero % 10) * (2 ** potencia)
        numero = numero // 10
        potencia += 1
    return decimal


def octal_a_decimal(numero):
    decimal = 0
    potencia = 0
    while int(numero) > 0:
        decimal += (int(numero) % 10) * (8 ** potencia)
        numero = int(numero) // 10
        potencia += 1
    return decimal


def hexadecimal_a_decimal(numero):
    decimal = 0
    potencia = 0

    for caracter in str(numero)[::-1]:
        match caracter.upper():
            case "A":
                decimal += 10 * (16 ** potencia)
            case "B":
                decimal += 11 * (16 ** potencia)
            case "C":
                decimal += 12 * (16 ** potencia)
            case "D":
                decimal += 13 * (16 ** potencia)
            case "E":
                decimal += 14 * (16 ** potencia)
            case "F":
                decimal += 15 * (16 ** potencia)
            case _:
                decimal += int(caracter) * (16 ** potencia)
        potencia += 1

    return decimal
