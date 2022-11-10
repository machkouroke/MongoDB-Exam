from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv(".env"))
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
MONGO_URL = os.getenv("MONGO_URL")