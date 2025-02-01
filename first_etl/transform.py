import polars as pl


class Transformer:
    def __init__(self) -> None:
        self.COLUMNS = [
            "icao24",
            "callsign",
            "departure_datetime",
            "departure_airport",
            "arrival_datetime",
            "arrival_aiport",
        ]
        self.columns_mapping = {
            "firstSeen": "departure_datetime",
            "estDepartureAirport": "departure_airport",
            "lastSeen": "arrival_datetime",
            "estArrivalAirport": "arrival_aiport",
        }

    def transform(self, source: list):
        df = self._transform_from_list_to_df(source)
        df = self._convert_columns_from_unix_time_to_utc(df)
        df = self._keep_relevant_columns(df)
        df = self._calculate_flight_duration(df)

        return df

    def _transform_from_list_to_df(self, source) -> pl.DataFrame:
        return pl.DataFrame(source)

    def _convert_columns_from_unix_time_to_utc(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.with_columns(
            pl.from_epoch(pl.col("lastSeen"), time_unit="s"),
            pl.from_epoch(pl.col("firstSeen"), time_unit="s"),
        )

    def _keep_relevant_columns(self, df: pl.DataFrame) -> pl.DataFrame:
        df = df.rename(self.columns_mapping)
        df = df.select(self.COLUMNS)

        return df

    def _calculate_flight_duration(self, df: pl.DataFrame) -> pl.DataFrame:
        df = df.with_columns(
            (pl.col("arrival_datetime") - pl.col("departure_datetime"))
            .dt.total_minutes()
            .alias("flight_duration_in_minutes")
        )
        return df
