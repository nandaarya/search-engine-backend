import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

client = MongoClient(os.environ.get('MONGODB_URI'))
db = client[os.environ.get('MONGODB_DATABASE')]
collection = db[os.environ.get('MONGODB_COLLECTION')]

def fetch_all_documents_from_database():
    all_documents = collection.find()
    data = [doc['title'] for doc in all_documents]

    return data

def get_document_file_url_from_database(title):
    document = collection.find_one({"title": title})

    return document['url']