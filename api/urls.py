from django.urls import path
from .views import (
    add_bill,
    get_bills,
    add_user,
)

urlpatterns = [
    path("addBill/<type>/", add_bill, name="add-bill"),
    path("getBills/<type>/<user_id>/", get_bills, name="get-bills"),
    path("addUser/", add_user, name="add-user"),
]
