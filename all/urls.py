from django.urls import path
from . import views

urlpatterns = [
    # Driver endpoints
    path('register_driver/', views.register_driver, name='register_driver'),
    path('get_driver_info/<int:telegram_id>/', views.get_driver_info, name='get_driver_info'),
    path('drivers/', views.driver_list.as_view(), name='driver_list'),
    path('drivers/<int:pk>/', views.driver_detail.as_view(), name='driver_detail'),
    # Advertisement endpoints
    path('create_reklama/', views.create_reklama, name='create_reklama'),
    path('advertisements/', views.reklama_list.as_view(), name='reklama_list'),
    path('advertisements/<int:pk>/', views.reklama_detail.as_view(), name='reklama_detail'),
    # Order endpoints
    path('request_driver/', views.request_driver, name='request_driver'),
    path('accept_driver/', views.accept_driver, name='accept_driver'),
    path('reject_driver/', views.reject_driver, name='reject_driver'),
    path('orders/', views.driver_request_list.as_view(), name='driver_request_list'),
    path('orders/<int:pk>/', views.driver_request_detail.as_view(), name='driver_request_detail'),
]