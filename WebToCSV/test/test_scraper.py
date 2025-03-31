import os
import unittest
import zipfile
from unittest.mock import patch

from src.scraper import baixar_pdfs, compactar_arquivos

# URL do site alvo
URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-dasociedade/atualizacao-do-rol-de-procedimentos"

# Diretórios e arquivos usados nos testes
DOWNLOAD_DIR = "downloads"
ZIP_FILE = "anexos.zip"

class TestScraper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Executado uma vez antes de todos os testes."""
        # Cria o diretório de downloads para os testes
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        """Executado uma vez após todos os testes."""
        # Remove o diretório de downloads e o arquivo ZIP após os testes
        for root, _, files in os.walk(DOWNLOAD_DIR):
            for file in files:
                os.remove(os.path.join(root, file))
        os.rmdir(DOWNLOAD_DIR)
        if os.path.exists(ZIP_FILE):
            os.remove(ZIP_FILE)

    def test_baixar_pdfs(self):
        """Testa se os PDFs são baixados corretamente."""
        pdf_links = baixar_pdfs()
        self.assertIsNotNone(pdf_links, "A função baixar_pdfs retornou None.")
        self.assertTrue(len(pdf_links) > 0, "Nenhum PDF foi encontrado para download.")

        # Verifica se os arquivos foram salvos no diretório de downloads
        for link in pdf_links:
            pdf_name = os.path.join(DOWNLOAD_DIR, link.split("/")[-1])
            self.assertTrue(os.path.exists(pdf_name), f"O arquivo {pdf_name} não foi baixado.")

    def test_compactar_arquivos(self):
        """Testa se os arquivos são compactados corretamente."""
        # Garante que há arquivos no diretório de downloads
        with open(os.path.join(DOWNLOAD_DIR, "test_file.txt"), "w") as f:
            f.write("Test content")

        # Executa a compactação
        compactar_arquivos()

        # Verifica se o arquivo ZIP foi criado
        self.assertTrue(os.path.exists(ZIP_FILE), "O arquivo ZIP não foi criado.")

        # Verifica se o arquivo ZIP contém o arquivo de teste
        with zipfile.ZipFile(ZIP_FILE, 'r') as zipf:
            files_in_zip = zipf.namelist()
            self.assertIn("test_file.txt", files_in_zip, "O arquivo de teste não foi adicionado ao ZIP.")

    def test_baixar_pdfs_erro_acesso_site(self):
        """Testa o caso em que o site não pode ser acessado."""
        # Usa mock para simular uma resposta HTTP com status_code diferente de 200
        with patch('src.scraper.requests.get') as mock_get:
            mock_response = mock_get.return_value
            mock_response.status_code = 404  # Simula um erro 404

            # Chama a função baixar_pdfs
            result = baixar_pdfs()

            # Verifica se a função retorna None quando o site não é acessível
            self.assertIsNone(result, "A função deveria retornar None quando o site não é acessível.")

            # Verifica se a mensagem de erro foi impressa
            import sys
            from io import StringIO
            old_stdout = sys.stdout
            sys.stdout = mystdout = StringIO()
            try:
                baixar_pdfs()
            finally:
                sys.stdout = old_stdout
            self.assertIn("Erro ao acessar o site.", mystdout.getvalue().strip())

    def test_main_flow(self):
        """Simula o fluxo principal do programa."""
        # Chama as funções diretamente
        baixar_pdfs()
        compactar_arquivos()

        # Verifica se o arquivo ZIP foi criado
        self.assertTrue(os.path.exists(ZIP_FILE), "O arquivo ZIP não foi criado.")

if __name__ == "__main__":
    unittest.main()