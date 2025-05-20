# Requisitos do Aplicativo de Transcrição de Vídeos

## Visão Geral
Desenvolver um aplicativo web que permita aos usuários transcrever o conteúdo de áudio de vídeos para texto, oferecendo múltiplas opções de entrada de vídeo.

## Requisitos Funcionais

### Entrada de Vídeos
1. Upload direto de arquivos de vídeo
   - Suportar formatos comuns (MP4, AVI, MOV, etc.)
   - Definir limite de tamanho adequado para upload
   - Mostrar barra de progresso durante o upload

2. Transcrição via link do YouTube
   - Permitir que o usuário cole um link do YouTube
   - Extrair o áudio do vídeo automaticamente
   - Validar links para garantir que são do YouTube

3. Transcrição via link do Instagram
   - Permitir que o usuário cole um link do Instagram
   - Extrair o áudio do vídeo/reels automaticamente
   - Validar links para garantir que são do Instagram

### Processamento e Saída
1. Transcrição Automática
   - Converter áudio para texto usando API de reconhecimento de fala
   - Mostrar progresso da transcrição
   - Suportar múltiplos idiomas (pelo menos português e inglês)

2. Resultados
   - Exibir o texto transcrito na interface
   - Permitir copiar o texto para a área de transferência
   - Oferecer opção para download do texto em formato TXT ou PDF
   - Opcionalmente, mostrar timestamps para facilitar a navegação

### Interface do Usuário
1. Design Responsivo
   - Funcionar em dispositivos móveis e desktop
   - Interface intuitiva e fácil de usar

2. Feedback ao Usuário
   - Mostrar status do processamento
   - Exibir mensagens de erro claras quando necessário
   - Indicar tempo estimado para conclusão

## Requisitos Não-Funcionais

1. Desempenho
   - Processar vídeos de tamanho médio (até 10 minutos) em tempo razoável
   - Otimizar o uso de recursos do servidor

2. Segurança
   - Não armazenar vídeos por longos períodos
   - Limpar arquivos temporários após processamento

3. Escalabilidade
   - Permitir processamento de múltiplos vídeos simultaneamente
   - Implementar sistema de fila se necessário

## Tecnologias Sugeridas
- Backend: Flask (Python)
- Frontend: HTML, CSS, JavaScript
- Processamento de Vídeo: FFmpeg, MoviePy
- Download de Vídeos: pytube (YouTube), instaloader ou yt-dlp (Instagram)
- Transcrição: OpenAI Whisper ou Google Speech-to-Text

## Limitações e Considerações
- Dependência de APIs externas para transcrição
- Possíveis restrições de acesso a conteúdo do Instagram (autenticação)
- Limitações de tamanho de arquivo para upload
- Considerações sobre uso de recursos computacionais para transcrição
