import os
from moviepy.editor import VideoFileClip

class Processor:
    def __init__(self, temp_dir):
        """
        Inicializa o serviço de processamento de vídeos
        
        Args:
            temp_dir (str): Diretório para armazenar arquivos temporários
        """
        self.temp_dir = temp_dir
        os.makedirs(self.temp_dir, exist_ok=True)
    
    def extract_audio(self, video_path):
        """
        Extrai o áudio de um arquivo de vídeo
        
        Args:
            video_path (str): Caminho para o arquivo de vídeo
            
        Returns:
            dict: Resultado da extração com caminho do arquivo de áudio
        """
        try:
            # Criar um arquivo para o áudio extraído
            audio_path = os.path.splitext(video_path)[0] + ".mp3"
            
            # Extrair o áudio usando moviepy
            video = VideoFileClip(video_path)
            video.audio.write_audiofile(audio_path, verbose=False, logger=None)
            
            return {
                'success': True,
                'file_path': audio_path,
                'message': 'Áudio extraído com sucesso'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'message': 'Erro ao extrair áudio do vídeo'
            }
    
    def cleanup_files(self, file_paths):
        """
        Remove arquivos temporários
        
        Args:
            file_paths (list): Lista de caminhos de arquivos para remover
            
        Returns:
            dict: Resultado da operação de limpeza
        """
        try:
            for file_path in file_paths:
                if os.path.exists(file_path):
                    os.remove(file_path)
            
            return {
                'success': True,
                'message': 'Arquivos temporários removidos com sucesso'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'message': 'Erro ao remover arquivos temporários'
            }
