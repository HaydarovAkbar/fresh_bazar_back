from elasticsearch_dsl import Document, Text

class ProductDocument(Document):
    name = Text()
    description = Text()

    class Index:
        name = 'products'