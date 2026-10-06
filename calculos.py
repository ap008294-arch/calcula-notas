def calcular_media_ponderada(n1, n2, n3):
    """Calcula a média ponderada com os pesos 2, 3 e 5."""
    peso1, peso2, peso3 = 2, 3, 5
    media = ((n1 * peso1) + (n2 * peso2) + (n3 * peso3)) / (peso1 + peso2 + peso3)
    return media