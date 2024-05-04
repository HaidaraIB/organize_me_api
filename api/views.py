from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from rest_framework import status

from api.serializers import UserSerializer
from base.models import User

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
    
    is_creds_valid = User.objects.filter(email=request.data["email"], password=request.data["password"])

    if is_creds_valid:
        return Response(
            {
                "message": "User logged in successfully",
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
                "message": f"{serializer.errors}",
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
