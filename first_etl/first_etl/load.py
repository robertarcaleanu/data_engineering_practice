import pandas as pd
import awswrangler as wr

class Loader:
    def __init__(self) -> None:
        pass

    def load(self, df: pd.DataFrame):
        wr.s3.to_parquet(
            df=df,
            database="production",
            dataset=True,
            table="nobel_prize",
            path='s3://bucket/',
            partition_cols=[],
            mode="overwrite_partitions"
        )