from numeros import decimal_a_binario, decimal_a_hexadecimal, decimal_a_octal, hexadecimal_a_decimal, octal_a_decimal


def test_decimal_to_binario():
    assert decimal_a_binario(4) == "100"


def test_decimal_to_binario_zero():
    assert decimal_a_binario(0) == 0


def test_decimal_to_hexadecimal():
    assert decimal_a_hexadecimal(51966) == "CAFE"


def test_hexadecimal_to_decimal():
    assert hexadecimal_a_decimal("CAFE") == 51966


def test_decimal_to_octal():
    assert decimal_a_octal(64) == "100"


def test_octal_to_decimal():
    assert octal_a_decimal("100") == 64
