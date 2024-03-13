from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from store import views

urlpatterns = [
    path("", views.get_all_flowers, name="get_all_flowers"),
    path("order_flower/<int:flower_id>", views.order_flower, name="order_flower"),
    path("order_form/", views.order_form, name="order_form"),
    path("order_success/", views.order_success, name="order_success"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)