from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

def get_admin_user():
    return os.getenv("ADMIN_LOGIN")

def get_admin_password():
    return os.getenv("ADMIN_PASSWORD")

def get_secret_key():
    return os.getenv("SECRET_KEY")

def get_algorithm():
    return os.getenv("ALGORITHM")

def  get_db_host():
    return os.getenv("DB_HOST")

def  get_db_name():
    return os.getenv("DB_NAME")

def  get_db_user():
    return os.getenv("DB_USER")

def get_db_password():
    return os.getenv("DB_PASSWORD")