import os


DATABASE_URL = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False
BASE_URL = os.getenv('BASE_URL')
BLOG_URL = 'https://blog.theerrata.com'
