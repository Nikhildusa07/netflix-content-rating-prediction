import pandas as pd


def prepare_features(df):
    df = df.copy()

    df["content_features"] = (
        df["type"].astype(str) + " " +
        df["director"].astype(str) + " " +
        df["country"].astype(str) + " " +
        df["listed_in"].astype(str)
    )

    return df