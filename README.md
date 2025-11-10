E-commerce Clothing Store (Flask)

Overview
This is a lightweight, responsive e-commerce web application built with Python (Flask). Users can:
- Browse clothing products with filters (age group, gender, price range, size)
- View product details (images, sizes available, price, description)
- Manage a shopping cart (add, update quantity, remove, clear)

Tech Stack
- Backend: Python 3 + Flask
- Templates: Jinja2 (server-rendered HTML)
- Styles: Minimal CSS, responsive layout
- State: Server-side session (cart)

Getting Started
1) Create and activate a virtual environment (Windows PowerShell):
   python -m venv .venv
   .\\.venv\\Scripts\\Activate.ps1

2) Install dependencies:
   pip install -r requirements.txt

3) Run the app:
   python app\\app.py

4) Open in browser:
   http://127.0.0.1:5000

Project Structure
- app/
  - app.py               Flask entrypoint and route definitions
  - models.py            Domain models for Product and Cart
  - data.py              Seed product catalog with images/sizes/prices
  - templates/
    - base.html
    - index.html
    - product.html
    - cart.html
  - static/
    - styles.css
- docs/
  - technical_architecture.md
  - prompts.md
- requirements.txt
- README.md

Notes
- Product data is in-memory for demo purposes. Replace with a database for production use.
- Sessions use Flask’s secure cookie session. Configure a strong SECRET_KEY in production via environment variable.


