# Instruções de Uso - Aplicativo de Transcrição de Vídeos

## Visão Geral

Este aplicativo permite transcrever o conteúdo de áudio de vídeos para texto, oferecendo três métodos de entrada:
1. Upload direto de arquivos de vídeo
2. Links de vídeos do YouTube
3. Links de vídeos do Instagram

## Requisitos do Sistema

- Python 3.8 ou superior
- FFmpeg instalado no sistema
- Conexão com a internet para download de vídeos

## Instalação

1. Clone o repositório ou extraia os arquivos para um diretório local
2. Instale as dependências necessárias:

```bash
pip install flask yt-dlp openai-whisper moviepy flask-wtf
```

3. Certifique-se de que o FFmpeg está instalado no seu sistema:

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# MacOS
brew install ffmpeg

# Windows (via Chocolatey)
choco install ffmpeg
```

## Executando o Aplicativo

1. Navegue até o diretório do projeto:

```bash
cd app_transcricao
```

2. Execute o aplicativo:

```bash
python src/main.py
```

3. Acesse o aplicativo no navegador:

```
http://localhost:5000
```

## Utilizando o Aplicativo

### Upload de Arquivo

1. Na aba "Upload de Arquivo", clique em "Selecione um arquivo de vídeo"
2. Escolha um arquivo de vídeo do seu computador (formatos suportados: MP4, AVI, MOV, MKV, WEBM)
3. Opcionalmente, selecione o idioma do áudio (ou deixe em "Detectar automaticamente")
4. Clique em "Transcrever"
5. Aguarde o processamento (o tempo varia conforme o tamanho do vídeo)
6. O texto transcrito será exibido na tela

### Link do YouTube

1. Na aba "Link do YouTube", cole a URL do vídeo do YouTube
2. Opcionalmente, selecione o idioma do áudio
3. Clique em "Transcrever"
4. Aguarde o download e processamento
5. O texto transcrito será exibido na tela

**Nota importante sobre o YouTube**: Alguns vídeos podem exigir autenticação devido a restrições anti-bot do YouTube. Se encontrar erros de acesso, considere:
- Tentar vídeos públicos e populares
- Usar o método de upload direto como alternativa
- Para uso avançado, consulte a documentação do yt-dlp sobre como fornecer cookies de autenticação

### Link do Instagram

1. Na aba "Link do Instagram", cole a URL do vídeo/reels do Instagram
2. Opcionalmente, selecione o idioma do áudio
3. Clique em "Transcrever"
4. Aguarde o download e processamento
5. O texto transcrito será exibido na tela

**Nota sobre o Instagram**: Alguns conteúdos do Instagram podem exigir autenticação. Recomendamos testar com vídeos públicos.

## Trabalhando com os Resultados

Após a transcrição, você pode:

1. Copiar o texto transcrito para a área de transferência clicando em "Copiar Texto"
2. Baixar o texto em formato TXT ou PDF usando o botão "Download"
3. Iniciar uma nova transcrição clicando em "Nova Transcrição"

## Solução de Problemas

### Erro ao baixar vídeos do YouTube ou Instagram

- Verifique se a URL está correta e o vídeo está disponível publicamente
- Alguns vídeos podem exigir autenticação devido a restrições das plataformas
- Tente usar o método de upload direto como alternativa

### Erro na transcrição

- Verifique se o áudio do vídeo é claro e sem ruídos excessivos
- A qualidade da transcrição varia conforme a clareza do áudio
- Para idiomas específicos, selecione manualmente o idioma em vez de usar a detecção automática

### Tempo de processamento longo

- Vídeos maiores levam mais tempo para processar
- O modelo de transcrição "small" é usado por padrão para equilibrar velocidade e precisão
- Para vídeos muito longos, considere dividir em partes menores

## Limitações Conhecidas

- Tamanho máximo de upload: 100MB
- Alguns vídeos do YouTube e Instagram podem exigir autenticação
- A precisão da transcrição varia conforme a qualidade do áudio e o idioma
- O processamento de vídeos longos pode levar vários minutos

## Próximas Melhorias Planejadas

- Adição de timestamps no texto transcrito
- Identificação de múltiplos falantes
- Suporte a mais idiomas
- Interface de edição do texto transcrito
- Integração com serviços de armazenamento em nuvem
