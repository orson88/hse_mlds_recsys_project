from fastapi import FastAPI
from scipy.sparse import load_npz
import pickle
import pandas as pd
import os
from pydantic import BaseModel
PROJ_PATH = os.path.dirname(
    os.path.dirname(
        os.path.realpath(__file__)
    )
)

class UserInput(BaseModel):
    user_id: str
    n: int

popular_songs = pd.read_csv(f"{PROJ_PATH}/datasets/popular_songs.csv")
user_item_matrix = load_npz(f"{PROJ_PATH}/app/data/train_user_item_matrix.npz")
user_item_matrix = user_item_matrix.astype('float').tocsr()

with open(f"{PROJ_PATH}/app/models/als_best_params.pkl", 'rb') as f:
    als = pickle.load(f)

with open(f"{PROJ_PATH}/app/data/userids.pkl", 'rb') as f:
    userids = pickle.load(f)

with open(f"{PROJ_PATH}/app/data/itemids.pkl", 'rb') as f:
    itemids = pickle.load(f)

# Словари для перевода userid в id и наоборот
userid_to_id = {user_id: idx for idx, user_id in enumerate(userids)}
id_to_userid = {val: key for key, val in userid_to_id.items()}

# Словари для перевода itemid в id и наоборот
item_to_id = {item_id: idx for idx, item_id in enumerate(itemids)}
id_to_item = {val: key for key, val in item_to_id.items()}

app = FastAPI()
@app.get("/predictions")
async def get_recommendations(input:UserInput):
    if input.user_id in userid_to_id:  # рекомендации для луществующих пользователей
        user_index = userid_to_id[input.user_id]
        recs = als.recommend(
            userid=user_index,
            user_items=user_item_matrix[user_index],
            N=input.n,  # кол-во рекомендаций
            filter_already_liked_items=False,
            filter_items=None,
            recalculate_user=False
        )

        return [id_to_item[rec] for rec in recs[0]]

    else:  # самые популярные треки для новых пользователей
        return list(popular_songs.iloc[:input.n, 1])

