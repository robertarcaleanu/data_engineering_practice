import awswrangler as wr
import pandas as pd
import polars as pl
from metadata import BUCKET_NAME, START_DATE


class Loader:
    def __init__(self) -> None:
        self.bucket_name = BUCKET_NAME
    
    def load_data(self, df: pl.DataFrame):
        s3_url = self._generate_s3_path()
        df = self._add_partition_column(df, START_DATE)
        df = self._transform_df_from_polars_to_pandas(df)
        wr.s3.to_parquet(
              dataframe=df,
              path=s3_url, 
              partition_cols = ["date"])
    
    def _generate_s3_path(self):
        return f"s3://{self.bucket_name}/departures/"

    def _transform_df_from_polars_to_pandas(self, df: pl.DataFrame) -> pd.DataFrame:
        return df.to_pandas()

    def _add_partition_column(self, df: pl.DataFrame, start_date: str) -> pl.DataFrame:
        df = df.with_columns(
            pl.lit(start_date).str.strptime(pl.Datetime, "%Y-%m-%d %H:%M:%S").alias("date")
            )