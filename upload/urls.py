from django.urls import path
from .views import upload_image, d3, save_image, confirm_conversion, home, gallery

urlpatterns = [
    path('', upload_image, name='upload_image'),
    path('gallery/', gallery, name='gallery'),
    path('3d/<str:model_id>/', d3, name='d3_view'),
    path('save-image/', save_image, name='save_image'),
    path('confirm/<int:image_id>/', confirm_conversion, name='confirm_conversion'),
]