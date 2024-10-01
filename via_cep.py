import requests

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        if "erro" not in dados:
            endereco = f"{dados['logradouro']} - {dados['bairro']}, {dados['localidade']} - {dados['uf']}, {dados['cep']}"
            print(endereco)
        else:
            print("CEP inválido.")
    else:
        print(f"Erro ao buscar CEP: {response.status_code}")

# Exemplo de uso
cep = input("Digite o CEP: ")
buscar_cep(cep)
