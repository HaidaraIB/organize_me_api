from api.serializers import (
    ElectricBillSerializer,
    WaterBillSerializer,
    TelecomBillSerializer,
)

from base.models import (
    ElectricBill,
    WaterBill,
    TelecomBill,
)

from django.db.models import Model
from rest_framework.serializers import Serializer

BILL_TYPES: dict[str, Model] = {
    'el': ElectricBill,
    'wa': WaterBill,
    'tel': TelecomBill,
}

SERIALIZER_TYPES: dict[str, Serializer] = {
    'el': ElectricBillSerializer,
    'wa': WaterBillSerializer,
    'tel': TelecomBillSerializer,
}