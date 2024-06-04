from django.urls import path
from .views import ClientListApiView, ClientDetailApiView, ClientAuthenticateApiView

urlpatterns = [
    path('clients/', ClientListApiView.as_view(), name='client-list-create'),
    path('clients/<int:id>/', ClientDetailApiView.as_view(), name='client-detail'),
    path('clients/authenticate/', ClientAuthenticateApiView.as_view(), name='client-authenticate'),
]
