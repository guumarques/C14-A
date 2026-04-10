
import pytest
from conversor_monetario import converter, obter_taxa, listar_moedas, TAXAS_CAMBIO

def test_brl_para_usd():
    """Converte 100 BRL para USD."""
    resultado = converter(100, "BRL", "USD")
    esperado = round(100 / 5.65, 2)
    assert resultado == esperado


def test_usd_para_brl():
    """Converte 50 USD para BRL."""
    resultado = converter(50, "USD", "BRL")
    esperado = round(50 * 5.65, 2)
    assert resultado == esperado


def test_eur_para_jpy():
    """Converte 200 EUR para JPY."""
    resultado = converter(200, "EUR", "JPY")
    valor_usd = 200 / 0.92
    esperado = round(valor_usd * 149.50, 2)
    assert resultado == esperado


def test_mesma_moeda():
    """Converter uma moeda para ela mesma deve retornar o mesmo valor."""
    assert converter(123.45, "BRL", "BRL") == 123.45


def test_valor_zero():
    """Converter zero deve retornar zero."""
    assert converter(0, "USD", "EUR") == 0.0


def test_gbp_para_cad():
    """Converte 500 GBP para CAD."""
    resultado = converter(500, "GBP", "CAD")
    valor_usd = 500 / 0.79
    esperado = round(valor_usd * 1.37, 2)
    assert resultado == esperado


def test_ars_para_brl():
    """Converte 10000 ARS para BRL."""
    resultado = converter(10000, "ARS", "BRL")
    valor_usd = 10000 / 910.0
    esperado = round(valor_usd * 5.65, 2)
    assert resultado == esperado


def test_obter_taxa_usd_brl():
    """A taxa USD->BRL deve ser 5.65."""
    taxa = obter_taxa("USD", "BRL")
    assert taxa == 5.65


def test_obter_taxa_inversa():
    """A taxa BRL->USD deve ser o inverso de USD->BRL."""
    taxa = obter_taxa("BRL", "USD")
    esperado = round(1 / 5.65, 6)
    assert taxa == esperado


def test_listar_moedas():
    """Deve retornar todas as moedas registradas."""
    moedas = listar_moedas()
    assert "USD" in moedas
    assert "BRL" in moedas
    assert "EUR" in moedas
    assert len(moedas) == len(TAXAS_CAMBIO)

def test_valor_negativo():
    """Deve lançar ValueError ao converter valor negativo."""
    with pytest.raises(ValueError, match="negativo"):
        converter(-100, "USD", "BRL")


def test_valor_tipo_string():
    """Deve lançar TypeError ao receber string como valor."""
    with pytest.raises(TypeError, match="numérico"):
        converter("cem", "USD", "BRL")


def test_valor_tipo_none():
    """Deve lançar TypeError ao receber None como valor."""
    with pytest.raises(TypeError):
        converter(None, "USD", "BRL")


def test_moeda_origem_invalida():
    """Deve lançar KeyError para moeda de origem não suportada."""
    with pytest.raises(KeyError, match="origem"):
        converter(100, "XYZ", "BRL")


def test_moeda_destino_invalida():
    """Deve lançar KeyError para moeda de destino não suportada."""
    with pytest.raises(KeyError, match="destino"):
        converter(100, "USD", "ABC")


def test_ambas_moedas_invalidas():
    """Deve lançar KeyError quando ambas as moedas são inválidas (origem primeiro)."""
    with pytest.raises(KeyError, match="origem"):
        converter(100, "FOO", "BAR")


def test_moeda_case_insensitive():
    """Deve aceitar moedas em lowercase e retornar resultado correto."""
    resultado_upper = converter(100, "USD", "BRL")
    resultado_lower = converter(100, "usd", "brl")
    assert resultado_upper == resultado_lower


def test_moeda_com_espacos():
    """Deve aceitar moedas com espaços em volta."""
    resultado = converter(100, " USD ", " BRL ")
    esperado = converter(100, "USD", "BRL")
    assert resultado == esperado


def test_obter_taxa_moeda_invalida():
    """obter_taxa deve lançar KeyError para moeda inexistente."""
    with pytest.raises(KeyError):
        obter_taxa("USD", "ZZZ")


def test_valor_tipo_lista():
    """Deve lançar TypeError ao receber lista como valor."""
    with pytest.raises(TypeError):
        converter([100], "USD", "BRL")
