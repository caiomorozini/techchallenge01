import os

server = os.environ.get('SQL_SERVER')  #"techchallengeserver.database.windows.net"
database = os.environ.get('DATABASE') #"techchallengeDB"
user = os.environ.get('USERDBTECH') #"admtech2"
password = os.environ.get('PASSWORD_USERDBTECH')  #"jklhb$#8239"
driver = "ODBC Driver 18 for SQL Server"
        
con_str = f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={user};PWD={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'