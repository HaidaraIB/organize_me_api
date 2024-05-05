from django.urls import path
from .views import (
    add_bill,
    add_bills,
    get_bills,
    add_user,
    login
)

urlpatterns = [
    path("addBill/<type>/", add_bill, name="add-bill"),
    path("addBills/<type>/", add_bills, name="add-bills"),
    path("getBills/<type>/<user_id>/", get_bills, name="get-bills"),
    path("addUser/", add_user, name="add-user"),
    path("login/", login, name="login"),
]
