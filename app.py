from flask import Flask, render_template
from forms import SignUpForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "sdb23b2i3ujbdjdb21"


profiles = []

product_list = [
    {"id":0, "name": "IBANEZ RG421AHM BMT EL GUITAR", "price": "1,599.00₾",
     "image": "https://musikis-saxli.ge/image/cache/catalog/products/237322-800x800.jpg"},
    {"id":1, "name": "Jackson Pro Series Signature Gus G. San Dimas Style 1. Maple Fingerboard, Candy Apple Red", "price": "4,300.00₾",
     "image": "https://musikis-saxli.ge/image/cache/catalog/products/237818-800x800.jpg"},
    {"id":2, "name": "Fender Squier Sonic® Mustang® HH, Laurel Fingerboard, Black Pickguard, California Blue", "price": "489.00₾",
     "image": "https://musikis-saxli.ge/image/cache/catalog/products/3160201-800x800.jpg"},
    {"id":3, "name": "Fender American Professional II Stratocaster, Rosewood Fingerboard, Olympic White", "price": "6,999.00₾",
     "image": "https://musikis-saxli.ge/image/cache/catalog/products/3062918-800x800.jpg"}
]


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def products():
    return render_template("products.html", product_list=product_list)

@app.route("/product/<int:product_id>")
def product(product_id):
    return render_template("product.html", product_details=product_list[product_id])

@app.route("/profile/<int:profile_id>")
def profile(profile_id):
    return render_template("profile.html", profiles=profiles[profile_id])


@app.route("/login")
@app.route("/sign-in")
def login():
    return render_template("login.html")

@app.route("/sign-up", methods=["get", "post"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        new_user = {
            "name": form.name.data,
            "surname": form.surname.data,
            "phone": form.phone.data
        }
        profiles.append(new_user)
        # ერორები უნდა დავამატო
        print(form.name.data, form.surname.data)
    return render_template("sign-up.html", form=form)



if __name__ == "__main__":
    app.run(debug=True)