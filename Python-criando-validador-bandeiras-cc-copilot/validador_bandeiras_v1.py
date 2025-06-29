def verificar_bandeira(numero_cartao):
    numero_cartao = str(numero_cartao)
    
    if numero_cartao.startswith('4'):
        return "Visa"
    elif numero_cartao.startswith(('51', '55', '2221', '2720')):
        return "MasterCard"
    # elif 4011 >= int(numero_cartao[:4]) <= 4389:
    #     return "Elo"
    elif numero_cartao.startswith('34') or numero_cartao.startswith('37'):
        return "American Express"
    elif numero_cartao.startswith(('6011', '65','644','645','646','647','648','649')):
        return "Discover"
    elif numero_cartao.startswith('6062'):
        return "Hipercard"
    elif numero_cartao.startswith('36'):
        return "Diners Club"
    else:
        return "Desculpe, não aceitamos essa bandeira!"

# Exemplo de uso
numero_cartao = input("Digite o número do cartão de crédito: ")
bandeira = verificar_bandeira(numero_cartao)
print(f"A bandeira do cartão é: {bandeira}")
