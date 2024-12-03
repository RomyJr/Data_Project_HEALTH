from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

def get_db_engine():
    """
    Charge les variables d'environnement depuis le fichier .env,
    génère une URL de connexion et retourne un moteur SQLAlchemy.

    Returns:
        sqlalchemy.engine.base.Engine: Le moteur SQLAlchemy pour la base de données.
    """
    # Charger les variables d'environnement
    load_dotenv()

    # Récupérer les configurations depuis le fichier .env
    db_config = {
        'host': os.getenv('DB_HOST'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_NAME')
    }

    # Construire l'URL de connexion
    connection_url = f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}"

    # Créer et retourner le moteur SQLAlchemy
    engine = create_engine(connection_url)
    return engine
