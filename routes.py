from ext import app, db, login_manager
from flask import render_template, redirect, flash
from forms import SignUpForm, ProductForm, LoginForm
from os import path
from models import Product, User
from flask_login import login_user,logout_user,login_required

from werkzeug.utils import secure_filename
import os

profiles = []

product_list = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/products")
def products():
    products = Product.query.all()
    return render_template("products.html", products=products, role="admin")


@app.route("/product/<int:product_id>")
def view_product(product_id):
    product = Product.query.get(product_id)
    return render_template("product.html", product=product)


@app.route("/profile/<int:profile_id>")
def profile(profile_id):
    return render_template("profile.html", profiles=profiles[profile_id])


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(form.email.data == User.email).first()
        if user != None:
            login_user(user)
            flash("You have been logged in.")
            return redirect("/")

    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route("/sign-up", methods=["get", "post"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        # new_user = {
        #     "image": form.image.data,
        #     "name": form.name.data,
        #     "surname": form.surname.data,
        #     "phone": form.phone.data
        # }
        # image = form.image.data
        # directory = path.join(app.root_path, "static", "images", image.filename)
        # image.save(f"{app.root_path}/static/images/{image.filename}")

        new_user = User(email=form.email.data, password=form.password.data)

        db.session.add(new_user)
        db.session.commit()
        return redirect("/")

        # new_user.create()

        # new_user["images"] = image.filename
        # profiles.append(new_user)
        # # ერორები უნდა დავამატო
        # print(profiles)
    return render_template("sign-up.html", form=form)


@app.route("/add_product", methods=["GET", "POST"])
@login_required
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        new_product = Product(name=form.name.data, price=form.price.data)

        image = form.image.data
        directory = path.join(app.root_path, "static", "images", image.filename)
        image.save(directory)
        new_product.image = image.filename

        db.session.add(new_product)
        db.session.commit()

        # new_product.create()

        return redirect("/products")

    # else:
    #     print("Form errors:", form.errors)

    return render_template("add_product.html", form=form)



@app.route("/delete_product/<int:product_id>", methods=["GET", "POST"])
@login_required
def delete_product(product_id):
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()

    # Product.delete(product)

    return  redirect("/products")


@app.route("/edit_product/<int:product_id>", methods=["GET", "POST"])
@login_required
def edit_product(product_id):
    product = Product.query.get(product_id)
    form = ProductForm(name=product.name, price=product.price, image=product.image)

    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data

        if form.image.data:
            image = form.image.data
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.root_path, "static", "images", filename)
            image.save(image_path)
            product.image = filename

            db.session.add(product)
            db.session.commit()

            # product.save()

        return redirect("/products")

    return render_template("edit_product.html", form=form, product=product)


