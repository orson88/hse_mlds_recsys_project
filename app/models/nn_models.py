import pickle
from pathlib import Path
from typing import List

import torch
import numpy as np
from torch import nn
from scipy.sparse import csr_matrix, load_npz, save_npz


class MatrixFactorization(nn.Module):
    def __init__(self, n_users: int, n_items: int, n_factors=150):
        super().__init__()
        self.n_users = n_users
        self.n_items = n_items
        self.user_factors = torch.nn.Embedding(n_users, n_factors, sparse=True)
        self.item_factors = torch.nn.Embedding(n_items, n_factors, sparse=True)

    def forward(self, user, item):
        return (self.user_factors(user) * self.item_factors(item)).sum(1)

    def predict(self, user_index) -> np.array:
        with torch.inference_mode():
            # pred = (
            #     self.item_factors.weight
            #     @ self.user_factors(torch.tensor([user_index])).t()
            # ).reshape(-1).numpy()
            pred = self.forward(
                torch.tensor([user_index]),
                torch.arange(self.n_items)
            ).numpy()

        # sorting item scores descending
        return np.flip(pred.argsort())


class NNModel(nn.Module):
    def __init__(self, net: nn.Module, net_params_path: Path, **kwargs):
        super().__init__()
        self.net = net(**kwargs)

        data_path = Path(__file__).parent.parent / 'data'
        with open(data_path / 'userids.pkl', 'rb') as f:
            userids = pickle.load(f)

        with open(data_path / 'itemids.pkl', 'rb') as f:
            itemids = pickle.load(f)

        self.userid_to_id = {user_id: idx for idx, user_id in enumerate(userids)}
        self.id_to_userid = {val: key for key, val in self.userid_to_id.items()}

        self.item_to_id = {item_id: idx for idx, item_id in enumerate(itemids)}
        self.id_to_item = {val: key for key, val in self.item_to_id.items()}

        model_params = torch.load(net_params_path, map_location=torch.device('cpu'))
        self.net.load_state_dict(model_params['model_state'])

    def get_recommendations(self, user_id, n=5, **kwargs) -> List[str]:
        user_index = self.userid_to_id[user_id]

        with torch.inference_mode():
            scores = self.net.predict(user_index=user_index, **kwargs)

        recs = [
            self.id_to_item[score] for score in scores[:n]
        ]
        return recs
