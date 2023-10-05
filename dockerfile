FROM ubuntu:latest

# Atualiza o índice de pacotes e instala as atualizações
RUN apt update && apt upgrade -y

# Instala o Python 3
RUN apt install python3 -y

# Baixa o arquivo Python do repositório do GitHub
RUN wget https://github.com/[NOME_DO_REPOSITORIO]/[NOME_DO_ARQUIVO].py

# Executa o arquivo Python
CMD python3 [NOME_DO_ARQUIVO].py