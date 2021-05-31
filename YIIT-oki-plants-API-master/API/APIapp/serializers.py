from django.db.models.query import QuerySet
from rest_framework import serializers

from .models import Post, User, Product, Category, Order, OrderItem

from django.contrib.auth.hashers import make_password

from django.contrib.auth.password_validation import validate_password

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User

        fields = ['username', 'password', 'password2', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
    
  
    


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "cost",
            "amount",
            "get_image",
            "get_thumbnail"
    
        )


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "get_absolute_url",
            "products",
        ]

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "cost",
            "product",
            "amount"
        )

class MyOrderItemSerializer(serializers.ModelSerializer):    
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = (
            "cost",
            "product",
            "amount",
        )

# class MyOrderSerializer(serializers.HyperlinkedModelSerializer):
#     items = MyOrderItemSerializer(many=True)
#     first_name = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field=User.first_name)
#     last_name = serializers.SlugRelatedField(querySet=User.objects.all(), slug_field=User.last_name)
#     city = serializers.SlugRelatedField(querySet=User.objects.all(), slug_field=User.city)
#     street = serializers.SlugRelatedField(querySet=User.objects.all(), slug_field=User.street)
#     zip_code = serializers.SlugRelatedField(querySet=User.objects.all(), slug_field=User.zip_code)
#     house_number = serializers.SlugRelatedField(querySet=User.objects.all(), slug_field=User.house_number)
#     flat_number = serializers.SlugRelatedField(querySet=User.objects.all(), slug_field=User.flat_number)
#     phone_number = serializers.SlugRelatedField(querySet=User.objects.all(), slug_field=User.phone_number)
#     class Meta:
#         model = Order
#         fields = (
#             "id",
#             "first_name",
#             "last_name",
#             "city",
#             "street",
#             "zip_code",
#             "house_number",
#             "flat_number",
#             "phone_number",
#             "items",
#             "stripe_token",
#             "paid_amount"
            
#         )

class MyOrderSerializer(serializers.HyperlinkedModelSerializer):
    items = MyOrderItemSerializer(many=True)
    
    first_name = serializers.RelatedField(source="first_name", read_only=True)
    last_name = serializers.RelatedField(source="last_name", read_only=True)
    city = serializers.RelatedField(source="city", read_only=True)
    street = serializers.RelatedField(source="street", read_only=True)
    zip_code = serializers.RelatedField(source="zip_code", read_only=True)
    house_number = serializers.RelatedField(source="house_number", read_only=True)
    flat_number = serializers.RelatedField(source="flat_number", read_only=True)
    phone_number = serializers.RelatedField(source="phone_number", read_only=True)
    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "city",
            "street",
            "zip_code",
            "house_number",
            "flat_number",
            "phone_number",
            "items",
            "stripe_token",
            "paid_amount"
            
        )

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    items = MyOrderItemSerializer(many=True)
    first_name = serializers.RelatedField(source="first_name", read_only=True)
    last_name = serializers.RelatedField(source="last_name", read_only=True)
    city = serializers.RelatedField(source="city", read_only=True)
    street = serializers.RelatedField(source="street", read_only=True)
    zip_code = serializers.RelatedField(source="zip_code", read_only=True)
    house_number = serializers.RelatedField(source="house_number", read_only=True)
    flat_number = serializers.RelatedField(source="flat_number", read_only=True)
    phone_number = serializers.RelatedField(source="phone_number", read_only=True)
    
    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "city",
            "street",
            "zip_code",
            "house_number",
            "flat_number",
            "phone_number",
            "stripe_token",
            "items"
            
        )

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
            
        return order





