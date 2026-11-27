import sqlite3
import os
from config import DATABASE_PATH


con = sqlite3.connect(DATABASE_PATH)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = os.path.join(BASE_DIR , "schema.sql")

with open(SCHEMA_PATH) as f:
    con.executescript(f.read())