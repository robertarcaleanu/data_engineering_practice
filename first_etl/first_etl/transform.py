import pandas as pd
from io import StringIO


class Transformer:
    def __init__(self) -> None:
        pass

    def transform(self, load_data) -> pd.DataFrame:
        df = pd.read_csv(StringIO(load_data.text))
        return df
