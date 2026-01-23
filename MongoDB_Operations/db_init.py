from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
mongodb_name = os.environ.get("MONGO_URI")

def get_mongo_client():    
 return MongoClient(mongodb_name)