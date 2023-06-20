import psycopg2
import pandas as pd
import scipy.sparse as scpspr
import pickle
from fastapi import FastAPI
import os

class MyConnection:
    def __init__(self):
        self.conn = psycopg2.connect(
            host = os.environ.get('POSTGRES_SERVICE_HOST'),
            port = 5432,
            user = 'postgres',
            password = 'test1',
            database = 'postgres'
        )
    def reinit_conn(self):
        self.conn = psycopg2.connect(
            host = os.environ.get('POSTGRES_SERVICE_HOST'),
            port = 5432,
            user = 'postgres',
            password = 'test1',
            database = 'postgres'
        )
    def get_query(self, query):
        self.reinit_conn()
        cursor = self.conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        df = pd.DataFrame(
            data,
            columns=[desc[0] for desc in cursor.description]
        )
        cursor.close()
        self.conn.close()
        return df

    def post_query(self, query):
        self.reinit_conn()
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        cursor.close()
        self.conn.close()







MC = MyConnection()


#### ДОЗА КОСТЫЛЕЙ
popular_songs = pd.read_csv(f"/var/popular_songs.csv")
user_item_matrix = scpspr.load_npz('/var/train_user_item_matrix.npz')
user_item_matrix = user_item_matrix.astype('float').tocsr()
with open('/var/als_best_params.pkl', 'rb') as f:
    als = pickle.load(f)

def gen_new_user_id():
    cnt = MC.get_query(f"""
    SELECT COUNT(DISTINCT user_id)
    FROM (
    SELECT user_id FROM train_table
    UNION
    SELECT user_id FROM test_table
    ) combined_set;
    """)['count'][0]
    return cnt+1

def gen_new_item_id():
    cnt = MC.get_query(f"""
    SELECT COUNT(DISTINCT song)
    FROM (
    SELECT song FROM train_table
    UNION
    SELECT song FROM test_table
    ) combined_set;
    """)['count'][0]
    return cnt+1

#### ЗАПРОСЫ К БД


userids = MC.get_query("SELECT DISTINCT user_id FROM train_table").values
userids = [_[0] for _ in userids]
itemids = MC.get_query("SELECT DISTINCT song FROM train_table").values
itemids = [_[0] for _ in itemids]


userid_to_id = {user_id: idx for idx, user_id in enumerate(userids)}
id_to_userid = {val: key for key, val in userid_to_id.items()}

item_to_id = {item_id: idx for idx, item_id in enumerate(itemids)}
id_to_item = {val: key for key, val in item_to_id.items()}

#### АПИ (AKA - Пошла Жара)
app = FastAPI()
@app.get("/predictions")
async def get_recommendations(user_id:str, n:str):
    
    n = int(n)
    if user_id in userid_to_id:  # рекомендации для луществующих пользователей
        user_index = userid_to_id[user_id]
        recs = als.recommend(
            userid=user_index,
            user_items=user_item_matrix[user_index],
            N=n,  # кол-во рекомендаций
            filter_already_liked_items=False,
            filter_items=None,
            recalculate_user=False
        )

        return [id_to_item[rec] for rec in recs[0]]

    else:  # самые популярные треки для новых пользователей
        return list(popular_songs.iloc[:n, 1])


@app.get("/all_users")
async def get_users(input):
    if input == 'gigalul':
        return list(MC.get_query("SELECT DISTINCT user_id FROM train_table")['user_id'].values)
    else:
        return "asdf"

@app.post('/register')
async def reg_new_reaction(input: str):
    if len(input.split(' --- ')) == 2:
        if len(input.split('__')) == 2:
            MC.post_query(f"""
            INSERT INTO test_table (user_id, song, new_user_id, song_id, connect)
            VALUES ('{input.split(' --- ')[0]}', '{input.split(' --- ')[1]}', {gen_new_user_id()}, {gen_new_item_id()}, 1);
            """)