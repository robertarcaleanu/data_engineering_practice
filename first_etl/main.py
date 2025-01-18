from first_etl.extract import Extractor
from first_etl.first_etl.load import Loader
from first_etl.transform import Transformer


def main():
    df = Extractor().extract_data()
    df = Transformer().transform(df)
    Loader().load()


if __name__ == "main":
    main()
