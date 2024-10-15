import dataclasses

from app.entities.category.category_codes import CategoryCode
from app.entities.collections.base_document import BaseDocument
from app.entities.collections.geo_json import GeoJsonPolygon


@dataclasses.dataclass
class ShopDeliveryAreaSubDocument:
    poly: GeoJsonPolygon


@dataclasses.dataclass
class ShopDocument(BaseDocument):
    name: str
    category_codes: list[CategoryCode] # 카테고리 코드는 개수 제한을 두자.
    delivery_areas: list[ShopDeliveryAreaSubDocument] # 배달구역