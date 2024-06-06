from rest_framework import serializers

from base.models import (
    ElectricBill,
    WaterBill,
    TelecomBill,
    User,
)

from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def validate_password(self, value: str) -> str:
        hashed_password = make_password(value)
        return hashed_password

    def update(self, instance: User, validated_data: dict) -> User:
        instance.email = validated_data.get("email", instance.email)
        instance.password = validated_data.get("password", instance.password)
        instance.username = validated_data.get("username", instance.username)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = "__all__"


class ElectricBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectricBill
        fields = "__all__"


class WaterBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterBill
        fields = "__all__"


class TelecomBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelecomBill
        fields = "__all__"
