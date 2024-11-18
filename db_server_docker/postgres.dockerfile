# Base image oficial do PostgreSQL
FROM postgres:15

# Copie o script SQL de inicialização (se houver) para o contêiner
COPY ./db_server_docker/createDB.sql /docker-entrypoint-initdb.d/

# O PostgreSQL já está configurado para executar arquivos em /docker-entrypoint-initdb.d/ durante a inicialização
