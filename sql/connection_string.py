import os

server = os.environ.get('SQL_SERVER')
database = os.environ.get('DATABASE') 
user = os.environ.get('USER') 
password = os.environ.get('PASSWORD') 
driver = "ODBC Driver 18 for SQL Server"
        
con_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password};TrustServerCertificate=yes' #;Encrypt=yes;Connection Timeout=30'