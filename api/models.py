from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class BaseModelMixin(object):
    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        db.session.add(obj)
        db.session.commit()
        return obj

    @classmethod
    def bulk_create(cls, cls_list):
        for obj in cls_list:
            db.session.add(obj)

        db.session.flush()
        db.session.commit()


class Order(BaseModelMixin, db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(120), nullable=False)
    comments = db.relationship('Comment', backref='order', lazy=True)


class Comment(BaseModelMixin, db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
