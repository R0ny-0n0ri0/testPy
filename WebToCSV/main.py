from src.scraper import baixar_pdfs, compactar_arquivos

if __name__ == "__main__":
    print("Iniciando o download dos PDFs...")
    baixar_pdfs()
    print("Compactando os arquivos baixados...")
    compactar_arquivos()
    print("Processo concluído!")