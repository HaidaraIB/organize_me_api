from rest_framework import serializers

from base.models import (
    ElectricBill,
    WaterBill,
    TelecomBill,
    User,
)

class UserSerializer(serializers.ModelSerializer):
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
