import requests

def buscar_repositorios_github(usuario):
    url = f"https://api.github.com/users/{usuario}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()
        if repos:
            print(f"Usuário '{usuario}' tem {len(repos)} repositórios:")
            for repo in repos:
                print(f" - {repo['name']}")
        else:
            print("Usuário não tem repositórios públicos.")
    else:
        print(f"Erro ao buscar repositórios: {response.status_code}")

# Exemplo de uso
usuario_github = input("Digite o nome de usuário do GitHub: ")
buscar_repositorios_github(usuario_github)
