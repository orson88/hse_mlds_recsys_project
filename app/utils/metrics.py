import numpy as np
from typing import List


def precision_at_k(recommended_list: List[str], true_list: List[str], k=5) -> float:
    true_list = np.array(true_list)
    recommended_list = np.array(recommended_list)
    recommended_list = recommended_list[:k]

    flags = np.isin(true_list, recommended_list)
    precision = flags.sum() / len(recommended_list)

    return precision
