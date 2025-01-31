import awswrangler as wr
import polars as pl
from metadata import BUCKET_NAME, START_DATE


class Loader:
    def __init__(self) -> None:
        self.bucket_name = BUCKET_NAME
        self.environment = "production"
    
    def load_data(self, df: pl.DataFrame):
        df = self._add_partition_column(df, START_DATE)
        df = self._transform_df_from_polars_to_pandas(df)
        wr.s3.to_parquet(
              df=df,
              path=f"s3://{self.bucket_name}/departures",
              dataset=True,
              partition_cols=["date"],
              table="departures",
              database=self.environment)
    
    def _transform_df_from_polars_to_pandas(self, df: pl.DataFrame):
        return df.to_pandas()

    def _add_partition_column(self, df: pl.DataFrame, start_date: str) -> pl.DataFrame:
        df = df.with_columns(
            pl.lit(start_date).str.strptime(pl.Date, "%Y-%m-%d %H:%M:%S").alias("date")
            )
        return df