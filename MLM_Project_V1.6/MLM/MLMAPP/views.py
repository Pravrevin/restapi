from MLMAPP.models import MyUser
from rest_framework import status , permissions
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from MLMAPP.serializers import RegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.authtoken.models import Token

class Registration(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowuserRegistration(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        snippets = MyUser.objects.all()
        serializer = RegistrationSerializer(snippets, many=True)
        return Response(serializer.data)

class UserDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return MyUser.objects.get(pk=pk)

        except MyUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        print('data',snippet)
        print('pk is =',pk)
        print('request ',request)

        obj = Token.objects.get(user=snippet)

        x = 'Token ' + str(obj)
        print('data',x)

        y = request.headers['Authorization']
        print('dsacs', y)

        if x!=y:
            return Response({'response':'You are not authorised !!!!'})

        serializer = RegistrationSerializer(snippet)
        return Response(serializer.data)