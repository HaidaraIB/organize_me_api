from django.urls import path
from .views import (
    update_user_info,
    add_bills,
    get_bills,
    add_user,
    login,
    get_user
)

urlpatterns = [
    path("addBills/<type>/", add_bills, name="add-bills"),
    path("getBills/<type>/<user_id>/", get_bills, name="get-bills"),
    path("addUser/", add_user, name="add-user"),
    path("updateUserInfo/", update_user_info, name="update-user-info"),
    path("login/", login, name="login"),
    path("getUser/<user_id>/", get_user, name="get-user"),
]
