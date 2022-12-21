import pandas as pd
from pathlib import Path


def join_tracks_feats(df: pd.DataFrame) -> pd.DataFrame:
    workdir = Path(__file__).parent
    tracks_feats = pd.read_csv(workdir / 'tracks_feats.csv', sep='\t')

    df = pd.merge(df, tracks_feats, left_on=['artistname', 'trackname'], right_on=['artist', 'song_name'])

    return df
