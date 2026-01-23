import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
sqlite_db_name = os.environ.get("SQLITE_DB_NAME")

def get_connection():    
 return sqlite3.connect(sqlite_db_name)