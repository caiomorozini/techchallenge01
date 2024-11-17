FROM python:3

# Instalando o driver odbc
RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg
RUN curl https://packages.microsoft.com/config/debian/12/prod.list | tee /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18

# Instalando ferramentas SQLServer
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools18
RUN echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
RUN . ~/.bashrc

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV SQL_SERVER="172.17.0.1,1522"
ENV DATABASE="techchallengeDB"
ENV USER="SA"
ENV PASSWORD="jklhb#8239"

RUN chmod +x /app/entrypoint_app.sh

ENTRYPOINT ["/app/entrypoint_app.sh"]