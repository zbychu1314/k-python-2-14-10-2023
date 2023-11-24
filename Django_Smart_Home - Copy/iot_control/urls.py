from django.urls import path
from . import views

app_name = "iot_control"
urlpatterns = [
    path("", views.show_list, name="show_list"),
    path("", views.unregister, name="unregister"),
    path("<int:id>/details", views.details, name="details"),
    path("<int:id>/connect", views.connect, name="connect"),
    path("<int:id>/disconnect", views.disconnect, name="disconnect"),
    path("<int:id>/status_update", views.status_update, name="status_update"),
    path(
        "execute_test_diagnostics",
        views.execute_test_diagnostics,
        name="execute_test_diagnostics",
    ),
]
