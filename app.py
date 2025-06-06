from flask import Flask, render_template

app = Flask(__name__)

product_list = [
    {"name": "IBANEZ RG421AHM BMT EL GUITAR", "price": "1,599.00₾",
     "image": "https://musikis-saxli.ge/image/cache/catalog/products/237322-800x800.jpg"},
    {"name": "Jackson Pro Series Signature Gus G. San Dimas Style 1. Maple Fingerboard, Candy Apple Red", "price": "4,300.00₾",
     "image": "https://musikis-saxli.ge/image/cache/catalog/products/237818-800x800.jpg"},
    {"name": "Fender Squier Sonic® Mustang® HH, Laurel Fingerboard, Black Pickguard, California Blue", "price": "489.00₾",
     "image": "https://musikis-saxli.ge/image/cache/catalog/products/3160201-800x800.jpg"},
    {"name": "Fender American Professional II Stratocaster, Rosewood Fingerboard, Olympic White", "price": "6,999.00₾",
     "image": "https://musikis-saxli.ge/image/cache/catalog/products/3062918-800x800.jpg"}
]


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def products():
    return render_template("products.html", product_list=product_list)

@app.route("/login")
@app.route("/sign-in")
def login():
    return render_template("login.html")

@app.route("/sign-up")
def signup():
    return render_template("sign-up.html")


@app.route("/profile/<profile_id>")
def profile(profile_id):
    return f"User's profile id: {profile_id}"


if __name__ == "__main__":
    app.run(debug=True)