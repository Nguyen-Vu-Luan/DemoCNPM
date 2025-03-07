from flask import Flask, render_template, request
from dao import load_categories, load_products

app = Flask(__name__)


@app.route("/")
def index():
    categories = load_categories()
    q = request.args.get("q")
    products = load_products(q)
    return render_template("index.html", categories=categories, products=products)


if __name__ == "__main__":
    app.run(debug=True)
