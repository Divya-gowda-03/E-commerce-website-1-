Technical Architecture - E-commerce Clothing Store

Overview
This document describes the architecture for a lightweight, Python-based e-commerce prototype that supports browsing, filtering, product details, and a session-backed shopping cart.

Goals
- Clean, responsive UI
- Simple Python backend to handle data and cart state
- Extensible product model with categories, sizes, gender, age group
- Minimal dependencies; easy to run locally

System Design
1) Client/UI
- Server-rendered HTML templates (Jinja2) for listing, filters, product details, and cart.
- Minimal CSS (no JS required) with responsive grid and forms.
- Forms submit via GET (filters, search) and POST (cart actions).

2) Backend
- Framework: Flask (Python 3)
- Routing:
  - GET / : product listing + filters (age, gender, size, price range, search)
  - GET /product/<id> : product detail page
  - GET /cart : view cart
  - POST /cart/add : add item to cart
  - POST /cart/update : update item quantity
  - POST /cart/remove : remove an item
  - POST /cart/clear : clear cart
- Session:
  - Flask secure cookie session stores cart as a serializable dict.

3) Data
- Seed data: in-memory list of Products with attributes:
  - id, name, description, gender, age_group, category, price, sizes, image_url
- Data access functions:
  - get_all_products(...) with filtering by gender, age_group, size, min/max price, and text search
  - get_product_by_id(id)
  - list_filters(): for UI dropdown population
- In production, replace in-memory data with a database (e.g., Postgres) or external API.

4) Domain Model (Python dataclasses)
- Product: immutable catalog record
- CartItem: product snapshot (id, name, price, size, quantity, image_url)
- Cart:
  - add_item(product, size, quantity)
  - update_item(product_id, size, quantity)
  - remove_item(product_id, size)
  - total()
  - to_dict() / from_dict() for session storage

Security & Config
- SECRET_KEY: environment-driven; defaults to a dev value.
- ProxyFix: enables correct URL generation behind proxies if deployed.
- Input validation:
  - Ensures product exists and size is valid for that product.
  - Quantity update: remove on zero or invalid values.

Performance & Scalability
- Server-side rendering keeps frontend simple and fast.
- In-memory catalog is O(n) filtering; adequate for prototypes.
- For scale:
  - Move catalog to DB with indexes (gender, age_group, price, size availability).
  - Add pagination and caching.
  - Use server-side sessions or persistent cart storage (e.g., Redis).

Extensibility
- Add user accounts; persist carts by user.
- Add inventory and stock checks per size.
- Add wishlist, checkout, payments integration.
- Add images CDN and thumbnail generation.

Build & Run
- pip install -r requirements.txt
- python app/app.py
- Visit http://127.0.0.1:5000

Testing Ideas
- Unit test Cart methods for add/update/remove/total.
- Integration test routes for 200 responses and redirects.
- Snapshot test HTML responses for key pages.


