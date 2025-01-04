import pandas as pd


def load(path: str) -> pd.DataFrame:
    """load a CSV file into pandas"""
    try:
        assert type(path) is str, "path must be string"
    except AssertionError as e:
        print("AssertionError:", e)
        return None

    try:
        df = pd.read_csv(path)
    except Exception as e:
        print(e)
        return None

    print("Loading dataset of dimensions", df.shape)
    return df
