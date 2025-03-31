import os
import requests
import zipfile
from bs4 import BeautifulSoup

# URL do site alvo
URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Diretório para armazenar os arquivos
DOWNLOAD_DIR = "downloads"
ZIP_FILE = "anexos.zip"

# Criar diretório se não existir
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def baixar_pdfs():
    response = requests.get(URL)
    if response.status_code != 200:
        print("Erro ao acessar o site.")
        return
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a", href=True)
    pdf_links = [link["href"] for link in links if link["href"].endswith(".pdf") and "Anexo" in link["href"]]
    for link in pdf_links:
        pdf_name = os.path.join(DOWNLOAD_DIR, link.split("/")[-1])
        pdf_content = requests.get(link).content
        with open(pdf_name, "wb") as pdf_file:
            pdf_file.write(pdf_content)
        print(f"Baixado: {pdf_name}")
    return pdf_links

def compactar_arquivos():
    with zipfile.ZipFile(ZIP_FILE, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(DOWNLOAD_DIR):
            for file in files:
                zipf.write(os.path.join(root, file), file)
    print(f"Compactação concluída: {ZIP_FILE}")

if __name__ == "__main__":
    baixar_pdfs()
    compactar_arquivos()