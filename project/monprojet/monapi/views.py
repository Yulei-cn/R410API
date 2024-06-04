from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Commentaire
from .serializers import CommentaireSerializer

class CommentaireListApiView(APIView):
    def get(self, request, *args, **kwargs):
        commentaires = Commentaire.objects.all()
        serializer = CommentaireSerializer(commentaires, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'titre': request.data.get('titre'),
            'commentaire': request.data.get('commentaire'),
            'date_publication': request.data.get('date_publication'),
        }
        serializer = CommentaireSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentaireDetailApiView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            commentaire = Commentaire.objects.get(pk=id)
        except Commentaire.DoesNotExist:
            return Response({"res": "Object with id does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = CommentaireSerializer(commentaire)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id, *args, **kwargs):
        try:
            commentaire = Commentaire.objects.get(pk=id)
        except Commentaire.DoesNotExist:
            return Response({"res": "Object with id does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        
        commentaire.delete()
        return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)
    
    def put(self, request, id, *args, **kwargs):
        try:
            commentaire = Commentaire.objects.get(pk=id)
        except Commentaire.DoesNotExist:
            return Response({"res": "Object with id does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = {
            'titre': request.data.get('titre'),
            'commentaire': request.data.get('commentaire'),
        }
        serializer = CommentaireSerializer(instance=commentaire, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
