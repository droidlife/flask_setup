from api.models import ma, Order, Comment
import datetime
from marshmallow import fields


class CommentDto(ma.ModelSchema):
    class Meta:
        model = Comment
        fields = ('text', )


class OrderDto(ma.ModelSchema):
    since_created = fields.Method("get_days_since_created")
    comments = ma.Nested(CommentDto, many=True)

    def get_days_since_created(self, obj):
        return datetime.datetime.now().day

    class Meta:
        model = Order
        fields = ('id', 'customer_name', 'customer_email', 'comments', 'since_created')
