import os
from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
import time
import uuid

from services.downloader import Downloader
from services.processor import Processor
from services.transcriber import Transcriber

app = Flask(__name__, 
            static_folder='../src/static',
            template_folder='../templates')

# Configurações
app.config['UPLOAD_FOLDER'] = '../tmp'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max
app.config['ALLOWED_EXTENSIONS'] = {'mp4', 'avi', 'mov', 'mkv', 'webm'}

# Inicializar serviços
downloader = Downloader(app.config['UPLOAD_FOLDER'])
processor = Processor(app.config['UPLOAD_FOLDER'])
transcriber = Transcriber(model_name="small")  # Usando modelo small para equilíbrio entre velocidade e precisão

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'Nenhum arquivo selecionado'}), 400
    
    if file and allowed_file(file.filename):
        # Gerar nome de arquivo único
        filename = secure_filename(file.filename)
        unique_id = str(uuid.uuid4())
        unique_filename = f"{unique_id}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        
        # Salvar arquivo
        file.save(filepath)
        
        # Processar vídeo e transcrever
        language = request.form.get('language', None)  # Idioma opcional
        
        # Transcrever diretamente o vídeo
        result = transcriber.process_video(filepath, language)
        
        # Limpar arquivos temporários
        try:
            os.remove(filepath)
        except:
            pass
        
        if result['success']:
            return jsonify({
                'success': True,
                'text': result['text'],
                'language': result.get('language', 'desconhecido'),
                'message': 'Transcrição concluída com sucesso'
            })
        else:
            return jsonify({
                'success': False,
                'error': result.get('error', 'Erro desconhecido'),
                'message': result.get('message', 'Falha na transcrição')
            }), 500
    
    return jsonify({'error': 'Tipo de arquivo não permitido'}), 400

@app.route('/youtube', methods=['POST'])
def process_youtube():
    data = request.json
    if not data or 'url' not in data:
        return jsonify({'error': 'URL não fornecida'}), 400
    
    youtube_url = data['url']
    language = data.get('language', None)  # Idioma opcional
    
    # Validação básica da URL
    if 'youtube.com' not in youtube_url and 'youtu.be' not in youtube_url:
        return jsonify({'error': 'URL inválida do YouTube'}), 400
    
    # Baixar vídeo do YouTube
    download_result = downloader.download_youtube(youtube_url)
    
    if not download_result['success']:
        return jsonify({
            'success': False,
            'error': download_result.get('error', 'Erro desconhecido'),
            'message': download_result.get('message', 'Falha ao baixar vídeo')
        }), 500
    
    # Transcrever o áudio baixado
    audio_path = download_result['file_path']
    transcription_result = transcriber.transcribe_audio(audio_path, language)
    
    # Limpar arquivos temporários
    try:
        os.remove(audio_path)
    except:
        pass
    
    if transcription_result['success']:
        return jsonify({
            'success': True,
            'text': transcription_result['text'],
            'language': transcription_result.get('language', 'desconhecido'),
            'message': 'Transcrição concluída com sucesso'
        })
    else:
        return jsonify({
            'success': False,
            'error': transcription_result.get('error', 'Erro desconhecido'),
            'message': transcription_result.get('message', 'Falha na transcrição')
        }), 500

@app.route('/instagram', methods=['POST'])
def process_instagram():
    data = request.json
    if not data or 'url' not in data:
        return jsonify({'error': 'URL não fornecida'}), 400
    
    instagram_url = data['url']
    language = data.get('language', None)  # Idioma opcional
    
    # Validação básica da URL
    if 'instagram.com' not in instagram_url:
        return jsonify({'error': 'URL inválida do Instagram'}), 400
    
    # Baixar vídeo do Instagram
    download_result = downloader.download_instagram(instagram_url)
    
    if not download_result['success']:
        return jsonify({
            'success': False,
            'error': download_result.get('error', 'Erro desconhecido'),
            'message': download_result.get('message', 'Falha ao baixar vídeo')
        }), 500
    
    # Transcrever o áudio baixado
    audio_path = download_result['file_path']
    transcription_result = transcriber.transcribe_audio(audio_path, language)
    
    # Limpar arquivos temporários
    try:
        os.remove(audio_path)
    except:
        pass
    
    if transcription_result['success']:
        return jsonify({
            'success': True,
            'text': transcription_result['text'],
            'language': transcription_result.get('language', 'desconhecido'),
            'message': 'Transcrição concluída com sucesso'
        })
    else:
        return jsonify({
            'success': False,
            'error': transcription_result.get('error', 'Erro desconhecido'),
            'message': transcription_result.get('message', 'Falha na transcrição')
        }), 500

@app.route('/download', methods=['POST'])
def download_text():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({'error': 'Texto não fornecido'}), 400
    
    text = data['text']
    format_type = data.get('format', 'txt')  # Formato padrão: txt
    
    # Gerar nome de arquivo único
    unique_id = str(uuid.uuid4())
    filename = f"transcricao_{unique_id}.{format_type}"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Salvar texto em arquivo
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    
    # Enviar arquivo para download
    return send_file(filepath, as_attachment=True, download_name=filename)

if __name__ == '__main__':
    # Garantir que o diretório de upload existe
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000)
