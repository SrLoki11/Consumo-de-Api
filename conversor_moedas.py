import requests

def converter_moeda(valor_reais):
    api_key = "sua_api_key_aqui"
    url = f"https://api.hgbrasil.com/finance?key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()['results']['currencies']
        dolar = dados['USD']['buy']
        euro = dados['EUR']['buy']
        
        valor_em_dolar = valor_reais / dolar
        valor_em_euro = valor_reais / euro

        print(f"{valor_reais} R$ = {valor_em_dolar:.2f} USD")
        print(f"{valor_reais} R$ = {valor_em_euro:.2f} EUR")
    else:
        print(f"Erro ao acessar a API: {response.status_code}")

# Exemplo de uso
valor = float(input("Digite o valor em reais (R$): "))
converter_moeda(valor)
