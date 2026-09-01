import pandas as pd
import os


def load_data():
    base_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    data_path = os.path.join(
        base_dir,
        "data",
        "Dataset.csv"
    )

    return pd.read_csv(data_path)


def clean_data(df):
    df = df.copy()

    df = df.drop_duplicates()

    columns = [
        "type",
        "director",
        "country",
        "rating",
        "listed_in"
    ]

    for column in columns:
        if column in df.columns:
            df[column] = (
                df[column]
                .fillna("Not Given")
                .astype(str)
                .str.strip()
            )

    return df