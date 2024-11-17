FROM mcr.microsoft.com/mssql/server:2022-latest

USER root

# Instalando ferramentas SQLServer
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools18
RUN echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
RUN . ~/.bashrc

# Create a config directory
RUN mkdir -p -m 777 /usr/config
WORKDIR /usr/config

# Bundle config source
COPY ./sqlserver_docker /usr/config

# Grant permissions for to our scripts to be executable
RUN chmod +x /usr/config/entrypoint.sh
RUN chmod +x /usr/config/configure-db.sh

USER mssql

ENTRYPOINT ["./entrypoint.sh"]