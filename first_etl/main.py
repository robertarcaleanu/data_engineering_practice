from first_etl.extract import Extractor
from first_etl.transform import Transformer
from first_etl.first_etl.load import Loader

def main():
    Extractor().extract_data()
    Transformer().transform()
    Loader().load()



if __name__== "main":
    main()
    