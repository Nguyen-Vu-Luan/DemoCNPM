import json


def load_categories(q=None):
    with open('data/categories.json', encoding="utf-8") as f:
        categories = json.load(f)
        if q:
            categories = [p for p in categories if p['id'].find(q) >= 0]
        return categories

def load_products(q=None):
    with open('data/products.json', encoding="utf-8") as f:
        products = json.load(f)
        if q:
            products = [p for p in products if p['name'].find(q) >= 0]
        return products


if __name__ == "__main__":
    print(load_categories())
