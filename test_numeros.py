import pytest
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


def test_decimal_a_binario_texto_invalido():
    with pytest.raises(TypeError):
        decimal_a_binario("texto")


def test_hexadecimal_a_decimal_char_invalido():
    with pytest.raises(ValueError):
        hexadecimal_a_decimal("G123")


def test_decimal_a_binario_negativo():
    assert decimal_a_binario(-1) == ""


def test_decimal_a_hexadecimal_negativo():
    assert decimal_a_hexadecimal(-10) == ""


def test_decimal_a_octal_negativo():
    assert decimal_a_octal(-100) == ""
