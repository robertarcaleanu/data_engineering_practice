import os

import awswrangler as wr
import boto3
import polars as pl
from metadata import BUCKET_NAME, START_DATE


class Loader:
    def __init__(self) -> None:
        self.bucket_name = BUCKET_NAME
        self.environment = "production"
        boto3.setup_default_session(region_name=os.getenv("AWS_REGION"))

    def load_data(self, df: pl.DataFrame):
        df = self._add_partition_column(df, START_DATE)
        wr.s3.to_parquet(
            df=df.to_pandas(),
            path=f"s3://{self.bucket_name}/departures",
            dataset=True,
            partition_cols=["date"],
            table="departures",
            database=self.environment,
        )

    def _add_partition_column(self, df: pl.DataFrame, start_date: str) -> pl.DataFrame:
        df = df.with_columns(
            pl.lit(start_date).str.strptime(pl.Date, "%Y-%m-%d %H:%M:%S").alias("date")
        )
        return df
