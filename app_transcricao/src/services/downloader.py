from flask import request, jsonify
import os
import yt_dlp
import tempfile
import uuid

class Downloader:
    def __init__(self, temp_dir):
        self.temp_dir = temp_dir
        os.makedirs(self.temp_dir, exist_ok=True)
        
    def download_youtube(self, url):
        """
        Baixa um vídeo do YouTube e retorna o caminho para o arquivo de áudio extraído
        """
        try:
            # Gerar um nome de arquivo único
            output_id = str(uuid.uuid4())
            audio_path = os.path.join(self.temp_dir, f"{output_id}.mp3")
            
            # Configurações do yt-dlp
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': os.path.join(self.temp_dir, f"{output_id}.%(ext)s"),
                'quiet': False,
                'no_warnings': True
            }
            
            # Baixar o vídeo
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            return {
                'success': True,
                'file_path': audio_path,
                'message': 'Vídeo do YouTube baixado com sucesso'
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'message': 'Erro ao baixar vídeo do YouTube'
            }
    
    def download_instagram(self, url):
        """
        Baixa um vídeo do Instagram e retorna o caminho para o arquivo de áudio extraído
        """
        try:
            # Gerar um nome de arquivo único
            output_id = str(uuid.uuid4())
            audio_path = os.path.join(self.temp_dir, f"{output_id}.mp3")
            
            # Configurações do yt-dlp para Instagram
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': os.path.join(self.temp_dir, f"{output_id}.%(ext)s"),
                'quiet': False,
                'no_warnings': True,
                # Opções específicas para Instagram
                'cookiefile': None,  # Se necessário, adicionar arquivo de cookies
                'extract_flat': False,
                'force_generic_extractor': False
            }
            
            # Baixar o vídeo
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            return {
                'success': True,
                'file_path': audio_path,
                'message': 'Vídeo do Instagram baixado com sucesso'
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'message': 'Erro ao baixar vídeo do Instagram'
            }
