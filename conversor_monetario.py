"""
Conversor Monetário - Converte valores entre diferentes moedas.
Utiliza taxas de câmbio fixas para fins de teste e demonstração.
"""

# Taxas de câmbio em relação ao USD 
TAXAS_CAMBIO = {
    "USD": 1.0,
    "BRL": 5.65,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 149.50,
    "ARS": 910.0,
    "CAD": 1.37,
}

MOEDAS_SUPORTADAS = list(TAXAS_CAMBIO.keys())


def converter(valor: float, origem: str, destino: str) -> float:

    if not isinstance(valor, (int, float)):
        raise TypeError(f"O valor deve ser numérico, recebeu {type(valor).__name__}")

    if valor < 0:
        raise ValueError("O valor não pode ser negativo")

    origem = origem.upper().strip()
    destino = destino.upper().strip()

    if origem not in TAXAS_CAMBIO:
        raise KeyError(f"Moeda de origem '{origem}' não suportada. Moedas disponíveis: {MOEDAS_SUPORTADAS}")

    if destino not in TAXAS_CAMBIO:
        raise KeyError(f"Moeda de destino '{destino}' não suportada. Moedas disponíveis: {MOEDAS_SUPORTADAS}")

    # Converte origem -> USD -> destino
    valor_em_usd = valor / TAXAS_CAMBIO[origem]
    valor_convertido = valor_em_usd * TAXAS_CAMBIO[destino]

    return round(valor_convertido, 2)


def obter_taxa(origem: str, destino: str) -> float:
    """
    Retorna a taxa de câmbio direta entre duas moedas.

    Returns:
        Taxa de conversão (1 unidade de origem = X unidades de destino).

    Raises:
        KeyError: Se a moeda não for suportada.
    """
    origem = origem.upper().strip()
    destino = destino.upper().strip()

    if origem not in TAXAS_CAMBIO:
        raise KeyError(f"Moeda '{origem}' não suportada")

    if destino not in TAXAS_CAMBIO:
        raise KeyError(f"Moeda '{destino}' não suportada")

    return round(TAXAS_CAMBIO[destino] / TAXAS_CAMBIO[origem], 6)


def listar_moedas() -> list:
    """Retorna a lista de moedas suportadas."""
    return MOEDAS_SUPORTADAS.copy()
