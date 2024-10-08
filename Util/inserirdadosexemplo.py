from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import os

# Adiciona o diretório 'Classes' ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Classes')))
from producaobase import Producao

# Configuração da conexão com o PostgreSQL
DATABASE_URL = "postgresql://postgres:fiap@localhost:5432/fiaptechchallenge01"  # Substitua com suas credenciais
engine = create_engine(DATABASE_URL)

# Criação da sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para criar a tabela e inserir dados fictícios
def criar_tabela_e_inserir_dados():
    # Cria a tabela no banco de dados (se não existir)
    Producao.metadata.create_all(bind=engine)

    # Cria uma nova sessão
    db = SessionLocal()

    try:
        # Dados fictícios para inserir na tabela
        dados_ficticios = [
            {"nome_produto": "Vinho Tinto", "quantidade": 1500.5, "ano": 2021},
            {"nome_produto": "Suco de Uva", "quantidade": 2000.0, "ano": 2020},
            {"nome_produto": "Espumante", "quantidade": 500.75, "ano": 2022},
            {"nome_produto": "Vinho Branco", "quantidade": 1200.0, "ano": 2021},
        ]

        # Itera sobre os dados fictícios e insere na tabela
        for item in dados_ficticios:
            novo_registro = Producao(
                nome_produto=item["nome_produto"],
                quantidade=item["quantidade"],
                ano=item["ano"]
            )
            db.add(novo_registro)  # Adiciona o novo registro à sessão

        db.commit()  # Confirma a transação
        print("Dados inseridos com sucesso!")

    except Exception as e:
        db.rollback()  # Desfaz a transação em caso de erro
        print(f"Erro ao inserir dados: {e}")

    finally:
        db.close()  # Fecha a sessão

# Executa a função para criar a tabela e inserir os dados
if __name__ == "__main__":
    criar_tabela_e_inserir_dados()