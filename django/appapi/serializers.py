from rest_framework import serializers
from .models import RasPi, User, UserBottle, BottleType, Container, ContainerImage
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email_address', 'hash_password',]
        read_only_fields = ['id', ]

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email_address = validated_data.get('email_address', instance.email_address)
        instance.hash_password = validated_data.get('hash_password', instance.hash_password)
        instance.save()
        return instance


class RasPiSerializer(serializers.ModelSerializer):
    class Meta:
        model = RasPi
        fields = ['id', 'individual_id', 'mac_address', 'in_use',]
        read_only_fields = ['id', ]

    def create(self, validated_data):
        return RasPi.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.individual_id = validated_data.get('individual_id', instance.individual_id)
        instance.mac_address = validated_data.get('mac_address', instance.mac_address)
        instance.is_use = validated_data.get('is_use', instance.is_use)
        instance.save()
        return instance

class UserBottleSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = UserBottle
        fields = ['id', 'name', 'product_name', 'user_id', 'raspi_id', 'bottle_type_id', 'container_id', 'bottle_volume', 'remaining_quantity', 'is_favorite', 'memo', 'created_at']
        read_only_fields = ['id', 'user_id', 'raspi_id', ]
        extra_kwargs = {
            # 'bottle_type_id': {'allow_blank': True, 'allow_null': True},
            'memo': {'allow_null': True, 'required': False}
        }
        # depth = 1

    def create(self, validated_data):
        return UserBottle.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.container_id = validated_data.get('container_id', instance.container_id)
        instance.bottle_volume = validated_data.get('bottle_volume', instance.bottle_volume)
        instance.remaining_quantity = validated_data.get('remaining_quantity', instance.remaining_quantity)
        instance.is_favorite = validated_data.get('is_favorite', instance.is_favorite)
        instance.memo = validated_data.get('memo', instance.memo)
        instance.save()
        return instance



# class ContainerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Container
#         fields = ['id', 'name']
#         read_only_fields = ['id',]
    
#     def create(self, validated_data):
#         return Container.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.save()
#         return instance

# class ContainerImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ContainerImage
#         fields = ['container_id', 'quantity', 'container_image']
    
#     def create(self, validated_data):
#         return ContainerImage.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.container_id = validated_data.get('container_id', instance.container_id)
#         instance.quantity = validated_data.get('quantity', instance.quantity)
#         instance.container_image = validated_data.get('container_image', instance.container_image)
#         instance.save()
#         return instance

# class FavoriteSerializer(serializers.BaseSerializer):
#     def to_internal_value(self, data):
#         id = data.get('id')
#         is_favorite = data.get('is_favorite')

#         return {
#             'id': id,
#             'is_favorite': is_favorite
#         }

#     def to_representation(self, instance):
#         return {
#             'id': instance.id,
#             'is_favorie': instance.is_favorite
#         }