from api.models import ma, Order


class OrderSerializer(ma.ModelSchema):
    class Meta:
        model = Order
        fields = ('id', 'customer_name', 'customer_email')
