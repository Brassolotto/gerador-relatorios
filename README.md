# Gerador de Relatórios em Python

## 📝 Descrição
Um aplicativo de linha de comando que gera relatórios em múltiplos formatos (TXT, HTML e PDF) a partir de dados inseridos pelo usuário.

## 🚀 Funcionalidades
- Inserção manual de dados
- Geração de relatórios em três formatos:
  - TXT (texto simples)
  - HTML (formatado para web)
  - PDF (pronto para impressão)
- Validação de entradas
- Formatação automática
- Paginação em PDF
- Estilização em HTML

## 📊 Dados Gerenciados
- Nome
- Idade
- Cidade

## 🔧 Como executar
1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/gerador-relatorios.git
```

2. Instale as dependências:
```bash
pip install reportlab
```

3. Execute o programa:
```bash
python gerador_relatorios.py
```

## 📋 Pré-requisitos
- Python 3.6 ou superior
- ReportLab (para geração de PDF)

## 💻 Como usar
1. Escolha uma opção do menu:
   - 1: Inserir dados
   - 2: Gerar relatório TXT
   - 3: Gerar relatório HTML
   - 4: Gerar relatório PDF
   - 5: Sair

2. Para inserir dados:
   - Digite o nome (Enter vazio para parar)
   - Digite a idade (número)
   - Digite a cidade

3. Para gerar relatórios:
   - Escolha o formato desejado
   - Digite o nome do arquivo
   - O relatório será gerado no diretório atual

## 📄 Formatos de Saída

### TXT
- Formato simples e legível
- Separadores visuais
- Cabeçalho e rodapé informativos

### HTML
- Layout responsivo
- Estilização CSS
- Formatação profissional
- Visualização em navegador

### PDF
- Formatação profissional
- Paginação automática
- Pronto para impressão
- Layout consistente

## ⚙️ Estrutura do Código
```
gerador_relatorios.py
├── Função inserir_dados()
├── Função gerar_relatorio_txt()
├── Função gerar_relatorio_html()
├── Função gerar_relatorio_pdf()
└── Função main()
```

## 🔍 Exemplo de Uso
```
=== Gerador de Relatórios ===
1. Inserir dados
2. Gerar relatório TXT
3. Gerar relatório HTML
4. Gerar relatório PDF
5. Sair

Escolha uma opção: 
```

## ⚠️ Tratamento de Erros
- Validação de entrada de dados
- Tratamento de arquivos
- Mensagens de erro informativas
- Feedback de operações

## 🤝 Contribuindo
Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adicionando nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## ✨ Possíveis Melhorias Futuras
- [ ] Importação de dados de CSV/Excel
- [ ] Mais opções de formatação
- [ ] Gráficos e visualizações
- [ ] Filtros e ordenação
- [ ] Interface gráfica
- [ ] Mais campos de dados
- [ ] Temas personalizados

## 📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor
Seu Nome
- GitHub: [@seu-usuario](https://github.com/Brassolotto)
- LinkedIn: [@seu-linkedin](https://linkedin.com/in/ricardo-brassolotto)

---
⌨️ com ❤️ por [Rick Brassolotto] 😊