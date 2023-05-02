from pymongo import MongoClient
from .config import uname, passwd, openai_key
import openai

openai.api_key = openai_key

def make_connection(host, port, username = uname, password = passwd):
    client = MongoClient(host=host,
                         port=int(port),
                         username=username,
                         password=password
                         )
    return client


def make_connection(username=uname, password=passwd):
    client = MongoClient(
        f"mongodb+srv://{username}:{password}@sa-tool.4vion3g.mongodb.net/?retryWrites=true&w=majority")
    return client


def get_db(db_name, db_client=make_connection()):
    if db_client is None:
        db_client = make_connection()

    db_handle = db_client[db_name]
    return db_handle


def get_collection(db_handle, collection_name):
    return db_handle[collection_name]

