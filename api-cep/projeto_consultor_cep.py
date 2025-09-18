import requests

def consulta_enderecos(dados_do_endereco):
    print("\n--- Endereço Encontrado ---")
    print(f"Logradouro: {dados_endereco.get('logradouro', 'N/A')}")
    print(f"Bairro: {dados_endereco.get('bairro', 'N/A')}")
    print(f"Cidade: {dados_endereco.get('localidade', 'N/A')}")
    print(f"Estado: {dados_endereco.get('uf', 'N/A')}")
    print(f"CEP: {dados_endereco.get('cep', 'N/A')}")
    print("---------------------------\n")
print("Bem vindo ao Consultor de Endereços!")
print("Digite o CEP no formato 00000000 ou 'sair' para terminar.")
while True:
    cep_input = input("Insira o CEP que deseja consultar: ")
    if cep_input.lower() == 'sair':
        break

    url = f"https://viacep.com.br/ws/{cep_input}/json/"

    try:
        resposta = requests.get(url)

        dados_endereco = resposta.json()

        if dados_endereco.get('erro'):
            print("CEP não encontrado ou inválido. Tente novamente.")
        else:
            consulta_enderecos(dados_endereco)
            
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")

print("Fim do programa.")

