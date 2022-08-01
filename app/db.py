import os
from flask import g

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv(verbose=True)


def get_db():
    if 'db' not in g:
        client = MongoClient(os.getenv('DATABASE'))
        g.db = client.test

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
