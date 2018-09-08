from marshmallow import Schema, fields
from api.models import ma, Order


class OrderDao(Schema):
    customer_name = fields.Str(required=True)
    customer_email = fields.Email(required=True, error_messages={'required': 'Missing Argument is required.'})
