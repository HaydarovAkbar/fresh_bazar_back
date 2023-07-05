from elasticsearch_dsl import Document, Text, Index, Field
from .models.product import Product

PUBLISHER_INDEX = Index('products')
PUBLISHER_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)


# @PUBLISHER_INDEX.doc_type
class ProductDocument(Document):
    name = Text()
    description = Text()
    price = Text()

    class Django(object):
        model = Product
