from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from rest_framework import status
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404
from django.http import Http404
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
        error_msg = serializer.errors.get("email")[0]
        return Response(
            {
                "message": error_msg,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )



@api_view(["POST"])
def update_user_info(request: Request):

    try:
        user = get_object_or_404(User, id=request.data.get("id"))
    except Http404:
        return Response(
            {"message": "User with the provided ID does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    serializer = UserSerializer(data=request.data, instance=user)

    if serializer.is_valid():
        # .save() here will call .update(),
        # because we're passing the User object as an instance to UserSerializer.
        serializer.save()
        return Response(
            {
                "message": "User updated successfully",
                "user": serializer.data,
            }
        )
    else:
        return Response(
            {"message": str(serializer.errors)},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["POST"])
def login(request: Request):
    try:
        user = get_object_or_404(User, email=request.data["email"])
    except Http404:
        return Response(
            {
                "message": "Email not found",
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    is_password_correct = check_password(request.data["password"], user.password)

    if is_password_correct:
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
