from marshmallow import Schema, fields


class OrderDao(Schema):
    customer_name = fields.Str(required=True)
    customer_email = fields.Email(required=True)
    comments = fields.List(fields.String(), required=True)
