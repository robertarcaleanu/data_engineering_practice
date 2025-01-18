import pandas as pd
import awswrangler as wr


class Loader:
    def __init__(self) -> None:
        pass

    def load(self, df: pd.DataFrame):
        wr.s3.to_parquet(df=df, path="s3://robert-arc-test-bucket/test.parquet")
