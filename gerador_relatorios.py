from datetime import datetime

def gerar_relatorio_txt(dados, nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            #cabeçalho
            arquivo.write("=" * 50 + "\n")
            arquivo.write("RELATÓRIO SIMPLES\n")
            arquivo.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
            arquivo.write("=" * 50  + "\n\n")

            #dados
            for i, item in enumerate(dados, 1):
                arquivo.write(f"Registro #{i}\n")
                arquivo.write(f"Nome: {item['nome']}\n")
                arquivo.write(f"Idade: {item['idade']}\n")
                arquivo.write(f"Cidade: {item['cidade']}\n")
                arquivo.write("-" * 30 + "\n\n")

            #rodape
            arquivo.write("\n" + "=" * 50 + "\n")
            arquivo.write(f"Total de registros: {len(dados)}\n")
            arquivo.write("=== FIM DO RELATÓRIO ===\n")

        print(f"\nRelatório gerado com sucesso: {nome_arquivo}")

    except Exception as e:
        print(f"Erro ao gerar relatório: {e}")

def inserir_dados():
    dados = []
    while True:
        print("\n=== Inserir Novo Registro ===")
        nome = input("Nome (ou Enter para parar): ").strip()

        if not nome:
            break

        try:
            idade = int(input("Idade: "))
            cidade = input("Cidade: ").strip()

            dados.append({
                "nome": nome,
                "idade": idade,
                "cidade": cidade
            })

            print("\nRegistro adicionado com sucesso!")

        except ValueError:
            print("\nIdade inválida! Registro não adicionado!")

    return dados

def main():
    while True:
        print("\n=== Gerador de Relatórios ===")
        print("1. Inserir dados")
        print("2.Gerar relatório")
        print("3. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            dados = inserir_dados()
        
        elif opcao == "2":
            if not dados:
                print("\nNenhum dado inserido!")
                continue

            nome_arquivo = input("\nNome do arquivo (ex: relatorio.txt): ").strip()
            if not nome_arquivo.endswith('.txt'):
                nome_arquivo += '.txt'

            gerar_relatorio_txt(dados, nome_arquivo)

        elif opcao == "3":
            print("\nObrigado por usar o Gerador de Relatórios!")
            break

        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    main()