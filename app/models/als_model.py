import pickle
from pathlib import Path
from typing import List

from scipy.sparse import csr_matrix, load_npz, save_npz


class ALSModel:
    def __init__(self, model_name: str):
        models_path = Path(__file__).parent
        data_path = Path(__file__).parent.parent / 'data'

        with open(models_path / model_name, 'rb') as f:
            self.model = pickle.load(f)

        self.user_item_matrix = load_npz(data_path / 'train_user_item_matrix.npz').astype('float')
        with open(data_path / 'userids.pkl', 'rb') as f:
            userids = pickle.load(f)

        with open(data_path / 'itemids.pkl', 'rb') as f:
            itemids = pickle.load(f)

        self.userid_to_id = {user_id: idx for idx, user_id in enumerate(userids)}
        self.id_to_userid = {val: key for key, val in self.userid_to_id.items()}

        self.item_to_id = {item_id: idx for idx, item_id in enumerate(itemids)}
        self.id_to_item = {val: key for key, val in self.item_to_id.items()}

    def get_recommendations(self, user_id, n=5, **kwargs) -> List[str]:
        user_index = self.userid_to_id[user_id]
        recs = self.model.recommend(
                userid=user_index, 
                user_items=self.user_item_matrix[user_index],   # на вход user-item matrix
                N=n, # кол-во рекомендаций
                filter_already_liked_items=False,   
                filter_items=None,   
                recalculate_user=False, 
                **kwargs
                )
        
        return [self.id_to_item[rec] for rec in recs[0]]

