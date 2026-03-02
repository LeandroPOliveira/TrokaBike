from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "products"

urlpatterns = [

    # 🌎 PUBLIC AREA
    path("", views.product_list, name="product_list"),
    path("category/<str:category>/", views.product_by_category, name="product_by_category"),


    # 🔐 SELLER AREA
    path("create/", views.product_create, name="product_create"),
    path("my-products/", views.my_products, name="my_products"),
    path("<slug:slug>/update/", views.product_update, name="product_update"),
    path("<slug:slug>/delete/", views.product_delete, name="product_delete"),
    path("<slug:slug>/", views.product_detail, name="product_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
