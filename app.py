from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "https://fakestoreapi.com/products"

@app.route("/")
def index():
    response = requests.get(API_URL)
    products = response.json()
    return render_template("index.html", products=products)

@app.route("/product/<int:product_id>")
def detail(product_id):
    response = requests.get(f"{API_URL}/{product_id}")
    product = response.json()
    return render_template("detail.html", product=product)

if __name__ == "__main__":
    app.run(debug=True)
