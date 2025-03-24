import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.getenv("DEBUG",'False') == 'True'
    MODEL_PATH = os.getenv('MODEL_PATH', 'src/utils/iris_pipeline.pkl')

