import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

supa_url = os.environ.get("SUPABASE_URL")
supa_key = os.environ.get("SUPABASE_KEY")

supa_db = create_client(supa_url, supa_key)
supa_table = "Python_CRUD"
