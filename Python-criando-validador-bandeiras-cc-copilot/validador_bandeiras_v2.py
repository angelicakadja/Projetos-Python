# Função para validar a bandeira do cartão de crédito
def validar_bandeira(cartao: str) -> str:
    """
    Função para identificar a bandeira do cartão de crédito com base no número do cartão.
    """
    bandeiras = {
        "Visa": [4],
        "MasterCard": [51, 52, 53, 54, 55],
        "American Express": [34, 37],
        "Discover": [6011, 622126, 622925, 644, 645, 646, 647, 648, 649, 65]
    }
    
    # Verificar se o número do cartão começa com um dos prefixos conhecidos
    for bandeira, prefixos in bandeiras.items():
        if any(cartao.startswith(str(prefixo)) for prefixo in prefixos):
            return bandeira
    return "Bandeira não identificada"

# Exemplo de uso
cartao_exemplo = "4111111111111111"  # Cartão Visa
print(validar_bandeira(cartao_exemplo))