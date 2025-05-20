import os
import whisper
import tempfile
from moviepy.editor import VideoFileClip

class Transcriber:
    def __init__(self, model_name="small"):
        """
        Inicializa o serviço de transcrição com o modelo Whisper especificado
        
        Args:
            model_name (str): Nome do modelo Whisper a ser usado (tiny, base, small, medium, large)
        """
        self.model = None
        self.model_name = model_name
        
    def load_model(self):
        """
        Carrega o modelo Whisper se ainda não estiver carregado
        """
        if self.model is None:
            self.model = whisper.load_model(self.model_name)
        return self.model
    
    def extract_audio_from_video(self, video_path):
        """
        Extrai o áudio de um arquivo de vídeo
        
        Args:
            video_path (str): Caminho para o arquivo de vídeo
            
        Returns:
            str: Caminho para o arquivo de áudio extraído
        """
        try:
            # Criar um arquivo temporário para o áudio
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
    
    def transcribe_audio(self, audio_path, language=None):
        """
        Transcreve um arquivo de áudio usando o modelo Whisper
        
        Args:
            audio_path (str): Caminho para o arquivo de áudio
            language (str, optional): Código do idioma para transcrição. Se None, detecta automaticamente.
            
        Returns:
            dict: Resultado da transcrição com texto e metadados
        """
        try:
            # Carregar o modelo se necessário
            model = self.load_model()
            
            # Opções de transcrição
            options = {}
            if language:
                options["language"] = language
            
            # Realizar a transcrição
            result = model.transcribe(audio_path, **options)
            
            return {
                'success': True,
                'text': result["text"],
                'language': result.get("language", "desconhecido"),
                'segments': result.get("segments", []),
                'message': 'Transcrição concluída com sucesso'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'message': 'Erro ao transcrever áudio'
            }
    
    def process_video(self, video_path, language=None):
        """
        Processa um vídeo completo: extrai áudio e transcreve
        
        Args:
            video_path (str): Caminho para o arquivo de vídeo
            language (str, optional): Código do idioma para transcrição
            
        Returns:
            dict: Resultado da transcrição
        """
        # Extrair áudio
        audio_result = self.extract_audio_from_video(video_path)
        if not audio_result['success']:
            return audio_result
        
        # Transcrever áudio
        transcription_result = self.transcribe_audio(audio_result['file_path'], language)
        
        # Limpar arquivos temporários
        try:
            os.remove(audio_result['file_path'])
        except:
            pass
        
        return transcription_result
