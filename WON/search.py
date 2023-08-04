import psycopg2
from pgvector.psycopg2 import register_vector
import numpy as np


conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="dnjswls38@!",
    host="db.pucmlvpdzlrswkmiljmp.supabase.co", #sapabase 데이터베이스가 설치되어있는 주소 - database seeting에서 host주소 
    port="5432",
)
cursor = conn.cursor()
register_vector(cursor)

import openai

search = input('search? ')
response = openai.Embedding.create(
    input=search,
    model="text-embedding-ada-002"
)
embedding = np.array(response['data'][0]['embedding'])

