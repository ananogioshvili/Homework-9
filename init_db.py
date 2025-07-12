from ext import app, db
from models import Product, User

with app.app_context():
    db.drop_all()
    db.create_all()

    admin_user = User(email="admin", password="<PASSWORD>", role="Admin")
    db.session.add(admin_user)
    db.session.commit()