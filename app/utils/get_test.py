import json
import pandas as pd
from pathlib import Path


def get_test(df: pd.DataFrame) -> pd.DataFrame:
    """

    :param df: All DataFrame
    :return: Test DataFrame
    """
    workdir = Path(__file__).parent

    if 'song' not in df.columns:
        df['artistname'].fillna('', inplace=True)
        df['trackname'].fillna('', inplace=True)

        df['song'] = df['artistname'] + '__' + df['trackname']

    with open(workdir.parent / 'data' / 'test_index.json') as f:
        test_index = json.load(f)

    test = (df.loc[test_index]
            .groupby('user_id')['song'].unique()
            .reset_index())

    test.rename(columns={'song': 'actual'}, inplace=True)

    assert test.shape[0] == 14560

    return test
