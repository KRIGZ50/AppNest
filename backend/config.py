import dotenv
import os


dotenv.load_dotenv()
DATABASE_PATH = os.environ.get("DATABASE_PATH", "keyauth.db")