from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from rest_framework import status

from api.serializers import (
    UserSerializer,
    ElectricBillSerializer,
    WaterBillSerializer,
    TelecomBillSerializer,
)
from base.models import User, ElectricBill, WaterBill, TelecomBill

from .constants import BILL_TYPES, SERIALIZER_TYPES


@api_view(["POST"])
def add_user(request: Request):

    is_email_exists = User.objects.filter(email=request.data["email"]).exists()

    if is_email_exists:
        return Response(
            {
                "message": "Email already exists",
            },
            status=status.HTTP_409_CONFLICT,
        )

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "User added successfully",
            }
        )
    else:
        return Response(
            {
                "message": "Invalid email",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["POST"])
def login(request: Request):

    is_email_exists = User.objects.filter(email=request.data["email"]).exists()

    if not is_email_exists:
        return Response(
            {
                "message": "Email not found",
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    is_creds_valid = User.objects.filter(
        email=request.data["email"], password=request.data["password"]
    )

    if is_creds_valid:
        user = is_creds_valid.values()[0]

        el_bills = ElectricBill.objects.filter(user_id=user["id"])
        el_bills_serializer = ElectricBillSerializer(el_bills, many=True)

        wa_bills = WaterBill.objects.filter(user_id=user["id"])
        wa_bills_serializer = WaterBillSerializer(wa_bills, many=True)

        tel_bills = TelecomBill.objects.filter(user_id=user["id"])
        tel_bills_serializer = TelecomBillSerializer(tel_bills, many=True)

        return Response(
            {
                "message": "User logged in successfully",
                "el": el_bills_serializer.data,
                "wa": wa_bills_serializer.data,
                "tel": tel_bills_serializer.data,
                "username": user["username"],
            }
        )
    else:
        return Response(
            {
                "message": "Incorrect email or password",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["POST"])
def add_bill(request: Request, type: str):
    serializer: Serializer = SERIALIZER_TYPES[type](data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Bill added successfully",
            }
        )
    else:
        return Response(
            {
                "message": f"Error {serializer.errors}",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["POST"])
def add_bills(request: Request, type: str):
    serializer: Serializer = SERIALIZER_TYPES[type](data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Bills added successfully",
            }
        )
    else:
        return Response(
            {
                "message": f"Error {serializer.errors}",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
def get_bills(_: Request, type: str, user_id: int):
    bills = BILL_TYPES[type].objects.filter(user_id=user_id)

    if not bills:
        return Response(
            {
                "message": f"There's no bills for this User(id={user_id})",
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    serializer: Serializer = SERIALIZER_TYPES[type](bills, many=True)
    return Response(serializer.data)
