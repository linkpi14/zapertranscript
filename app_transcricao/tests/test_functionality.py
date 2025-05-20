import os
import sys

# Adicionar diretório raiz ao path para importações relativas
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_youtube_download():
    """Testa o download de um vídeo do YouTube"""
    print("Testando download de vídeo do YouTube...")
    
    # Importar apenas o downloader para evitar problemas de dependência
    from src.services.downloader import Downloader
    
    # Inicializar serviços
    temp_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tmp")
    os.makedirs(temp_dir, exist_ok=True)
    
    downloader = Downloader(temp_dir)
    
    # URL de teste do YouTube (vídeo curto)
    test_url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"  # "Me at the zoo" - primeiro vídeo do YouTube
    
    # Baixar vídeo
    print("Baixando vídeo do YouTube...")
    download_result = downloader.download_youtube(test_url)
    
    if not download_result['success']:
        print(f"ERRO: {download_result.get('message', 'Falha ao baixar vídeo')}")
        print(f"Detalhes: {download_result.get('error', 'Sem detalhes')}")
        return False
    
    print(f"Vídeo baixado com sucesso: {download_result['file_path']}")
    
    # Limpar arquivos temporários
    try:
        os.remove(download_result['file_path'])
        print(f"Arquivo temporário removido: {download_result['file_path']}")
    except Exception as e:
        print(f"Não foi possível remover o arquivo temporário: {download_result['file_path']}")
        print(f"Erro: {str(e)}")
    
    return True

def test_whisper_import():
    """Testa a importação do modelo Whisper"""
    print("Testando importação do modelo Whisper...")
    
    try:
        import whisper
        print("Whisper importado com sucesso!")
        return True
    except Exception as e:
        print(f"ERRO ao importar Whisper: {str(e)}")
        return False

if __name__ == "__main__":
    print("Iniciando testes de funcionalidades...")
    
    whisper_test = test_whisper_import()
    youtube_test = test_youtube_download()
    
    if whisper_test and youtube_test:
        print("\nTodos os testes concluídos com sucesso!")
    else:
        print("\nAlguns testes falharam. Verifique os logs acima.")
