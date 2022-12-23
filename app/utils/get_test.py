import json
import pandas as pd
from pathlib import Path


def get_test(df: pd.DataFrame) -> pd.DataFrame:
    """

    :param df: All DataFrame
    :return: Test DataFrame
    """
    workdir = Path(__file__)

    with open(workdir / 'test_index.json') as f:
        test_index = json.load(f)

    test = (df.loc[test_index]
            .groupby('user_id')['song'].unique()
            .reset_index())

    test.rename(columns={'song': 'actual'})

    assert test.shape[0] == 14560

    return test
