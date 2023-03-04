import numpy as np
from typing import List


def precision(true_list: List[str], recommended_list: List[str]) -> float:
    true_list = np.array(true_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(true_list, recommended_list)
    precision = flags.sum() / len(recommended_list)

    return precision


def precision_at_k(true_list: List[str], recommended_list: List[str], k=5) -> float:
    recommended_list = recommended_list[:k]

    return precision(true_list, recommended_list)


def recall(true_list: List[str], recommended_list: List[str]) -> float:
    true_list = np.array(true_list)
    recommended_list = np.array(recommended_list)
    recommended_list = recommended_list

    flags = np.isin(true_list, recommended_list)
    recall = flags.sum() / len(true_list)

    return recall


def recall_at_k(true_list: List[str], recommended_list: List[str], k=5) -> float:
    recommended_list = recommended_list[:k]

    return recall(true_list, recommended_list)


def ap_k(true_list: List[str], recommended_list: List[str], k=5) -> float:
    if len(recommended_list) > k:
        recommended_list = recommended_list[:k]

    score = 0.
    num_hits = 0.

    for i, p in enumerate(recommended_list):
        if p in true_list and p not in recommended_list[:i]:
            num_hits += 1
            score += num_hits / (i+1)

    if len(true_list) == 0:
        return 0.

    return score / min(len(true_list), k)


def map_k(true_list: List[str], recommended_list: List[str], k=5) -> float:
    return np.mean([ap_k(a, p, k) for a, p in zip(true_list, recommended_list)])
