from app.entities.category.category_codes import CategoryCode
from app.entities.collections.geo_json import GeoJsonPolygon
from app.entities.collections.shop.shop_collection import ShopCollection
from app.entities.collections.shop.shop_document import ShopDeliveryAreaSubDocument


async def test_shop_insert_one() -> None:
    # Given
    name = "치킨집"
    category_codes = [CategoryCode.CHICKEN]
    delivery_areas = [
        ShopDeliveryAreaSubDocument(
            poly=GeoJsonPolygon(coordinates=[[[0, 0], [0, 10], [10, 10], [10, 0], [0, 0]]]),
        )
    ]

    # When
    shop = await ShopCollection.insert_one(name=name, category_codes=category_codes, delivery_areas=delivery_areas)
    # results = await ShopCollection._collection.find({name : "치킨집"}).to_list(None)
    cursor = await ShopCollection._collection.find({}).to_list(None)
    # results = await cursor.to_list(None)
    results = await cursor.to_list(100) # LIMIT 100

    # Then
    assert len(results) == 1
    result = results[0]
    assert result["_id"] == shop.id
    assert result["name"] == shop.name
    assert result["category_codes"] == ["chicken"]
    assert result["delivery_areas"] == [
        {"poly": {"type": "Polygon", "coordinates": [[[0, 0], [0, 10], [10, 10], [10, 0], [0, 0]]]}}
    ]