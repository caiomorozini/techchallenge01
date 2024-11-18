import os

server = os.environ.get('SERVER')
database = os.environ.get('DATABASE') 
user = os.environ.get('USER') 
password = os.environ.get('PASSWORD')
port="5432"

        
con_str = f"postgresql+psycopg2://{user}:{password}@{server}:{port}/{database}"