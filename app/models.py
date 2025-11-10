from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any


@dataclass
class Product:
	id: str
	name: str
	description: str
	gender: str                 # "men", "women", "unisex"
	age_group: str              # "kids", "teens", "adults"
	category: str               # "tops", "bottoms", "outerwear", etc.
	price: float
	sizes: List[str]
	image_url: str

	def to_dict(self) -> Dict[str, Any]:
		return asdict(self)


@dataclass
class CartItem:
	product_id: str
	name: str
	price: float
	size: Optional[str]
	quantity: int
	image_url: str

	def subtotal(self) -> float:
		return round(self.price * self.quantity, 2)

	def to_dict(self) -> Dict[str, Any]:
		return {
			"product_id": self.product_id,
			"name": self.name,
			"price": self.price,
			"size": self.size,
			"quantity": self.quantity,
			"image_url": self.image_url,
		}

	@staticmethod
	def from_dict(data: Dict[str, Any]) -> "CartItem":
		return CartItem(
			product_id=data["product_id"],
			name=data["name"],
			price=float(data["price"]),
			size=data.get("size"),
			quantity=int(data["quantity"]),
			image_url=data.get("image_url", ""),
		)


@dataclass
class Cart:
	items: List[CartItem] = field(default_factory=list)

	def add_item(self, product: Product, size: Optional[str], quantity: int = 1) -> None:
		for item in self.items:
			if item.product_id == product.id and item.size == size:
				item.quantity += quantity
				return
		self.items.append(CartItem(
			product_id=product.id,
			name=product.name,
			price=product.price,
			size=size,
			quantity=quantity,
			image_url=product.image_url
		))

	def update_item(self, product_id: str, size: Optional[str], quantity: Optional[int]) -> None:
		for item in self.items:
			if item.product_id == product_id and item.size == size:
				if quantity is None or quantity < 1:
					self.items.remove(item)
				else:
					item.quantity = quantity
				return

	def remove_item(self, product_id: str, size: Optional[str]) -> None:
		self.items = [i for i in self.items if not (i.product_id == product_id and i.size == size)]

	def total(self) -> float:
		return round(sum(i.subtotal() for i in self.items), 2)

	def to_dict(self) -> Dict[str, Any]:
		return {"items": [i.to_dict() for i in self.items]}

	@staticmethod
	def from_dict(data: Dict[str, Any]) -> "Cart":
		items = [CartItem.from_dict(d) for d in data.get("items", [])]
		return Cart(items=items)


