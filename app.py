from ext import app


if __name__ == "__main__":
    from routes import home, products, view_product, profile, login, signup, add_product, delete_product, edit_product
    app.run(debug=True)