from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.middleware.proxy_fix import ProxyFix
from .models import Product, Cart, CartItem
from .data import get_all_products, get_product_by_id, list_filters
import os


def create_app() -> Flask:
	app = Flask(__name__, template_folder="templates", static_folder="static")
	app.wsgi_app = ProxyFix(app.wsgi_app)
	app.secret_key = os.environ.get("SECRET_KEY", "dev-insecure-secret")

	@app.context_processor
	def inject_filters():
		return {
			"FILTERS": list_filters()
		}

	def get_cart() -> Cart:
		if "cart" not in session:
			session["cart"] = Cart(items=[]).to_dict()
		return Cart.from_dict(session["cart"])

	def save_cart(cart: Cart) -> None:
		session["cart"] = cart.to_dict()
		session.modified = True

	@app.route("/")
	def index():
		# Query parameters for filters
		gender = request.args.get("gender")
		age_group = request.args.get("age")
		size = request.args.get("size")
		min_price = request.args.get("min_price", type=float)
		max_price = request.args.get("max_price", type=float)
		search = request.args.get("q", type=str)

		products = get_all_products(
			gender=gender,
			age_group=age_group,
			size=size,
			min_price=min_price,
			max_price=max_price,
			search=search
		)
		return render_template("index.html", products=products)

	@app.route("/product/<product_id>")
	def product_detail(product_id: str):
		product = get_product_by_id(product_id)
		if not product:
			flash("Product not found.", "error")
			return redirect(url_for("index"))
		return render_template("product.html", product=product)

	@app.route("/cart")
	def view_cart():
		cart = get_cart()
		return render_template("cart.html", cart=cart)

	@app.route("/cart/add", methods=["POST"])
	def add_to_cart():
		product_id = request.form.get("product_id")
		size = request.form.get("size")
		quantity = request.form.get("quantity", type=int) or 1
		product = get_product_by_id(product_id)
		if not product:
			flash("Unable to add: Product not found.", "error")
			return redirect(url_for("index"))
		if size and size not in product.sizes:
			flash("Selected size is not available.", "error")
			return redirect(url_for("product_detail", product_id=product_id))
		cart = get_cart()
		cart.add_item(product, size, quantity)
		save_cart(cart)
		flash("Added to cart.", "success")
		return redirect(url_for("view_cart"))

	@app.route("/cart/update", methods=["POST"])
	def update_cart():
		product_id = request.form.get("product_id")
		size = request.form.get("size")
		quantity = request.form.get("quantity", type=int)
		cart = get_cart()
		cart.update_item(product_id, size, quantity)
		save_cart(cart)
		flash("Cart updated.", "success")
		return redirect(url_for("view_cart"))

	@app.route("/cart/remove", methods=["POST"])
	def remove_from_cart():
		product_id = request.form.get("product_id")
		size = request.form.get("size")
		cart = get_cart()
		cart.remove_item(product_id, size)
		save_cart(cart)
		flash("Removed from cart.", "success")
		return redirect(url_for("view_cart"))

	@app.route("/cart/clear", methods=["POST"])
	def clear_cart():
		save_cart(Cart(items=[]))
		flash("Cart cleared.", "success")
		return redirect(url_for("view_cart"))

	return app


if __name__ == "__main__":
	application = create_app()
	application.run(debug=True)  # For development


