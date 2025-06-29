from ext import db, login_manager
from flask_login import UserMixin

# class BaseModel(db.Model):
#     def create(self):
#         db.session.add(self)
#         db.session.commit()
#
#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()
#
#     @staticmethod
#     def save():
#         db.session.commit()



class Product(db.Model, UserMixin):
    __tablename__ = "products"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    image = db.Column(db.String(), default="default_image.jpg")


class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)