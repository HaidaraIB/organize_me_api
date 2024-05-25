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
                "me": serializer.data,
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
def update_user_info(request: Request):

    user = User.objects.get(id=request.data["id"])

    serializer = UserSerializer(data=request.data, instance=user)

    if serializer.is_valid():
        user.email = request.data["email"]
        user.password = request.data["password"]
        user.username = request.data["username"]
        user.save()

        return Response(
            {
                "message": "User updated successfully",
                "user": serializer.data,
            }
        )
    else:
        return Response(
            {
                "message": str(serializer.errors),
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["POST"])
def login(request: Request):
    try:
        User.objects.get(email=request.data["email"])
    except User.DoesNotExist:
        return Response(
            {
                "message": "Email not found",
            },
            status=status.HTTP_404_NOT_FOUND,
        )
    user = User.objects.get(
        email=request.data["email"], password=request.data["password"]
    )
    if user is not None:
        user_serializer = UserSerializer(user)
        el_bills = ElectricBill.objects.filter(user_id=user_serializer.data["id"])
        el_bills_serializer = ElectricBillSerializer(el_bills, many=True)

        wa_bills = WaterBill.objects.filter(user_id=user_serializer.data["id"])
        wa_bills_serializer = WaterBillSerializer(wa_bills, many=True)

        tel_bills = TelecomBill.objects.filter(user_id=user_serializer.data["id"])
        tel_bills_serializer = TelecomBillSerializer(tel_bills, many=True)

        return Response(
            {
                "message": "User logged in successfully",
                "el": el_bills_serializer.data,
                "wa": wa_bills_serializer.data,
                "tel": tel_bills_serializer.data,
                "user": user_serializer.data,
            }
        )
    else:
        return Response(
            {
                "message": "Icorrect password",
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


@api_view(["GET"])
def get_user(_: Request, user_id: int):
    user = User.objects.filter(id=user_id)[0]
    if not user:
        return Response(
            {
                "message": f"There's no user with an id: {user_id}",
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    serializer: UserSerializer = UserSerializer(user)
    return Response(serializer.data)
