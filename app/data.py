from typing import List, Optional, Dict, Any
from .models import Product


_PRODUCTS: List[Product] = [
	Product(
		id="p001",
		name="Classic Tee",
		description="Soft cotton tee for everyday comfort.",
		gender="unisex",
		age_group="adults",
		category="tops",
		price=19.99,
		sizes=["S", "M", "L", "XL"],
		image_url="https://images.unsplash.com/photo-1512436991641-6745cdb1723f?w=800&q=80",
	),
	Product(
		id="p002",
		name="Kids Hoodie",
		description="Warm and cozy hoodie for kids.",
		gender="unisex",
		age_group="kids",
		category="outerwear",
		price=24.99,
		sizes=["XS", "S", "M"],
		image_url="https://images.unsplash.com/photo-1516259762381-22954d7d3ad2?w=800&q=80",
	),
	Product(
		id="p003",
		name="Women’s Denim Jacket",
		description="Timeless denim jacket with a modern cut.",
		gender="women",
		age_group="adults",
		category="outerwear",
		price=59.5,
		sizes=["S", "M", "L"],
		image_url="https://images.unsplash.com/photo-1520975922284-4f0f46307f1d?w=800&q=80",
	),
	Product(
		id="p004",
		name="Men’s Chinos",
		description="Stretch chinos for style and comfort.",
		gender="men",
		age_group="adults",
		category="bottoms",
		price=42.0,
		sizes=["30", "32", "34", "36"],
		image_url="https://images.unsplash.com/photo-1516822003754-cca485356ecb?w=800&q=80",
	),
	Product(
		id="p005",
		name="Teens Graphic Tee",
		description="Bold graphic tee for teens.",
		gender="unisex",
		age_group="teens",
		category="tops",
		price=17.25,
		sizes=["S", "M", "L"],
		image_url="https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=800&q=80",
	),
	Product(
		id="p006",
		name="Women’s Summer Dress",
		description="Lightweight dress perfect for warm days.",
		gender="women",
		age_group="adults",
		category="dresses",
		price=49.99,
		sizes=["S", "M", "L"],
		image_url="https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?w=800&q=80",
	),
	Product(
		id="p007",
		name="Kids Joggers",
		description="Comfortable joggers for active kids.",
		gender="unisex",
		age_group="kids",
		category="bottoms",
		price=22.75,
		sizes=["XS", "S", "M"],
		image_url="https://images.unsplash.com/photo-1551022370-1b5b3c6a9f47?w=800&q=80",
	),
	Product(
		id="p008",
		name="Men’s Sports Jacket",
		description="Light sports jacket for casual wear.",
		gender="men",
		age_group="adults",
		category="outerwear",
		price=65.0,
		sizes=["M", "L", "XL"],
		image_url="https://images.unsplash.com/photo-1512320050020-2c48fb0a37f1?w=800&q=80",
	),
	Product(
		id="p009",
		name="Teens Hoodie",
		description="Trendy hoodie for teens.",
		gender="unisex",
		age_group="teens",
		category="outerwear",
		price=28.0,
		sizes=["S", "M", "L"],
		image_url="https://images.unsplash.com/photo-1520975656235-09515d6d3815?w=800&q=80",
	),
	Product(
		id="p010",
		name="Women’s Yoga Pants",
		description="High-waist yoga pants for comfort.",
		gender="women",
		age_group="adults",
		category="bottoms",
		price=39.99,
		sizes=["S", "M", "L", "XL"],
		image_url="https://images.unsplash.com/photo-1555529669-e69e7aa0ba9a?w=800&q=80",
	),
]


def get_product_by_id(product_id: str) -> Optional[Product]:
	for p in _PRODUCTS:
		if p.id == product_id:
			return p
	return None


def get_all_products(
	gender: Optional[str] = None,
	age_group: Optional[str] = None,
	size: Optional[str] = None,
	min_price: Optional[float] = None,
	max_price: Optional[float] = None,
	search: Optional[str] = None,
) -> List[Product]:
	results = list(_PRODUCTS)
	if gender:
		results = [p for p in results if p.gender == gender]
	if age_group:
		results = [p for p in results if p.age_group == age_group]
	if size:
		results = [p for p in results if size in p.sizes]
	if min_price is not None:
		results = [p for p in results if p.price >= min_price]
	if max_price is not None:
		results = [p for p in results if p.price <= max_price]
	if search:
		q = search.lower()
		results = [p for p in results if q in p.name.lower() or q in p.description.lower()]
	return results


def list_filters() -> Dict[str, Any]:
	return {
		"genders": ["men", "women", "unisex"],
		"age_groups": ["kids", "teens", "adults"],
		"sizes": sorted({s for p in _PRODUCTS for s in p.sizes}),
		"categories": sorted({p.category for p in _PRODUCTS}),
	}


