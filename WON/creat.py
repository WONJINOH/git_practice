import psycopg2
from pgvector.psycopg2 import register_vector
import numpy as np

conn = None

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

title = input('title?')
body = input('body?')
response = openai.Embedding.create(
    input=f'''title:{title}\n\nbody:{body}''',
    model="text-embedding-ada-002"
)

embeddings = np.array(response['data'][0]['embedding'])
cursor.execute('INSERT INTO topics (title, body, embedding) VALUES(%s, %s, %s)', (title, body, embeddings))

# cursor.execute('INSERT INTO topics (title, body) VALUES(%s, %s)', (title, body))
conn.commit()
conn.close()
