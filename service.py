from fastapi import FastAPI
import pickle
from scipy.sparse import load_npz


app = FastAPI(
    title="RecSys App"
)


@app.get("/")
async def root():
    return "root"


user_item_matrix = load_npz('app/data/train_user_item_matrix.npz')
user_item_matrix = user_item_matrix.astype('float').tocsr()

with open('app/models/als_best_params.pkl', 'rb') as f:
    als = pickle.load(f)

with open('app/data/userids.pkl', 'rb') as f:
    userids = pickle.load(f)

with open('app/data/itemids.pkl', 'rb') as f:
    itemids = pickle.load(f)

userid_to_id = {user_id: idx for idx, user_id in enumerate(userids)}
id_to_userid = {val: key for key, val in userid_to_id.items()}

item_to_id = {item_id: idx for idx, item_id in enumerate(itemids)}
id_to_item = {val: key for key, val in item_to_id.items()}


@app.get("/predictions")
async def get_recommendations(user_id: str = '00055176fea33f6e027cd3302289378b', n: int = 5):
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
