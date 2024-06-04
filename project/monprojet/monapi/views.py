from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Client
from .serializers import ClientSerializer

class ClientListApiView(APIView):
    def get(self, request, *args, **kwargs):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        if Client.objects.filter(identifiant=data.get('identifiant')).exists():
            return Response({'error': 'Identifiant already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientDetailApiView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            client = Client.objects.get(pk=id)
        except Client.DoesNotExist:
            return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id, *args, **kwargs):
        try:
            client = Client.objects.get(pk=id)
        except Client.DoesNotExist:
            return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
        
        client.delete()
        return Response({"message": "Client deleted"}, status=status.HTTP_200_OK)
    
    def put(self, request, id, *args, **kwargs):
        try:
            client = Client.objects.get(pk=id)
        except Client.DoesNotExist:
            return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ClientSerializer(instance=client, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientAuthenticateApiView(APIView):
    def post(self, request, *args, **kwargs):
        identifiant = request.data.get('identifiant')
        mot_de_passe = request.data.get('mot_de_passe')
        
        try:
            client = Client.objects.get(identifiant=identifiant)
            if client.mot_de_passe == mot_de_passe:
                return Response({"authenticated": True}, status=status.HTTP_200_OK)
            else:
                return Response({"authenticated": False}, status=status.HTTP_401_UNAUTHORIZED)
        except Client.DoesNotExist:
            return Response({"authenticated": False}, status=status.HTTP_401_UNAUTHORIZED)
