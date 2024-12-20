from extract import Extractor
from transform import Transformer
from load import Loader

def main():
    Extractor().extract_data()
    Transformer().transform()
    Loader().load()



if __name__== "main":
    main()
    