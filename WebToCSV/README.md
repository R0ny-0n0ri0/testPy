
# WebToCSV

WebToCSV é uma ferramenta automatizada para baixar arquivos PDF de um site específico, salvá-los localmente e compactá-los em um arquivo ZIP.

## Funcionalidades
- Acessa o site alvo e identifica links de arquivos PDF.
- Baixa os arquivos PDF para um diretório local.
- Compacta todos os arquivos baixados em um único arquivo ZIP.

## Pré-requisitos
Certifique-se de ter as seguintes ferramentas instaladas:
- Python 3.12.6
- Bibliotecas Python: `requests`, `beautifulsoup4`

### Instalação das Dependências
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/WebToCSV.git
   cd WebToCSV
   ```
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   - No Windows:
     ```bash
     python -m venv .venv
     .\.venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como Executar
1. Execute o script principal:
   ```bash
   python main.py
   ```
2. Os arquivos PDF serão baixados para o diretório `downloads/`.
3. Um arquivo ZIP chamado `anexos.zip` será criado no diretório raiz do projeto.

## Testes Unitários
Este projeto inclui testes unitários para garantir o funcionamento correto das funcionalidades principais.

### Como Executar os Testes
Para executar os testes unitários, use o seguinte comando:

```bash
python -m unittest discover -s tests
```

- **Saída esperada**: Se todos os testes passarem, você verá algo como:
  ```plaintext
  ..
  ----------------------------------------------------------------------
  Ran 2 tests in X.XXXs

  OK
  ```

### O que os Testes Verificam
- **Teste de Download (`test_baixar_pdfs`)**:
  - Verifica se os arquivos PDF são baixados corretamente.
  - Confirma que os arquivos estão presentes no diretório `downloads/`.
- **Teste de Compactação (`test_compactar_arquivos`)**:
  - Verifica se os arquivos baixados são compactados em um arquivo ZIP.
  - Confirma que o arquivo ZIP contém os arquivos esperados.

## Estrutura do Projeto
```
WebToCSV/
├── .venv/               # Ambiente virtual
├── src/                 # Código-fonte
│   ├── __init__.py      # Indica que este é um pacote Python
│   └── scraper.py       # Funções de scraping e compactação
├── tests/               # Diretório para testes unitários
│   └── test_scraper.py  # Testes para as funções em scraper.py
├── downloads/           # Diretório onde os PDFs são salvos
├── anexos.zip           # Arquivo ZIP gerado
├── requirements.txt     # Lista de dependências
├── README.md            # Documentação inicial
└── main.py              # Ponto de entrada do programa
```