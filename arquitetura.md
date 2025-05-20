# Arquitetura do Aplicativo de Transcrição de Vídeos

## Visão Geral da Arquitetura

O aplicativo será desenvolvido como uma aplicação web utilizando Flask como framework backend e uma interface frontend simples e intuitiva. A arquitetura será modular para facilitar a manutenção e extensão futura.

## Componentes Principais

### 1. Interface do Usuário (Frontend)
- **Tecnologias**: HTML, CSS, JavaScript
- **Responsabilidades**:
  - Formulário para upload de arquivos de vídeo
  - Campo para inserção de links do YouTube e Instagram
  - Exibição do progresso de processamento
  - Apresentação do texto transcrito
  - Opções para download do texto transcrito

### 2. Servidor Web (Backend)
- **Tecnologia**: Flask (Python)
- **Responsabilidades**:
  - Roteamento de requisições
  - Validação de entradas
  - Coordenação do fluxo de processamento
  - Gerenciamento de arquivos temporários
  - Entrega dos resultados ao frontend

### 3. Módulo de Processamento de Vídeo
- **Tecnologias**: FFmpeg, MoviePy
- **Responsabilidades**:
  - Conversão de formatos de vídeo
  - Extração de áudio de vídeos
  - Preparação do áudio para transcrição

### 4. Módulo de Download de Vídeos
- **Tecnologias**: yt-dlp (para YouTube e Instagram)
- **Responsabilidades**:
  - Download de vídeos do YouTube
  - Download de vídeos do Instagram
  - Validação de links
  - Tratamento de erros de acesso

### 5. Módulo de Transcrição
- **Tecnologia**: OpenAI Whisper
- **Responsabilidades**:
  - Processamento do áudio para transcrição
  - Conversão de fala para texto
  - Suporte a múltiplos idiomas

## Fluxo de Dados

### Fluxo 1: Upload de Arquivo
1. Usuário faz upload do arquivo de vídeo
2. Backend valida o formato e tamanho do arquivo
3. Módulo de Processamento extrai o áudio do vídeo
4. Módulo de Transcrição converte o áudio em texto
5. Backend retorna o texto transcrito para o frontend
6. Frontend exibe o resultado e opções de download

### Fluxo 2: Link do YouTube
1. Usuário insere link do YouTube
2. Backend valida o link
3. Módulo de Download baixa o vídeo do YouTube
4. Módulo de Processamento extrai o áudio
5. Módulo de Transcrição converte o áudio em texto
6. Backend retorna o texto transcrito para o frontend
7. Frontend exibe o resultado e opções de download

### Fluxo 3: Link do Instagram
1. Usuário insere link do Instagram
2. Backend valida o link
3. Módulo de Download baixa o vídeo do Instagram
4. Módulo de Processamento extrai o áudio
5. Módulo de Transcrição converte o áudio em texto
6. Backend retorna o texto transcrito para o frontend
7. Frontend exibe o resultado e opções de download

## Detalhes de Implementação

### Estrutura de Diretórios
```
app_transcricao/
├── src/
│   ├── main.py              # Ponto de entrada da aplicação
│   ├── config.py            # Configurações da aplicação
│   ├── routes/
│   │   └── api.py           # Rotas da API
│   ├── services/
│   │   ├── downloader.py    # Serviço de download de vídeos
│   │   ├── processor.py     # Serviço de processamento de vídeos
│   │   └── transcriber.py   # Serviço de transcrição
│   ├── utils/
│   │   ├── validators.py    # Validadores de entrada
│   │   └── file_manager.py  # Gerenciamento de arquivos
│   └── static/
│       ├── css/
│       ├── js/
│       └── img/
├── templates/
│   ├── index.html           # Página principal
│   └── result.html          # Página de resultados
├── tests/                   # Testes unitários e de integração
├── tmp/                     # Diretório temporário para arquivos
└── requirements.txt         # Dependências do projeto
```

### Bibliotecas e Dependências

1. **Flask e Extensões**:
   - Flask: Framework web
   - Flask-WTF: Validação de formulários
   - Flask-Uploads: Gerenciamento de uploads

2. **Processamento de Vídeo**:
   - FFmpeg: Manipulação de vídeo e áudio
   - MoviePy: Interface Python para FFmpeg

3. **Download de Vídeos**:
   - yt-dlp: Download de vídeos do YouTube e Instagram
   - Alternativa para Instagram: Instaloader (caso necessário)

4. **Transcrição**:
   - OpenAI Whisper: Modelo de reconhecimento de fala
   - Opção: Whisper API (se disponível) ou modelo local

### Considerações Técnicas

#### 1. Modelo Whisper
- Utilizaremos o modelo "medium" ou "small" para balancear precisão e velocidade
- Suporte a múltiplos idiomas, com detecção automática
- Opção para especificar o idioma manualmente

#### 2. Download de Vídeos do Instagram
- O yt-dlp será a primeira opção para download de vídeos do Instagram
- Implementação de fallback para Instaloader caso o yt-dlp falhe
- Possível necessidade de autenticação para alguns conteúdos do Instagram

#### 3. Gerenciamento de Arquivos
- Arquivos temporários serão armazenados no diretório `tmp/`
- Limpeza automática de arquivos após processamento
- Limite de tamanho para uploads diretos (sugestão: 100MB)

#### 4. Tratamento de Erros
- Validação de links antes do download
- Timeout para downloads e processamentos longos
- Mensagens de erro amigáveis para o usuário

#### 5. Escalabilidade
- Implementação de sistema de filas para processamento assíncrono
- Possibilidade de adicionar workers para processamento paralelo

## Interface do Usuário

### Página Principal
- Design limpo e intuitivo
- Três abas para os diferentes métodos de entrada:
  1. Upload de arquivo
  2. Link do YouTube
  3. Link do Instagram
- Indicador de progresso durante o processamento
- Opções de configuração avançada (opcional)

### Página de Resultados
- Exibição do texto transcrito
- Opções para copiar o texto
- Botões para download em diferentes formatos (TXT, PDF)
- Opção para nova transcrição

## Limitações e Considerações Futuras

### Limitações Atuais
- Dependência de APIs externas para download de vídeos
- Possíveis restrições de acesso a conteúdo do Instagram
- Tempo de processamento para vídeos longos
- Precisão da transcrição varia conforme qualidade do áudio

### Melhorias Futuras
- Implementação de timestamps no texto transcrito
- Identificação de múltiplos falantes
- Suporte a mais idiomas
- Interface de edição do texto transcrito
- Integração com serviços de armazenamento em nuvem
