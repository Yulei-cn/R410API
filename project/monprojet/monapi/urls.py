from django.urls import path
from .views import CommentaireListApiView, CommentaireDetailApiView

urlpatterns = [
    path('api/', CommentaireListApiView.as_view(), name='commentaire-list-create'),
    path('api/<int:id>/', CommentaireDetailApiView.as_view(), name='commentaire-detail'),
]
