from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
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

def gerar_relatorio_html(dados, nome_arquivo):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            # Início do HTML
            arquivo.write("""
            <html>
            <head>
                <meta charset="utf-8">
                <style>
                    body { 
                        font-family: Arial, sans-serif; 
                        margin: 40px; 
                    }
                    .header { 
                        text-align: center; 
                        margin-bottom: 30px; 
                    }
                    .registro { 
                        border: 1px solid #ddd; 
                        margin: 10px 0; 
                        padding: 10px; 
                    }
                    .footer { 
                        text-align: center; 
                        margin-top: 30px; 
                    }
                </style>
            </head>
            <body>
            """)

            # Cabeçalho
            arquivo.write(f"""
                <div class="header">
                    <h1>RELATÓRIO</h1>
                    <p>Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
                </div>
            """)

            # Registros
            for i, item in enumerate(dados, 1):
                arquivo.write(f"""
                <div class="registro">
                    <h3>Registro #{i}</h3>
                    <p><strong>Nome:</strong> {item['nome']}</p>
                    <p><strong>Idade:</strong> {item['idade']}</p>
                    <p><strong>Cidade:</strong> {item['cidade']}</p>
                </div>
                """)

            # Rodapé
            arquivo.write(f"""
                <div class="footer">
                    <p>Total de registros: {len(dados)}</p>
                    <p>Fim do Relatório</p>
                </div>
            </body>
            </html>
            """)

        print(f"\nRelatório HTML gerado com sucesso: {nome_arquivo}")

    except Exception as e:
        print(f"\nErro ao gerar relatório HTML: {e}")

def gerar_relatorio_pdf(dados, nome_arquivo):
    try:
        c = canvas.Canvas(nome_arquivo, pagesize=letter)
        width, height = letter
        
        # Título
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(width/2, height-50, "RELATÓRIO")
        
        # Data
        c.setFont("Helvetica", 10)
        c.drawCentredString(width/2, height-70, 
            f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        
        # Registros
        y = height - 120  # Aumentei o espaço inicial
        c.setFont("Helvetica", 12)
        
        for i, item in enumerate(dados, 1):
            if y < 100:  # Nova página se necessário
                c.showPage()
                y = height - 100
                c.setFont("Helvetica", 12)  # Precisa resetar a fonte em nova página
            
            # Ajustei o posicionamento e espaçamento
            c.drawString(50, y, f"Registro #{i}")
            y -= 20
            c.drawString(70, y, f"Nome: {item['nome']}")
            y -= 20
            c.drawString(70, y, f"Idade: {str(item['idade'])}")
            y -= 20
            c.drawString(70, y, f"Cidade: {item['cidade']}")
            y -= 30  # Espaço entre registros
            
            # Linha separadora
            c.line(50, y, width-50, y)
            y -= 20  # Espaço após a linha
        
        # Rodapé
        c.setFont("Helvetica", 10)
        c.drawCentredString(width/2, 30, f"Total de registros: {len(dados)}")
        c.drawCentredString(width/2, 15, "=== FIM DO RELATÓRIO ===")
        
        c.save()
        print(f"\nRelatório PDF gerado com sucesso: {nome_arquivo}")
    
    except Exception as e:
        print(f"\nErro ao gerar relatório PDF: {e}")

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
    dados = []
    while True:
        print("\n=== Gerador de Relatórios ===")
        print("1. Inserir dados")
        print("2. Gerar relatório TXT")
        print("3. Gerar relatório HTML")
        print("4. Gerar relatório PDF")
        print("5. Sair")

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
            if not dados:
                print("\nNenhum dado inserido!")
                continue

            nome_arquivo = input("\nNome do arquivo (ex: relatorio.html): ").strip()
            if not nome_arquivo.endswith('.html'):
                nome_arquivo += '.html'

            gerar_relatorio_html(dados, nome_arquivo)

        elif opcao == "4":
            if not dados:
                print("\nNenhum dado inserido!")
                continue

            nome_arquivo = input("\nNome do arquivo (ex: relatorio.pdf): ").strip()
            if not nome_arquivo.endswith('.pdf'):
                nome_arquivo += '.pdf'

            gerar_relatorio_pdf(dados, nome_arquivo)

        elif opcao == "5":
            print("\nObrigado por usar o Gerador de Relatórios!")
            break

        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    main()